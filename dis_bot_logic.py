import random as r
import requests

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""

    for i in range(pass_length):
        password += r.choice(elements)

    return password

def smail():
    elements = ['(͡° ͜ʖ ͡°)', '[✖‿✖]', '[̲̅$̲̅(̲̅5̲̅)̲̅$̲̅]', '(づ｡◕‿‿◕｡)づ', 'ᕦ(ò_óˇ)ᕤ', '(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ ✧ﾟ･: *ヽ(◕ヮ◕ヽ)']
    itog = ''

    for i in range(1):
        itog = r.choice(elements)
    
    return itog

def coin():
    storoni = ['Орел', 'Решка']
    pobeda = ''
    
    for i in range(1):
        pobeda = r.choice(storoni)
    
    return pobeda

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']

def get_fox_image_url():    
    url = 'https://randomfox.ca/floof/'
    res = requests.get(url)
    data = res.json()
    return data['url']

def get_anime_image_url(filter):
    url = 'https://kitsu.io/api/edge/anime?filter[text]='+ filter
    res = requests.get(url)
    data = res.json()
    return data['url']

