# def scrape_careers_page():
#     import requests
#     from bs4 import BeautifulSoup
    
#     url = "https://careers.microsoft.com/us/en/search-results?keywords=&from=0&to=100&sort_by=relevance&category=&location=&job_function=&brand=&language=&"
#     page = requests.get(url)
#     soup = BeautifulSoup(page.content, 'html.parser')
    
#     job_listings = soup.find_all('div', class_='job-listing')
    
#     for job in job_listings:
#         company_name = job.find('div', class_='job-listing__company').text.strip()
#         job_title = job.find('div', class_='job-listing__title').text.strip()
#         job_url = "https://careers.microsoft.com" + job.find('a')['href']
        
#         print("Company Name:", company_name)
#         print("Job Title:", job_title)
#         print("Job Description URL:", job_url)
        


def scrape_careers_page():
    import requests
    from bs4 import BeautifulSoup
    
    # choose a random company from the list
    company = "Microsoft"
    
    # search for jobs with the keyword "AI"
    url = f"https://careers.microsoft.com/professionals/us/en/search-results?keywords=AI&from={company}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # click on the first entry of the results
    job_url = soup.find('a', class_='job-title-link')['href']
    job_response = requests.get(job_url)
    job_soup = BeautifulSoup(job_response.content, 'html.parser')
    
    # create a JSON object for the relevant information
    company_name = company
    job_title = job_soup.find('h1', class_='job-title').text.strip()
    job_description_url = job_url
    
    job_info = {
        "company_name": company_name,
        "job_title": job_title,
        "job_description_url": job_description_url
    }
    
    return job_info

scrape_careers_page()