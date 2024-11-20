'''
Real-World Example: Multithreading for I/O-bound Tasks
Scenario: Web Scrapping
Web Scrapping often involves making numerous network requests to fetch web pages. These tasks are I/O bound because they spend a lot of  time waiting for the responses from the servers. Multithreading can significaantly improve the performance by allowing multiple web pages to be fetched concurrently.

urls to scrape
1. https://python.langchain.com/docs/introduction/
2. https://python.langchain.com/docs/concepts/
3. https://python.langchain.com/docs/tutorials/

'''

import  threading
import requests
from bs4 import BeautifulSoup

urls = ["https://python.langchain.com/docs/introduction/","https://python.langchain.com/docs/concepts/","https://python.langchain.com/docs/tutorials/"]

def fetch_contents(url):
    respone = requests.get(url)
    soup = BeautifulSoup(respone.content,'html.parser')
    print(f"Fetched: {len(soup.text)} from {url}")


threads = []
for url in urls:
    thread = threading.Thread(target=fetch_contents,args=(url,))
    threads.append(thread)
    thread.start()


for thread in threads:
    thread.join()

print("All web pages are scrapped")