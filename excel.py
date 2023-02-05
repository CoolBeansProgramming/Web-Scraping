import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup

# get URL

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=java&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')


    company = []
    experience = []
    skills = []
    location = []
    information = []
    
    
    for job in jobs:
        added_date = job.find('span', class_='sim-posted').span.text
        if ('few' in added_date) or ('1' in added_date):
            try: 
                company.append(job.find('h3', class_='joblist-comp-name').text.upper())
            except:
                company.append(np.nan)
            try: 
                experience.append(job.find('ul', class_='top-jd-dtl clearfix').text.strip()[11:20])
            except:
                experience.append(np.nan)
            try: 
                skills.append(job.find('span', class_= 'srp-skills').text.replace(' ',''))
            except:
                skills.append(np.nan) 
            try:
                location.append(job.find('ul', class_='top-jd-dtl clearfix').text.strip()[34:])
            except:
                location.append(np.nan)
            try: 
                information.append(job.header.h2.a['href'])
            except:
                information.append(np.nan)

            final = pd.DataFrame()
            fields = {'Company': company, 'Experience':experience, 'Skills': skills, 'Location': location, 'Information': information}
            df = pd.DataFrame(fields)
            df.to_excel('jobs.xlsx')
            

if __name__ == '__main__':
    find_jobs()