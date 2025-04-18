import random

game = int(input("\nDeseja: Jogar[1] Sair [2]"))

while game !=1 and game != 2:
    print("Opção invalida")
    game = int(input("\nDeseja: Jogar[1] Sair [2]"))

while game == 1:

    cpu = int(input("\nJogar com: CPU[1] Jogador[2]"))
    while cpu != 1 and cpu != 2:
        print("Opção invalida")
        cpu = int(input("\nDeseja: Jogar[1] Sair [2]"))


    num_player = 2

    player = {}

    hp = random.randint(1, 50)

    for i in range(num_player):
        dano = random.randint(1, 50)
        defesa = random.randint(1, 50)
        cura = random.randint(1, 50)

        player[f'player{i}'] = {
            'dano': dano,
            'defesa': defesa,
            'cura': cura,
            'HP': hp,
        }

    print("=== DUELO DE HERÓIS ===")
    # Exibindo os jogadores
    for nome, stats in player.items():
        print(f"\n=== {nome} ===")
        print("HP: ", stats['HP'])
        print("Dano: ", stats['dano'])
        print("Defesa: ", stats['defesa'])
        print("Cura: ", stats['cura'])

    i = 1
    while player['player0']['HP'] > 0 and player['player1']['HP'] > 0:
        print(f"\n--- Turno: {i} ---")
        print(f"HP do Jogador 0: {player['player0']['HP']} | HP do Jogador 1: {player['player1']['HP']}")
        escolha = int(input("\nSua vez: [1] Atacar ou [2] Curar?"))

        while escolha != 1 and escolha != 2:
            print("Escolha inválida!")
            escolha = int(input("\nSua vez: [1] Atacar ou [2] Curar?"))
        if escolha == 1:
            att = player['player0']['dano'] - player['player1']['defesa']
            if att < 0:
                att = 0
            player['player1']['HP'] -= att
            print(f"Player0 ataca! Player1 perde {att} HP")
        elif escolha == 2:
            player['player0']['HP'] += player['player0']['cura']
            print(f"Player0 se cura {player['player0']['cura']} HP")

        if cpu == 1:
            escolha = random.randint(1, 2)

        elif cpu == 2:
            escolha = int(input("\nSua vez: [1] Atacar ou [2] Curar?"))

            while escolha != 1 and escolha != 2:
                print("Escolha inválida!")
                escolha = int(input("\nSua vez: [1] Atacar ou [2] Curar?"))

        if escolha == 1:
            att = player['player1']['dano'] - player['player0']['defesa']
            if att < 0:
                att = 0
            player['player0']['HP'] -= att
            print(f"Player1 ataca! Player0 perde {att} HP")
        elif escolha == 2:
            player['player1']['HP'] += player['player1']['cura']
            print(f"Player1 se cura {player['player1']['cura']} HP")

        if player['player0']['HP'] <= 0:
            print("Player1 ganhou!")
        elif player['player1']['HP'] <= 0:
            print("Player0 ganhou!")
        i+= 1
    game = int(input("\nDeseja: Continuar[1] Sair [2]"))
print("Você saiu do jogo!")