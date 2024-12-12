import unittest
from Clases import Simulator, Clase


class TestSimulator(unittest.TestCase):

    def setUp(self):
        self.simulador = Simulator()

    def test_class_creation_with_valid_data(self):
        self.simulador.add_class("Y", ["x", "e"])
        self.assertIsInstance(self.simulador.classes["Y"], Clase)
        self.assertEqual(self.simulador.classes["Y"].getmetodo("x"), "Y :: x")
        self.assertEqual(self.simulador.classes["Y"].getmetodo("e"), "Y :: e")

    def test_class_creation_with_existing_name(self):
        self.simulador.add_class("W", ["k", "m"])
        self.simulador.add_class("W", ["r"])
        self.assertEqual(len(self.simulador.classes), 1)

    def test_class_creation_with_non_existing_superclass(self):
        self.simulador.add_class("U", ["v", "a"], "L")
        self.assertEqual(len(self.simulador.classes), 0)

    def test_class_creation_with_duplicate_methods(self):
        self.simulador.add_class("Q", ["b", "b"])
        self.assertEqual(len(self.simulador.classes), 0)

    def test_class_creation_with_self_inheritance(self):
        self.simulador.add_class("T", ["p", "s"], "T")
        self.assertEqual(len(self.simulador.classes), 0)

    def test_describe_non_existing_class(self):
        self.assertIsNone(self.simulador.describe_class("L"))

    def test_describe_class_without_methods(self):
        self.simulador.add_class("N", [])
        self.assertEqual(self.simulador.describe_class("N"), "La clase N no tiene metodos")

    def test_describe_class_example_exam(self):
        self.simulador.add_class("G", ["j", "h"])
        self.assertIsInstance(self.simulador.classes["G"], Clase)
        self.assertEqual(self.simulador.classes["G"].getmetodo("j"), "G :: j")
        self.assertEqual(self.simulador.classes["G"].getmetodo("h"), "G :: h")
        self.simulador.add_class("Z", ["j", "i"], "G")
        self.assertIsInstance(self.simulador.classes["Z"], Clase)
        self.assertEqual(self.simulador.classes["Z"].getmetodo("h"), "G :: h")
        self.assertEqual(self.simulador.classes["Z"].getmetodo("i"), "Z :: i")
        self.assertEqual(self.simulador.classes["Z"].getmetodo("j"), "Z :: j")
        self.assertEqual(self.simulador.describe_class("G"), "j -> G :: j\nh -> G :: h")
        self.assertEqual(self.simulador.describe_class("Z"), "j -> Z :: j\ni -> Z :: i\nh -> G :: h")

    def test_class_creation_without_methods(self):
        self.simulador.add_class("O", [])
        self.assertIsInstance(self.simulador.classes["O"], Clase)

    def test_class_creation_with_superclass_having_methods(self):
        self.simulador.add_class("Y", ["x", "e"])
        self.simulador.add_class("V", ["d", "f"], "Y")
        self.assertIsInstance(self.simulador.classes["V"], Clase)
        self.assertEqual(self.simulador.classes["V"].getmetodo("d"), "V :: d")
        self.assertEqual(self.simulador.classes["V"].getmetodo("f"), "V :: f")

    def test_class_creation_with_superclass_without_methods(self):
        self.simulador.add_class("O", [])
        self.simulador.add_class("W", ["k", "l"], "O")
        self.assertIsInstance(self.simulador.classes["W"], Clase)
        self.assertEqual(self.simulador.classes["W"].getmetodo("k"), "W :: k")
        self.assertEqual(self.simulador.classes["W"].getmetodo("l"), "W :: l")

    def test_describe_class_with_superclass_having_methods(self):
        self.simulador.add_class("Y", ["x", "e"])
        self.simulador.add_class("S", ["u", "z"], "Y")
        self.assertEqual(self.simulador.describe_class("S"), "u -> S :: u\nz -> S :: z\nx -> Y :: x\ne -> Y :: e")

    def test_describe_class_with_superclass_without_methods(self):
        self.simulador.add_class("O", [])
        self.simulador.add_class("X", ["t", "g"], "O")
        self.assertEqual(self.simulador.describe_class("X"), "t -> X :: t\ng -> X :: g")


if __name__ == '__main__':
    unittest.main()
