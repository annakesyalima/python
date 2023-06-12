from random import randint
from time import sleep
from operator import itemgetter
jogo = {'Luz': randint(1, 6),
        'Amity': randint(1, 6),
        'Gus': randint(1, 6),
        'Willow': randint(1, 6)}
ranking = []
for k, v in jogo.items():
    print(f'{k} scored {v} points')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
print('== BEST FLYER DERBY PLAYERS OF THE MATCH ==')
for i, v in enumerate(ranking):
    print(f'  {i+1}º place: {v[0]} with {v[1]}.')
    sleep(1)