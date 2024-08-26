from bs4 import BeautifulSoup
import requests

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

# Ví dụ sử dụng:
html_string = """
<html>
<body>
  <a href="http://dictionary.cambridge.org/dictionary/english-russian/ability" target="_blank">ability</a>
  <a href="http://dictionary.cambridge.org/dictionary/english-russian/abandon" target="_blank">abandon</a>
  <a href="http://dictionary.cambridge.org/dictionary/english-russian/abbey">abbey</a>  </body>
</html>
"""

response = requests.get("http://sherwoodschool.ru/vocabulary/proficiency/")
# print(response.content)
words = extract_words_from_links(response.content)
print(words)  # Output: ['ability', 'abandon']