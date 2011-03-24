import unittest
from should_dsl import should
from codigo_morse import codigo_morse

class TestCodigoMorse(unittest.TestCase):
    def test_a_em_morse(self):
        codigo_morse("a") |should| equal_to ("._")

    def test_b_em_morse(self):
        codigo_morse("b") |should| equal_to("_...")

    def test_casa_em_morse(self):
        codigo_morse("casa") |should| equal_to("_._.._...._")

    def test_Weslleymberg_em_morse(self):
        codigo_morse("weslleymberg") |should| equal_to("\
.__....._..._..._._____....._.__.")

if __name__ == "__main__":
    unittest.main()
