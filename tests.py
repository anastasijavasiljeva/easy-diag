import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import autoit
from selenium.webdriver.common.by import By

#D:\Documents\Teh uni\8 semestras\BBD\test.txt

class UploadTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://google.com")
        

    def test_1(self):
        time.sleep(5)
    def test_2(self):
        time.sleep(5)
    def test_3(self):
        time.sleep(5)
    def test_4(self):
        time.sleep(5)
    def test_5(self):
        time.sleep(5)
    def test_6(self):
        time.sleep(5)
    def test_7(self):
        time.sleep(5)
    def test_8(self):
        time.sleep(5)
    def test_9(self):
        time.sleep(5)
    def test_10(self):
        time.sleep(5)
    def test_11(self):
        time.sleep(5)
    def test_12(self):
        time.sleep(5)
    def test_13(self):
        time.sleep(5)
    def test_14(self):
        time.sleep(5)
    def test_15(self):
        time.sleep(5)
    
    def tearDown(self):
        self.driver.close()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(UploadTests('test_1'))
    suite.addTest(UploadTests('test_2'))
    suite.addTest(UploadTests('test_3'))
    suite.addTest(UploadTests('test_4'))
    suite.addTest(UploadTests('test_5'))
    suite.addTest(UploadTests('test_6'))
    suite.addTest(UploadTests('test_7'))
    suite.addTest(UploadTests('test_8'))
    suite.addTest(UploadTests('test_9'))
    suite.addTest(UploadTests('test_10'))
    suite.addTest(UploadTests('test_11'))
    suite.addTest(UploadTests('test_12'))
    suite.addTest(UploadTests('test_13'))
    suite.addTest(UploadTests('test_14'))
    suite.addTest(UploadTests('test_15'))
    return suite

# execute the script
if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())