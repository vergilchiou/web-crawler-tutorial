import requests
from bs4 import BeautifulSoup
import urllib.parse


Y_DICT_URL= 'https://tw.dictionary.yahoo.com/dictionary?p='


def get_web_page(url, query):
    query = urllib.parse.quote_plus(query)
    resp = requests.get(
        url+query,
        headers={'Referer': 'https://tw.dictionary.yahoo.com/dictionary?'}
    )
    if resp.status_code != 200:
        print('Invalid url:', resp.url)
        return None
    else:
        return resp.text


def get_dict_info(dom):
    soup = BeautifulSoup(dom, 'html5lib')
    for li in soup.find('ul', 'explanations').find_all('li', 'exp-item'):
        print(li.text)


if __name__ == '__main__':
    #page = get_web_page(Y_DICT_URL, '非常')
    page = get_web_page(Y_DICT_URL, 'out of order')
    if page:
        get_dict_info(page)