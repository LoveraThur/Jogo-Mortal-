import os, random, time
from main import mensagemMorte, mensagemParabens
time.sleep(2)
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('RESOLVA O ENIGMA A SEGUIR')
    time.sleep(2)
    print('\nUm programador encontra um nano computador que trabalha apenas\ncom bits. O computador tem exatamente 41.943.040 bits de memória.\nQuantos Megabytes isso representa?')# apresenta a pergunta ao usuário
    resposta5 = int(input('\nResposta\n>>> '))# pede ao usuário a resposta

    if resposta5 == 5: # verifica se a resposta ertá correta
        print(f'\033[32m{mensagemParabens}')
        break
    else:
        print('resposta: 1 byte = 8 bits\n41.943.040÷8=5.242.880 bytes\n\n1 MB = 1024 × 1024 = 1.048.576 bytes\n5.242.880÷1.048.576=5')
        print('Recomeçando...')
        time.sleep(2)

print('FIM DE JOGO!')