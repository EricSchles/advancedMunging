import requests
import lxml.html
import simplejson as json

#fifth from the bottum at http://www.missingkids.com/search?action=continueSearch&searchSubject=child
r = requests.get("http://www.missingkids.com/missingkids/servlet/JSONDataServlet")
if r.status_code == 200:
    print r.text
    
    
