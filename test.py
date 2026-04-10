import requests as reqeust;

response = reqeust.get('https://i.ytimg.com/vi/KczYjTVrK_o/hqdefault.jpg');
print(response.text);