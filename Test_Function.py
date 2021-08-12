import unittest
import tax_calculator as tx


class MyTestCase(unittest.TestCase):
    def test_something(self):
        ##Test Tax_Calculator

        # net_pay = tx.cal_tax(10, 100)
        net_pay_age = tx.cal_tax(100, 10)

        # self.assertEqual(90, net_pay)
        self.assertEqual(91, net_pay_age)


if __name__ == '__main__':
    unittest.main()
