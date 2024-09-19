from bs4 import BeautifulSoup
import requests
import pandas as pd
import json


from bs4 import BeautifulSoup
import re

def extract_word_data(ur):
    base_url="https://www.oxfordlearnersdictionaries.com"
    headers = requests.utils.default_headers()
    headers.update(
        {
            'User-Agent': 'Your Name/Project (optional, for identification)'
        }
    )
    response = requests.get(ur,headers=headers)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')

    # Regular expression to match word links
    word_link_pattern = r'<a href="/definition/english/([^"]+)"a>'

    filtered_data = []
    index = 0
    li_elements = soup.find_all('li', attrs={'data-hw': True})

    # Extract word data from each 'li' element
    word_data = []
    for li in li_elements:
        word = li['data-hw']
        pos_element = li.find('span', class_='pos')
        level_element = li.find('span', class_='belong-to')

        pos = pos_element.text if pos_element else None
        level = level_element.text.strip() if level_element else None
        pronunciation_uk = getSound('us',word)
        pronunciation_us = getSound('uk',word)
        topic = getTopicname(word)
        wordInfo = [index,word,pos,level,pronunciation_uk,pronunciation_us,topic]

        print(wordInfo)
        filtered_data.append(wordInfo)
        index += 1

    return filtered_data


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

def getTopicname(word):

    url = f"https://www.oxfordlearnersdictionaries.com/definition/english/{word}_1"
    headers = requests.utils.default_headers()
    headers.update(
        {
            'User-Agent': 'Your Name/Project (optional, for identification)'
        }
    )
    response = requests.get(url,headers=headers)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    topic_name_element = soup.find('span', class_='topic_name')

    topic_name = topic_name_element.text.strip()if topic_name_element else None

    return topic_name

def write_data_to_excel(words):
 
  vocabulary_df = pd.DataFrame(
      data=words,
      columns=['index','word','pos','level','pronunciation_uk','pronunciation_us','topic']
  )

  vocabulary_df.to_excel(
      'oxford_vocabulary.xlsx',
      index=False
  )




words = extract_word_data("https://www.oxfordlearnersdictionaries.com/wordlists/oxford3000-5000")
write_data_to_excel(words)
