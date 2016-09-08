from bs4 import BeautifulSoup
import urllib.request
import word_count
import re
import os

def urls_to_txt(urls_list1,doc_id):
    pages_created = []
    for page_url in urls_list1:
        print (page_url)
        page_doc = urllib.request.urlopen(page_url).read()
        page_soup = BeautifulSoup(page_doc)
        #getting body content and text
        body_content = page_soup.find_all('p')
        para_text = ""
        for p_text in body_content:
            para_text = para_text + str(p_text.get_text()) + "\n"
            #getting content length    
        content_length = word_count.word_count_func(para_text)
        if(content_length<150):
            continue
        doc_id = doc_id+1
        #to determine the number of pages required
        #getting the page title
        page_title = page_soup.title
        page_title_string = page_title.string
        #getting the meta tags
        meta_tag_strings = "No meta tag found in document"
        for meta_tags in page_soup.find_all('meta'):
            if meta_tags!=None :
            #print(meta_tags.get("content"))
                meta_con = str(meta_tags.get("name"))
                if meta_con=="keywords":
                    meta_tag_strings = str(meta_tags.get("content"))
                    break
                else:
                    continue
        #getting the document last updated date
        date_regex = r"(Jan(uary)?|Feb(ruary)?|Mar(ch)?|Apr(il)?|May|Jun(e)?|Jul(y)?|Aug(ust)?|Sep(tember)?|Oct(ober)?|Nov(ember)?|Dec(ember)?)\s+\d{1,2},\s+\d{4}"
        footer_div = page_soup.find("div", {"class":"footer"})
        try:
            footer_text = str(footer_div.get_text())
        except AttributeError:
            footer_text = "Jul 29, 2016"
        re_date_match = re.search(date_regex,footer_text)
        if re_date_match!=None:
            re_date = re_date_match.group(0)
            #section to create and write the content into file
            #para_text = str(para_text,encoding='utf-8', errors='ignore')
            #para_text = para_text.encode('UTF-8')    
        doc_id_str = str(doc_id)
        file_path = "./Text_files/link_" + doc_id_str + ".txt"
        with open(file_path, "w", encoding = 'utf-8') as f:
            f.write("URL: " + page_url + "\n\n"
                +"Title: " + page_title_string + "\n\n"
                + "Doc Id: " + doc_id_str + "\n\n"
                +"Meta Tags : " + meta_tag_strings + "\n\n"
                +"Date :" + re_date + "\n" 
                + "\n" +"Content :" + para_text + "\n")
        f.close()
        pages_created.append(page_url)
    return doc_id,pages_created