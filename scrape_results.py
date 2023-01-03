import requests
from typing  import List
import pandas
import csv
from urllib.request import urlopen
from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
class Command(BaseCommand):
    help='load data'
    def handle(self,*args, **kwargs):
     urls=self.construct_urls()
     listfinale=[]  
     lis=[]    
     dic={'Adresse':'','Surface': '','Prix': '','Text': '','Insérée le': '',}
     l = []
     for url in urls:
      q=[] 
      t1= [] 
      t4=[]
      t= []
      r=requests.get( url)
      souup=BeautifulSoup(r.text,'html.parser')
      tb=souup.find('table')  
      for tr in  tb.find_all('tr'):
           for td in tr.find_all('td'):
          
             for tab in td.find_all('table'):
               for tr in  tab.find_all('tr'):
                for td in tr.find_all('td'):
                
                 for tab in td.find_all('table',class_="da_rub_cadre"):
                     for tab in td.find_all('table',class_="da_rub_cadre"):
                        for tr in  tab.find_all('tr'):
                            for td in tr.find_all('td',class_="da_label_field"):
                             if td.text  not in  t:
                                 t.append(td.text)
                             
                            
                            for td in tr.find_all('td',class_="da_field_text"):
                               t1.append(td.text.strip()) 
                               
                              
      t3=[t1[x:x+7] for x in range(0, len(t1),7)]  
        
      for ind in t3:
                   if ind  not in  t4:
                     t4.append(t3)
              
                    
      for a in range(1,7,1):#pour les champs    
                       
                          q.append(t4[0][0][a])
        
            
     l.append(q)       
     

     
        #   dic={'Adresse':'','Surface': '','Prix': '','Text': '','Insérée le': '',}
        
     for l in l: 
    
       dic['Adresse']=l[0]
       dic['Surface']=l[1]
       dic['Prix']=l[2]
       dic['Text']=l[3]
       dic['Insérée le']=l[4]
       lis.append(dic)
     listfinale.append(lis)  
     print(listfinale)                           
    def construct_urls(self) ->List[str]:
         
         page= requests.get("http://www.annonce-algerie.com/AnnoncesImmobilier.asp")

         soupi =BeautifulSoup (page.content, 'html.parser') 
         links= soupi.find_all('a', href=True)

         details_annonces=[]

         for link in links:


          if "DetailsAnnonceImmobilier" in link['href']: 
              details_annonces.append(f" {'http://www.annonce-algerie.com/'}{link['href']}")


         
         return details_annonces





