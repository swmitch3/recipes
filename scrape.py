import urllib.request as ur
import socket
from bs4 import BeautifulSoup as bs
import requests

fhand = ur.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())

'''
rhand = ur.urlopen('https://www.melskitchencafe.com/sour-cream-banana-bread/') #
for line in rhand:
    print(line.decode().strip())
'''

'''
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()



mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.allrecipes.com', 80))
cmd = 'GET https://www.allrecipes.com/recipe/220943/chef-johns-buttermilk-biscuits/ HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()



mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.melskitchencafe.com', 80))
cmd = 'GET https://www.melskitchencafe.com/sour-cream-banana-bread/ HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()
'''
url = 'https://www.melskitchencafe.com/sour-cream-banana-bread/'
html_doc = requests.get(url).content
soup = bs(html_doc, 'html.parser')
recipe_container = soup.find('div', {'class': 'wprm-recipe-container'})

from IPython import embed
embed()