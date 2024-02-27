#web stuff
from bs4 import BeautifulSoup as bs
from selenium import webdriver

#time
import time

#data
import pandas as pd

#WD
wd = "D:/Python Work Area/01_Py_Automation/data/"

"""
Step0: input pokemon name
"""

name = input('type pokemon name \n>>')

driver = webdriver.Chrome()

driver.get("https://www.pokellector.com/search?criteria="+ name +"&x=0&y=0")

#driver.execute_script("window.scrollBy(0,600)")
time.sleep(1)
cards_name = []
cards_set = []
cards_price = []

data_index = 0

html = driver.page_source
time.sleep(1)

soup  = bs(html,  "html.parser")

"""
Step1: find how many pages there are
"""
page = 0
page_url = []

try:
    pages = soup.find_all("div", attrs={"class":"pagination"})

    for a in pages[0].find_all('a', href=True):
        page += 1
        #print(f"Page {page} - {a['href']}")
        page_url.append(a['href'])
        
except:
    pass

#print(f"This card has {page} Page(s)")
#print(page_url)

"""
Step2: jp cards
"""
eng_url = "https://www.pokellector.com/"
jp_url = "https://jp.pokellector.com/"

urls = [eng_url, jp_url]

"""
Step3: loop over pages & pull card data
"""
for vs in urls:
    for pg in page_url:
        driver.get(vs+ pg)
        time.sleep(1)
        html = driver.page_source
        time.sleep(1)
        soup  = bs(html,  "html.parser")

        card = soup.find_all("div", attrs={"class":"cardresult"})
        #print(f"\nhow many cards... {len(card)}\n")

        for i in card:
            data_index += 1
            try:
                card_name = i.find("div", attrs={"class":"name"})
                card_set = i.find("div", attrs={"class":"set"})
                card_price = i.find("div", attrs={"class":"prices"})

                #print(card[i])
                cards_name.append(card_name.text)
                print(f"Card #{data_index} - {card_name.text}")
                cards_set.append(card_set.text)
                #print(card_set.text)
                cards_price.append(card_price.text)
                #print(card_price.text)

            except:
                card_name = i.find("div", attrs={"class":"name"})
                card_set = i.find("div", attrs={"class":"set"})
                cards_name.append(card_name.text)
                cards_set.append(card_set.text)
                cards_price.append("NULL")

                print(f"Card #{data_index} - {card_name.text}")

print("----Done Data Pull----")
time.sleep(1)

#print(len(cards_name))
#print(len(cards_set))
#print(len(cards_price))

dict = {'name': cards_name, 'set': cards_set, 'price': cards_price}

df = pd.DataFrame(dict)

df.to_csv(wd+name+".csv")
print(f"----Saved to {wd}----")
#print(df)
