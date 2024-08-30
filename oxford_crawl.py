from bs4 import BeautifulSoup
import requests
import pandas as pd
import time


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
        pronunciation_uk_element = li.find('div', class_='pron-uk')
        pronunciation_us_element = li.find('div', class_='pron-us')

        pos = pos_element.text if pos_element else None
        level = level_element.text.strip() if level_element else None
        pronunciation_uk = base_url + pronunciation_uk_element.get('data-src-mp3') if pronunciation_uk_element else None
        pronunciation_us = base_url + pronunciation_us_element.get('data-src-mp3') if pronunciation_us_element else None

        wordInfo = [index,word,pos,level,pronunciation_uk,pronunciation_us]

        print(wordInfo)
        filtered_data.append(wordInfo)
        index += 1

    return filtered_data


def write_data_to_excel(words):
 
  vocabulary_df = pd.DataFrame(
      data=words,
      columns=['index','word','pos','level','pronunciation_uk','pronunciation_us']
  )

  vocabulary_df.to_excel(
      'oxford_vocabulary.xlsx',
      index=False
  )




words = extract_word_data("https://www.oxfordlearnersdictionaries.com/wordlists/oxford3000-5000")
write_data_to_excel(words)
