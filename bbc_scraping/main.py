import fake_useragent
import requests
from bs4 import BeautifulSoup
import lxml
import json
import random

def get_data(url):
    user_agent = fake_useragent.UserAgent().random
    headers = dict(user_agent=user_agent)
    req = requests.get(url=url, headers=headers)
    with open('bbc.html', 'w', encoding="utf-8") as file:
        file.write(req.text)

def main():
    get_data('https://www.bbc.com/')

'''if __name__ == '__main__':
    main()'''
with open('bbc.html', encoding="utf-8") as file:
    scr = file.read()
    soup = BeautifulSoup(scr, 'lxml')
    news = soup.find('div', class_="content--block--modules").find('div', class_='module__content').find_all('li')
    url_news = []
    for i in news:
        div_previous = i.find('div', class_="media__content").find('h3', class_="media__title").find('a', class_="media__link").get('href')
        url_news.append('https://www.bbc.com' + div_previous)

'''for newss in url_news:
    name_url = newss.split('/')[-1]
    user_agent = fake_useragent.UserAgent().random
    headers = dict(user_agent=user_agent)
    req = requests.get(url=newss, headers=headers)
    with open(f'data/{name_url}.html', 'w', encoding="utf-8") as file:
        file.write(req.text)'''

for news_url in url_news:
    news_url = news_url.split('/')[-1]

    with open(f'data/{news_url}.html', encoding="utf-8") as file:
        scr = file.read()
        soup = BeautifulSoup(scr, 'lxml')
        url_news = 'https://www.bbc.com/' + news_url
        print('Url - ', url_news)
        title_news = soup.find('article').find('h1', id="main-heading").text
        print('Title - ', title_news)
        description_all_p = soup.find('article').find_all('p')
        description = []
        for p in description_all_p:

            if p.text != 'This video can not be played' and 'By' not in p.text:
                description.append(p.text)
        description = ''.join(description)
        print('Description - ', description)
        all_data = {
            'Url': f'{url_news}',
            'Title': f'{title_news}',
            'Description': f'{description}'
        }

    with open('bbc_news.json', 'a', encoding="utf-8") as file:
        json.dump(all_data, file, indent=4, ensure_ascii=False)

