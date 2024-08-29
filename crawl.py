from bs4 import BeautifulSoup
import requests
import pandas as pd
import time


def extract_words_from_links(html_content):
  """Lọc các từ trong thẻ a có thuộc tính target="_blank" từ nội dung HTML.

  Args:
    html_content: Nội dung HTML cần xử lý.

  Returns:
    Danh sách các từ đã lọc.
  """

  soup = BeautifulSoup(html_content, 'html.parser')
  links = soup.find_all('a', target='_blank')
  words = [link.text for link in links]
  return words

def write_data_to_excel(words):
  
 
  seattle_restaurants_df = pd.DataFrame(
      data=words,
      columns=['word']
  )

  seattle_restaurants_df.to_excel(
      'vocabulary.xlsx',
      # Don't save the auto-generated numeric index
      index=False
  )

def getWordInfomation(word):
  headers = requests.utils.default_headers()
  headers.update(
      {
          'User-Agent': 'Your Name/Project (optional, for identification)'
      }
  )

  url = "https://dictionary.cambridge.org/dictionary/english/" + word

  for attempt in range(5):
    try:
      response = requests.get(url, headers=headers)
      response.raise_for_status()  # Raise an exception for error status codes
      break
    except requests.exceptions.RequestException as e:
      print(f"Error: {e}")
      time.sleep(5)  # Wait for 5 secon

  soup = BeautifulSoup(response.content, 'html.parser')

 
  response = requests.get("https://dictionary.cambridge.org/dictionary/english/"+word, headers=headers)

  soup = BeautifulSoup(response.content, 'html.parser')

  ipa_element = soup.find('span', class_='ipa dipa lpr-2 lpl-1')
  ipa = ipa_element.text if ipa_element else None

  level_element = soup.find('span', class_='def-info ddef-info')
  level = level_element.text if level_element else None



  return [ipa,level]



# response = requests.get("http://sherwoodschool.ru/vocabulary/proficiency/a")
# words = extract_words_from_links(response.content)
# print(words)  # Output: ['ability', 'abandon']
# write_data_to_excel(words)
word = getWordInfomation("alert")
print(word)
