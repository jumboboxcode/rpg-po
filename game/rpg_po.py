import getpass
import time

def batalha(escolha_player1, escolha_player2):
    if escolha_player1=="ladino" and escolha_player2=="mago": return "mago"
    if escolha_player1=="ladino" and escolha_player2=="guerreiro": return "ladino"
    if escolha_player1=="guerreiro" and escolha_player2=="ladino": return "ladino"
    if escolha_player1=="mago" and escolha_player2=="ladino": return "mago"
    if escolha_player1=="mago" and escolha_player2=="guerreiro": return "guerreiro"
    if escolha_player1=="guerreiro" and escolha_player2=="mago": return "guerreiro"

def main():
    print("player1,faça sua escolha! você vai à batalha como ladino, mago, ou guerreiro?")
    escolha_player1 = getpass.getpass("player1, digite sua escolha e aperte enter...")
    
    print("player2,faça sua escolha! você vai à batalha como ladino, mago, ou guerreiro?")
    escolha_player2 = getpass.getpass("player2, digite sua escolha e aperte enter...")
    
    print("E a batalha começa...")
    print("QUE VENÇA O MELHOR!")
    time.sleep(3)

    vencedor = batalha (escolha_player1, escolha_player2)
    if vencedor==escolha_player1: print("player1, você venceu essa grande e honrada batalha!!!")
    if vencedor==escolha_player2: print("player2, você venceu essa grande e honrada batalha!!!")
    










if  __name__ == "__main__":
    main()
