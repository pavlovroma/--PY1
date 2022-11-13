from pprint import pprint
i = 7
pop = {
    'bin': bin(i),'oct': oct(i),'hex': (i) in range(16) }

pprint(pop)
