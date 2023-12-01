from element import *
from locator import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
import time

class BasePage(object):
  def __init__(self, driver) -> None:
    self.driver = driver
    
class LoginPage(BasePage):
  
  user_name_element = UserNameElement()
  password_element = PasswordElement()
  
  def click_submit_button(self):
    login_button = self.driver.find_element(*LoginPageLocator.LOGIN_BUTTON)
    login_button.click()
    
  def is_login_sucessfully(self):
    return "Incorrect username or password" not in self.driver.page_source
  
class MainPage(BasePage):
  
  def click_grades_menu(self):
    wait = WebDriverWait(self.driver, 5)
    grade_menu = self.driver.find_element(*MainPageLocator.GRADE_MENU)
    wait.until(lambda _: grade_menu.is_displayed())
    grade_menu.click()
    
    WebDriverWait(self.driver, 2).until(
      lambda driver: driver.find_element(*MainPageLocator.GRADE_MENU_UL).is_displayed()
    )
    
    self.driver.find_element(*MainPageLocator.ASSIGNMENT_ITEM_IN_MENU).click()
    
  def assignment_type_is_shown(self):
    return "Assignment Type" in self.driver.page_source
  
class AssignmentPage(BasePage):
  def click_create_new_assignment(self):
    self.driver.implicitly_wait(2)
    self.driver.find_element(*AssignmentPageLocator.ASSIGNMENT_OPTION).click()
    
    WebDriverWait(self.driver, 2).until(
      lambda driver: driver.find_element(*AssignmentPageLocator.ASSIGNMENT_LIST).is_displayed()
    )
    
    assignment_list = self.driver.find_element(*AssignmentPageLocator.ASSIGNMENT_LIST)
    assignment_list.find_element(*AssignmentPageLocator.CREATE_ASSIGNMENT_BUTTON).click()
    
    time.sleep(2)
    
  def assignment_form_is_shown(self):
    return "New Assignment" in self.driver.page_source
  
class CreateAssignmentPage(BasePage):
  title_field = Assignmemt_Title()
  point_field = Assignmemt_Point()
  default_point = Assignmemt_Default_Point()
  
  def __init__(self, driver) -> None:
    super().__init__(driver)
  
  def input_create_form(self, assigned_date, due_date):
    self.title_field = "Blackbox-testing"
    self.point_field = "500"
    self.default_point = "0"
    
    """ Fill assigned date section """
    assigned_date_month_selector = self.driver.find_element(*CreateAssignmentPageLocator.ASSIGNED_DATE_MONTH_LIST)
    assigned_month_list = Select(assigned_date_month_selector)
    assigned_month_list.select_by_value(assigned_date.month)
    
    assigned_date_day_selector = self.driver.find_element(*CreateAssignmentPageLocator.ASSIGNED_DATE_DAY_LIST)
    assignned_day_list = Select(assigned_date_day_selector)
    assignned_day_list.select_by_value(assigned_date.day)
    
    assigned_date_year_selector = self.driver.find_element(*CreateAssignmentPageLocator.ASSIGNED_DATE_YEAR_LIST)
    assignned_year_list = Select(assigned_date_year_selector)
    assignned_year_list.select_by_value(assigned_date.year)
    
    """ Fill due date section """
    due_date_month_selector = self.driver.find_element(*CreateAssignmentPageLocator.DUE_DATE_MONTH_LIST)
    due_month_list = Select(due_date_month_selector)
    due_month_list.select_by_value(due_date.month)

    due_date_day_selector = self.driver.find_element(*CreateAssignmentPageLocator.DUE_DATE_DAY_LIST)
    due_day_list = Select(due_date_day_selector)
    due_day_list.select_by_value(due_date.day)

    due_date_year_selector = self.driver.find_element(*CreateAssignmentPageLocator.DUE_DATE_YEAR_LIST)
    due_year_list = Select(due_date_year_selector)
    due_year_list.select_by_value(due_date.year)
    
    time.sleep(2)
  
  def click_save_button(self):
    self.driver.execute_script("window.scrollTo({ top: 0, behavior: 'smooth' });")
    time.sleep(2)
    submit_button = WebDriverWait(self.driver, 10).until(
      EC.element_to_be_clickable(CreateAssignmentPageLocator.SAVE_BUTTON)
    )
    submit_button.click()
  
  def scroll_to_the_end(self, element):
    self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});", element)
    time.sleep(3)
  
  def is_match_expected_result(self, expected_result):
    if(expected_result != ""):
      result_array = expected_result.split(';')
      error_section = self.driver.find_element(*CreateAssignmentPageLocator.ERROR_SECTION)
      wait = WebDriverWait(self.driver, 10)
      wait.until(lambda d: error_section.is_displayed())
      self.scroll_to_the_end(error_section)
      bool_array = [item in self.driver.page_source for item in result_array]
      return all(bool_array)
    else:
      delete_button = self.driver.find_element(*CreateAssignmentPageLocator.DELETE_BUTTON)
      wait = WebDriverWait(self.driver, 10)
      wait.until(lambda d: delete_button.is_displayed())
      return "Error" not in self.driver.page_source
  