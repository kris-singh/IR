import link_retriever
import list_urls_to_txt

#provide the url to crawl here
url_to_crawl = "https://docs.python.org/3/"
#obtain the url list
urls_list = link_retriever.Ret_href(url_to_crawl)
doc_id,page_created = list_urls_to_txt.urls_to_txt(urls_list,0)# returns last doc_id used and list of pages created
temp = []
file_made = {}#dictionary for keeping the pages created
for i in page_created:
	file_made[i] = 1
for i in urls_list:
	temp = link_retriever.Ret_href(i)
	for i in temp:
		if i in file_made:
			temp.remove(i)#if file already has been written to disk remove from temp
	temp_doc_id,page_created = list_urls_to_txt.urls_to_txt(temp,doc_id)
	for i in page_created:
		file_made[i] = 1
	#union of temp and url_list for no duplication of urls
	url_list = list(set(temp) | set(urls_list))
	temp = []
	doc_id = temp_doc_id

