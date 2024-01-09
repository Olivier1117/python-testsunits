import unittest

from calcul import Calcul

# classe de tests
class TestCalcul (unittest.TestCase):
    
    # methode de set up
    def setUp (self):
        self.calc = Calcul()
        
    # Test d'addition
    def test_additionner_2_pos(self):
        resultat = self.calc.additionner(3,5)
        resultat_attendu = 8
        # test l'égalité
        self.assertEqual(resultat, resultat_attendu, "Addition OK")
    
    def test_additionner_2_neg(self):
        resultat = self.calc.additionner(-3,-5)
        resultat_attendu = -8
        # test l'égalité
        self.assertEqual(resultat, resultat_attendu, "Addition OK")
    
    def test_additionner_neg_pos(self):
        resultat = self.calc.additionner(-3,5)
        resultat_attendu = 2
        # test l'égalité
        self.assertEqual(resultat, resultat_attendu, "Addition OK")
    
    def test_additionner_pos_neg(self):
        resultat = self.calc.additionner(3,-5)
        resultat_attendu = -2
        # test l'égalité
        self.assertEqual(resultat, resultat_attendu, "Addition OK")
    
    # Test de soustraction
    def test_soustraire(self):
        resultat = self.calc.soustraire(5,3)
        resultat_attendu = 2
        # test l'égalité
        self.assertEqual(resultat, resultat_attendu, "Soustraction OK")
        
    # Test de multiplication
    def test_multiplier(self):
        resultat = self.calc.multiplier(5,3)
        resultat_attendu = 15
        # test l'égalité
        self.assertEqual(resultat, resultat_attendu, "Multiplication OK")
        
    # Test de division
    def test_diviser(self):
        resultat = self.calc.diviser(6,3)
        resultat_attendu = 2
        # test l'égalité
        self.assertEqual(resultat, resultat_attendu, "Division OK")
    
    # Test de division par 0
    def test_diviser_0(self):
        self.assertEqual(resultat, resultat_attendu, "Division OK")
        with self.assertRaises(ZeroDivisionError, msg="Division par zéro impossible"):
                    self.calc.diviser(5, 0)
        
        
# Exécuter les tests si le script est exécuté directement
if __name__ == '__main__':
    unittest.main()
