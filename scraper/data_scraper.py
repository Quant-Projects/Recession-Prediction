import requests
from bs4 import BeautifulSoup
import numpy as np
import html5lib

def get_yield():
	url = "https://www.treasury.gov/resource-center/data-chart-center/interest-rates/pages/TextView.aspx?data=yield"
	data = requests.get(url).text
	soup = BeautifulSoup(data, 'html5lib')
	
	main_table = soup.find_all("table")[1]
	last_col = main_table.find_all("tr")[len(main_table.find_all("tr")) - 1].find_all("td")
		
	return last_col[0].text, float(last_col[1].text), float(last_col[3].text), float(last_col[4].text), float(last_col[5].text), float(last_col[7].text), float(last_col[8].text), float(last_col[10].text)
	
def get_vix():
	url = "https://finance.yahoo.com/quote/%5EVIX?p=%5EVIX"
	data = requests.get(url).text
	soup = BeautifulSoup(data, 'html5lib')
	
	return float(soup.find_all("span")[11].text)