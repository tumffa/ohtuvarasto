import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(-2, -4)
        self.varasto = Varasto(3, -2)
        self.varasto = Varasto(10, 11)
        self.varasto = Varasto(10, 0)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_lisaa_varastoon_miinusmaara_palauttaa_none(self):
        #metodi palauttaa 0
        self.assertEqual(self.varasto.lisaa_varastoon(-5), None)

    def test_lisaa_enemman_kuin_mahtuu(self):
        self.varasto.lisaa_varastoon(13)
        self.assertEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_ota_varastosta_miinusmaara_palauttaa_nolla(self):
        #metodi palauttaa 0
        self.assertEqual(self.varasto.ota_varastosta(-5), 0.0)

    def test_ota_enemman_kuin_on_saldoa(self):
        max = self.varasto.saldo
        #ottaa kaiken saldon, eli metodi palauttaa saldon
        self.assertEqual(self.varasto.ota_varastosta(13), max)

    def test_str_toimii(self):
        #tila=10 ja saldo=0 eli tulostus on seuraava
        self.assertEqual(self.varasto.__str__(), "saldo = 0, vielä tilaa")