from unittest import TestCase


class TestRpgPo(TestCase):

    def test_em_batalha_entre_ladino_e_guerreiro_ganha_o_ladino(self):
        escolha_player1 = "ladino"
        escolha_player2 = "guerreiro"
        vencedor = rpgpo.batalha(escolha_player1, escolha_player2)
        self.assertEqual(vencedor, escolha_player1)
        