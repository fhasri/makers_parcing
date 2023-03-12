import requests

from bs4 import BeautifulSoup

import csv
'''Вы должны спарсить сайт 
https://www.kivano.kg/mobilnye-telefony. Как результат вы должны получить: 
1. Наименование всех телефонов 
2. Цену каждого продукта(в KGS) 
3. И ссылка к фотографии 
4. Все это записать в CSV файл 
Рекомендации: 
1. BeautifulSoup 
2. CSV 
3. Requests 
Дополнительно(по желанию): 
1. Ваш парсинг скрипт должен выполняться каждые 60 минут
'''

"""Here is nothing have to be changed only link we are giving, all other codes are similar (html code). Needed to just change the linke  that's all it requeres. Works pretty simple. """


def write_to_csv(data):
    with open('data1.csv', 'a') as file:
        write = csv.writer(file)
        write.writerow([data['title']]) #, data['image'], data['price']])
        write.writerow([data['image']])
        write.writerow([data['price']])

def get_html(url):
    response = requests.get(url)
    # print(response.text)
    return response.text

# url = 'https://www.kivano.kg/mobilnye-telefony'

# get_html(url)

def get_total_pages(html):
    soup = BeautifulSoup(html,'lxml')
    page_list = soup.find('div',class_ = 'pager-wrap').find('ul', class_ = 'pagination').find_all('li',)
    # print(page_list)
    last_page = page_list [-1].text
    return int(last_page)


get_total_pages(get_html('https://www.kivano.kg/mobilnye-telefony'))


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    # print(soup)
    products = soup.find('div' , class_ = 'list-view').find_all('div', class_= 'item')
    # print(product)
    for product in products:
        title = product.find('div', class_ = 'listbox_title').find('strong').text.strip()
        image = 'https://www.kivano.kg/'  + product.find('img').get('src')
        price = product.find('div', class_="listbox_price text-center").find('strong').text.strip()
        dict_ = {'title': title, 'image': image, 'price': price}

    # print(dict_)
        write_to_csv(dict_)
    
with open('data1.csv' , 'w') as file: 
    write = csv.writer(file)
    write.writerow(['title    ' ,    'image      ', 'price           '])


# get_data(get_html(url))

def main():
    url = 'https://www.kivano.kg/mobilnye-telefony'
    pages = '?page='
    html = get_html(url)
    number = get_total_pages(html)
    get_data(html)

    for i in range(2,number+1):
        url_with_page = url + pages + str(i)
        html = get_html(url_with_page)
        get_data(html)
        # print(url_with_page)


main()






