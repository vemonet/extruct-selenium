import extruct
import time 
import sys
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


url = 'https://fair-enough.semanticscience.org/evaluation/f0b7a7f7e05592e776c1a54040416500ec69e45c'
wait_rendering = 2

# Get URL from arg if provided:
if len(sys.argv) > 1:
    url = sys.argv[1]

# Selenium browser options for no display:
opts = Options()
opts.add_argument("--headless")
browser = webdriver.Firefox(options=opts)

browser.get(url)

time.sleep(wait_rendering)

html_text = browser.page_source
browser.quit()

# print(html_text)

extracted_metadata = extruct.extract(html_text.encode('utf8'))
print(extracted_metadata)