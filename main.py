import os, time, random

os.system('clear')
#os.system('color1')

boasVindas = '''
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

msgMorte = '''     .... NO! ...                  ... MNO! ...
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

print(boasVindas) #Aprensetei boas vindas tela com variavel boasVindas

time.sleep(3) #Aguardar 3s para passar
os.system('clear') #Limpa tela

while True: #Adicionamos um while para pedir se o usuario que jogar mesmo.
    jogar = str(input('Are you ready (S/N)?\n>>> ')).upper()

    if jogar == 'S':
        break
    #elif jogar == 'N':
        #os.system('shutdown -r now')
    else:
        pass

#FALTA POR COR VERMELHA
# ---------------------------------------------
#FASE 1

os.system('clear')
sorteio = random.randint(1,3)


jogoAzar = int(input('Try to guess the number drawn:\n>>> '))

if jogoAzar == sorteio:
    print('continua')
else:
    os.system('clear')
    print(msgMorte)
    
