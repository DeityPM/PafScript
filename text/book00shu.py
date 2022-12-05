import requests
from bs4 import BeautifulSoup
import urllib.parse

"""
name:00小说网
site:https://www.00shu.com/
"""


def search(keyword: str):
    r = requests.get(
        f"https://www.00shu.com/modules/article/search.php?q={keyword}")
    r.encoding = "utf-8"
    html = BeautifulSoup(r.text, "lxml")
    result = []
    for book in html.select('#nr'):
        author = book.select_one('td:nth-child(3)').text
        raw = book.select_one('td:nth-child(1)')
        title = raw.text
        href = raw.a.get("href")
        book_id = href[22:].split("/")
        img = f"https://www.00shu.com/files/article/image/{book_id[0]}/{book_id[1]}/{book_id[1]}s.jpg"
        is_end = book.select_one('td:nth-child(6)').text == "完成"
        result.append({
            "name": title,
            "author": author,
            "img": img,
            "url": href,
            "is_end": is_end
        })
    return result


def catalog(data: dict):
    r = requests.get(data["url"])
    r.encoding = "utf-8"

    html = BeautifulSoup(r.text, "lxml")
    result = []
    for item in html.select('#list > dl > dd'):
        title = item.text
        url = item.a.get("href")
        result.append({
            "name": title,
            "url": url
        })

    return result


def detail(data: dict):
    r = requests.get("https://www.00shu.com/" + data["url"])
    r.encoding = "utf-8"

    html = BeautifulSoup(r.text, "lxml")
    title = html.select_one("div.bookname > h1").text
    content = html.select_one("#content").text.replace(u'\xa0', u' ').replace(u'\r\n', "")
    return {
        "title": title,
        "message": content
    }
