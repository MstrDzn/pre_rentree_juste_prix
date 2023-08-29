import unittest
import verif from prerentree_demo

class TestStringMethods(unittest.TestCase):

    def test_bravo(self):
        resultat = verif(5,5)
        self.assertEqual(resultat, True)

    def test_non_trouvé(self):
        resultat = verif(5,3)
        self.assertEqual(resultat, True)
        
if __name__ == '__main__':
    unittest.main()