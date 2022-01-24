from bs4 import BeautifulSoup
import urllib.request
url = 'https://www.amazon.in/CASE-Microphone-Streaming-Recording-Conferencing/dp/B08TMKP7JZ/ref=sr_1_1_sspa?crid=2POJOXCKV25AD&dchild=1&keywords=web+cam+1808p+with+mic&qid=1614884582&sprefix=web+cam+%2Caps%2C399&sr=8-1-spons&psc=1&smid=APF8KRJZ1HH7F&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzTVhKQVQwQ0pBMzNaJmVuY3J5cHRlZElkPUEwMTM0MDkyM0ZJSjVPOU5KMVJGQyZlbmNyeXB0ZWRBZElkPUEwNjQ5MDc4VVg2U0NUNjU2VlUyJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='

sauce = urllib.request.urlopen(url).read()
soup = BeautifulSoup(sauce, "html.parser")
price  = soup.find(id="priceblock_ourprice").get_text()
print(price)




