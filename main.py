from text import book56zw,aixdzs

if __name__ == '__main__':
    # keyword = "斗破"
    # book_list = aixdzs.search(keyword)
    # print(book_list)

    # book = {'name': '从斗罗的世界归来', 'author': '斗罗斗破无敌', 'img': 'https://img22.aixdzs.com/81/a9/81a9da54ee5737bafc66777d63705781.jpg', 'url': '/novel/%E4%BB%8E%E6%96%97%E7%BD%97%E7%9A%84%E4%B8%96%E7%95%8C%E5%BD%92%E6%9D%A5'}
    # catalog_list = aixdzs.catalog(book)
    # print(catalog_list)
    #
    catalog = {'name': '第1章 获得双生武魂', 'url': '/read/251/251499/p2.html'}
    msg = aixdzs.detail(catalog)
    print(msg)
