import random
import requests

def Coin():
    coin = random.randint(1,2)
    
    if coin == 1:
        coin_chosen = "heads"
    else:
        coin_chosen = "tails"
        
    return coin_chosen

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>1234567890abcdefgfijklmnoqprstuvwyzxABCDEFGHIJKLMNOQPRSTUWXYZ"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password
