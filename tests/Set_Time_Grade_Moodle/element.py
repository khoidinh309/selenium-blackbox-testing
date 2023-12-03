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
  
class UserNameElement(BaseElement):
  locator = LogInPageLocator.USER_NAME_FIELD
  
class PasswordElement(BaseElement):
  locator = LogInPageLocator.PASSWORD_FIELD
  
class MaximumGradeElement(BaseElement):
  locator = SettingAssignmentPageLocator.MAXIMUM_GRADE_FIELD
  
class GradePassElement(BaseElement):
  locator = SettingAssignmentPageLocator.GRADE_PASS_FIELD