
import requests
from bs4 import BeautifulSoup

# Function to scrape job titles and URLs from the Reed job search page
def scrape_page(url):
    res = requests.get(url)
    if res.status_code == 200:
        soup = BeautifulSoup(res.text, 'html.parser')
        h2_elements = soup.find_all('h2', class_='job-card_jobResultHeading__title__IQ8iT') #can modify this part if you want to output different things.
        for h2_element in h2_elements:
            a_tag = h2_element.find('a')
            if a_tag:
                job_title = a_tag.text.strip()
                href = a_tag.get('href')
                full_url = 'https://www.reed.co.uk' + href #concatenate the first part of the url with the href, as the outputted href isn't clickable 
                print("Job Title:", job_title)
                print("URL:", full_url)
                print()
            else:
                print("No <a> tag found within <h2> element")
    else:
        print("Failed to retrieve the page")

# URL of the results page from searching for python jobs in London
base_url = 'https://www.reed.co.uk/jobs/python-jobs-in-london'

# Iterate from pages 1 to 43. (Currently there are 45 pages, but chose a lower number to reduce the chance of a bug occuring)
for page_number in range(1, 43): 
    page_url = f'{base_url}?pageno={page_number}'  
    print(f"Scraping data from page {page_number}...")
    scrape_page(page_url)
    print()

print("Finished scraping all pages.")
