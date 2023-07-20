import requests 
from bs4 import BeautifulSoup as BS
page = 1
while True:
    #####r = requests.get("https://stopgame.ru/review/new/izumitelno/p" + str(page))
    #####https://stopgame.ru/review/p3?subsection=izumitelno
    
    r = requests.get('https://stopgame.ru/review/p'+ str(page)+'?subsection=izumitelno')
    
    #'https://stopgame.ru/review/p'+str(page)+'?subsection=izumitelno'
    if 'https://stopgame.ru/review/p'+str(3)+'?subsection=izumitelno'=='https://stopgame.ru/review/p3?subsection=izumitelno':
        print("ok")
    #_card__title_givrd_1 _card__title--has-subtitle_givrd_1
    html = BS(r.content, 'html.parser')
    items = html.select(".items > .article-summary")
    print('lol')
    #if(len(items)):
    for el in items:
        title = el.select('.caption > a')
        print( title[0].text )
    page += 1
    #else:
    #    break