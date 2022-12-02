def search(keyword: str):
    """
    搜索

    :param keyword:搜索关键词

    :return 书本列表,列表应为字典列表，字典应具有以下参数，可包含其他参数

    :return name:书本名称

    :return img:书本封面

    :return author:书本作者

    :return is_end:是否完结
    """
    pass


def catalog(data: str):
    """
    目录

    :param data: 搜索返回的字典

    :return 目录列表，列表应为字典列表，字典应具有以下参数，可包含其他参数

    :return name:章节名称

    """
    pass


def detail(data: str):
    """
    详情

    :param data:目录返回的字典

    :return 字典，应具有以下参数，可包含其他参数(暂无用)

    :return title:章节完整名称

    :return message:章节内容
    """
    pass
