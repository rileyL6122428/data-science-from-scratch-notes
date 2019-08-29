from bs4 import BeautifulSoup
import requests
wikipedia_home_page = requests.get('https://ja.wikipedia.org/wiki/メインページ').text
soup = BeautifulSoup(wikipedia_home_page, 'html5lib')

print('body = %s' % soup.find('body'))

first_paragraph = soup.find('p')
first_paragraph_text = first_paragraph.text
print('first paragraph = %s' % first_paragraph)
print('first paragraph text = %s' % first_paragraph_text)

first_link = soup.find('a')
first_link_id = first_link.get('id')
print('first link = %s' % first_link)
print('first link id = %s' % first_link_id)

all_links_with_id_attribute = [
    links for links in soup.find_all('a') if links.get('id')
]

print('all_links_with_id_attr = %s' % all_links_with_id_attribute)

lists_with_no_print = soup.find_all('ul', { 'class': 'noprint' })
print('list with no print = %s' % lists_with_no_print)
