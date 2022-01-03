import requests
from bs4 import BeautifulSoup
import re

response = requests.get('https://ncov.dxy.cn/ncovh5/view/pneumonia')
home_page = response.content.decode()
#print(home_page)

soup = BeautifulSoup(home_page,'lxml')
script = soup.find(id = 'getListByCountryTypeService2true')
st = script.string

json_string = re.findall(r'\[.+\]',st)[0]

print(json_string)

