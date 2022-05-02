import datetime

import requests
from bs4 import BeautifulSoup
from django.shortcuts import render


def home(request):
    currentdate = datetime.date.today()
    formatDate = currentdate.strftime("%d/%m/%Y")

    url = "https://www.imdb.com/chart/moviemeter/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    table = soup.find('table', {'class': 'chart full-width'})
    rows = table.find_all('tr')
    number = 1
    movies = []
    for row in rows:
        image = row.find('img')
        if image:
            movies.append({"number": number, "title": image['alt'], "image": image['src']})
            number += 1
    return render(request, "movierank/pages/home.html", {'movies': movies, 'format_date': formatDate})
