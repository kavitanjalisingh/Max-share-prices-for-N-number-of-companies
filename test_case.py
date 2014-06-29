import unittest
from highest_share_price import HighestShareForCompany


class HSFCTest(unittest.TestCase):
    """
    Test cases of highest share for companies in year and month.
    """
    def setUp(self):
        self.data = '/home/kavitanjali/Documents/assignment/test.csv'


    def test_check_total_companies(self):
        """
        Check the total number of company data in CSV.
        """
        self.assertEqual(len(HighestShareForCompany(self.data)), 4)


    def test_yearnmonth_of_highestshare_companyB(self):
        """
        Test the year and month of highest share for companyB.
	"""
        self.assertEqual(
            HighestShareForCompany(self.data)[1]['CompanyB'],
            (1990, ' Feb', 1578))


    def test_yearnmonth_of_highestshare_companyA(self):
        """
        If the highest share price occurs in more than once,
        it will list all the years and their respective months \
        in which share price was highest.
	"""
        self.assertEqual(
            HighestShareForCompany(self.data)[0]['CompanyA'],
            [(1997, 'Mar', 5465), (1997, 'May', 5465)])


if __name__ == '__main__':
    unittest.main()
