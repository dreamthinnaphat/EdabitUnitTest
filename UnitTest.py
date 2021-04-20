import unittest
import Program

class TestCalc(unittest.TestCase):

    def test_invert(self):
        self.assertEqual(Program.invert({ "z": "q", "w": "f" }),  {"q": "z", "f": "w"})
        self.assertEqual(Program.invert({ "a": 1, "b": 2, "c": 3 }), { 1: "a", 2: "b", 3: "c" })
        self.assertEqual(Program.invert({ "zebra": "koala", "horse": "camel" }), { "koala": "zebra", "camel": "horse" })

    def test_format_date(self):
        self.assertEqual(Program.format_date("11/12/2019"), "20191211")
        self.assertEqual(Program.format_date("12/31/2019"), "20193112")
        self.assertEqual(Program.format_date("01/15/2019"), "20191501")

    def test_Expensive(self):
        self.assertEqual(Program.expensive_orders({ "a": 3000, "b": 200, "c": 1050 }, 1000), { "a": 3000, "c": 1050 })
        self.assertEqual(Program.expensive_orders({ "Gucci Fur": 24600, "Teak Dining Table": 3200, "Louis Vutton Bag": 5550, "Dolce Gabana Heels": 4000 }, 20000), { "Gucci Fur": 24600 })
        self.assertEqual(Program.expensive_orders({ "Deluxe Burger": 35, "Icecream Shake": 4, "Fries": 5 }, 40), {})

    def test_Emphasise(self):
        self.assertEqual(Program.emphasise("hello world"), "Hello World")
        self.assertEqual(Program.emphasise("GOOD MORNING"), "Good Morning")
        self.assertEqual(Program.emphasise("99 red balloons!"), "99 Red Balloons!")
    
    def test_Reversible(self):
        self.assertEqual(Program.reversible_inclusive_list(1, 5), [1, 2, 3, 4, 5])
        self.assertEqual(Program.reversible_inclusive_list(2, 8), [2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(Program.reversible_inclusive_list(10, 20), [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
        self.assertEqual(Program.reversible_inclusive_list(24, 17), [24, 23, 22, 21, 20, 19, 18, 17])


if __name__ == '__main__':
    unittest.main()
