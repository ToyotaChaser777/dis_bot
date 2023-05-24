import random as ran
import requests

choices = [('https://randomfox.ca/floof/', 0.3), ('https://random.dog/woof.json', 0.5), ('https://random-d.uk/api/random', 0.2)]

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""

    for i in range(pass_length):
        password += ran.choice(elements)

    return password

def smail():
    elements = ['(͡° ͜ʖ ͡°)', '[✖‿✖]', '[̲̅$̲̅(̲̅5̲̅)̲̅$̲̅]', '(づ｡◕‿‿◕｡)づ', 'ᕦ(ò_óˇ)ᕤ', '(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ ✧ﾟ･: *ヽ(◕ヮ◕ヽ)']
    itog = ''

    for i in range(1):
        itog = ran.choice(elements)
    
    return itog

def coin():
    storoni = ['Орел', 'Решка']
    pobeda = ''
    
    for i in range(1):
        pobeda = ran.choice(storoni)
    
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

def weighted_choice(choices):
    total = sum(weight for choice, weight in choices)
    r = ran.uniform(0, total)
    cumulative_weight = 0
    for choice, weight in choices:
        cumulative_weight += weight
        if r <= cumulative_weight:
            return choice



def get_animal_image_url():    
    url = weighted_choice(choices)
    res = requests.get(url)
    data = res.json()
    print(data['url'])
    return data['url']
