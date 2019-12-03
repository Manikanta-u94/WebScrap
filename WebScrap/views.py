from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
import urllib.request
import time
from bs4 import BeautifulSoup


@api_view()
def Scrapdata(request,product):
	try:
		data=getScrapData(product)
		if not data:
			data='No product name matched.Please enter correct product name...'
		return Response(data)
	except Exception as e:
		raise e

def getScrapData(bank):
	info=[]
	value="".join(bank.split()).lower()
	link='https://www.mouthshut.com/search/prodsrch.aspx?data='+value
	# print(link)
	response = requests.get(link)
	soup1 = BeautifulSoup(response.text, "html.parser")
	# print(soup1)
	v=None
	div1 = soup1.find_all('a', class_='')
	for d in div1:
		v=d.get_text()
		v1="".join(v.split()).lower()
		if v1 == value and d.has_attr('href'):
			print(v,d.attrs['href'])
			url =d.attrs['href']
			response = requests.get(url)
			soup = BeautifulSoup(response.text, "html.parser")
			div = soup.find_all('div',class_="row review-article")
			for div1 in div :
				for d in div1:
					r=d.find('div',class_= "rating").find('span')
					i1={'review_title':d.find("strong").get_text(), 
					'review_content' : d.find('div',class_= "more reviewdata").get_text().strip(),
					'review_rating':len(r.find_all('i',class_="icon-rating rated-star"))}
				info.append(i1)
	return info














