# import requests
# from lxml import etree

# url = 'https://dldl1.nsbuket.cc/xiaoshuo/douluodalu/3.html'


# while True:

#     headers={
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
#     }  #根据要求使用代码伪装访问
#     resp = requests.get(url, headers=headers)  # 发送 GET 请求
#     resp.encoding = 'utf-8'  # 设置编码为 utf-8

#     e = etree.HTML(resp.text)  # 解析 HTML 内容
#     info = '\n'.join (e.xpath('//div[@class="m-post"]/p/text()'))
#     title = e.xpath('//h1/text()')[0]  # 获取小说标题
#     url = f'https://dldl1.nsbuket.cc{e.xpath("//tr/td[2]]/a/@href")[0]}'

#     with open('douluodalu.txt', 'w', encoding='utf-8') as f:
#         f.write(title + '\n\n'+info + '\n\n')  # 写入标题

#      # 获取下一页链接

#     # if url == 'https://dldl1.nsbuket.cc/xiaoshuo/douluodalu/':
#     #     print('已到达最后一页')
#     # break


import requests
from lxml import etree



url = 'https://dldl1.nsbuket.cc/xiaoshuo/douluodalu/3.html' #访问页面链接

while True:  # 循环访问页面，直到到达最后一页

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }  # 根据要求使用代码伪装访问

    resp = requests.get(url, headers=headers)  # 发送 GET 请求
    resp.encoding = 'utf-8'  # 设置编码为 utf-8


    e = etree.HTML(resp.text)  # 解析 HTML 内容
    info = '\n'.join(e.xpath('//div[@class="m-post"]/p/text()'))
    title = e.xpath('//h1/text()')[0]  # 获取小说标题
    url = f'https://dldl1.nsbuket.cc{e.xpath("//tr/td[2]/a/@href")[0]}'  # 获取下一页链接

    with open('斗罗大陆.txt', 'a', encoding='utf-8') as f:     # 以追加模式打开文件,如果是使用的w会把之前的内容覆盖掉
        f.write(title + '\n\n' + info + '\n\n')  # 写入标题和内容

        if url == 'https://dldl1.nsbuket.cc/xiaoshuo/douluodalu/':
            print('已到达最后一页')
            break