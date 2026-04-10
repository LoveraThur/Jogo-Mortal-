import os, time, random
os.system('clear')

sort3 = random.randint(1,101)
sort4 = random.randint(1,101)
sort5 = random.randint(1,101)
sort6 = random.randint(1,101)
sort7 = random.randint(1,101)
list = (sort3, sort4, sort5, sort6, sort7)

time.sleep(2)
os.system('clear')
print(list)
contador = 0
while True:
    contador += 1 
    resposta4 = int(input(f'Qual foi o {contador}° número?\n>>> '))
    
    if contador == 1 and resposta4 == sort3:
        pass
    elif contador == 2 and resposta4 == sort4:
        pass
    elif contador == 3 and resposta4 == sort5:
        pass
    elif contador == 4 and resposta4 == sort6:
        pass
    elif contador == 5 and resposta4 == sort7:
        print('Você acertou todos os números')
        break
    else:
        print('deadMessage')
        break