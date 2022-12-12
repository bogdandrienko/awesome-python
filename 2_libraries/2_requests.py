########################################################################################################################
# TODO get json data and write

import requests
import json

# HTTP (TCP/IP) - протоколы запросов
# request - запрос / response - ответ

# get - read
# post - create
# put (patch) - update
# delete - delete

# текст
# html
# картинки
# валюта - с сайтов банков
# цены - с сайтов маркетплейсов
# погода - с сайтов погоды
# реферат - с википедии

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/102.0.0.0 Safari/537.36'
}

url1 = "https://jsonplaceholder.typicode.com/posts/66"
response = requests.get(url=url1, headers=headers)

print(response, type(response))  # 200 OK <Response [200]> <class 'requests.models.Response'>
print(response.status_code, type(response.status_code))
print(response.content, type(response.content))
print(response.text, type(response.text))
print(response.json(), type(response.json()))

with open("data/new0.json", "w") as f:
    json.dump(response.json(), f)

url2 = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url=url2, headers=headers)

for index, json_obj in enumerate(response.json(), 1):
    with open(f"data/new{index}.json", "w") as f:
        json.dump(json_obj, f)

########################################################################################################################

########################################################################################################################
# TODO get html text data and write

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/102.0.0.0 Safari/537.36'
}

url1 = "https://ru.wikipedia.org/wiki/Python"
response = requests.get(url=url1, headers=headers)

with open("data/python.html", "w", encoding="utf-8") as f:
    f.write(response.text)

########################################################################################################################

########################################################################################################################
# TODO get image binary data and write

# url = "https://mirpozitiva.ru/wp-content/uploads/2019/11/1472042719_15.jpg"
url = "https://picsum.photos/320/240/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/102.0.0.0 Safari/537.36'
}
response = requests.get(url=url, headers=headers)

with open("temp/img.jpg", "wb") as opened_file:
    opened_file.write(response.content)

########################################################################################################################

########################################################################################################################
# TODO async get image binary data

import asyncio
import aiohttp

url = 'https://picsum.photos/600/600/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/102.0.0.0 Safari/537.36'
}


async def as_write_image_from_url(image_name: str) -> None:
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url, headers=headers) as response_instance:
            response = await response_instance.read()
            with open(f'data/{image_name}.jpg', mode='wb') as file:
                file.write(response)


def async_download_image():
    asyncio.run(asyncio.gather(*[as_write_image_from_url(f'img{i}') for i in range(1, 10 + 1)]))

########################################################################################################################
