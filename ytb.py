from selenium import webdriver
import requests as req
import re,time

temp = []
links = []

link = "https://youtu.be/8pU7d_XzQa4"
result = req.get(link).text

for i in range(0,len(result)):
    try:
        re.search("https://",result)
        result = result[re.search("googlevideo",result).span()[0]-150:]
        result = result[re.search("http",result).span()[0]:]
        link = result[:re.search('"',result).span()[0]]
        temp.append(link)
        result = result[re.search('"',result).span()[0]:]
    except:
        break

for link in temp:
    if re.search(r'\\u0026',link) != None:
        links.append(re.sub(r'\\u0026',"&",link))
    else:
        l = re.sub(r'%3F',"?",link)
        l = re.sub(r'%3D',"=",l)
        l = re.sub(r'%26',"&",l)
        links.append(l)

driver = webdriver.Chrome("Z:/Downloads/chromedriver_win32 (3)/chromedriver.exe")  #directory should be changed based on where the driver file was downloaded
driver.get(links[1])
time.sleep(10000)
