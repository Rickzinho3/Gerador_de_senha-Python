import random
import os

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

lower = "abcdefghijklmnopqrstuvwxyz" 
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()."

mix_str = lower + upper + numbers + symbols

res = str(input('Deseja criar uma nova senha? [s/n] '))
if res == 's':
    password = "".join(random.sample
                   (mix_str, 10))
    print('')
    print("Password: "+password)
elif res == 'n':
    limpar()
    exit()
