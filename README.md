# contexor

#### A python classifier that provides accurates contextual classifying for any website in seconds. 

## 1. Background 

Researchers commonly can benefit from a capability to classify websites automatically based on prominent content on the site. For example, a researcher may want to scan a large number of sites to identify sites that have a strong affinity with a specific topic ('privacy') or behaviour ('strong language').

## 2. Solution 

The solution consist of three primary capabilities: 

1) to capture a representative set of pages from the site
2) to distinguis between sections (e.g. comments) on the page and parse clean text 
3) make prediction for classification 

### 2.1. data capture 

1) domain/s input from user
2) extract urls of prominent pages from landing page
3) extract html from invididual pages

### 2.2. content capture 

- separate the page to sections (e.g. comments, body, ads) 
- separate clean text from other elements in each page section 

### 2.3. classification 

- tokenize text for analysis
- run models 
- output classification 

