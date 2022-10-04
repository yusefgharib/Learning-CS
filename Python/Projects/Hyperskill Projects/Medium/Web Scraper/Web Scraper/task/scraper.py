import requests, re, os
from bs4 import BeautifulSoup

pages, category = int(input()), input()
for i in range(1, pages + 1):
    links = []
    os.makedirs(f'Page_{i}')
    response = requests.get('https://www.nature.com/nature/articles/', params={'year': '2020', 'page': i})
    soup = BeautifulSoup(response.content, 'html.parser')
    for article in soup.find_all('article'):
        if article.find('span', 'c-meta__type').get_text() == category:
            links.append(article.find('a')['href'])

    for link in links:
        response = requests.get(f'https://www.nature.com{link}')
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find('h1', 'c-article-magazine-title').string
        file_name = re.sub(r'[^\w\s]', '', title).replace(' ', '_') + '.txt'
        with open(f'./Page_{i}/{file_name}', 'wb') as f:
            text = soup.find("div", "c-article-body").text.strip().encode()
            f.write(text)
