class Contexor:
    
    'EXAMPLE USE: o = Contexor(\'nytimes.com\') and then o.similar([\'cnn.com\',\'wsj.com\',\'bbc.com\'])'

    def __init__(self, control_url):
        
        self.control_url = control_url
        self.req = urllib2.build_opener(urllib2.HTTPCookieProcessor())
        self.nlp = spacy.load('en')
        self.control_doc = self._control_group()

    def _control_group(self):
        
        html = self.req.open('http://' + self.control_url)
        soup = BeautifulSoup(html, "lxml")
        self.control_doc = nlp(unicode(soup.find_all('p')))
        
        return self.control_doc
    
    def similar(self,comparison_url):
        
        if len(comparison_url) == 1:
            
            comparison_url = [comparison_url]
        
        for url in comparison_url:    
        
            html = self.req.open('http://' + url)
            soup = BeautifulSoup(html, "lxml")
            self.comparison_doc = nlp(unicode(soup.find_all('p')))
        
            print url,self.control_doc.similarity(self.comparison_doc)
