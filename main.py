from bs4 import BeautifulSoup  # 引用BeautifulSoup库
import requests  # 引用requests
import os  # os
import pandas as pd
import csv
import codecs

lst = []
url = 'http://datachart.500.com/dlt/history/newinc/history.php?start=07001&end=22122'
r = requests.get(url)
r.encoding = 'utf-8'
text = r.text
soup = BeautifulSoup(text, "html.parser")
tbody = soup.find('tbody', id="tdata")
tr = tbody.find_all('tr')
td = tr[0].find_all('td')
for page in range(0, 14016):
    td = tr[page].find_all('td')

    lst.append([td[0].text, td[1].text, td[2].text, td[3].text, td[4].text, td[5].text, td[6].text, td[7].text])
    with open("Lottery_data.csv", 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['期号', '号码1', '号码2', '号码3', '号码4', '号码5', '号码6', '号码7'])
        writer.writerows(lst)
csvfile.close()

