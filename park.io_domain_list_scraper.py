import requests
from bs4 import BeautifulSoup

def remove_duplicates(listofElements):
    
    # Create an empty list to store unique elements
    uniqueList = []
    
    for elem in listofElements:
        if elem not in uniqueList:
            uniqueList.append(elem)
    
    # Return the list of unique elements        
    return uniqueList

def fetch_domain_list(tld):

	url = 'https://park.io/domains/index/' + str(tld) + "/page:1"
	page = requests.get(url)

	# Create a BeautifulSoup object
	soup = BeautifulSoup(page.text, 'html.parser')

	links = soup.find_all('a')
	link_array = []

	# Check how many pages to crawl
	try:
		last_page_nav_link = soup.find('a', attrs={'rel': 'last'})
		page_count = int((last_page_nav_link.get("href")).replace("/domains/index/io/page:", ""))
	except:
		# In case the last_page_nav_link isn't on the page, set page_count to 1
		page_count = 1 

	for i in range(page_count):
		
		i = int(i) + 1 # Start with Page 1 instead of Page 0
		print ("Crawled Page " + str(i))

		url = 'https://park.io/domains/index/' + str(tld) + "/page:" + str(i)
		page = requests.get(url)
		soup = BeautifulSoup(page.text, 'html.parser')
		links = soup.find_all('a')
		
		# Grab all links and append to array
		for link in links:
			if "domains/view/" in link.get("href"):
				domain = str(link.get("href").replace("/domains/view/", ""))
				link_array.append(domain)

	link_array = remove_duplicates(link_array)

	return link_array



io_domain_array = fetch_domain_list("io")
print (str(len(io_domain_array)) + " .io domains are dropping soon")

ly_domain_array = fetch_domain_list("ly")
print (str(len(ly_domain_array)) + " .ly domains are dropping soon")

to_domain_array = fetch_domain_list("to")
print (str(len(to_domain_array)) + " .to domains are dropping soon")

me_domain_array = fetch_domain_list("me")
print (str(len(me_domain_array)) + " .me domains are dropping soon")

pro_domain_array = fetch_domain_list("pro")
print (str(len(pro_domain_array)) + " .pro domains are dropping soon")

sh_domain_array = fetch_domain_list("sh")
print (str(len(sh_domain_array)) + " .sh domains are dropping soon")

ac_domain_array = fetch_domain_list("ac")
print (str(len(ac_domain_array)) + " .ac domains are dropping soon")

vc_domain_array = fetch_domain_list("vc")
print (str(len(vc_domain_array)) + " .vc domains are dropping soon")

gg_domain_array = fetch_domain_list("gg")
print (str(len(gg_domain_array)) + " .gg domains are dropping soon")

je_domain_array = fetch_domain_list("je")
print (str(len(je_domain_array)) + " .je domains are dropping soon")

mn_domain_array = fetch_domain_list("mn")
print (str(len(mn_domain_array)) + " .mn domains are dropping soon")

bz_domain_array = fetch_domain_list("bz")
print (str(len(bz_domain_array)) + " .bz domains are dropping soon")

ag_domain_array = fetch_domain_list("ag")
print (str(len(ag_domain_array)) + " .ag domains are dropping soon")

sc_domain_array = fetch_domain_list("sc")
print (str(len(sc_domain_array)) + " .sc domains are dropping soon")

lc_domain_array = fetch_domain_list("lc")
print (str(len(lc_domain_array)) + " .lc domains are dropping soon")

"""

https://tld-list.com/tld/io $26
https://tld-list.com/tld/ly $88
https://tld-list.com/tld/to $37
https://tld-list.com/tld/me $12
https://tld-list.com/tld/pro $10
https://tld-list.com/tld/sh $30
https://tld-list.com/tld/ac $30
https://tld-list.com/tld/vc $27
https://tld-list.com/tld/gg $50
https://tld-list.com/tld/je $50
https://tld-list.com/tld/mn $40
https://tld-list.com/tld/bz $20
https://tld-list.com/tld/ag $87
https://tld-list.com/tld/sc $84
https://tld-list.com/tld/lc $25


"""