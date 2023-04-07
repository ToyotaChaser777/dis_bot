import random as r

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
