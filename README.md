# GIS Job Scraper

## Project Overview

<p>
    This project focuses on scraping GIS (Geographic Information Systems) developer job listings in indeed.
    Using BeautifulSoup and requests in Python, I extracted job titles, company names, locations, 
    posting dates, and descriptions. The extracted data is saved into a JSON file.
</p>

## What I Learned

<ul>
    <li>Web scraping using BeautifulSoup and requests</li>
    <li>Data extraction and cleaning</li>
    <li>Handling HTTP requests and headers</li>
    <li>Saving and structuring data in JSON format</li>
</ul>

## Future Notes

<ul>
    <li>Always check the website's <code>robots.txt</code> file before scraping.</li>
    <li>Use appropriate headers to mimic a browser request.</li>
 </ul>

## Project Tutorial

### Installation

<ol>
    <li>
        <strong>Install the required packages:</strong>
        <pre><code>pip install beautifulsoup4 requests</code></pre>
    </li>
</ol>

### Usage

<ol>
    <li>
        <strong>Run the scraper script:</strong>
        <pre><code>python jobs.py</code></pre>
    </li>
    <li>
        <strong>Check the output:</strong>
        <p>The scraped job data will be saved in <code>jobs.json</code>.</p>
    </li>
</ol>

## Code Example

<pre><code>
# URL to scrape
url = "https://www.indeed.com/q-gis-developer-jobs.html"

# Define headers to mimic a web browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Fetch the HTML content with headers
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
</code></pre>

<p>This script is designed to scrape GIS job listings from Indeed. Adjust the URL and HTML parsing logic.</p>
<p>The script includes headers to mimic a real browser.</p>

## Additional Resources

<ul>
    <li><a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/">BeautifulSoup Documentation</a></li>
    <li><a href="https://docs.python-requests.org/en/master/">Requests Documentation</a></li>
    <li><a href="https://docs.python.org/3/library/json.html">JSON in Python</a></li>
</ul>

