# Import libraries
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

val=input('product name : ')
value="".join(val.split()).lower()
link1='https://www.mouthshut.com/search/prodsrch.aspx?data='+value
print(link1)
response1 = requests.get(link1)
soup1 = BeautifulSoup(response1.text, "html.parser")
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


		# div=soup.findAll('a',id='ctl00_ctl00_ContentPlaceHolderFooter_ContentPlaceHolderBody_rptreviews_ctl00_lnkTitle')


		# div=soup.findAll('div',class_='rating')

		# print(len(div))

		# div = soup.find_all('div',class_= "more reviewdata")

		div = soup.find_all('div',class_="row review-article")

		for d in div[6]:
			c=d.find('div',class_= "more reviewdata").get_text()
			title=d.find("strong").get_text()
			r=d.find('div',class_= "rating").find('span')
			rat=len(r.find_all('i',class_="icon-rating rated-star"))

			print(rat,c,'\n',title)

# for i in div:
# 	div=i.get_text()
# 	print(div)

# text = div[0].get_text()
# print(text)



