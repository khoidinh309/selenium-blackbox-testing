import unittest
from selenium import webdriver
from services import TestService as TService
from page import *

""" Moodle testing setion """
class MoodleTest(unittest.TestCase):
  def setUp(self):
    self.driver = webdriver.Chrome()
    self.driver.get('https://school.moodledemo.net/')
    self.set_time_test_case_file_path = 'D:\\Workspace\\selenium\\soft-ware-testing-ass3\\Moodle\\set_time_test_case.csv'
    self.set_time_result_file_path = 'D:\\Workspace\\selenium\\soft-ware-testing-ass3\\Moodle\\set_time_test_result.csv'
    self.column_list = ['Id', 'allow_submission_date', 'due_date', 'cutoff_date', 'remind_me_date', 'expected_result']
    self.date_column = ['allow_submission_date', 'due_date', 'cutoff_date', 'remind_me_date']   
    self.wait = WebDriverWait(self.driver, 100)
    
  def go_to_assignment_page(self):
    welcome_page = WelComePage(self.driver)
    welcome_page.click_teacher_option()
    
    teacher_page = TeacherPage(self.driver)
    teacher_page.click_set_up_assignment_time_option()
    
    enrollment_page = EnrollmentPage(self.driver)
    enrollment_page.click_continue_button()
    
    login_page = LoginPage(self.driver)
    login_page.user_name = 'teacher'
    login_page.password = 'moodle'
    login_page.click_login_button()
    
    assignment_page = AssignmentPage(self.driver)
    assignment_page.click_setting_button()
    
  def prepare_date_object(self, raw_data):
    date_object_array = []
    
    for key in self.date_column:
      date_object = TService.create_date_object(raw_data[key])
      date_object_array.append(date_object)
      
    return date_object_array  
  
  
  def test_set_assignment_time(self):
    self.go_to_assignment_page()  
    
    test_cases = TService.read_csv_data(self.set_time_test_case_file_path, self.column_list)
    test_results = []
    setting_assignment_page = SettingAssignmentPage(self.driver)
    
    for data in test_cases:
      with self.subTest(data=data):
        date_object_array = self.prepare_date_object(data)
        setting_assignment_page.input_date_to_form(*date_object_array)
        
        setting_assignment_page.click_save_and_display_button()
        
        test_result = setting_assignment_page.is_match_expected_result(data['expected_result'])
        assert test_result
        
        if data['expected_result'] == '':
          AssignmentPage(self.driver).click_setting_button()
        
        test_results.append({"Id": data['Id'], 'Passed': ('Passed' if test_result == True else 'Failed')})
        time.sleep(2)
    
    TService.write_test_results(self.set_time_result_file_path, test_results)
    
  def tearDown(self) -> None:
    return self.driver.close()
   
if __name__ == "__main__":
  unittest.main()
    