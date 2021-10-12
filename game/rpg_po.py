import getpass
import time

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

def main():
    print("BEM VINDO AO RPG-PÔ!!!")
    
    time.sleep(1)

    print("aquele era o dia, os player acordavam... eles têm poderes e rivalidades entre sí incríveis... rola uma luta daora!")

    time.sleep(2)

    print("player1,faça sua escolha! você vai à batalha como ladino, mago, ou guerreiro?")
    escolha_player1 = getpass.getpass("player1, digite sua escolha e aperte enter...")
    
    print("player2,faça sua escolha! você vai à batalha como ladino, mago, ou guerreiro?")
    escolha_player2 = getpass.getpass("player2, digite sua escolha e aperte enter...")
    
    print("um velho misterioso diz que é ninguém e aposta no nada...")
    ninguém = "nada"

    time.sleep(1)

    print("E a batalha começa...")
    print("QUE VENÇA O MELHOR!")
    time.sleep(3)

    vencedor = batalha (escolha_player1, escolha_player2, ninguém)
    if vencedor==escolha_player1: print("player1, você venceu essa grande e honrada batalha!!!")
    if vencedor==escolha_player2: print("player2, você venceu essa grande e honrada batalha!!!")
    if vencedor==ninguém: print ("a batalha foi muito disputada, ambos morreram, então, não é que aquele velho estava certo? ninguém foi considerado vencedor!... nada... nada...")
    preferência = input()
    
    



if  __name__ == "__main__":
    main()
