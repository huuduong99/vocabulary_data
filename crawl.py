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

def write_data_to_excel():
  seattle_restaurants = [
    ['Bakery Nouveau', 'French', 4.6],
    ['Pizzeria Credo', 'Italian', 4.6],
    ['Chan Seattle', 'Korean', 4.4],
    ['Tilikum Place Cafe', 'European', 4.6],
    ['Ba Bar Capitol Hill', 'Vietnamese', 4.5]
  ]
 
  seattle_restaurants_df = pd.DataFrame(
      data=seattle_restaurants,
      columns=['Restaurant', 'Cuisine', 'Rating']
  )

  seattle_restaurants_df.to_excel(
      'seattle_restaurants.xlsx',
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
write_data_to_excel()
print(words)  # Output: ['ability', 'abandon']