#Arthur Lovera - 1139243 e Arthur Silvani - 1139247
#este programa foi utiliazado a lingua inglesa para que nós praticasse a lingua

import os, time, random

os.system('cls' if os.name == 'nt' else 'clear')

bemVindo = '''\033[32m
 ____                  __     ___           _       _                   
| __ )  ___ _ __ ___   \ \   / (_)_ __   __| | ___ | |                  
|  _ \ / _ \ '_ ` _ \   \ \ / /| | '_ \ / _` |/ _ \| |                  
| |_) |  __/ | | | | |   \ V / | | | | | (_| | (_) |_|                  
|____/ \___|_| |_| |_|    \_/_ |_|_| |_|\__,_|\___/(_)                  
| __ )  ___  _ __ __ _      | | ___   __ _  __ _ _ __   _   _ _ __ ___  
|  _ \ / _ \| '__/ _` |  _  | |/ _ \ / _` |/ _` | '__| | | | | '_ ` _ \ 
| |_) | (_) | | | (_| | | |_| | (_) | (_| | (_| | |    | |_| | | | | | |
|____/ \___/|_|  \__,_| _\___/ \___/ \__, |\__,_|_|     \__,_|_| |_| |_|
    | | ___   __ _  ___|__ \         |___/                              
 _  | |/ _ \ / _` |/ _ \ / /                                            
| |_| | (_) | (_| | (_) |_|                                             
 \___/ \___/ \__, |\___/(_)                                             
             |___/                                                                                                                         '''

mensagemMorte = r'''     

-----=+=:....:.............:.:.::...:::....:.................::------==--
-----+:....:.................:...::::::---:....................:.::.::---
----+-:..::.........................::..:.........................:::::--
--=-=-.-:....................:..-+..-=:-:--.........................-:-:-
----:-:::..............:-=+***+=+*#*+=+#%%%##**=-:...................:---
=---=:::.:..........+*#*#%%%#%%#+%#+#@%%@@@@%%#*++++:...............:::-:
--+-:::..........-#%@@@@@@@@%%@@*@@@%@@@@@@%%#*#**+++**:..............::-
:=:--:.........-%@@@@@@@@@@@@%@@@@@@%@@@@@@@@%#*+**+++*##:.......:.....::
+:::-.........=@@@@%@@@@@@@@@@@@@@%@@@@@@%%%%%%%*+****+*##=.......:..:..-
--:=.........+%@@@@@@@@@@@@@@@@@@@@@@@@@@@@%##**#***##*+*#%*.......:....:
=:-::.......*%@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#*##*#%#**##%#.......:....
:-:-.:.....+%@@%#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%###%%%%######+.......:...
-:-::.....-%%@%#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#%%%#%@%%#%%%%-..........
.-:.-.....#%@@%@###%%##%@%@@@@@@@@@@@@@@@%%%%%%%%%*##%#####%%%%..........
-::-:....+%@@@@@@@@@@@@@@@@@#+%@@%@@@@%%%%*=#@@@@@@@%@%@@@@@%%%*.....:...
:-:=....:*@@@@@@%#@@@@@@@@@@@@#=*##%####*+%@@@@@@@%@@+%#%@@@@@#+:.....:..
:--:...*@@@@@@%%####*#%%%%@@@@@@#:+*+++:%@@@@@@%%%%#**####%@@@@%%+.......
--.:..-@@%%#=:..::::::-=*%%%@%@@@@#-::%@@@@#@@@%*=-:::.....:=##%#@-......
=.::...*%*=::....:------:.=##%#%@@@-.-@@@@#@@%-.-------:....::-*%+...:...
...-...=+@+--....==:..:--:..-+**#%@=.*@%%##*-..:--:..---....=-=#+=....:..
..::...%%@@*++...---::---:...=--=-:.:::=--==...:---::---...+*+*#%%....:..
..:....%@@@@%#*-..------:....+--:::--:.::--+....:-----:..:*#*##*%#...:...
..:...-@###%#*+*#==-.......=+-:++:#%@%*:=-.:+=.......-=-*+++%#*+*%-..::..
.::...****+==-=**%**+#*+++=*+=%*%+%@@@*====:-+******+*+*##=---=+*+=...:..
.::..*%###%@@%=-=%@%%#%%%###%@@@@@%@@@*++**+**###%##%@@%=-=%@@%#*##*..::.
::..-####+=--@@=--*%@@%###***%@@@@@@@@%++#*+++####%%@@*--+@%=---***+:..:.
.:..*@@@@@@#--*@%=-##########@@@@@@@@@%++*#+=+***###%#--%@*-=#@@@#*#+..:.
::..%*+==-#@%--*@*:.=**+++##%@@@@@@@@@@++*#=+*#=+=*#=..*%*--%@#=--==*...:
:..:*@@@@=-+%+..*#=:-*=*+**#%@@@@%@@@@@+****+++*+*+*=:=%*..*%+-=%#**+....
....+*+=+#::+#=:-#=--++++**##*@@@%@@@@@#**#+++###+**--*%::+#=::#=-=+=....
....-+*=.+*:-#*--*=--+++++**#%#@@@@@@@@#+*+*********=-=#--*#-:+=.=+-:....
.....+=+##=-=#*--*=--*=:--:+-=@@@@@@@@@****=:=:--:=*=-=*--*#---+*+=+.....
......:++++#%*-=#*--+++===+=*@@@@#@@@@@++**#=-=-===+=--+=--====+++:......
..........::-+*=----::.-++=*=%@@@@@@@@@%**##-+-==:..::::-=+=:::..........
.......::.....-#%%%+#::--=--=:-#%%@@@@@#++-:-:-::::.--==+=:..............
....:.-::......=#@@@@*---:-----::+@@@@*-:::--::::::-=++==-........:......
...:..:-:.......##@@@@%*:--====----------------::-=+++++=..........::....
......-:-.:......@@@@@#%=-=----------------:-----++*****..........:::....
.....-:-..:......=@@@@%%=*@#*+*++*-...-+=+==+*#+:+*##*#-..........-.:....
....::=...:.......#@@@%%+*@@@@@@@@#***####%%%##*-*#%#%*....:......:.:....
....::....:.:.....-@@@##*#@@@@@@@@%#*##%%%##%%#+=*%%#%-....:..:...-:.:...
............:......@@@***#@@@@@@@@#%###%@@%%%%#+=*#%%%.........:..-::....
...................-@@##*#@@@*@@@@%#%##@@@@*@@#+=*##%:.........:..-...:..
.................:::=%%#=#@@@+@@@@@###@@@@@+@@#*-*#*-:::.........:.:.....
.................---..:::#@@@%@@@@@##*@@@@@%@@#*....::-:..........::.....
.................:-=-:::-#@%#@@@@@@%*%@@@@@%*%%*:..:---..................
..................::=-=+-#%##@@@@@@#*@@@@@@%#%%#-=--=-:..................
..................:-=====-:+#%%%@%%#*#%@@%##+=::-:---::..................'''

mensagemParabens = '''
__     __         //\   ____        _                    _                  
\ \   / /__   ___|/_\| / ___|  ___ | |__  _ __ _____   _(_)_   _____ _   _  
 \ \ / / _ \ / __/ _ \ \___ \ / _ \| '_ \| '__/ _ \ \ / / \ \ / / _ \ | | | 
  \ V / (_) | (_|  __/  ___) | (_) | |_) | | |  __/\ V /| |\ V /  __/ |_| | 
   \_/ \___/ \___\___| |____/ \___/|_.__/|_|  \___| \_/ |_| \_/ \___|\__,_| 
         _            _             ____                   __ _             
  __ _  | |_ ___   __| | ___  ___  |  _ \  ___  ___  __ _ / _(_) ___  ___   
 / _` | | __/ _ \ / _` |/ _ \/ __| | | | |/ _ \/ __|/ _` | |_| |/ _ \/ __|  
| (_| | | || (_) | (_| | (_) \__ \ | |_| |  __/\__ \ (_| |  _| | (_) \__ \_ 
 \__,_|  \__\___/ \__,_|\___/|___/ |____/ \___||___/\__,_|_| |_|\___/|___(_)
 ____                 _       __           _                                
|  _ \ __ _ _ __ __ _| |__   /_/ _ __  ___| |                               
| |_) / _` | '__/ _` | '_ \ / _ \ '_ \/ __| |                               
|  __/ (_| | | | (_| | |_) |  __/ | | \__ \_|                               
|_|   \__,_|_|  \__,_|_.__/ \___|_| |_|___(_)                               

'''

print(bemVindo) #Aprensetei boas vindas tela com variavel boasVindas

time.sleep(3) #Aguardar 3s para passar
print('Para melhor experiência utilize o terminal estendido!')
while True:
    os.system('cls' if os.name == 'nt' else 'clear') #Limpa tela

    while True: #Adicionamos um while para pedir se o usuario que jogar mesmo.
        jogar = str(input('Você está Pronto (S/N)?\n>>> ')).upper()

        if jogar == 'S': #caso o usuário aceite, ele irá jogar..
            print('Lembre-se dos números de cada fase... pode lhe ajudar...')
            time.sleep(3)
            break
        elif jogar == 'N':
            print('Então você não irá utilizar o PC...')
            time.sleep(3)
            os.system('shutdown -t -s' if os.name == 'nt' else 'shutdown -h now') #desliga o PC caso o usuario nao queira jogar
        else: 
            print('Respostas permitidas: \033[1mS/N\033[0;32m\n')
            time.sleep(3)

    # ---------------------------------------------
    #FASE 1

    os.system('cls' if os.name == 'nt' else 'clear')
    sort1 = random.randint(1,3) #sorteia um numero de 1 a 3
    #print(sort1)

    resposta1 = int(input('\033[31mTente adivinhar o número sorteado (1 à 3):\n >>> ')) # pergunta ao usuário tentar adivinhar o número sorteado

    if resposta1 == sort1: #caso acerte o número, o jogo continua
        print('\033[32mResposta Correta!\nContinua... \033[31m')
        time.sleep(3)
    else: # caso erre o numero apresenta a mensagem de morte ao usuario
        os.system('cls' if os.name == 'nt' else 'clear')
        print(mensagemMorte)
        break
        
    # ---------------------------------------------
    #FASE 2

    os.system('cls' if os.name == 'nt' else 'clear')
    sort2 = random.randint(1,10) # sorteia um número de 1 a 10
    print(f'resolva a Seguinte Fórmula:\n   respostaFase1 ^ {sort2}')
    operacao = sort1 ** sort2 # efetua a operação
    resposta2 = int(input('Resposta da Fórmula:\n >>> ')) #pede ao usuário a resposata da operação
    if resposta2 == operacao: # confere se a resposta é igual à operação, caso não for: Mensagem de morte
        print('\033[32mResposta Correta! \033[31m')
        time.sleep(3)
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(mensagemMorte)
        break

    # ---------------------------------------------
    #FASE 3

    os.system('cls' if os.name == 'nt' else 'clear')
    print('Aguarde...')
    time.sleep(5)
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Responda a seguinte Fórmula:\n   (respostaFase1 + respostaFase2)**respostaFase1 - respostaFase2')
    operacao2 = (resposta1 + resposta2) ** resposta1 - resposta2
    #print(operacao2)
    resposta3 = int(input('Resposta da Fórmula:\n >>> '))# pede ao usuário a resposta da fórmula
    if resposta3 == operacao2: # verifica se a resposta está correta
        print('\033[32mResposta Correta! \033[31m')
        time.sleep(3)
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(mensagemMorte)
        break

    # ---------------------------------------------
    #FASE 4

    os.system('cls' if os.name == 'nt' else 'clear')

    sort3 = random.randint(1,101) # efetua o sorteio de um número
    sort4 = random.randint(1,101) # efetua o sorteio de um número
    sort5 = random.randint(1,101) # efetua o sorteio de um número
    sort6 = random.randint(1,101) # efetua o sorteio de um número
    sort7 = random.randint(1,101) # efetua o sorteio de um número

    time.sleep(3)
    print(f'[{sort3}, {sort4}, {sort5}, {sort6}, {sort7}]')
    time.sleep(2)
     # mostra os numeros sorteados por 2 segundos

    contador = 0 #inicia um contador apenas como forma de avaliar a resposta
    while True:
        contador += 1 #soma 1 no contador
        resposta4 = int(input(f'Qual foi o {contador}° número?\n>>> '))# pede ao usuário os numeros sorteados(1 por 1)
        
        if contador == 1 and resposta4 == sort3: #avalia se a resposata foi correta
            pass
        elif contador == 2 and resposta4 == sort4:
            pass
        elif contador == 3 and resposta4 == sort5:
            pass
        elif contador == 4 and resposta4 == sort6:
            pass
        elif contador == 5 and resposta4 == sort7:
            print('\033[32mVocê acertou todos os números!\033[31m')
            break
        else:
            print(mensagemMorte)
            quit()

    # ---------------------------------------------
    #FASE 5
    
    time.sleep(2)
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

print('FIM DE JOGO!')#acaba o jogo