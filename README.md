<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GIS Job Scraper</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
        h1, h2, h3 {
            color: #333;
        }
        .section {
            margin-bottom: 20px;
        }
        .code-block {
            background-color: #f4f4f4;
            border: 1px solid #ddd;
            padding: 10px;
            overflow-x: auto;
        }
        .image-container {
            text-align: center;
            margin-top: 20px;
        }
        .image-container img {
            border-radius: 50%;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>GIS Job Scraper</h1>

        <div class="section">
            <h2>Project Overview</h2>
            <p>
                This project focuses on scraping GIS (Geographic Information Systems) job listings from the web.
                Using BeautifulSoup and requests in Python, I extracted job titles, company names, locations, 
                posting dates, and descriptions. The extracted data is saved into a JSON file for further analysis.
            </p>
        </div>

        <div class="section">
            <h2>What I Learned</h2>
            <ul>
                <li>Web scraping using BeautifulSoup and requests</li>
                <li>Data extraction and cleaning</li>
                <li>Handling HTTP requests and headers</li>
                <li>Saving and structuring data in JSON format</li>
                <li>Basic principles of web scraping ethics</li>
            </ul>
        </div>

        <div class="section">
            <h2>Future Notes</h2>
            <ul>
                <li>Always check the website's <code>robots.txt</code> file before scraping.</li>
                <li>Use appropriate headers to mimic a browser request.</li>
                <li>Be respectful of the website's bandwidth by adding delays between requests.</li>
                <li>Keep the scraping logic modular to easily adapt to website structure changes.</li>
            </ul>
        </div>

        <div class="section">
            <h2>Project Tutorial</h2>
            <h3>Installation</h3>
            <ol>
                <li>
                    <strong>Clone the repository:</strong>
                    <div class="code-block">
                        <pre>git clone https://github.com/yourusername/gis-job-scraper.git
cd gis-job-scraper</pre>
                    </div>
                </li>
                <li>
                    <strong>Create a virtual environment:</strong>
                    <div class="code-block">
                        <pre>python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`</pre>
                    </div>
                </li>
                <li>
                    <strong>Install the required packages:</strong>
                    <div class="code-block">
                        <pre>pip install -r requirements.txt</pre>
                    </div>
                </li>
            </ol>

            <h3>Usage</h3>
            <ol>
                <li>
                    <strong>Run the scraper script:</strong>
                    <div class="code-block">
                        <pre>python scraper.py</pre>
                    </div>
                </li>
                <li>
                    <strong>Check the output:</strong>
                    <p>The scraped job data will be saved in <code>jobs.json</code>.</p>
                </li>
            </ol>
        </div>

        <div class="section">
            <h3>Code Example</h3>
            <div class="code-block">
                <pre>

# Define headers to mimic a web browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}                </pre>
            </div>
            <p>This script is designed to scrape GIS job listings from Indeed. Adjust the URL and HTML parsing logic for different websites.</p>
            <p>The script includes headers to mimic a real browser and avoid common blocking mechanisms.</p>
        </div>

        <div class="section">
            <h2>Additional Resources</h2>
            <ul>
                <li><a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/">BeautifulSoup Documentation</a></li>
                <li><a href="https://docs.python-requests.org/en/master/">Requests Documentation</a></li>
                <li><a href="https://docs.python.org/3/library/json.html">JSON in Python</a></li>
            </ul>
        </div>

        <div class="section">
            <h2>License</h2>
            <p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>
        </div>
   
   </div>
</body>
</html>
