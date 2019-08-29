from bs4 import BeautifulSoup
import requests

oreilly_data_search_html = requests.get('https://ssearch.oreilly.com/?q=data').text

oreilly_data_search_soup = BeautifulSoup(oreilly_data_search_html, 'html5lib')
data_search_results = oreilly_data_search_soup.find_all('article', { 'class': 'result' })
# print('data_search_results = %s' % data_search_results)
# print('first data_search_result = %s' % data_search_results[0])

# get titles and authors of books!!!
books_list_item_text = oreilly_data_search_soup.find_all('div', { 'class': 'book_text' })

def extract_title(div):
    title_paragraph = div.find('p', { 'class': 'title' })
    title = title_paragraph.find('a').text
    return title.strip()

def extract_author(div):
    author_paragraph = div.find_all('p')[1]
    author = author_paragraph.text[2:]
    return author

titles = [
    { 'title': extract_title(book_text), 'author': extract_author(book_text) }
    for book_text
    in books_list_item_text
]

print('data titles on first page of search results = %s' % titles)
