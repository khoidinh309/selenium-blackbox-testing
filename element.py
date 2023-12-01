from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from locator import  *

class BaseElement(object):
  
  def __set__(self, obj, value):
    driver = obj.driver
    WebDriverWait(driver, 100).until(
      lambda driver: driver.find_element(By.NAME, self.locator)
    )
    driver.find_element(By.NAME, self.locator).clear()
    driver.find_element(By.NAME, self.locator).send_keys(value)
    
  def __get__(self, obj, owner):
    driver = obj.driver
    WebDriverWait(driver, 100).until(
      lambda driver: driver.find_element(By.NAME, self.locator)
    )
    element = driver.find_element(By.NAME, self.locator).clear()
    return element.get_attribute("value")

""" Login page elements"""
class UserNameElement(BaseElement):
  locator = LoginPageLocator.USER_NAME_FIELD
  
class PasswordElement(BaseElement):
  locator = LoginPageLocator.PASSWORD_FIELD


""" Create assignment page elements"""
class Assignmemt_Title(BaseElement):
  locator = CreateAssignmentPageLocator.TITLE_FIELD
  
class Assignmemt_Point(BaseElement):
  locator = CreateAssignmentPageLocator.POINT_FIELD
  
class Assignmemt_Default_Point(BaseElement):
  locator = CreateAssignmentPageLocator.DEFAULT_POINT_FIELD
