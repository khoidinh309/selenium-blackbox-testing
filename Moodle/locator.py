from selenium.webdriver.common.by import By

class WelcomePageLocator:
  TEACHER_OPTION = (By.LINK_TEXT, 'teacher')
  
class TeacherPageLocator:
  SET_UP_ASSIGNMENT_TIME_OPTION = (By.LINK_TEXT, 'Set up a timed assignment')

class EnrollmentPageLocator:
  CONTINUE_BUTTON = (By.XPATH, '//button[@type="submit"]')