from unittest import TestCase
import game.rpg_po as rpgpo


class TestRpgPo(TestCase):

    def teste_em_batalha_entre_ladino_e_guerreiro_ganha_o_ladino(self):
        escolha_player1 = "ladino"
        escolha_player2 = "guerreiro"
        vencedor = rpgpo.batalha(escolha_player1, escolha_player2)
        self.assertEqual(vencedor, escolha_player1)


    def teste_em_batalha_entre_ladino_e_mago_ganha_o_mago(self):
        escolha_player1 = "ladino"
        escolha_player2 = "mago"
        vencedor = rpgpo.batalha(escolha_player1, escolha_player2) 
        self.assertEqual(vencedor, escolha_player2)


    def teste_em_batalha_entre_guerreiro_e_ladino_ganha_o_ladino(self):
        escolha_player1 = "guerreiro"
        escolha_player2 = "ladino"
        vencedor = rpgpo.batalha(escolha_player1, escolha_player2)
        self.assertEqual(vencedor, escolha_player2)

    def teste_em_batalha_entre_mago_e_ladino_ganha_o_mago(self):
        escolha_player1 = "mago"
        escolha_player2 = "ladino"
        vencedor = rpgpo.batalha(escolha_player1, escolha_player2)
        self.assertEqual(vencedor, escolha_player1)  

    def teste_em_batalha_entre_mago_e_guerreiro_ganha_o_guerreiro(self):
        escolha_player1 = "mago"
        escolha_player2 = "guerreiro"
        vencedor = rpgpo.batalha(escolha_player1, escolha_player2)
        self.assertEqual(vencedor, escolha_player2)
    
    
