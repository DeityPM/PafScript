import requests
from bs4 import BeautifulSoup
import urllib.parse

"""
name:爱下电子书
site:https://www.aixdzs.com/
"""


def search(keyword: str):
    encode_key = urllib.parse.quote(keyword)
    r = requests.get(
        f"https://www.aixdzs.com/bsearch?q={encode_key}")
    html = BeautifulSoup(r.text, "lxml")
    result = []
    for book in html.select('div.box_k > ul > li'):
        info = book.select_one('.list_info')
        title = info.h2.a.text
        href = info.h2.a.get("href")
        author = info.span.a.text
        img = book.select_one(".list_img").a.img.get("src")
        result.append({
            "name": title,
            "author": author,
            "img": img,
            "url": href
        })
    return result


def catalog(data: dict):
    r = requests.get("https://www.aixdzs.com" + data["url"])

    html = BeautifulSoup(r.text, "lxml")
    result = []
    for item in html.select('#i-chapter > ul > li.chapter'):
        title = item.a.text
        url = item.a.get("href")
        result.append({
            "name": title,
            "url": url
        })

    return result


def detail(data: dict):
    r = requests.get("https://www.aixdzs.com" + data["url"])

    html = BeautifulSoup(r.text, "lxml")
    title = html.select_one("div.line > h1").text
    content = html.select_one("div.content").text.replace(u'\xa0', u' ').replace(u'\r\n', "")
    return {
        "title": title,
        "message": content
    }
