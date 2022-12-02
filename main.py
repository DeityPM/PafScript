from text import book56zw

if __name__ == '__main__':
    # keyword = "斗破"
    # book_list = book56zw.search(keyword)
    # catalog_list = book56zw.catalog(book_list[0])
    # print(catalog_list)
    #
    catalog = {'name': '第一章 叶家嫡子', 'url': '/6_6249/4756942.html'}
    msg = book56zw.detail(catalog)
    print(msg)
