import sys
sys.path.append('./RasriosisTest')

import unittest
from selenium import webdriver
from RasriosisTest.main import *
from date import DateObject
import csv

class RosariosisTest(unittest.TestCase):
  def setUp(self) -> None:
    self.driver = webdriver.Chrome()
    self.driver.get("https://www.rosariosis.org/demonstration/")
    self.test_case_file_path = 'D:\\Workspace\\selenium\\soft-ware-testing-ass3\\RasriosisTest\\testcase.csv'
    self.test_result_file_path = 'D:\\Workspace\\selenium\\soft-ware-testing-ass3\\RasriosisTest\\test_result.csv'
    
  def remove_assignment_after_create(self):
    wait = WebDriverWait(self.driver, timeout=5)
    delete_btn = self.driver.find_element(*CreateAssignmentPageLocator.DELETE_BUTTON)
    self.driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(1)
    delete_btn.click()
    delete_modal = self.driver.find_element(*CreateAssignmentPageLocator.DELETE_CONFIRMATION_MODAL)
    wait.until(lambda _: delete_modal.is_displayed())
    delete_modal.find_element(*CreateAssignmentPageLocator.CONFIRM_DELETE_BUTTON).click()
    
  def login_and_access_assignment_page_action(self):
    """ This is log in action set""" 
    login_page = LoginPage(self.driver)
    login_page.user_name_element = "teacher"
    login_page.password_element = "teacher"
    login_page.click_submit_button()
    assert login_page.is_login_sucessfully()
    time.sleep(1)
    """ This is main page action set"""
    main_page = MainPage(self.driver)
    main_page.click_grades_menu()
    assert main_page.assignment_type_is_shown()
    time.sleep(1)
    """ This is accessing assignment action set"""
    assignment_page = AssignmentPage(self.driver)
    assignment_page.click_create_new_assignment()
    assert assignment_page.assignment_form_is_shown()
   
  def read_csv_data(self, file_path):
    with open(file_path, 'r') as file:
      reader = csv.DictReader(file)
      return [{'Id': row['Id'],'assigned_date': row['assigned_date'], 'due_date': row['due_date'], 'expected_result': row['expected_result']} for row in reader]
  
  def write_test_results(self, file_path, test_results):
    with open(file_path, 'w', newline='') as file:
      writer = csv.writer(file)
      writer.writerow(['Id', 'Test_Result'])
      for result in test_results:
        writer.writerow([result['Id'], result['Passed']])
  
  def create_date_object(self, date):
    [day, month, year] = date.split('/')
    return DateObject(month=str(month), day=str(day), year=str(year))
  
  def test_create_assignment_rosariosis(self):
    test_cases = self.read_csv_data(self.test_case_file_path)
    test_results = []
    create_assignment_page = CreateAssignmentPage(self.driver)
    wait = WebDriverWait(self.driver, timeout=5)
    
    for data in test_cases:
      with self.subTest(data=data):
        self.login_and_access_assignment_page_action()
        create_assignment_page.input_create_form(self.create_date_object(data['assigned_date']), self.create_date_object(data['due_date']))
        create_assignment_page.click_save_button()
        
        test_result =  create_assignment_page.is_match_expected_result(data['expected_result'])
        assert test_result
        self.remove_assignment_after_create()
        logout_button = self.driver.find_element(*MainPageLocator.LOGOUT_BUTTON)
        wait.until(lambda _: logout_button.is_displayed())
        logout_button.click()
        test_results.append({'Id': data['Id'], 'Passed': ('Passed' if test_result == True else 'Failed')})
        time.sleep(2)
        
    self.write_test_results(self.test_result_file_path, test_results)
      
    
  def tearDown(self) -> None:
    self.driver.close()
    
if __name__ == "__main__":
  unittest.main()
    