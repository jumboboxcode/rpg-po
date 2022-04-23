import getpass
import time

def main():
    jogador_quer_continuar = "sim"

    mostrar_boas_vindas()
    mostrar_espacos()
    while jogador_quer_continuar == "sim":
        entrar_na_batalha()
        jogador_quer_continuar = ver_se_o_jogador_quer_continuar()
        mostrar_espacos()

def mostrar_boas_vindas():
    print("BEM VINDO AO RPG-PÔ!!!")
    time.sleep(1)
    print("DIA DE BATALHA!")

def mostrar_espacos():
    print("--------------------------------")

def entrar_na_batalha():
    escolha_do_player1 = oferecer_escolha_ao_player1()
    escolha_do_player2 = oferecer_escolha_ao_player2()
    mostrar_mensagem_de_suspense()
    mostrar_resultado(escolha_do_player1, escolha_do_player2)

def ver_se_o_jogador_quer_continuar():
    print("Você quer jogar mais uma partida? Em caso positivo, digite sim: ")
    preferência = input()
    return preferência

def oferecer_escolha_ao_player1():
    print("player1,faça sua escolha! você vai à batalha como ladino, mago, ou guerreiro?")
    escolha_player1 = getpass.getpass("player1, digite sua escolha e aperte enter...")
    mostrar_espacos()
    return escolha_player1

def oferecer_escolha_ao_player2():
    print("player2,faça sua escolha! você vai à batalha como ladino, mago, ou guerreiro?")
    escolha_player2 = getpass.getpass("player2, digite sua escolha e aperte enter...")
    mostrar_espacos()
    return escolha_player2

def mostrar_mensagem_de_suspense():
    print("Um velho misterioso diz que é ninguém e aposta no nada...")
    mostrar_espacos()

    time.sleep(1)

    print("E a batalha começa...")
    print("QUE VENÇA O MELHOR!")
    time.sleep(3)

def mostrar_resultado(escolha_do_player1, escolha_do_player2):
    ninguém = "nada"
    vencedor = batalha (escolha_do_player1, escolha_do_player2, ninguém)
    if vencedor==escolha_do_player1: print("player1, você venceu essa grande e honrada batalha!!!")
    if vencedor==escolha_do_player2: print("player2, você venceu essa grande e honrada batalha!!!")
    if vencedor==ninguém: print ("a batalha foi uma bagunça! tanto que aquelhe velho foi considerado vencedor!") 
    time.sleep(3)
    mostrar_espacos()

def batalha(escolha_player1, escolha_player2, ninguém):
    if escolha_player1=="ladino" and escolha_player2=="mago" and ninguém=="nada": return "mago"
    if escolha_player1=="ladino" and escolha_player2=="guerreiro" and ninguém=="nada": return "ladino"
    if escolha_player1=="guerreiro" and escolha_player2=="ladino" and ninguém=="nada": return "ladino"
    if escolha_player1=="mago" and escolha_player2=="ladino" and ninguém=="nada": return "mago"
    if escolha_player1=="mago" and escolha_player2=="guerreiro" and ninguém=="nada": return "guerreiro"
    if escolha_player1=="guerreiro" and escolha_player2=="mago" and ninguém=="nada": return "guerreiro"
    if escolha_player1=="ladino" and escolha_player2=="ladino" and ninguém=="nada": return "nada"
    if escolha_player1=="guerreiro" and escolha_player2=="guerreiro" and ninguém=="nada": return "nada"
    if escolha_player1=="mago" and escolha_player2=="mago" and ninguém=="nada": return "nada"
    if escolha_player1 != ("ladino, mago, guerreiro") and escolha_player2 != ("ladino, mago, guerreiro") and ninguém=="nada": return "nada"

if  __name__ == "__main__":
    main()