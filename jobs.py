from bs4 import BeautifulSoup
import requests
import json

# URL to scrape
url = "https://www.indeed.com/q-gis-developer-jobs.html"

# headers to mimic a web browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Fetch HTML content with headers using the get method
response = requests.get(url, headers=headers)


# Check if the request was successful
if response.status_code == 200:
    html_content = response.content
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all job cards
    # using underscore in class_ to deffientiate keywrd class
    job_cards = soup.find_all('div', class_='cardOutline')

    # list to store job details
    jobs = []

    # Iterate on job card
    for card in job_cards:
        # Extract job title
        title_element = card.find('h2', class_='jobTitle')
        title = title_element.get_text(strip=True) if title_element else 'N/A'

        # company name
        company_element = card.find('span', {'data-testid': 'company-name'})
        company = company_element.get_text(
            strip=True) if company_element else 'N/A'

        # job location
        location_element = card.find('div', {'data-testid': 'text-location'})
        location = location_element.get_text(
            strip=True) if location_element else 'N/A'

        # job posting date
        posted_element = card.find('span', {'data-testid': 'myJobsStateDate'})
        posted = posted_element.get_text(strip=True).replace(
            'Posted', '').strip() if posted_element else 'N/A'

        # Extract job description snippet
        description_element = card.find('ul')
        description = description_element.get_text(
            strip=True) if description_element else 'N/A'

        # Print info using f string
        print(f"Title: {title}")
        print(f"Company: {company}")
        print(f"Location: {location}")
        print(f"Posted: {posted}")
        print(f"Description: {description}")
        print("-" + "-"*50 + "-")

        # Add job
        jobs.append({
            'Title': title,
            'Company': company,
            'Location': location,
            'Posted': posted,
            'Description': description
        })

    # details to a JSON file
    with open('jobs.json', 'w', encoding='utf-8') as f:
        json.dump(jobs, f, ensure_ascii=False, indent=4)
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
