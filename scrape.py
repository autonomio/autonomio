import urllib2
from bs4 import BeautifulSoup

class Scrape:
    
    def __init__(self,url,tag='a'):
        
        self.url = url
        self.session = urllib2.build_opener(urllib2.HTTPCookieProcessor())
        self.soup = self._fetch()
        self.tag = tag
        self.text = self._parse(tag)
        
    def _fetch(self):
        
        self.html = self.session.open('http://' + self.url)
        self.soup = BeautifulSoup(self.html, "lxml")
        
        return self.soup
    
    def _parse(self,tag):
        
        l=[]
        
        for item in self.soup.findAll(tag):
    
             l.append(item.get_text())
        
        return l
