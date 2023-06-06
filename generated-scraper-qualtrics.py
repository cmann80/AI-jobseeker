def scrape_careers_page():
    import requests
    from bs4 import BeautifulSoup
    
    url = 'https://www.qualtrics.com/careers/'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    job_listings = []
    
    for job in soup.find_all('div', class_='job-listing'):
        company_name = 'Qualtrics'
        job_title = job.find('h3', class_='job-title').text.strip()
        job_description_url = job.find('a')['href']
        
        job_listings.append({
            'company_name': company_name,
            'job_title': job_title,
            'job_description_url': job_description_url
        })
        print(job_listings)
        
    return job_listings

scrape_careers_page()