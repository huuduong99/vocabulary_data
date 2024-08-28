from bs4 import BeautifulSoup
import requests
import pandas as pd


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

def getInfomationWord(word):
  response = requests.get("https://dictionary.cambridge.org/dictionary/english/{word}")
  soup = BeautifulSoup(response.content, 'html.parser')
  links = soup.find_all('a', target='_blank')
  words = [link.text for link in links]
  return words



response = requests.get("http://sherwoodschool.ru/vocabulary/proficiency/")
# print(response.content)
words = extract_words_from_links(response.content)
write_data_to_excel(words)
print(words)  # Output: ['ability', 'abandon']