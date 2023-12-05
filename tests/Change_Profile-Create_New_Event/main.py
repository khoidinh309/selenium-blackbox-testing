import unittest
# import HTMLTestRunner
from read_data import Read
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from parameterized import parameterized
from steps import ChangProfile, CreateEvent

data_profile = Read().read('./data_profile.csv')
data_event = Read().read("./data_event.csv")

class TestChangeProfile(unittest.TestCase):
    def setUp(self):
        print("========== [ Begin Test ] ==========")
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.get("https://school.moodledemo.net/user/profile.php")

    @parameterized.expand(data_profile)
    def test_change_profile(self, fname,lname, email, message1, message2, message3, title):
        result = ChangProfile(self.driver).test_change_profile(fname, lname, email)
        self.assertTrue(result)


    def tearDown(self):
        self.driver.quit()
        print("========== [ End Test ] ==========")

class TestCreateEvent(unittest.TestCase):
    def setUp(self):
        print("========== [ Begin Test ] ==========")
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://sandbox.moodledemo.net/login/index.php")
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()

    @parameterized.expand(data_event)
    def test_create_event(self, title, start_date, start_month, duration_date, duration_month, duration_min):
        result = CreateEvent(self.driver).test_create_event(title, start_date, start_month, duration_date, duration_month, duration_min)
        self.assertTrue(result)


    def tearDown(self):
        self.driver.quit()
        print("========== [ End Test ] ==========")

if __name__ == "__main__":
    unittest.main()