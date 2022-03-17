import requests
from bs4 import BeautifulSoup
import lxml
import json

def html_code(url):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    }
    req = requests.get(url, headers)
    print(req.text)
    with open('sereals_top.html', 'w', encoding="utf-8") as file:
        file.write(req.text)

film_urls = []
film_name_url = []

with open('sereals_top.html', encoding="utf-8") as file:
    scr = file.read()
    soup = BeautifulSoup(scr, 'lxml')
    film_name = soup.find_all('div', class_='vid-t')
    film_url = soup.find('div', class_='cont-body-films').find_all('a')
    for fi_ur in film_url:
        film_urls.append(fi_ur.get('href'))

for i in range(len(film_name)):
    film_name_url.append(
        {
            'name': f'{film_name[i].text}',
            'url': f'{film_urls[i]}'
        }
    )
def html_code_2(url, name):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    }
    req = requests.get(url, headers)
    with open(f'data/{name}.html', 'w', encoding="utf-8") as file:
        file.write(req.text)

for i in range(len(film_name_url)):
    url = film_name_url[i].get('url')
    name = film_name_url[i].get('name').replace(':', '')
    with open(f'data/{name}.html', encoding="utf-8") as file:
        scr = file.read()
        soup = BeautifulSoup(scr, 'lxml')
        mediablock = soup.find('div', class_='mediablock').text.strip()
        country = mediablock[15:]
        year = mediablock[:4]
        grade = mediablock[5:14]
        film_name_url[i].update(
            {
            'country': f'{country}',
            'year': f'{year}',
            'grade': f'{grade}'
            }
        )

with open('dict_film.json', 'w', encoding="utf-8") as file:
    json.dump(film_name_url, file, indent=4, ensure_ascii=False)



