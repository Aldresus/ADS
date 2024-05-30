#curl https://thispersondoesnotexist.com --output \Users\leobo\Desktop\ads\test2.png
#fetch this url 100 times and store the images in a folder
import os
import requests

url = "https://thispersondoesnotexist.com"

for i in range(10000):
    r = requests.get(url)
    with open(f"dataset/10000/fake/{i}.png", "wb") as f:
        f.write(r.content) 
