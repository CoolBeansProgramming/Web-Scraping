import requests
from bs4 import BeautifulSoup


def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=java&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    for index, job in enumerate(jobs):
        added_date = job.find('span', class_='sim-posted').span.text
    
        if ('few' in added_date) or ('1' in added_date):
            company_name = job.find('h3', class_='joblist-comp-name').text.upper()
            experience = job.find('ul', class_='top-jd-dtl clearfix').text.strip()[11:20]
            skills = job.find('span', class_= 'srp-skills').text.replace(' ','')
            location = job.find('ul', class_='top-jd-dtl clearfix').text.strip()[34:]
            info = job.header.h2.a['href']
            
            
            with open(f'posts/{index}.txt','w') as f:
                f.write(f'Company: {company_name.strip()}\n')
                f.write(f'Experience: {experience}\n')
                f.write(f'Skills: {skills.strip()}\n')
                f.write(f'Location: {location}\n')
                f.write(f'Info: {info}')
            print(f'File saved: {index}')
        
            
if __name__ == '__main__':
    find_jobs()