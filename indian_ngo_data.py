import requests
from bs4 import BeautifulSoup
import json
from pprint import pprint

url = 'https://www.giveindia.org/certified-indian-ngos'
def getRequestSoup(url):
	return BeautifulSoup(requests.get(url).text,'html.parser')
first_call = getRequestSoup(url)
# print (first_call)
def list_of_ngo(url):
    dic = {}
    soup = url.find('div', class_="ngo-list-desktop display-desktop-only col-12 col-sm-12 col-md-12 col-lg-12")
    table = soup.find('table', class_="jsx-697282504 certified-ngo-table")
    tr = table.find_all('tr', class_="jsx-697282504")
    name_list = []
    cause_list = []
    state_list = []
    for i in tr:
        td = i.find_all('td', class_="jsx-697282504")
        for name in td[:1]:
            text_1 =name.text
            name_list.append(text_1)
           
        for cause in td[1:2]:
            text_2 = cause.text
            cause_list.append(text_2)
           
        for state in td[2:3]:
            text_3 = state.text
            state_list.append(text_3)
        dic['state'] = state_list
        dic['name'] = name_list
        dic['cause'] = cause_list
    return dic
ngos_list =list_of_ngo(first_call)
pprint (ngos_list)

def state_by_ngo(list1):
    dic = {}
    for (x,y,z) in zip(list1['name'], list1['cause'], list1['state']): 
        if z in dic:
            dic[z].append(x)
        else:
            dic[z] = [x]
    return dic        
pprint (state_by_ngo(ngos_list))