import requests
from bs4 import BeautifulSoup

baseurl = 'https://indeks.kompas.com/?site=all&date=2021-03-18'
page = requests.get(baseurl)
soup = BeautifulSoup(page.content, 'html.parser')

jumlah_page = soup.find(
        'a', class_='paging__link--prev').get('data-ci-pagination-page')


for i in range(1, int(jumlah_page)):
    url = baseurl + '&page=' + str(i)
   
    page = requests.get(url)
    if page.status_code == 200:
        soup = BeautifulSoup(page.content, 'html.parser')
        kompas = soup.find_all('div', class_='article__list')
        
        result = []
        for q in kompas:
            title = q.find('h3', class_='article__title--medium').text
            category = q.find('div', class_='article__subtitle--inline').text
            url = q.find('a', class_='article__link').get('href')
            date = q.find('div', class_='article__date').text
            result.append({
                'title': title,
                'category': category,
                'url': url,
                'date': date
            })

print(result)
