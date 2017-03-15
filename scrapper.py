import requests
from bs4 import BeautifulSoup
import csv
from tqdm import tqdm
idno = 1215316201
sem = 1
l = []
print "contacting Server ....."
print "Fetching results...."
for i in tqdm(range(0,64)):
	url="https://doeresults.gitam.edu/onlineresults/pages/Newgrdcrdinput1.aspx"
	payload={'__EVENTTARGET': '', '__EVENTARGUMENT': '', 'txtreg':idno , 'Button1': 'Get+Result', '__EVENTVALIDATION': '/wEWFQKj/sbfBgLnsLO+DQLIk+gdAsmT6B0CypPoHQLLk+gdAsyT6B0CzZPoHQLOk+gdAt+T6B0C0JPoHQLIk6geAsiTpB4CyJOgHgLIk5weAsiTmB4CyJOUHgKL+46CBgKM54rGBgK7q7GGCALWlM+bAsr6TbZa4e1ProM8biQQXbC9/wS2', '__VIEWSTATE': '/wEPDwULLTE3MTAzMDk3NzUPZBYCAgMPZBYCAgcPDxYCHgRUZXh0ZWRkZKKjA/8YeuWfLRpWAZ2J1Qp0eXCJ', 'cbosem': sem, '__VIEWSTATEGENERATOR': '65B05190'}
	q=requests.post(url,data=payload)
	idno += 1
	s=BeautifulSoup(q.text,'html.parser')
	name=s.find("span",{"id":"lblname"}).text
	x=s.find("table",{"class":"table-responsive"})
	a=x.findAll("tr")[1:]
	gpa=float(s.find("span",{"id":"lblgpa"}).text)
	cgpa=float(s.find("span",{"id":"lblcgpa"}).text)
	l.append(name)
	l.append(x)
	l.append(a)
	l.append(gpa)
	l.append(cgpa)
	with open('gitams.csv','wb') as myfile:
		wr = csv.writer(myfile,quoting=csv.QUOTE_ALL)
		wr.writerow(l)
