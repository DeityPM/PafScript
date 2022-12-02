import requests
from bs4 import BeautifulSoup
import urllib.parse

"""
name:五六中文网
site:https://www.56zw.com/
"""


def search(keyword: str):
    encode_key = urllib.parse.quote(keyword, encoding="gbk")
    r = requests.get(
        f"https://www.56zw.com/modules/article/search.php?searchkey={encode_key}&searchtype=articlename&page=1")
    r.encoding = "gbk"
    html = BeautifulSoup(r.text, "lxml")
    result = []
    for book in html.select('#nr'):
        author = book.select_one('td:nth-child(3)').text
        raw = book.select_one('td:nth-child(1)')
        title = raw.text
        href = raw.a.get("href")
        book_id = href[21:27].split("_")
        img = f"https://www.56zw.com/files/article/image/{book_id[0]}/{book_id[1]}/{book_id[1]}s.jpg"
        result.append({
            "name": title,
            "author": author,
            "img": img,
            "url": href
        })
    return result


def catalog(data: dict):
    r = requests.get(data["url"])
    r.encoding = "gbk"

    html = BeautifulSoup(r.text, "lxml")
    result = []
    start_foreach = 0
    for item in html.select('#list > dl > dd,dt'):
        if start_foreach > 1:
            title = item.text
            url = item.a.get("href")
            result.append({
                "name": title,
                "url": url
            })

        elif item.name == "dt":
            start_foreach = start_foreach + 1

    return result


def detail(data: dict):
    r = requests.get("https://www.56zw.com/" + data["url"])
    r.encoding = "gbk"

    html = BeautifulSoup(r.text, "lxml")
    title = html.select_one("div.bookname > h1").text
    content = html.select_one("#content").text.replace(u'\xa0', u' ').replace(u'\r\n', "")
    return {
        "title": title,
        "message": content
    }
