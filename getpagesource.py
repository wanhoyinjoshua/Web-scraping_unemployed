
import time
import json
from csv import reader
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys
import csv
from time import sleep
#import requests
from bs4 import BeautifulSoup
import json
import re
edgeBrowser = webdriver.Edge(r"C:\Users\wanho\edgedriver_win64\msedgedriver.exe")
#for loop here
mastercompanyinfo=[]
#at page 8

for i in range(400):
    """
    if(i<8):
        i += 1
        continue
    """
    i+=1

    edgeBrowser.get("https://www.yellowpages.com.au/search/listings?clue=IT&locationClue=All+States&pageNumber={}".format(i))
    html = edgeBrowser.page_source
    html =str(html)






    soup = BeautifulSoup(html, 'lxml')
    script = soup.find_all("script")
    pattern = re.compile('window\.__INITIAL_STATE__ = \{.*}' )
    pattern1 = re.compile('\{"env":\{.*}')
    stringlist=[]
    for i in script:
        strObj = i.text
        match = pattern.search(strObj)
        if match:


             new= str(match.group())



             print(new)
             for i in range(len(new)):
                 if i > 26:
                     stringlist.append(new[i])

             with open('D:\yellowpage\jeadme.txt', 'w', encoding="utf-8") as f:
                 f.write(str(''.join(stringlist)))




             with open('D:\yellowpage\jeadme.txt', 'r', encoding="utf-8") as f:
                 json_data = json.load(f)
                 print(json_data)

                 x = json_data.get("model")


                 for i in range(len(x["inAreaResultViews"])):
                     companyaddress= x["inAreaResultViews"][i]['searchableAddress']['addressLine']
                     email = x["inAreaResultViews"][i]['primaryEmail']
                     website= x["inAreaResultViews"][i]['website']
                     try:
                        address= x["inAreaResultViews"][i]['addressView']['asContactCardFormat']
                     except:
                         try:
                            address = x["inAreaResultViews"][i]['addressView']['addressLine']
                         except:
                            address="nil"
                     phonenumber=x["inAreaResultViews"][i]["callContactNumber"][ "displayValue"]
                     longdesscription=x["inAreaResultViews"][i]['longDescriptor']
                     name =x["inAreaResultViews"][i]["name"]
                     type=  x["inAreaResultViews"][i]["category"]["name"]



                     subcompanyinfop=[name,email,address,website,phonenumber,type]
                     mastercompanyinfo.append((subcompanyinfop))
                     print(subcompanyinfop)



             #print(mastercompanyinfo)
             #convert this to csv
             fields=["name","email","address","website","category","phone"]
             with open('D:\yellowpage\_keyword_IT.csv', 'w', encoding='UTF8', newline='') as f:

                 # using csv.writer method from CSV package
                 write = csv.writer(f)

                 write.writerow(fields)
                 write.writerows(mastercompanyinfo)

             time.sleep(2)




