import sys
sys.path.append('./RasriosisTest')

import unittest
from selenium import webdriver
from RasriosisTest.main import *
from date import DateObject

class RosariosisTest(unittest.TestCase):
  def setUp(self) -> None:
    self.driver = webdriver.Chrome()
    self.driver.get("https://www.rosariosis.org/demonstration/")
    
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
    
    """ This is main page action set"""
    main_page = MainPage(self.driver)
    main_page.click_grades_menu()
    assert main_page.assignment_type_is_shown()
    
    """ This is accessing assignment action set"""
    assignment_page = AssignmentPage(self.driver)
    assignment_page.click_create_new_assignment()
    assert assignment_page.assignment_form_is_shown()
  
  """ Start testing section of the creating new assignment """
  def test_new_assignment_due_date_less_assigned_date(self):
    self.login_and_access_assignment_page_action()
    
    create_assignment_page = CreateAssignmentPage(self.driver)
    create_assignment_page.input_create_form(DateObject(month="11", day="20", year="2023"), DateObject(month="08",day="14", year="2023"))
    create_assignment_page.click_save_button()
    
    assert create_assignment_page.due_date_less_assigned_date_error()
    self.remove_assignment_after_create()
    
  def test_new_assignment_create_sucessfully(self):
    self.login_and_access_assignment_page_action()
    
    create_assignment_page = CreateAssignmentPage(self.driver)
    create_assignment_page.input_create_form(DateObject(month="11", day="20", year="2023"), DateObject(month="11",day="24", year="2023"))
    create_assignment_page.click_save_button()
    
    assert create_assignment_page.create_new_assignment_succesfully()
    self.remove_assignment_after_create()
    
    
  def test_new_assignment_due_date_is_after_end_of_quarter(self):
    self.login_and_access_assignment_page_action()
    
    create_assignment_page = CreateAssignmentPage(self.driver)
    create_assignment_page.input_create_form(DateObject(month="11", day="20", year="2023"), DateObject(month="12",day="19", year="2024"))
    create_assignment_page.click_save_button()
    
    assert create_assignment_page.due_date_is_after_end_of_quarter()
    self.remove_assignment_after_create()
    
  def test_new_assignment_assigned_date_is_after_end_of_quarter(self):
    self.login_and_access_assignment_page_action()
    
    create_assignment_page = CreateAssignmentPage(self.driver)
    create_assignment_page.input_create_form(DateObject(month="11", day="20", year="2024"), DateObject(month="12",day="19", year="2023"))
    create_assignment_page.click_save_button()
    
    assert create_assignment_page.assigned_date_is_after_end_of_quarter()
    self.remove_assignment_after_create()
    
  def test_new_assignment_both_dates_are_after_end_of_quarter(self):
    self.login_and_access_assignment_page_action()
    
    create_assignment_page = CreateAssignmentPage(self.driver)
    create_assignment_page.input_create_form(DateObject(month="11", day="20", year="2024"), DateObject(month="12",day="19", year="2024"))
    create_assignment_page.click_save_button()
    
    assert create_assignment_page.both_date_are_after_end_of_quarter()
    self.remove_assignment_after_create()
    
  def tearDown(self) -> None:
    self.driver.close()
    
if __name__ == "__main__":
  unittest.main()
    