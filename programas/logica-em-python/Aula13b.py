n = str(input('Digite seu nome: '))


print(n.strip())
print(n.split())
print(f'O seu nome tem {len(n)} caracteres')
print(f'O seu nome tem {n.count("a")} As')
print(f"Você tem Maria no seu nome: {'maria' in n}")
print(n.replace("anna", "mana"))
print(f"O seu nome em maiusculo é {n.upper()}")
print(f'O seu nome em minusculo é {n.lower()}')
print(f'O seu nome capitalizado é {n.capitalize()}')
print(f'O seu nome capitalizado é {n.title()}')
print('-'.join(n))



