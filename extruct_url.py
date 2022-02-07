import extruct 
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import requests
import click
import json


@click.command()
@click.argument('url')
@click.option('-w', '--wait-rendering', default=3,
    help='Number of seconds to wait for the JavaScript to render the HTML page with Selenium.')
@click.option('--render-js/--no-render', default=True,
    help='Execute the JavaScript with Selenium to render the HTML pages sent by the server.')
@click.option('-e', '--extract-metadata', default='all',
    help='Filter which extracted metadata to show between json-ld, microdata, rdfa, opengraph, dublincore, and microformat. Default to all.')
@click.option('--verbose/--no-verbose', default=False,
    help='Display more logs messages.')
def extruct_url(url, wait_rendering, render_js, extract_metadata, verbose):
    if verbose: print(f'🧃 Extracting metadata from \033[1m{url}\033[0m\n')

    if render_js == False:
        resp = requests.get(url)
        html_text = resp.text
    else:
        if verbose: print(f'🌜️ Running Selenium for {wait_rendering} seconds to let JavaScript generate the HTML page\n')
        
        # Selenium browser options for no display:
        opts = Options()
        opts.add_argument('--headless')
        browser = webdriver.Firefox(options=opts)

        browser.get(url)
        time.sleep(wait_rendering)

        html_text = browser.page_source
        browser.quit()

    extracted_metadata = extruct.extract(html_text.encode('utf8'))

    if extract_metadata == 'all':
        print(json.dumps(extracted_metadata, indent=2))
    else:
        try:
            print(json.dumps(extracted_metadata[extract_metadata], indent=2))
        except Exception as e:
            print(f'The type of metadata provided {extract_metadata} is not supported by extruct')


if __name__ == '__main__':
    extruct_url()