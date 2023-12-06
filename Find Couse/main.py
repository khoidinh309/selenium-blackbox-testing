import os
import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from page import FindCoursePage
import csv

class TestFindCourse(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.find_course_page = FindCoursePage(self.driver)
        self.driver.get("https://school.moodledemo.net/")
        self.driver.set_page_load_timeout(60)
        
    def tearDown(self):
        self.driver.quit()
        
    def test_find_course(self):
        self.find_course_page.click_login_link()
        self.find_course_page.login("student", "moodle")
        self.find_course_page.select_all_grouping()
        self.find_course_page.sort_by_course_name()
        
        # Get the absolute path of the CSV file
        current_directory = os.path.dirname(__file__)  # Get the directory of the current script
        csv_file_path = os.path.join(current_directory, r".\test.csv")

        # Use this absolute path for opening the CSV file
        with open(csv_file_path, "r") as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                keyword = row[0]  # Get each keyword from the first column in the CSV file
                self.find_course_page.search_course(keyword)
                time.sleep(5)
                # Add your logic here to validate search results
                # For example: EC.presence_of_element_located((By.XPATH, "//your_locator_for_search_results"))
                # assert <some_assertion_here>, "Keyword '{}' not found".format(keyword)

if __name__ == "__main__":
    unittest.main()
