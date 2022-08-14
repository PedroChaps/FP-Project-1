# Pedro Alexandre Chaparro _ ist199298

def eh_tabuleiro(tab):
    if type(tab) == tuple and len(tab) == 3:
        for t in tab:
            if type(t) != tuple:
                return False

            for i in range(3):
                if not len(t) == 3 or not t[i] in (-1, 1, 0) or not (type(t[i]) == int and type(t[i]) != str):
                    return False

        return True
                                               # So' da True apo's ter verificado todos os elementos

    return False                                                        # Caso o 1o "if" == false


def eh_posicao(nr):
    if type(nr) == int:
        return 1 <= nr <= 9

    return False


def obter_coluna(tab, nr):
    if eh_tabuleiro(tab) and type(nr) == int and 1 <= nr <= 3:
        return (tab[0][nr-1], tab[1][nr-1], tab[2][nr-1])

    raise ValueError('obter_coluna: algum dos argumentos e invalido')


def obter_linha(tab, nr):
    if eh_tabuleiro(tab) and type(nr) == int and 1 <= nr <= 3:
        return (tab[nr-1][0], tab[nr-1][1], tab[nr-1][2])

    raise ValueError('obter_linha: algum dos argumentos e invalido')


def obter_diagonal(tab, nr):
    if eh_tabuleiro(tab) and type(nr) == int:
        if nr == 1:
            return (tab[0][0], tab[1][1], tab[2][2])
        if nr == 2:
            return (tab[2][0], tab[1][1], tab[0][2])

    raise ValueError('obter_diagonal: algum dos argumentos e invalido')


def aux_converte_tab(tab):  # Funcao auxiliar. Recebe um tabuleiro e da' a representacao do tab (com X, 0,  ).

    if eh_tabuleiro(tab):
        TuploRep = ()
        TuploNovoLinha = ()

        for t in tab:
            for i in (range(3)):
                if t[i] == -1:
                    TuploNovoLinha += ('O',)
                if t[i] == 1:
                    TuploNovoLinha += ('X',)
                if t[i] == 0:
                    TuploNovoLinha += (' ',)

            TuploRep += (TuploNovoLinha, )
            TuploNovoLinha = ()

        return TuploRep

    raise ValueError('converte_tab: or argumento e invalido')


def tabuleiro_str(tab):
    if not eh_tabuleiro(tab):
        raise ValueError('tabuleiro_str: o argumento e invalido')

    TR = aux_converte_tab(tab)                          # Abstracao procedimental
    div = ' | '
    esp = ' \n-----------\n '
    p1, p2, p3 = TR[0][0], TR[0][1], TR[0][2]
    p4, p5, p6 = TR[1][0], TR[1][1], TR[1][2]
    p7, p8, p9 = TR[2][0], TR[2][1], TR[2][2]

    return " " + p1 + div + p2 + div + p3 + esp + p4 + div + p5 + div + p6 + esp + p7 + div + p8 + div + p9 + " "


"""def tabuleiro_str(tab):
    TR = converte_tab(tab)                          #Abstracao procedimental          #Nao correu bem, o return fica feio
    if not(type(TR) == tuple):
        raise ValueError('tabuleiro_str: o argumento e invalido')

    return                '', TR[0][0], '|', TR[0][1], '|', TR[0][2], ' ' \
           '\n-----------\n', TR[1][0], '|', TR[1][1], '|', TR[1][2],     \
           '\n-----------\n', TR[2][0], '|', TR[2][1], '|', TR[2][2], ' ' 
"""


"""def converte_posi(tab, nr):        # Funcao auxiliar. Converte posicao para indices.  STANDBY, AFINAL N FOI PRECISA
    if not (eh_tabuleiro(tab) and eh_posicao(nr)):
        raise ValueError('eh_posicao_livre: algum dos argumentos e invalido')

    if 1 <= nr <= 3:
        return tab[0][nr - 1]
    if 4 <= nr <= 6:
        return tab[1][nr - 1]
    if 7 <= nr <= 9:
        return tab[2][nr - 1]"""


def eh_posicao_livre(tab, posi):
    if not(eh_tabuleiro(tab) and eh_posicao(posi)):
        raise ValueError('eh_posicao_livre: algum dos argumentos e invalido')

    if 1 <= posi <= 3:
        return tab[0][posi - 1] == 0
    if 4 <= posi <= 6:
        return tab[1][posi - 4] == 0
    if 7 <= posi <= 9:
        return tab[2][posi - 7] == 0


def obter_posicoes_livres(tab):
    if not(eh_tabuleiro(tab)):
        raise ValueError('obter_posicoes_livres: o argumento e invalido')

    posi_livres = ()

    for posi in range(1, 10):
         if eh_posicao_livre(tab, posi):
             posi_livres += (posi, )

    return posi_livres


def jogador_ganhador(tab):                                               #Verifica se as entradas das 3 colunas, linhas e 2 diagonais sao todas ==. Se sim, retorna a entrada. Se nao, ninguem ganhou, logo retorna 0.
    if not(eh_tabuleiro(tab)):
        raise ValueError('jogador_ganhador: o argumento e invalido')

    for i in range(1, 4):                                                    #A ordem e col 1, li 1, col 2, li 2, col 3, lin 3.
        if obter_coluna(tab, i)[0] == obter_coluna(tab, i)[1] == obter_coluna(tab, i)[2]:
            return obter_coluna(tab, i)[0]                                      #Nao importa qual indice, pois sao todos iguais
        if obter_linha(tab, i)[0] == obter_linha(tab, i)[1] == obter_linha(tab, i)[2]:
            return obter_linha(tab, i)[0]

# Se chegou ate aqui, e pq nenhuma linha nem coluna tinha as entradas todas =. Achei que n valia a pena um ciclo apenas para 2 possibilidades.
    if obter_diagonal(tab, 1)[0] == obter_diagonal(tab, 1)[1] == obter_diagonal(tab, 1)[2]:
        return obter_diagonal(tab, 1)[0]
    if obter_diagonal(tab, 2)[0] == obter_diagonal(tab, 2)[1] == obter_diagonal(tab, 2)[2]:
        return obter_diagonal(tab, 2)[0]

    return 0    # se chegou ate aqui e pq as linhas, colunas e diagonais eram todas diferentes. logo ngm ganhou.


def marcar_posicao(tab, player, posi):
    if not(eh_tabuleiro(tab) and type(player) == int and (player == -1 or player == 1) and eh_posicao(posi) and
           eh_posicao_livre(tab, posi)):
        raise ValueError('marcar_posicao: algum dos argumentos e invalido')

    a = (tab[0][0], tab[0][1], tab[0][2])                 # a,b,c, sao as linhas do tabuleiro
    b = (tab[1][0], tab[1][1], tab[1][2])
    c = (tab[2][0], tab[2][1], tab[2][2])

    if 1 <= posi <= 3:
        if posi == 1:
            a = (player, tab[0][1], tab[0][2])
        if posi == 2:
            a = (tab[0][0], player, tab[0][2])
        if posi == 3:
            a = (tab[0][0], tab[0][1], player)

    if 4 <= posi <= 6:
        if posi == 4:
            b = (player, tab[1][1], tab[1][2])
        if posi == 5:
            b = (tab[1][0], player, tab[1][2])
        if posi == 6:
            b = (tab[1][0], tab[1][1], player)

    if 7 <= posi <= 9:
        if posi == 7:
            c = (player, tab[2][1], tab[2][2])
        if posi == 8:
            c = (tab[2][0], player, tab[2][2])
        if posi == 9:
            c = (tab[2][0], tab[2][1], player)

    return (a, b, c)


def aux_eh_posicao_livre_modi(tab, posi):                       # funcao auxiliar. Serve para alterar o raise ValueError
    if not(eh_posicao(posi)):
        raise ValueError('escolher_posicao_manual: a posicao introduzida e invalida')

    if 1 <= posi <= 3:
        return tab[0][posi - 1] == 0
    if 4 <= posi <= 6:
        return tab[1][posi - 4] == 0
    if 7 <= posi <= 9:
        return tab[2][posi - 7] == 0


def escolher_posicao_manual(tab):
    if not(eh_tabuleiro(tab)):
        raise ValueError('escolher_posicao_manual: o argumento e invalido')

    posi = eval(input('Turno do jogador. Escolha uma posicao livre: '))

    if not aux_eh_posicao_livre_modi(tab, posi):
        raise ValueError('escolher_posicao_manual: a posicao introduzida e invalida')# chamo a funcao apenas para ver se a posicao e valida

    return posi


def aux_coluna_de_posi(tab, posi): # funcao auxiliar. Recebe uma tab e uma posicao e retorna a coluna que interseta essa posi.
    if posi in (1, 4, 7):
        return obter_coluna(tab, 1)
    if posi in (2, 5, 8):
        return obter_coluna(tab, 2)
    if posi in (3, 6, 9):
        return obter_coluna(tab, 3)


def aux_linha_de_posi(tab, posi): # funcao auxiliar. Recebe uma tab e uma posicao e retorna a linha que interseta essa posi.
    if 1 <= posi <= 3:
        return tab[0]
    if 4 <= posi <= 6:
        return tab[1]
    if 7 <= posi <= 9:
        return tab[2]


def aux_diagonal_de_posi(tab, posi): # funcao auxiliar. Recebe uma tab e uma posicao e retorna a/s diagonal/is que intersetam essa posi.
    if posi in (1, 9):
        return obter_diagonal(tab, 1)
    if posi in (3, 7):
        return obter_diagonal(tab, 2)
    if posi == 5:
        return (obter_diagonal(tab, 1), obter_diagonal(tab, 2))


def rule1(tab, player):
    livres = obter_posicoes_livres(tab)
    for i in livres:
        col = aux_coluna_de_posi(tab, i)
        pla_cnt = 0
        vaz_cnt = 0

        for el in col:
            if el == player:
                pla_cnt += 1
            if el == 0:
                vaz_cnt += 1

        if pla_cnt == 2 and vaz_cnt == 1:
            return i  # marcar_posicao(tab, player, i)

        lin = aux_linha_de_posi(tab, i)
        pla_cnt = 0
        vaz_cnt = 0

        for el in lin:
            if el == player:
                pla_cnt += 1
            if el == 0:
                vaz_cnt += 1

        if pla_cnt == 2 and vaz_cnt == 1:
            return i  # marcar_posicao(tab, player, i)

        dia = aux_diagonal_de_posi(tab, i)
        pla_cnt = 0
        vaz_cnt = 0
        if i in (1, 3, 7, 9):
            for el in dia:
                if el == player:
                    pla_cnt += 1
                if el == 0:
                    vaz_cnt += 1

            if pla_cnt == 2 and vaz_cnt == 1:
                return i  # marcar_posicao(tab, player, i)

        if i == 5:    # Apenas para tornar mais claro. Quando i == 5, aux_diagonal retorna 1 tup com 2 tup (caso especial)
            for el in dia:
                pla_cnt = 0
                vaz_cnt = 0
                for el2 in el:
                    if el2 == player:
                        pla_cnt += 1
                    if el2 == 0:
                        vaz_cnt += 1
                if pla_cnt == 2 and vaz_cnt == 1:
                    return i  # marcar_posicao(tab, player, i)


def rule2(tab, player):

    playerOposto = -1
    if player == -1:
        playerOposto = 1

    livres = obter_posicoes_livres(tab)
    for i in livres:
        col = aux_coluna_de_posi(tab, i)
        pla_cnt = 0
        vaz_cnt = 0

        for el in col:
            if el == playerOposto:
                pla_cnt += 1
            if el == 0:
                vaz_cnt += 1

        if pla_cnt == 2 and vaz_cnt == 1:
            return i  # marcar_posicao(tab, player, i)

        lin = aux_linha_de_posi(tab, i)
        pla_cnt = 0
        vaz_cnt = 0

        for el in lin:
            if el == playerOposto:
                pla_cnt += 1
            if el == 0:
                vaz_cnt += 1

        if pla_cnt == 2 and vaz_cnt == 1:
            return i  # marcar_posicao(tab, player, i)

        dia = aux_diagonal_de_posi(tab, i)
        pla_cnt = 0
        vaz_cnt = 0
        if i in (1, 3, 7, 9):
            for el in dia:
                if el == playerOposto:
                    pla_cnt += 1
                if el == 0:
                    vaz_cnt += 1

            if pla_cnt == 2 and vaz_cnt == 1:
                return i  # marcar_posicao(tab, player, i)

        if i == 5:  # Apenas para tornar mais claro. Quando i == 5, aux_diagonal retorna 1 tup com 2 tup (caso especial)
            for el in dia:
                pla_cnt = 0
                vaz_cnt = 0
                for el2 in el:
                    if el2 == playerOposto:
                        pla_cnt += 1
                    if el2 == 0:
                        vaz_cnt += 1
                if pla_cnt == 2 and vaz_cnt == 1:
                    return i  # marcar_posicao(tab, player, i)


def rule3(tab, player):
    livres = obter_posicoes_livres(tab)
    for i in livres:
        col = aux_coluna_de_posi(tab, i)
        pla_cnt = 0
        vaz_cnt = 0

        for el in col:
            if el == player:
                pla_cnt += 1
            if el == 0:
                vaz_cnt += 1

        if pla_cnt == 1 and vaz_cnt == 2:
            col = ()

        lin = aux_linha_de_posi(tab, i)
        pla_cnt = 0
        vaz_cnt = 0

        for el in lin:
            if el == player:
                pla_cnt += 1
            if el == 0:
                vaz_cnt += 1

        if pla_cnt == 1 and vaz_cnt == 2:
            lin = ()

        dia = aux_diagonal_de_posi(tab, i)
        pla_cnt = 0
        vaz_cnt = 0
        if i in (1, 3, 7, 9):
            for el in dia:
                if el == player:
                    pla_cnt += 1
                if el == 0:
                    vaz_cnt += 1

            if pla_cnt == 1 and vaz_cnt == 2:
                dia = ()

        if i == 5:
            diag1 = dia[0]
            diag2 = dia[1]
            pla_cnt, vaz_cnt = 0, 0

            for el in dia[0]:

                if el == player:
                    pla_cnt += 1
                if el == 0:
                    vaz_cnt += 1

            if pla_cnt == 1 and vaz_cnt == 2:
                diag1 = ()

            pla_cnt, vaz_cnt = 0, 0
            for el in dia[1]:
                pla_cnt = 0
                vaz_cnt = 0

                if el == player:
                    pla_cnt += 1
                if el == 0:
                    vaz_cnt += 1
            if pla_cnt == 1 and vaz_cnt == 2:
                diag2 = ()

        if i in (2, 4, 6, 8):
            if (col + lin) == ():
                return i  # marcar_posicao(tab, player, i)
        if i in (1, 3, 7, 9):
            if (col + lin == ()) or (col + dia == ()) or (dia + lin == ()):  # Basta 1 para haver bif
                return i  # marcar_posicao(tab, player, i)
        if i == 5:
            if (col + lin == ()) or (col + diag1 == ()) or (col + diag2 == ()) or (lin + diag1 == ()) or \
               (lin + diag2 == ()) or (diag1 + diag2 == 0):

                return i  # marcar_posicao(tab, player, i)


def aux_contador_bif(tab, player):
    playerOposto = -1
    if player == -1:
        playerOposto = 1

    bif_counter = 0
    posi_bif = ()

    livres = obter_posicoes_livres(tab)
    for i in livres:
        col = aux_coluna_de_posi(tab, i)
        pla_cnt = 0
        vaz_cnt = 0

        for el in col:
            if el == playerOposto:
                pla_cnt += 1
            if el == 0:
                vaz_cnt += 1

        if pla_cnt == 1 and vaz_cnt == 2:
            col = ()

        lin = aux_linha_de_posi(tab, i)
        pla_cnt = 0
        vaz_cnt = 0

        for el in lin:
            if el == playerOposto:
                pla_cnt += 1
            if el == 0:
                vaz_cnt += 1

        if pla_cnt == 1 and vaz_cnt == 2:
            lin = ()

        dia = aux_diagonal_de_posi(tab, i)
        pla_cnt = 0
        vaz_cnt = 0
        if i in (1, 3, 7, 9):
            for el in dia:
                if el == playerOposto:
                    pla_cnt += 1
                if el == 0:
                    vaz_cnt += 1

            if pla_cnt == 1 and vaz_cnt == 2:
                dia = ()

        if i == 5:
            diag1 = dia[0]
            diag2 = dia[1]
            pla_cnt, vaz_cnt = 0, 0

            for el in dia[0]:

                if el == playerOposto:
                    pla_cnt += 1
                if el == 0:
                    vaz_cnt += 1

            if pla_cnt == 1 and vaz_cnt == 2:
                diag1 = ()

            pla_cnt, vaz_cnt = 0, 0
            for el in dia[1]:
                pla_cnt = 0
                vaz_cnt = 0

                if el == playerOposto:
                    pla_cnt += 1
                if el == 0:
                    vaz_cnt += 1
            if pla_cnt == 1 and vaz_cnt == 2:
                diag2 = ()

        if i in (2, 4, 6, 8):
            if (col + lin) == ():
                bif_counter += 1
        if i in (1, 3, 7, 9):
            if (col + lin == ()) or (col + dia == ()) or (dia + lin == ()):  # Basta 1 para haver bif
                bif_counter += 1
        if i == 5:
            if (col + lin == ()) or (col + diag1 == ()) or (col + diag2 == ()) or (lin + diag1 == ()) or \
                    (lin + diag2 == ()) or (diag1 + diag2 == 0):
                bif_counter += 1

    return bif_counter


def aux_hipoteses_ganhar(tab, player):
    livres = obter_posicoes_livres(tab)

    hipoteses = ()

    for i in livres:
        col = aux_coluna_de_posi(tab, i)
        pla_cnt = 0
        vaz_cnt = 0
        # print("a posi (i) e:", i)
        # print("a coluna do tab de teste e:", col)
        for el in col:
            if el == player:
                pla_cnt += 1
            if el == 0:
                vaz_cnt += 1
        # print("player count =", pla_cnt, "e vazio count =", vaz_cnt)
        if pla_cnt == 2 and vaz_cnt == 1:
            if i not in hipoteses:
                # print("Chegou ate aqui!")
                hipoteses += (i, )

        lin = aux_linha_de_posi(tab, i)
        pla_cnt = 0
        vaz_cnt = 0

        for el in lin:
            if el == player:
                pla_cnt += 1
            if el == 0:
                vaz_cnt += 1

        if pla_cnt == 2 and vaz_cnt == 1:
            if i not in hipoteses:
                # print("Chegou ate aqui!")
                hipoteses += (i,)

        dia = aux_diagonal_de_posi(tab, i)
        pla_cnt = 0
        vaz_cnt = 0
        if i in (1, 3, 7, 9):
            for el in dia:
                if el == player:
                    pla_cnt += 1
                if el == 0:
                    vaz_cnt += 1

            if pla_cnt == 2 and vaz_cnt == 1:
                if i not in hipoteses:
                    # print("Chegou ate aqui!")
                    hipoteses += (i,)

        if i == 5:  # Apenas para tornar mais claro. Quando i == 5, aux_diagonal retorna 1 tup com 2 tup (caso especial)
            for el in dia:
                pla_cnt = 0
                vaz_cnt = 0
                for el2 in el:
                    if el2 == player:
                        pla_cnt += 1
                    if el2 == 0:
                        vaz_cnt += 1
                if pla_cnt == 2 and vaz_cnt == 1:
                    if i not in hipoteses:
                        # print("Chegou ate aqui!")
                        hipoteses += (i,)
    return hipoteses


def aux_gera_bifucurcacao_paralelo(tab_novo, player, posi):
    playerOposto = -1
    if player == -1:
        playerOposto = 1

    tab_novo = marcar_posicao(tab_novo, player, posi)                # tabuleiro novo em que marco o i na posi de teste
    # print("tabuleiro novo, testePt1: \n", tabuleiro_str(tab_novo))

    tab_novo = marcar_posicao(tab_novo, playerOposto, rule2(tab_novo, playerOposto))
    # ("tabuleiro novo, testePt2: \n", tabuleiro_str(tab_novo))      # como player oposto, bloqueio a vitoria

    # verifico se o player oposto, caso fosse ele a jogar, tem 2 hipoteses de ganhar (havendo bifurcacao)
    # print("hipoteses de ganhar:", aux_hipoteses_ganhar(tab_novo, player))
    return len(aux_hipoteses_ganhar(tab_novo, playerOposto)) >= 2  #gera uma bifucarcao se >= 2. Entao descartamos esta posi


def aux_dois_em_linha(tab, player, posi_bif):
    playerOposto = -1
    if player == -1:
        playerOposto = 1

    tabNova = tab
    livres = obter_posicoes_livres(tab)
    for i in livres:
        #if i not in posi_bif:
            col = aux_coluna_de_posi(tab, i)
            pla_cnt, vaz_cnt = 0, 0

            for el in col:
                if el == player:
                    pla_cnt += 1
                if el == 0:
                    vaz_cnt += 1

            if pla_cnt == 1 and vaz_cnt == 2:
                if not aux_gera_bifucurcacao_paralelo(tabNova, player, i):
                    return i  # marcar_posicao(tab, player, i)

            lin = aux_linha_de_posi(tab, i)
            pla_cnt, vaz_cnt = 0, 0

            for el in lin:
                if el == player:
                    pla_cnt += 1
                if el == 0:
                    vaz_cnt += 1

            if pla_cnt == 1 and vaz_cnt == 2:
                # print("dois_em_linha, lin")
                # print("rule2:", rule2(tab, playerOposto), "posicoes das bifurcacoes:", posi_bif)
                if not aux_gera_bifucurcacao_paralelo(tabNova, player, i):
                    return i  # marcar_posicao(tab, player, i)

            if i in (1, 3, 5, 7, 9):
                dia = aux_diagonal_de_posi(tab, i)
                pla_cnt, vaz_cnt = 0, 0

                if type(dia) == tuple and len(dia) == 3:
                    for el in dia:
                        if el == player:
                            pla_cnt += 1
                        if el == 0:
                            vaz_cnt += 1

                        if pla_cnt == 1 and vaz_cnt == 2:

                            # print("dois_em_linha, dia")
                            if not aux_gera_bifucurcacao_paralelo(tabNova, player, i):
                                return i  # marcar_posicao(tab, player, i)

                if type(dia) == tuple and len(dia) == 2:
                    for el in dia[0]:

                        if el == player:
                            pla_cnt += 1
                        if el == 0:
                            vaz_cnt += 1

                    if pla_cnt == 1 and vaz_cnt == 2:

                        # print("dois_em_linha, dia0")
                        if not aux_gera_bifucurcacao_paralelo(tabNova, player, i):
                            return i  # marcar_posicao(tab, player, i)

                    pla_cnt, vaz_cnt = 0, 0
                    for el in dia[1]:
                        pla_cnt = 0
                        vaz_cnt = 0

                        if el == player:
                            pla_cnt += 1
                        if el == 0:
                            vaz_cnt += 1
                    if pla_cnt == 1 and vaz_cnt == 2:
                        # print("aux, dia1")
                        if not aux_gera_bifucurcacao_paralelo(tabNova, player, i):
                            return i  # marcar_posicao(tab, player, i)

                    # gera uma bifucarcao se >= 2. Entao descartamos esta posi


"""def aux_dois_em_linha(tab, player, posi_bif):

    tabNova = tab
    livres = obter_posicoes_livres(tab)
    for i in livres:
        #if i not in posi_bif:
            col = aux_coluna_de_posi(tab, i)
            pla_cnt, vaz_cnt = 0, 0

            for el in col:
                if el == player:
                    pla_cnt += 1
                if el == 0:
                    vaz_cnt += 1

            if pla_cnt == 1 and vaz_cnt == 2:
                marcar_posicao(tabNova, player, i)
                print("aux, col")
                print(aux_contador_bif(tabNova, player))
                print(len(posi_bif))
                if aux_contador_bif(tabNova, player) < len(posi_bif):
                    return i  # marcar_posicao(tab, player, i)

            lin = aux_linha_de_posi(tab, i)
            pla_cnt, vaz_cnt = 0, 0

            for el in lin:
                if el == player:
                    pla_cnt += 1
                if el == 0:
                    vaz_cnt += 1

            if pla_cnt == 1 and vaz_cnt == 2:
                marcar_posicao(tabNova, player, i)
                print("aux, lin")
                print(aux_contador_bif(tabNova, player))
                print(len(posi_bif))
                if aux_contador_bif(tabNova, player) < len(posi_bif):
                    return i  # marcar_posicao(tab, player, i)

            if i in (1, 3, 5, 7, 9):
                dia = aux_diagonal_de_posi(tab, i)
                pla_cnt, vaz_cnt = 0, 0

                if type(dia) == tuple and len(dia) == 3:
                    for el in dia:
                        if el == player:
                            pla_cnt += 1
                        if el == 0:
                            vaz_cnt += 1

                        if pla_cnt == 1 and vaz_cnt == 2:
                            marcar_posicao(tabNova, player, i)
                            print("aux, dia")
                            print(aux_contador_bif(tabNova, player))
                            print(len(posi_bif))
                            if aux_contador_bif(tabNova, player) < len(posi_bif):
                                return i  # marcar_posicao(tab, player, i)

                if type(dia) == tuple and len(dia) == 2:
                    for el in dia[0]:

                        if el == player:
                            pla_cnt += 1
                        if el == 0:
                            vaz_cnt += 1

                    if pla_cnt == 1 and vaz_cnt == 2:
                        marcar_posicao(tabNova, player, i)
                        print("aux, dia0")
                        print(aux_contador_bif(tabNova, player))
                        print(len(posi_bif))
                        if aux_contador_bif(tabNova, player) < len(posi_bif):
                            return i  # marcar_posicao(tab, player, i)

                    pla_cnt, vaz_cnt = 0, 0
                    for el in dia[1]:
                        pla_cnt = 0
                        vaz_cnt = 0

                        if el == player:
                            pla_cnt += 1
                        if el == 0:
                            vaz_cnt += 1
                    if pla_cnt == 1 and vaz_cnt == 2:
                        marcar_posicao(tabNova, player, i)
                        print("aux, dia1")
                        print(aux_contador_bif(tabNova, player))
                        print(len(posi_bif))
                        if aux_contador_bif(tabNova, player) < len(posi_bif):
                            return i  # marcar_posicao(tab, player, i)"""


def rule4(tab, player):
    playerOposto = -1
    if player == -1:
        playerOposto = 1

    bif_counter = 0
    posi_bif = ()

    livres = obter_posicoes_livres(tab)
    for i in livres:
        col = aux_coluna_de_posi(tab, i)
        pla_cnt = 0
        vaz_cnt = 0

        for el in col:
            if el == playerOposto:
                pla_cnt += 1
            if el == 0:
                vaz_cnt += 1

        if pla_cnt == 1 and vaz_cnt == 2:
            col = ()

        lin = aux_linha_de_posi(tab, i)
        pla_cnt = 0
        vaz_cnt = 0

        for el in lin:
            if el == playerOposto:
                pla_cnt += 1
            if el == 0:
                vaz_cnt += 1

        if pla_cnt == 1 and vaz_cnt == 2:
            lin = ()

        dia = aux_diagonal_de_posi(tab, i)
        pla_cnt = 0
        vaz_cnt = 0
        if i in (1, 3, 7, 9):
            for el in dia:
                if el == playerOposto:
                    pla_cnt += 1
                if el == 0:
                    vaz_cnt += 1

            if pla_cnt == 1 and vaz_cnt == 2:
                dia = ()

        if i == 5:
            diag1 = dia[0]
            diag2 = dia[1]
            pla_cnt, vaz_cnt = 0, 0

            for el in dia[0]:

                if el == playerOposto:
                    pla_cnt += 1
                if el == 0:
                    vaz_cnt += 1

            if pla_cnt == 1 and vaz_cnt == 2:
                diag1 = ()

            pla_cnt, vaz_cnt = 0, 0
            for el in dia[1]:
                pla_cnt = 0
                vaz_cnt = 0

                if el == playerOposto:
                    pla_cnt += 1
                if el == 0:
                    vaz_cnt += 1
            if pla_cnt == 1 and vaz_cnt == 2:
                diag2 = ()

        if i in (2, 4, 6, 8):
            if (col + lin) == ():
                bif_counter += 1
                posi_bif += (i, )
        if i in (1, 3, 7, 9):
            if (col + lin == ()) or (col + dia == ()) or (dia + lin == ()):  # Basta 1 para haver bif
                bif_counter += 1
                posi_bif += (i, )
        if i == 5:
            if (col + lin == ()) or (col + diag1 == ()) or (col + diag2 == ()) or (lin + diag1 == ()) or \
                    (lin + diag2 == ()) or (diag1 + diag2 == 0):
                bif_counter += 1
                posi_bif += (i, )

    # print("rule4:")
    # print(posi_bif)
    # print(bif_counter)
    if bif_counter == 1:
        return posi_bif[0]  # marcar_posicao(tab, player, posi_bif[0])
    if bif_counter > 1:
        return aux_dois_em_linha(tab, player, posi_bif)


"""
tab = ((-1,0,0),(0,1,0),(0,-1,1))
def rule4(tab, player):

tab = ((0,0,0),(0,-1,1),(1,0,0))     expected:O no 9
tab = ((0,0,1),(0,-1,0),(1,0,0))     expected:0 no 2
"""


def rule5(tab, player):
    # print("Chegou a rule 5")
    livres = obter_posicoes_livres(tab)
    if 5 in livres:
        return 5  # marcar_posicao(tab, player, 5)


def rule6(tab, player):
    livres = obter_posicoes_livres(tab)

    playerOposto = -1
    if player == -1:
        playerOposto = 1

    for i in livres:
        if i == 1:
            if tab[2][2] == playerOposto:
                return i  # marcar_posicao(tab, player, i)
        if i == 3:
            if tab[2][0] == playerOposto:
                return i  # marcar_posicao(tab, player, i)
        if i == 7:
            if tab[0][2] == playerOposto:
                return i  # marcar_posicao(tab, player, i)
        if i == 9:
            if tab[0][0] == playerOposto:
                return i  # marcar_posicao(tab, player, i)


def rule7(tab, player):
    livres = obter_posicoes_livres(tab)
    for i in livres:
        if i in (1, 3, 7, 9):
            if eh_posicao_livre(tab, i):
                return i  # marcar_posicao(tab, player, i)


def rule8(tab, player):
    livres = obter_posicoes_livres(tab)
    for i in livres:
        if i in (2, 4, 6, 8):
            if eh_posicao_livre(tab, i):
                return i  # marcar_posicao(tab, player, i)


def escolher_posicao_auto(tab, player2, dificuldade):
    if not(eh_tabuleiro(tab) and (player2 == -1 or player2 == 1) and (dificuldade in ('basico', 'normal', 'perfeito'))):
        raise ValueError('escolher_posicao_auto: algum dos argumentos e invalido')

    if dificuldade == 'basico':
        if type(rule5(tab, player2)) == int:
            return rule5(tab, player2)

        if type(rule7(tab, player2)) == int:
            return rule7(tab, player2)

        return rule8(tab, player2)

    if dificuldade == 'normal':
        if type(rule1(tab, player2)) == int:
            return rule1(tab, player2)
        if type(rule2(tab, player2)) == int:
            return rule2(tab, player2)
        if type(rule5(tab, player2)) == int:
            return rule5(tab, player2)
        if type(rule6(tab, player2)) == int:
            return rule6(tab, player2)
        if type(rule7(tab, player2)) == int:
            return rule7(tab, player2)
        return rule8(tab, player2)

    if dificuldade == 'perfeito':
        if type(rule1(tab, player2)) == int:
            return rule1(tab, player2)
        if type(rule2(tab, player2)) == int:
            return rule2(tab, player2)
        if type(rule3(tab, player2)) == int:
            return rule3(tab, player2)
        if type(rule4(tab, player2)) == int:
            return rule4(tab, player2)
        if type(rule5(tab, player2)) == int:
            return rule5(tab, player2)
        if type(rule6(tab, player2)) == int:
            return rule6(tab, player2)
        if type(rule7(tab, player2)) == int:
            return rule7(tab, player2)
        return rule8(tab, player2)


def jogo_do_galo(desig, dificuldade):           # player1 - pessoa   player2 - computador
    if not (desig == 'X' or desig == 'O' and (dificuldade in ('basico', 'normal', 'perfeito'))):
        raise ValueError('jogo_do_galo: algum dos argumentos e invalido')

    print("Bem-vindo ao JOGO DO GALO.\nO jogador joga com '" + desig + "'.")
    tab = ((0, 0, 0), (0, 0, 0), (0, 0, 0))

    jogadas_totais = 0

    if desig == 'X':
        player1 = 1
        player1desig = 'X'
        player2 = -1
        player2desig = 'O'

    else:
        player1 = -1
        player1desig = 'O'
        player2 = 1
        player2desig = 'X'

    if player1 > player2:            # Pessoa comeca

        #  print(tabuleiro_str(tab))
        posicao = escolher_posicao_manual(tab)
        tab = marcar_posicao(tab, player1, posicao)
        print(tabuleiro_str(tab))

        jogadas_totais += 1

    for i in range(5):

        posicao = escolher_posicao_auto(tab, player2, dificuldade)
        tab = marcar_posicao(tab, player2, posicao)
        print('Turno do computador (' + dificuldade + '):\n' + tabuleiro_str(tab))

        if jogador_ganhador(tab) == 0:
            if jogadas_totais == 8:
                return 'EMPATE'
            jogadas_totais += 1
        else:
            return player2desig

        posicao = escolher_posicao_manual(tab)
        tab = marcar_posicao(tab, player1, posicao)
        print(tabuleiro_str(tab))

        if jogador_ganhador(tab) == 0:
            if jogadas_totais == 8:
                return 'EMPATE'
            jogadas_totais += 1
        else:
            return player1desig
