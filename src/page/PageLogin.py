from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PageLongin:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.btn_online_banking=(By.XPATH, "//a[normalize-space()='Online Banking']")


    def click_button(self):
        self.wait.until(self,EC.element_to_be_clickable(self.btn_online_banking))
        #self.driver.find_element(*self.btn_online_banking).click()

