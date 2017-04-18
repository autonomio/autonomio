import urllib2
import spacy
from bs4 import BeautifulSoup

class Similarity:
    
    'EXAMPLE USE: o = Contexor(\'nytimes.com\') and then o.similar([\'cnn.com\',\'wsj.com\',\'bbc.com\'])'

    def __init__(self, control_url):
        
        self.control_url = control_url
        self.req = urllib2.build_opener(urllib2.HTTPCookieProcessor())
        self.nlp = spacy.load('en')
        self.control_doc = self._control_group()

    def _control_group(self):
        
        html = self.req.open('http://' + self.control_url)
        soup = BeautifulSoup(html, "lxml")
        self.control_doc = self.nlp(unicode(soup.find_all('p')))
        
        return self.control_doc
    
    def similar(self,comparison_url):
        
        if len(comparison_url) == 1:
            
            comparison_url = [comparison_url]
        
        for url in comparison_url:    
        
            html = self.req.open('http://' + url)
            soup = BeautifulSoup(html, "lxml")
            
            text = ''

            for item in soup.find_all('p'):

                item = item.get_text()
                item = unicode(item)
                item = item.replace('  ','')
                text += ' ' + item
                
            self.comparison_doc = self.nlp(unicode(text))
        
            print url,self.control_doc.similarity(self.comparison_doc)
