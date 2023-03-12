
import requests

from bs4 import BeautifulSoup

import csv

"""● Спарсить mashina.kg, категорию:
1.Название всех моделей.
2.Цену всех моделей
3.Изображение всех моделей
4.Краткое описание всех моделей
5.Записать все в csv файл

● Библиотеки, которыми вы должны воспользоваться:
BeautifulSoup4
csv
requests"""

# def write_to_csv(data):
#     with open('mashina.kg', 'a') as file:
#         write = csv.writer(file)
#         write.writerow([data['title']])
#         write.writerow([data['image']])
#         write.writerow([data['price']])




# def get_html(url):
#     response = requests.get(url)
#     # print(response.text)
#     return response.text

# url = 'https://www.mashina.kg/search/lexus/all/?currency=2&sort_by=upped_at%20desc'

# get_html(url)

# def get_total_pages(html):
#     soup = BeautifulSoup(html, 'lxml')
#     page_list = soup.find('ul', class_ = 'pagination').find_all('li')
#     last_page = page_list[-2].text
#     return int(last_page)
#     print(page_list)

# get_total_pages(get_html('https://www.mashina.kg/search/lexus'))

# def get_data(html):
#     soup = BeautifulSoup(html, 'lxml')
#     cars = soup.find('div',class_="search-results-table").find_all('div')#.find_all('a')
#     for car in cars:
        
#         try:
#             title = car.find('div', class_ = 'block title').find('h2',class_ = 'name').text.strip()
#             # print(title)
#         except:
#             title = ''
#         # print(title)


#         try:
#             image = car.find('div', class_ = 'thumb-item-carousel').find('img')
#             # print(image)
        
#         except:
#             image = 'working not correctly'
#         # print(image)

#         try:
#             price = car.find('div', class_="block price").text #. #find(title_="или ~ 450 000 сом ").text
#             # print(price)
#         except:
#             price = ''

#         data = {'title': title, 'image': image,'price': price}

#         write_to_csv(data)

#     # print(cars)

# get_data(get_html('https://www.mashina.kg/search/lexus/all/?currency=2&sort_by=upped_at+desc&page=1'))

# with open('mashina.kg', 'w') as file:
#     write = csv.writer(file)
#     write.writerow(['title             ', 'image                 ', 'price            '])

# def main():
#     url = 'https://www.mashina.kg/search/lexus/all/?currency=2&sort_by=upped_at+desc&page='
#     pages = 1
#     html = get_html(url)
#     number = get_total_pages(html)
#     i = 1

#     # while i <= number:
#     for i in range(3,number+1):
#         # print(i)
#         # url = f'https://www.mashina.kg/search/lexus/all/?currency=2&sort_by=upped_at+desc&page={i}'
#         url_with_pages = url + str(i)
#         html = get_html(url_with_pages)
#         # number = int(get_total_pages(html))
#         i+=1
#         # if not BeautifulSoup(html, 'lxml').find()
#         get_data(html)

# main()

# url_seconed_page = 'https://www.mashina.kg/search/lexus/all/?currency=2&sort_by=upped_at+desc&page=3'

# url = 'https://www.mashina.kg/search/lexus/all/?currency=2&sort_by=upped_at+desc&page=1'



###################################3

def write_to_csv(data):
    with open('mashina.csv','a') as file:
        write = csv.writer(file)
        write.writerow([data['title'],data['discription'], data['price'],data['image']])

def get_html(url):
    response = requests.get(url)
    return response.text
    # print(response.text)
    
    # url = 'https://www.mashina.kg/search/lexus/all/?currency=2&sort_by=upped_at%20desc'

# get_html('https://www.mashina.kg/search/lexus/all/?currency=2&sort_by=upped_at%20desc')


def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')
    page_list = soup.find('ul',class_="pagination" ).find_all('li')
    last_page = page_list[-4].text
    return int(last_page)

    # str(last_page)
    # print(type(int(last_page)))

# print(type(get_total_pages(get_html('https://www.mashina.kg/search/lexus/all/?currency=2&sort_by=upped_at%20desc'))))

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    cars = soup.find('div', class_ ="search-results-table").find_all('div', class_="list-item list-label")
    for car in cars:
        title = car.find('div', class_ = 'block title').text.strip()
        # print(title)
        price = car.find('div', class_="block price").find('strong').text.strip()
        # price = car.find('div', class_="block price").text.strip()
        # print(price)
        image = car.find('div', class_ = 'thumb-item-carousel').find('img')
        # image = car.find('div',class_='thumb-item-carousel').find('img').get('data-src')
        # image = car.find('div',class_='thumb-item-carousel').find('img').get('data-src').strip()


        # print(image)
        # disc = car.find('div',class_="block info-wrapper item-info-wrapper").text.strip()
        # print(disc)
        miles = car.find('div',class_='block info-wrapper item-info-wrapper').find('p', class_ = 'year-miles').text.strip()
        body = car.find('div',class_='block info-wrapper item-info-wrapper').find('p', class_ = 'body-type').text.strip()
        vol = car.find('div',class_='block info-wrapper item-info-wrapper').find('p', class_ = 'volume').text.strip()
        discription =  body + miles + vol
        # print(discription)
        data = {'title':title, 'discription':discription,'price':price ,'image': image}
        write_to_csv(data)

with open('mashina.csv','w') as file:
    write = csv.writer(file)
    write.writerow(['title','                            discription', '                          price','        image  '])


# def main():
#     url = 'https://www.mashina.kg/search/lexus/all/?currency=2&sort_by=upped_at+desc&page=1'
#     html = get_html(url)
#     get_data(html)

# main()

def main():
    url = 'https://www.mashina.kg/search/lexus/all/?currency=2&sort_by=upped_at+desc&page=1'
    # pages = 1
    html = get_html(url)
    number = get_total_pages(html)
    get_data(html)

    for i in range(2,112+1):
        # pages+=1
        print(i)
        url_with_page = url[:-1] + str(i)
        # print(url_with_page)
        html = get_html(url_with_page)
        get_data(html)

main()



# get_data(get_html('https://www.mashina.kg/search/lexus/all/?currency=2&sort_by=upped_at%20desc'))

# url = 'https://www.mashina.kg/search/lexus/all/?currency=2&sort_by=upped_at+desc&page=1'

# h = url[:-1] + str(2)
# # b = str(h)
# print(h)

