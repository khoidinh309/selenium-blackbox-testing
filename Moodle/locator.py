from selenium.webdriver.common.by import By

class WelcomePageLocator:
  REMOVE_PRIVACY_BUTTON = (By.LINK_TEXT, 'x')
  TEACHER_OPTION = (By.LINK_TEXT, 'teacher')
  
class TeacherPageLocator:
  SET_UP_ASSIGNMENT_TIME_OPTION = (By.LINK_TEXT, 'Set up a timed assignment')

class EnrollmentPageLocator:
  CONTINUE_BUTTON_CONTAINER = (By.CLASS_NAME, "continuebutton")
  CONTINUE_BUTTON = (By.CSS_SELECTOR, 'button')
  
class LogInPageLocator:
  USER_NAME_FIELD = "username"
  PASSWORD_FIELD = "password"
  LOG_IN_BUTTON = (By.ID, 'loginbtn')
  
class AssignmentPageLocator:
  SETTINGS_BUTTON = (By.PARTIAL_LINK_TEXT, "Settings")
  
class SettingAssignmentPageLocator:
  ENABLE_ALSUB_CHECKBOX = (By.NAME, 'allowsubmissionsfromdate[enabled]')
  ALLOW_SUBMISSION_DAY_FIELD = (By.NAME,'allowsubmissionsfromdate[day]')
  ALLOW_SUBMISSION_MONTH_FIELD = (By.NAME,'allowsubmissionsfromdate[month]')
  ALLOW_SUBMISSION_YEAR_FIELD = (By.NAME,'allowsubmissionsfromdate[year]')
  
  ENABLE_DUE_CHECKBOX = (By.NAME, 'duedate[enabled]')
  DUE_DAY_FIELD = (By.NAME,'duedate[day]')
  DUE_MONTH_FIELD = (By.NAME,'duedate[month]')
  DUE_YEAR_FIELD = (By.NAME,'duedate[year]')
  
  ENABLE_CUTOFF_CHECKBOX = (By.NAME,'cutoffdate[enabled]')
  CUTOFF_DAY_FIELD = (By.NAME,'cutoffdate[day]')
  CUTOFF_MONTH_FIELD = (By.NAME,'cutoffdate[month]')
  CUTOFF_YEAR_FIELD = (By.NAME,'cutoffdate[year]')
  
  ENABLE_REMIND_ME_CHECKBOX = (By.NAME,'gradingduedate[enabled]')
  REMIND_ME_DAY_FIELD = (By.NAME,'gradingduedate[day]')
  REMIND_ME_MONTH_FIELD = (By.NAME,'gradingduedate[month]')
  REMIND_ME_YEAR_FIELD = (By.NAME,'gradingduedate[year]')
  
  SAVE_AND_DISPLAY_BUTTON = (By.ID, 'id_submitbutton')
  INVALID_FEEDBACK_MESSAGE = (By.ID, 'id_error_duedate')
  GRADE_SUMMARY_SECTION = (By.CLASS_NAME, 'gradingsummarytable')
  
class DateTypeConst:
  Allow_Submission = "ALLOW_SUBMISSION"
  Due = 'DUE'
  Cutoff = 'CUTOFF'
  Remind_Me = 'REMIND_ME'
  
  