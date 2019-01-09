from bs4 import BeautifulSoup



def read_file():
    file = open('intro_to_soup_html.html')
    data = file.read()
    file.close()
    return data


# Mqke soup
# Syntax = BeautifulSoup(html_data,parser)
# Our parser is lxml or html.parser which we have installed

html_file = read_file()

print(html_file)

soup = BeautifulSoup(html_file, 'lxml') # or for those who haven't installed lxml - BeautifulSoup(html_data,parser)

# soup prettify

soup.prettify()

# identify tags

