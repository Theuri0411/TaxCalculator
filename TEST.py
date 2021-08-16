import unittest
import person as person

elijah = person.Person(
    "Elijah",
    23,
    100)


class MyTestCase(unittest.TestCase):
    def test_net_pay_calculations(self):
        """Test Net Pay"""
        net_pay = elijah.calc_tax(10)
        self.assertEqual(90, net_pay)

    def test_calc(self):
        """Test Calculator OutPut"""
        self.assertEqual("| 1 | Elijah | 23 | 100 | 91.0 |", elijah.toString(1))

    def test_tax_age_bracket_45(self):
        """Test tax with the age bracket of less than 46 years"""
        net_pay_age = elijah.total_calc_tax()
        self.assertEqual(91, net_pay_age)

    def test_tax_age_bracket_65(self):
        """Test tax with the age bracket of greater than 45 less than 66 years"""
        net_pay_age = elijah.total_calc_tax()
        self.assertNotEqual(95, net_pay_age)

    def test_tax_age_bracket_above_65(self):
        """Test tax with the age bracket of greater than 65 years"""
        net_pay_age = elijah.total_calc_tax()
        self.assertNotEqual(97, net_pay_age)


if __name__ == '__main__':
    unittest.main()