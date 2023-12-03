from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from element import *
from locator import *
import time

class BasePage(object):
  def __init__(self, driver) -> None:
    self.driver = driver
    self.wait = WebDriverWait(self.driver, 100)
    
  def find_element(self, parent_element, locator):
    return parent_element.find_element(*locator)
  
  def go_to_the_element(self, element):
    self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});", element)
    time.sleep(2)
    
  def go_to_the_end_of_page(self):
    self.driver.execute_script("window.scrollTo({ top: document.body.scrollHeight, behavior: 'smooth' });")   
  
  def click_button(self,container, locator):
    button = self.find_element(container, locator)
    self.wait.until(lambda _: button.is_displayed())
    self.go_to_the_element(button)
    button.click()
     
class WelComePage(BasePage):
  def click_teacher_option(self):
    self.click_button(self.driver, WelcomePageLocator.REMOVE_PRIVACY_BUTTON)
    self.click_button(self.driver, WelcomePageLocator.TEACHER_OPTION)
    
class TeacherPage(BasePage):
  def click_set_up_assignment_time_option(self):
    self.click_button(self.driver, TeacherPageLocator.SET_UP_ASSIGNMENT_TIME_OPTION)
    
class EnrollmentPage(BasePage):
  def click_continue_button(self):
    self.go_to_the_end_of_page()
    button_container = self.find_element(self.driver, EnrollmentPageLocator.CONTINUE_BUTTON_CONTAINER)
    self.click_button(button_container, EnrollmentPageLocator.CONTINUE_BUTTON)
class LoginPage(BasePage):
  user_name = UserNameElement()
  password = PasswordElement()
  
  def click_login_button(self):
    self.click_button(self.driver, LogInPageLocator.LOG_IN_BUTTON)
    
class AssignmentPage(BasePage):
  def click_setting_button(self):
    self.click_button(self.driver, AssignmentPageLocator.SETTINGS_BUTTON)
    
class SettingAssignmentPage(BasePage):
  maxmium_grade_field = MaximumGradeElement()
  grade_pass_field = GradePassElement()
  
  def activate_enable_checkbox(self, enable_locator):
    enable_checkbox = self.find_element(self.driver, enable_locator)
    self.wait.until(lambda _: enable_checkbox.is_displayed())
    if enable_checkbox.is_selected() is False:
      enable_checkbox.click()
  
  def handle_input_date(self, field_locator, value):
    drop_list = Select(self.find_element(self.driver, field_locator))
    drop_list.select_by_value(value)
    
  def handle_input_date_field(self, date_object, date_type):
    attribute_array = ['day', 'month', 'year']

    for attr in attribute_array:
      locator = f"{date_type}_{attr.upper()}_FIELD"
      self.handle_input_date(getattr(SettingAssignmentPageLocator, locator), getattr(date_object, attr))
     
  def input_date_to_form(self, as_date, due_date, cutoff_date, remind_me_date):
    self.activate_enable_checkbox(SettingAssignmentPageLocator.ENABLE_ALSUB_CHECKBOX)
    self.handle_input_date_field(as_date, DateTypeConst.Allow_Submission)
    
    self.activate_enable_checkbox(SettingAssignmentPageLocator.ENABLE_DUE_CHECKBOX)
    self.handle_input_date_field(due_date, DateTypeConst.Due)
    
    self.activate_enable_checkbox(SettingAssignmentPageLocator.ENABLE_CUTOFF_CHECKBOX)
    self.handle_input_date_field(cutoff_date, DateTypeConst.Cutoff)
    
    self.activate_enable_checkbox(SettingAssignmentPageLocator.ENABLE_REMIND_ME_CHECKBOX)
    self.handle_input_date_field(remind_me_date, DateTypeConst.Remind_Me)
    
    time.sleep(2)
    
  def click_save_and_display_button(self):
    self.click_button(self.driver, SettingAssignmentPageLocator.SAVE_AND_DISPLAY_BUTTON)
    
  def click_expand_grade_section_button(self):
    self.click_button(self.driver, SettingAssignmentPageLocator.EXPAND_GRADE_SECTION_BUTTON)
    
  def is_match_expected_result(self, expected_result, set_type):
    if expected_result != "":
      result_array = expected_result.split(';')
      error_section = self.find_element(self.driver, SettingAssignmentPageLocator.SET_TIME_SECTION if set_type == SetType.SET_TIME else SettingAssignmentPageLocator.SET_GRADE_SECTION)
      self.wait.until(lambda d: error_section.is_displayed())
      self.go_to_the_element(error_section)
      bool_array = [item in self.driver.page_source for item in result_array]
      return all(bool_array)
    else:
      grade_summary_page = self.find_element(self.driver, SettingAssignmentPageLocator.GRADE_SUMMARY_SECTION)
      self.wait.until(lambda d: grade_summary_page.is_displayed())
      return "Grading summary" in self.driver.page_source
    

    
    