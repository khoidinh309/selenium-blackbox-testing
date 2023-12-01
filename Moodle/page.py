from selenium.webdriver.support.ui import WebDriverWait
from element import *
from locator import *
import time

class BasePage(object):
  def __init__(self, driver) -> None:
    self.driver = driver
    self.wait = WebDriverWait(self.driver, 5)
    
  def find_element(self, parent_element, locator):
    return parent_element.find_element(*locator)
  
  def go_to_the_element(self, element):
    self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});", element)
  
  def click_button(self, locator):
    button = self.driver.find_element(*locator)
    self.wait.until(lambda _: button.is_displayed())
    self.go_to_the_element(button)
    time.sleep(2)
    button.click()
     
class WelComePage(BasePage):
  def click_teacher_option(self):
    self.click_button(WelcomePageLocator.TEACHER_OPTION)
    
class TeacherPage(BasePage):
  def click_set_up_assignment_time_option(self):
    self.click_button(TeacherPageLocator.SET_UP_ASSIGNMENT_TIME_OPTION)
    
class EnrollmentPage(BasePage):
  def click_continue_button(self):
    self.click_button(EnrollmentPageLocator.CONTINUE_BUTTON)
    
    