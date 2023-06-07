def scrape_careers_page():
    import requests
    from bs4 import BeautifulSoup
    
    url = "https://careers.microsoft.com/us/en/search-results?keywords=&from=0&to=100&sort_by=relevance&category=&location=&job_function=&brand=&language=&"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    job_listings = soup.find_all('div', class_='job-listing')
    
    for job in job_listings:
        company_name = job.find('div', class_='job-listing__company').text.strip()
        job_title = job.find('div', class_='job-listing__title').text.strip()
        job_url = "https://careers.microsoft.com" + job.find('a')['href']
        
        print("Company Name:", company_name)
        print("Job Title:", job_title)
        print("Job Description URL:", job_url)
        
scrape_careers_page()