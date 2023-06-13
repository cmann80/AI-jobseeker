def scrape_careers_page(url):
    import requests
    from bs4 import BeautifulSoup
    
    # navigate to careers page
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # find link to job search page
    search_link = soup.find('a', string='Search Jobs')['href']
    
    # navigate to job search page
    response = requests.get(search_link)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # find job listings with keyword "AI"
    job_items = soup.find_all('div', class_='job-item')
    for job in job_items:
        if 'AI' in job.text:
            # navigate to job description page
            job_link = job.find('a')['href']
            response = requests.get(job_link)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # extract relevant information
            company_name = soup.find('div', class_='company-name').text.strip()
            job_title = soup.find('h1', class_='job-title').text.strip()
            job_description_url = job_link
            
            # create JSON object
            job_info = {
                'company_name': company_name,
                'job_title': job_title,
                'job_description_url': job_description_url
            }
            
            return job_info
        
scrape_careers_page("https://careers.google.com/jobs/")