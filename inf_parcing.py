import requests

from bs4 import BeautifulSoup

import csv



def get_html(url):
    response = requests.get(url)
    # print(response.text)
    return response.text

url = 'https://www.mashina.kg/search/all/?page=2'


get_html(url)

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    # print(soup)
    # products = soup.find('div',class_ = 'list-item list-label').find('div',class_='block title')
    # products = soup.find('div',class_ = 'list-item list-label').find('a').text
    cars = soup.find('div',class_="search-results-table").find_all('div')#.find_all('a')
    for car in cars:
        try:
            title = car.find('div',class_ = "block title").text.strip()
            # title = car.find('h2')#,class_ = "name").text.strip()
        except:
            title = ""
        # print(title)

        try:
            image = car.find('div', class_ = 'thumb-item-carousel').find('img')

        except:
            image = 'working not correctly'
        print(image)

        # try:
        #     price = car.find('span', class_="catalog-item-price").text #. #find(title_="или ~ 450 000 сом ").text
        
        # except:
        #     price = ''

        # data = {'title': title, 'image': image,'price': price}

        # write_to_csv(data)

    # print(cars)

get_data(get_html(url))