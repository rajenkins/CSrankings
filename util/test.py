from csrankings import *
import unittest

class TestMain(unittest.TestCase):
	testdict = None
	def test_csv_to_dict(self):
		testdict = csv2dict_str_str("testData.csv")
		self.assertEqual(testdict["Claudio Orlandi"], "Aarhus University")
	def test_start_page(self):
		st = startpage("12-37")
		self.assertEqual(st, 12)
	def test_start_page_adv(self):
                st = startpage("12-22:24-37")
		self.assertEqual(st, 12)
	def test_pagecount(self):
		ct = pagecount("123-456")
		self.assertEqual(ct, 334)
	def test_pagecount_adv(self):
                ct = pagecount("1-2:3-4")
                self.assertEqual(ct, 2)

if __name__ == '__main__':
    unittest.main()
