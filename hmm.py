from pprint import pprint

with open('what.txt', 'r+', encoding='utf-8') as file:
    rua = file.read()
    rue = rua.split(' ')

pprint(rua)
pprint(rue)

# 45 2A 3A 5F 50 -> 10010

