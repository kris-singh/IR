import urllib.request  #importing the module to handle url's
from bs4 import BeautifulSoup  
import re
import validators
import urllib.parse
def PageParser (url):  ##Parsing the url
    try:
        html_doc = urllib.request.urlopen(url)  #opening the url
        html_content = BeautifulSoup(html_doc,'html.parser')  #saving the html content of url in variable.
        return html_content
    except:
        pass

def Ret_href(url): #defining function to retrieve hyper references from given url
    url = url.strip()
    soup=PageParser(url)
    links_list=[]  #list declaration to store links on html document.
    for url_links in soup.find_all('a'):  ##finding anchors in the html document and saving their hyperlinks in a list
        hlink = url_links.get('href')  ##saving hyper link in hlink
        hlink = hlink.strip()
        regex = '^/\w+ | \w+\.html'
        regex_https = 'http|https'##first throw all external links and internal links to page
        regex_except = url
        ##take the source url split it on '/'
        if re.search(regex_https,hlink,re.I|re.M):
            continue
        regex_except = '#'
        if re.search(regex_except,hlink,re.I|re.M):
            continue
        regex_except = '\.html|\.htm'
        if re.search(regex_except,hlink,re.I|re.M):
	        ##append the absolute path to all the links
	        hlink = urllib.parse.urljoin(url,hlink)
	       	if hlink in links_list:  ##no repetion allow
	        	continue
	        else:
	            links_list.append(hlink)
    #print (links_list)
    for i in links_list:
    	if not validators.url(i):
    		links_list.remove(i)
    		#print ("invalid")
    return links_list