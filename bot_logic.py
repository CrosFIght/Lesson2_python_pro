import random

def Coin():
    coin = random.randint(1,2)
    
    if coin == 1:
        coin_chosen = "heads"
    else:
        coin_chosen = "tails"
        
    return coin_chosen
    

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password
