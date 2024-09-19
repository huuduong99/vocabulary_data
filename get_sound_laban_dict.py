from bs4 import BeautifulSoup
import requests
import json

from bs4 import BeautifulSoup


def getSound(language,word):

    url = f'https://m.dict.laban.vn/ajax/getsound?accent={language}&word={word}&type=mobile'

    referer = f'https://m.dict.laban.vn/en_vn/find?keyword={word}'
    host = 'm.dict.laban.vn'

    headers = requests.utils.default_headers()
    headers.update(
        {
            'Referer': referer,
            'Host': host,
            'Content-Type': 'application/json',
        }
    )
    response = requests.get(url,headers=headers)

    parsed_data = json.loads(response.text)
    return parsed_data["data"]



word_us = getSound('us','above')
word_uk = getSound('uk','above')


print(word_us)
print(word_uk)
