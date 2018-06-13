from bs4 import BeautifulSoup
import urllib.request
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import time
davaiyan = {}
cause = {}
complication = {}
symptom = {}
diagnose = {}
def medicine_finder(choice):
    opts = Options()
    opts.set_headless()
    assert opts.headless
    import time
    browser = Firefox(options=opts)
    browser.get('https://www.drugs.com/')
    medicine = []
    search_form = browser.find_element_by_id('livesearch-main')
    search_form.send_keys(choice)
    search_form.submit()
    time.sleep(2)
    first_link = browser.find_element_by_css_selector('div.snippet:nth-child(2) > h3:nth-child(1) > a:nth-child(1)')
    first_link.click()
    time.sleep(2)
    medication_link = browser.find_element_by_css_selector('.visible-links > li:nth-child(3) > a:nth-child(1)')
    medication_link.click()
    time.sleep(2)
    page = browser.page_source
    soup  = BeautifulSoup(page,'html.parser')
    dava = []
    for row in soup.findAll('table')[0].tbody.findAll('tr'):
        medicine = row.find_all('a',{'class':'condition-table__drug-name__link'})
        if len(medicine)>0:
            dava.append(medicine[0].text)
    return dava

site = "https://www.nhp.gov.in"

def introduction(input_disease):
    page = urllib.request.urlopen(site+'/disease/'+input_disease)
    soup = BeautifulSoup(page,'html.parser')
    return  soup.find('div',{'id':'Introduction'}).text.strip().replace('\n\n','\n')

def symptoms(input_disease):
    page = urllib.request.urlopen(site+'/disease/'+input_disease)
    soup = BeautifulSoup(page,'html.parser')
    return  soup.find('div',{'id':'Symptoms'}).text.strip().replace('\n\n','\n')
    # for k,v in symptom.items():
    #     print(k,":",v)

def causes(input_disease):
    page = urllib.request.urlopen(site + '/disease/' + input_disease)
    soup = BeautifulSoup(page, 'html.parser')
    return soup.find('div', {'id': 'Causes'}).text.strip().replace('\n\n', '\n')

def diagnosis(input_disease):
    page = urllib.request.urlopen(site + '/disease/' + input_disease)
    soup = BeautifulSoup(page, 'html.parser')
    return soup.find('div', {'id': 'Diagnosis'}).text.strip().replace('\n\n', '\n')

def complications(input_disease):
    page = urllib.request.urlopen(site + '/disease/' + input_disease)
    soup = BeautifulSoup(page, 'html.parser')
    if len(soup.find('div', {'id': 'Complications'}).text.strip().replace('\n\n', '\n'))>10:
        return  soup.find('div', {'id': 'Complications'}).text.strip().replace('\n\n', '\n')
    else:
        return soup.find('div', {'id': 'Management'}).text.strip().replace('\n\n', '\n')

# def get_location():
#     import requests
#     import json
#     send_url = 'http://api.zippopotam.us/IN/492001'
#     r = requests.get(send_url)
#     r = r.json();
#     a = []
#     for i in r:
#         for j in r['places']:
#             lat = j['latitude']
#             lon = j['longitude']
#             a.append(lat)
#             a.append(lon)
#             break
#         break
#     return a
#
# def get_doctor():
#     latlon = get_location()
#     lat = latlon[0]
#     lon = latlon[1]
#     import requests
#     send_url = 'https://api.betterdoctor.com/2016-03-01/doctors?location='+lat+'%2C'+lon+'%2C100&skip=0&limit=10&user_key=3e793332c913070b13242550b61af2c3'
#     r = requests.get(send_url)
#     r = r.json()
#     for i in r['data']:
#         for j in i['practices']:
#             return j['name']
#
# get_doctor()
