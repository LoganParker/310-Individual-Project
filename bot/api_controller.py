import json
import random
import requests

base_url = "https://www.flickr.com/services/rest/?method=flickr.photos.search&api_key=fe84077f5a26a83d3a5a9c2626d9a391"


def update_image(search_tag):
    print("UPDATE IMAGE REACHED")
    addon = "&tags=" + search_tag + "&per_page=5&page=1&format=json"
    query_url = base_url + addon
    response = requests.get(query_url)
    #print(response.content[26:-1].decode())
    res_cont = response.content[14:-1].decode()
    print(res_cont)
    res_json = json.loads(res_cont)["photos"]["photo"][random.randint(0, 4)]
    return url_builder(res_json)


def url_builder(response):
    print("URL BUILDER REACHED")
    return "https://live.staticflickr.com/"+response['server']+"/"+response['id']+"_"+response['secret']+".jpg"
