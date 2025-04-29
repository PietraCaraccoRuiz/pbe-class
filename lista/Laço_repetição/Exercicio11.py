import random

game = int(input("\nDeseja: Jogar[1] Sair [2]"))
while game != 1 and game != 2:
    print("Opção invalida")
    game = int(input("\nDeseja: Jogar[1] Sair [2]"))

while game == 1:
    cpu = int(input("\nJogar com: CPU[1] Jogador[2]"))
    while cpu != 1 and cpu != 2:
        cpu = int(input("Opção invalida. CPU[1] Jogador[2]"))

    player = {}
    for i in range(2):
        hp = random.randint(40, 60)
        player[f'P{i}'] = {
            'HP': hp, 'Max': hp, 'Dano': random.randint(10, 25),
            'Def': random.randint(5, 15), 'Cura': random.randint(10, 20),
            'Forca': 0, 'DefX': 0, 'St': '', 'StT': 0, 'Cache': False
        }

    turno = 0
    while player['P0']['HP'] > 0 and player['P1']['HP'] > 0:
        print(f"\nTurno {turno+1} | HP P0: {player['P0']['HP']} | P1: {player['P1']['HP']}")

        for i in range(2):
            p = f'P{i}'
            o = f'P{1-i}'
            if player[p]['HP'] <= 0: continue

            # Efeitos
            if player[p]['St'] == 'Buffer':
                d = int(player[p]['Max'] * 0.05)
                player[p]['HP'] -= d
                print(f"{p} sofre {d} de Buffer Overflow")
            if player[p]['StT'] > 0:
                player[p]['StT'] -= 1
                if player[p]['StT'] == 0: player[p]['St'] = ''
            if player[p]['Forca'] > 0: player[p]['Forca'] -= 1
            if player[p]['DefX'] > 0: player[p]['DefX'] -= 1

            if cpu == 1 and p == 'P1':
                acao = random.randint(1, 4)
            else:
                print(f"\nTurno de {p}:\n[1] Atacar [2] Curar [3] Item [4] Efeito")
                acao = int(input("Escolha: "))

            if player[p]['St'] == 'Loop':
                print(f"{p} perdeu a vez por Loop Infinito!")
                continue

            if acao == 1:
                dano = player[p]['Dano'] + (10 if player[p]['Forca'] > 0 else 0)
                if random.randint(1,10) == 1:
                    dano *= 2
                    print("Crítico!")
                defesa = 0 if player[o]['St'] == 'Tela' else player[o]['Def']
                if player[o]['DefX'] > 0: defesa += 10
                player[o]['HP'] -= max(0, dano - defesa)
                print(f"{p} ataca {o}!")

            elif acao == 2:
                player[p]['HP'] += player[p]['Cura']
                print(f"{p} curou {player[p]['Cura']}!")

            elif acao == 3:
                print("[1] Poção de Força [2] Escudo Extra [3] Buffer [4] Tela Azul")
                item = int(input("Item: "))
                if item == 1:
                    player[p]['Forca'] = 2
                elif item == 2:
                    player[p]['DefX'] = 2
                elif item == 3:
                    player[o]['St'] = 'Buffer'
                    player[o]['StT'] = 5
                elif item == 4:
                    player[o]['St'] = 'Tela'
                    player[o]['StT'] = 2

            elif acao == 4:
                print("[1] Buffer [2] Loop [3] Tela Azul [4] Cache Hit")
                ef = int(input("Efeito: "))
                if ef == 1:
                    player[o]['St'] = 'Buffer'; player[o]['StT'] = 5
                elif ef == 2:
                    player[o]['St'] = 'Loop'; player[o]['StT'] = 1
                elif ef == 3:
                    player[o]['St'] = 'Tela'; player[o]['StT'] = 2
                elif ef == 4:
                    if player[p]['HP'] < player[p]['Max'] * 0.25 and not player[p]['Cache']:
                        cura = int(player[p]['Max'] * 0.3)
                        player[p]['HP'] += cura
                        player[p]['Cache'] = True
                        print(f"{p} ativou Cache Hit +{cura} HP!")
                    else:
                        print("Não pode usar Cache Hit!")

        turno += 1

    if player['P0']['HP'] <= 0:
        print("Player 1 venceu!")
    else:
        print("Player 0 venceu!")
    game = int(input("\nDeseja: Jogar[1] Sair [2]"))
print("Você saiu do jogo!")