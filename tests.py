from typing_extensions import Self
import unittest
#from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import autoit
from selenium.webdriver.common.by import By
from seleniumwire import webdriver

#D:\Documents\Teh uni\8 semestras\BBD\test.txt

enable_localhost_ssl  = "chrome.send('enableExperimentalFeature', ['allow-insecure-localhost', 'true'])"

def chrome_configure_experimental_flags(myDriver):
    myDriver.get('chrome://flags')                      
    myDriver.execute_script(enable_localhost_ssl)        
    myDriver.get('chrome://flags')                      
    time.sleep(5)         

class WebAppTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        chrome_configure_experimental_flags(self.driver)
        self.driver.get("https://127.0.0.1:5000")
        time.sleep(5)
        
    def test_uploadvalidimg(self):
        upload_btn = self.driver.find_element(By.CLASS_NAME, 'dropzone')
        upload_btn.click()
        time.sleep(5)
        autoit.win_active("Open") 
        autoit.control_set_text("Open","Edit1",r"D:\Documents\Teh uni\8 semestras\BBD\data\fracture\P_09294_1.png")
        autoit.control_send("Open","Edit1","{ENTER}")
        time.sleep(3)
        img_preview = self.driver.find_element(By.CLASS_NAME, 'imgPreview')
        self.assertTrue(img_preview.is_displayed())
    
    def test_uploadinvalidfile(self):
        upload_btn = self.driver.find_element(By.CLASS_NAME, 'dropzone')
        upload_btn.click()
        time.sleep(5)
        autoit.win_active("Open") 
        autoit.control_set_text("Open","Edit1",r"D:\Documents\Teh uni\8 semestras\BBD\test.txt")
        autoit.control_send("Open","Edit1","{ENTER}")
        time.sleep(3)
        img_preview = self.driver.find_elements(By.CLASS_NAME, 'imgPreview')
        self.assertFalse(img_preview)

    def test_inactiveupload(self):
        upload_btn = self.driver.find_element(By.CLASS_NAME, 'btn-success')
        self.assertFalse(upload_btn.is_enabled())

    def test_inactiveremove(self):
        clear_btn = self.driver.find_element(By.CLASS_NAME, 'btn-secondary')
        self.assertFalse(clear_btn.is_enabled())

    def test_removevalidimg(self):
        upload_btn = self.driver.find_element(By.CLASS_NAME, 'dropzone')
        upload_btn.click()
        time.sleep(5)
        autoit.win_active("Open") 
        autoit.control_set_text("Open","Edit1",r"D:\Documents\Teh uni\8 semestras\BBD\data\fracture\P_09294_1.png")
        autoit.control_send("Open","Edit1","{ENTER}")
        time.sleep(3)
        img_preview = self.driver.find_element(By.CLASS_NAME, 'imgPreview')
        clear_btn = self.driver.find_element(By.CLASS_NAME, 'btn-secondary')
        clear_btn.click()
        time.sleep(2)
        self.assertFalse(clear_btn.is_enabled())

    def test_sendimage(self):
        upload_btn = self.driver.find_element(By.CLASS_NAME, 'dropzone')
        upload_btn.click()
        time.sleep(5)
        autoit.win_active("Open") 
        autoit.control_set_text("Open","Edit1",r"D:\Documents\Teh uni\8 semestras\BBD\data\fracture\P_09294_1.png")
        autoit.control_send("Open","Edit1","{ENTER}")
        time.sleep(3)
        send_btn = self.driver.find_element(By.CLASS_NAME, 'btn-success')
        send_btn.click()
        time.sleep(5)
        self.assertTrue(self.driver.find_element(By.CLASS_NAME, 'dropzone') == -1)

    def test_resultisdisplayed(self):
        upload_btn = self.driver.find_element(By.CLASS_NAME, 'dropzone')
        upload_btn.click()
        time.sleep(5)
        autoit.win_active("Open") 
        autoit.control_set_text("Open","Edit1",r"D:\Documents\Teh uni\8 semestras\BBD\data\fracture\P_09294_1.png")
        autoit.control_send("Open","Edit1","{ENTER}")
        time.sleep(3)
        send_btn = self.driver.find_element(By.CLASS_NAME, 'btn-success')
        send_btn.click()
        time.sleep(8)
        self.assertTrue(self.driver.find_element(By.CLASS_NAME, 'resultImg').is_displayed())

    def test_explanationtextisdisplayed(self):
        upload_btn = self.driver.find_element(By.CLASS_NAME, 'dropzone')
        upload_btn.click()
        time.sleep(5)
        autoit.win_active("Open") 
        autoit.control_set_text("Open","Edit1",r"D:\Documents\Teh uni\8 semestras\BBD\data\fracture\P_09294_1.png")
        autoit.control_send("Open","Edit1","{ENTER}")
        time.sleep(3)
        send_btn = self.driver.find_element(By.CLASS_NAME, 'btn-success')
        send_btn.click()
        time.sleep(8)
        self.assertTrue(self.driver.find_element(By.CSS_SELECTOR, 'h2').is_displayed())

    def test_precision1(self):
        upload_btn = self.driver.find_element(By.CLASS_NAME, 'dropzone')
        upload_btn.click()
        time.sleep(5)
        autoit.win_active("Open") 
        autoit.control_set_text("Open","Edit1",r"D:\Documents\Teh uni\8 semestras\BBD\data\fracture\P_09294_1.png")
        autoit.control_send("Open","Edit1","{ENTER}")
        time.sleep(3)
        send_btn = self.driver.find_element(By.CLASS_NAME, 'btn-success')
        send_btn.click()
        time.sleep(8)
        self.assertTrue(self.driver.find_element(By.CSS_SELECTOR, 'h2').text.find("88%") != -1)

    def test_contrast(self):
        contrast_switch = self.driver.find_element(By.CLASS_NAME, 'MuiSwitch-input')
        contrast_switch.click()
        time.sleep(3)
        self.assertTrue(self.driver.find_element(By.CSS_SELECTOR, '[data-theme=light]') != -1)

    def test_language(self):
        time.sleep(5)
        self.assertTrue(self.driver.find_elements(By.CSS_SELECTOR, '.App>div>div')[0].text == 'Upload a fracture image and start diagnosing!')

    def test_changeimage(self):
        upload_btn = self.driver.find_element(By.CLASS_NAME, 'dropzone')
        upload_btn.click()
        time.sleep(5)
        autoit.win_active("Open") 
        autoit.control_set_text("Open","Edit1",r"D:\Documents\Teh uni\8 semestras\BBD\data\fracture\P_09294_1.png")
        autoit.control_send("Open","Edit1","{ENTER}")
        time.sleep(3)
        upload_btn = self.driver.find_element(By.CLASS_NAME, 'dropzone')
        upload_btn.click()
        time.sleep(5)
        autoit.win_active("Open") 
        autoit.control_set_text("Open","Edit1",r"D:\Documents\Teh uni\8 semestras\BBD\data\fracture\P_09294_2.png")
        autoit.control_send("Open","Edit1","{ENTER}")
        time.sleep(3)
        self.assertTrue(self.driver.find_elements(By.CSS_SELECTOR, '.selected-file .row')[1].text == 'P_09294_2.png')

    def test_download(self):
        upload_btn = self.driver.find_element(By.CLASS_NAME, 'dropzone')
        upload_btn.click()
        time.sleep(5)
        autoit.win_active("Open") 
        autoit.control_set_text("Open","Edit1",r"D:\Documents\Teh uni\8 semestras\BBD\data\fracture\P_09294_1.png")
        autoit.control_send("Open","Edit1","{ENTER}")
        time.sleep(3)
        send_btn = self.driver.find_element(By.CLASS_NAME, 'btn-success')
        send_btn.click()
        time.sleep(8)
        self.assertTrue(self.driver.find_element(By.CLASS_NAME, 'btn-success').is_enabled())

    def test_return(self):
        upload_btn = self.driver.find_element(By.CLASS_NAME, 'dropzone')
        upload_btn.click()
        time.sleep(5)
        autoit.win_active("Open") 
        autoit.control_set_text("Open","Edit1",r"D:\Documents\Teh uni\8 semestras\BBD\data\fracture\P_09294_1.png")
        autoit.control_send("Open","Edit1","{ENTER}")
        time.sleep(3)
        send_btn = self.driver.find_element(By.CLASS_NAME, 'btn-success')
        send_btn.click()
        time.sleep(8)
        self.assertTrue(self.driver.find_element(By.CLASS_NAME, 'btn-secondary').is_enabled())

    def test_checkhttps(self):
        self.driver.get("https://127.0.0.1:5000")
        response = self.driver.requests[0].response
        self.assertTrue(response.status_code == 200)
    
    def tearDown(self):
        self.driver.close()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(WebAppTests('test_uploadvalidimg'))
    suite.addTest(WebAppTests('test_uploadinvalidfile'))
    suite.addTest(WebAppTests('test_inactiveupload'))
    suite.addTest(WebAppTests('test_inactiveremove'))
    suite.addTest(WebAppTests('test_removevalidimg'))
    suite.addTest(WebAppTests('test_sendimage'))
    suite.addTest(WebAppTests('test_resultisdisplayed'))
    suite.addTest(WebAppTests('test_explanationtextisdisplayed'))
    suite.addTest(WebAppTests('test_precision1'))
    suite.addTest(WebAppTests('test_contrast'))
    suite.addTest(WebAppTests('test_language'))
    suite.addTest(WebAppTests('test_changeimage'))
    suite.addTest(WebAppTests('test_download'))
    suite.addTest(WebAppTests('test_return'))
    suite.addTest(WebAppTests('test_checkhttps'))
    return suite

# execute the script
if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())