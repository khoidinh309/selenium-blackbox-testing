from selenium.webdriver.common.by import By

class LoginPageLocator:
  LOGIN_BUTTON = (By.CLASS_NAME, "button-primary")
  USER_NAME_FIELD = "USERNAME"
  PASSWORD_FIELD = "PASSWORD"

class MainPageLocator:
  GRADE_MENU = (By.CLASS_NAME, "grades")
  GRADE_MENU_ANCHOR = (By.ID, "selectedModuleLink")
  GRADE_MENU_UL = (By.ID, "menu_Grades")
  ASSIGNMENT_ITEM_IN_MENU = (By.LINK_TEXT, "Assignments")

class AssignmentPageLocator:
  ASSIGNMENT_OPTION = (By.LINK_TEXT, "Homework")
  ASSIGNMENT_LIST = (By.XPATH, "//div[@class='list-outer assignments']")
  CREATE_ASSIGNMENT_BUTTON = (By.CSS_SELECTOR, 'img')
  
class CreateAssignmentPageLocator:
  TITLE_FIELD = "tables[new][TITLE]"
  POINT_FIELD = "tables[new][POINTS]"
  DEFAULT_POINT_FIELD = "tables[new][DEFAULT_POINTS]"
  ASSIGNED_DATE_MONTH_LIST = (By.NAME, "month_tables[new][ASSIGNED_DATE]")
  ASSIGNED_DATE_DAY_LIST = (By.NAME, "day_tables[new][ASSIGNED_DATE]")
  ASSIGNED_DATE_YEAR_LIST = (By.NAME, "year_tables[new][ASSIGNED_DATE]")
  DUE_DATE_MONTH_LIST = (By.NAME, "month_tables[new][DUE_DATE]")
  DUE_DATE_DAY_LIST = (By.NAME, "day_tables[new][DUE_DATE]")
  DUE_DATE_YEAR_LIST = (By.NAME, "year_tables[new][DUE_DATE]")
  SAVE_BUTTON = (By.XPATH, '//input[@type="submit" and @value="Save" and @class="button-primary"]')
  DELETE_BUTTON = (By.XPATH, '//input[@type="button" and @value = "Delete"]')
  ERROR_SECTION = (By.CLASS_NAME, "error")
  
  