#Arthur Lovera - 1139243 e Arthur Silvani - 1139247
#este programa foi utiliazado a lingua inglesa para que nós praticasse a lingua

import os, time, random

os.system('clear')
#os.system('color1')

welcome = '''\033[32m
__        __   _                          _   ____                         
\ \      / /__| | ___ ___  _ __ ___   ___| | |  _ \  ___                   
 \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | | | | |/ _ \                  
  \ V  V /  __/ | (_| (_) | | | | | |  __/_| | |_| | (_) |                 
   \_/\_/ \___|_|\___\___/|_| |_| |_|\___(_) |____/ \___/                  
 _   _  ___  _   _  __      ____ _ _ __ | |_   _ __ | | __ _ _   _    __ _ 
| | | |/ _ \| | | | \ \ /\ / / _` | '_ \| __| | '_ \| |/ _` | | | |  / _` |
| |_| | (_) | |_| |  \ V  V / (_| | | | | |_  | |_) | | (_| | |_| | | (_| |
 \__, |\___/ \__,_|   \_/\_/_\__,_|_| |_|\__| | .__/|_|\__,_|\__, |  \__,_|
 |___/  __ _ _ __ ___   __|__ \               |_|            |___/         
 / _` |/ _` | '_ ` _ \ / _ \/ /                                            
| (_| | (_| | | | | | |  __/_|                                             
 \__, |\__,_|_| |_| |_|\___(_)                                             
 |___/                                                                    '''

deadMessage = '''     
    .... NO! ...                  ... MNO! ...
   ..... MNO!! ...................... MNNOO! ...
 ..... MMNO! ......................... MNNOO!! .
.... MNOONNOO!   MMMMMMMMMMPPPOII!   MNNO!!!! .
 ... !O! NNO! MMMMMMMMMMMMMPPPOOOII!! NO! ....
    ...... ! MMMMMMMMMMMMMPPPPOOOOIII! ! ...
   ........ MMMMMMMMMMMMPPPPPOOOOOOII!! .....
   ........ MMMMMOOOOOOPPPPPPPPOOOOMII! ...
    ....... MMMMM..    OPPMMP    .,OMI! ....
     ...... MMMM::   o.,OPMP,.o   ::I!! ...
         .... NNM:::.,,OOPM!P,.::::!! ....
          .. MMNNNNNOOOOPMO!!IIPPO!!O! .....
         ... MMMMMNNNNOO:!!:!!IPPPPOO! ....
           .. MMMMMNNOOMMNNIIIPPPOO!! ......
          ...... MMMONNMMNNNIIIOO!..........
       ....... MN MOMMMNNNIIIIIO! OO ..........
    ......... MNO! IiiiiiiiiiiiI OOOO ...........
  ...... NNN.MNO! . O!!!!!!!!!O . OONO NO! ........
   .... MNNNNNO! ...OOOOOOOOOOO .  MMNNON!........
   ...... MNNNNO! .. PPPPPPPPP .. MMNON!........
      ...... OO! ................. ON! .......
         ................................'''

print(welcome) #Aprensetei boas vindas tela com variavel boasVindas

time.sleep(3) #Aguardar 3s para passar
os.system('clear') #Limpa tela

while True: #Adicionamos um while para pedir se o usuario que jogar mesmo.
    play = str(input('Are you ready (Y/N)?\n>>> ')).upper()

    if play == 'Y':
        break
    #elif jogar == 'N':
        #os.system('shutdown -r now')
    else:
        pass


# ---------------------------------------------
#FASE 1

os.system('clear')
sort1 = random.randint(1,3)
print(sort1)

resposta1 = int(input('\033[31mTry to guess the number drawn:\n >>> '))

if resposta1 == sort1:
    print('\033[32mResposta Correta!\nContinua... \033[31m')
    time.sleep(3)
else:
    os.system('clear')
    print(deadMessage)
    
# ---------------------------------------------
#FASE 2
os.system('clear')
sort2 = random.randint(1,10)
print(f'resolva a Seguinte Fórmula:\n   {sort2} ^ respostaFase1')
operacao = sort2 ** sort1
resposta2 = int(input('Resposta da Fórmula:\n >>> '))
if resposta2 == operacao:
    print('\033[32mResposta Correta! \033[31m')
    time.sleep(3)
else:
    os.system('clear')
    print(deadMessage)

# ---------------------------------------------
#FASE 3
os.system('clear')
print('Aguarde...')
time.sleep(5)
os.system('clear')
print('Responda a seguinte Fórmula:\n   (respostaFase1 + respostaFase2)**respostaFase1 - respostaFase2')
operacao2 = (resposta1 + resposta2) ** resposta1 - resposta2
print(operacao2)
resposta3 = int(input('Resposta da Fórmula:\n >>>'))
if resposta3 == operacao2:
    print('\033[32mResposta Correta! \033[31m')
    time.sleep(3)
else:
    os.system('clear')
    print(deadMessage)

# ---------------------------------------------
#FASE 4

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
    if contador == 2 and resposta4 == sort4:
        pass
    if contador == 3 and resposta4 == sort5:
        pass
    if contador == 4 and resposta4 == sort6:
        pass
    if contador == 5 and resposta4 == sort7:
        print('VOcê acertou todos os números')
        break
    else:
        print(deadMessage)
        break

# ---------------------------------------------
#FASE 5
