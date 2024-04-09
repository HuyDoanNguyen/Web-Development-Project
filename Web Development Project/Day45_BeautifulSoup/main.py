# from bs4 import BeautifulSoup
# # import lxml

# with open("bs4-start\\website.html", encoding='utf-8') as file:
#     contents = file.read()
    
# soup = BeautifulSoup(contents, 'html.parser')


# # print(soup.prettify())

# all_anchor_tags = soup.find_all(name="a")


# # for tag in all_anchor_tags:
# #     print(tag.getText())
# #     print(tag.get("href"))

# # heading = soup.find(name="h1", id="name")
# # print(heading)

# # company_url = soup.select_one(selector="#name")
# # print(company_url)

# heading=soup.select(".heading")
# print(heading)


# import requests
# from bs4 import BeautifulSoup
# import lxml

# response = requests.get("https://news.ycombinator.com/news")

# ys_web_page = response.text
# soup = BeautifulSoup(ys_web_page, "lxml")

# article_tag = soup.find_all(name="a", class_="storylink")
# article_texts = []
# article_links = []

# for tag in article_tag:
#     text = article_tag.getText()
#     link = article_tag.get("href")
#     article_links.append(link)
#     article_texts.append(text)
    
# article_upvotes.append(int(article.span.find(class_="score").contents[0].split()[0]))

# print(article_texts)
# print(article_links)
# print(article_upvotes)


# Thanks to Charlie for this code
# https://www.udemy.com/course/100-days-of-code/learn/#questions/19476080

from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, 'html.parser')

article_titles = []
article_links = []
for article_tag in soup.find_all(name="span", class_="titleline"):
    article_titles.append(article_tag.getText())
    article_links.append(article_tag.find("a")["href"])

article_upvotes = []
for article in soup.find_all(name="td", class_="subtext"):
    if article.span.find(class_="score") is None:
        article_upvotes.append(0)
    else:
        article_upvotes.append(int(article.span.find(class_="score").contents[0].split()[0]))

max_points_index = article_upvotes.index(max(article_upvotes))
print(
    f"{article_titles[max_points_index]}, "
    f"{article_upvotes[max_points_index]} points, "
    f"available at: {article_links[max_points_index]}."
)
