import requests 
from bs4 import BeautifulSoup


CLIENT_ID = "b650b86caf1e4f63bda33222e80b1f3b"
CLIENT_SECRET = "c1e35494e7664c7fb596fbd7b392260a"

input_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")


URL="https://www.billboard.com/charts/hot-100/"


request = requests.get(URL+input_date+"/")
website_html = request.text

soup = BeautifulSoup(website_html, "html.parser")

song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

print(song_names)

