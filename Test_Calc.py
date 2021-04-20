import unittest
import Calc

class TestCalc(unittest.TestCase):

    def test_invert(self):
        self.assertEqual(Calc.invert({ "z": "q", "w": "f" }),  {"q": "z", "f": "w"} )
        self.assertEqual(Calc.invert({ "a": 1, "b": 2, "c": 3 }), { 1: "a", 2: "b", 3: "c" })
        self.assertEqual(Calc.invert({ "zebra": "koala", "horse": "camel" }), { "koala": "zebra", "camel": "horse" })


if __name__ == '__main__':
    unittest.main()
