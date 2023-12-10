import unittest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from services import TestService as TService
from page import *

""" Moodle testing setion """
class MoodleTest(unittest.TestCase):
  def setUp(self):
    print("\n\n----------Start set grade and set time assignment tests------------\n\n")
    self.driver = webdriver.Chrome()
    self.driver.get('https://school.moodledemo.net/')
    self.set_time_test_case_file_path = os.path.abspath('./tests/Set_Time_Grade_Moodle/set_time_test_case.csv')
    self.set_time_result_file_path = os.path.abspath('./tests/Set_Time_Grade_Moodle/set_time_test_result.csv')
    self.set_grade_test_case_file_path = os.path.abspath('./tests/Set_Time_Grade_Moodle/set_grade_test_case.csv')
    self.set_grade_result_file_path = os.path.abspath('./tests/Set_Time_Grade_Moodle/set_grade_test_result.csv')
    self.set_time_column_list = ['Id', 'allow_submission_date', 'due_date', 'cutoff_date', 'remind_me_date', 'expected_result']
    self.set_grade_column_list = ['Id', 'maximum_grade', 'grade_pass', 'expected_result', 'max_response_time']
    self.MAXIMUM_GRADE_COLUMN = 'maximum_grade'
    self.GRADE_PASS_COLUMN = 'grade_pass'
    self.set_time_date_column = ['allow_submission_date', 'due_date', 'cutoff_date', 'remind_me_date']   
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
    
    for key in self.set_time_date_column:
      date_object = TService.create_date_object(raw_data[key])
      date_object_array.append(date_object)
      
    return date_object_array  
  
  
  def test_set_assignment_time(self):
    print("\n\n-------------Start set time tests-----------------\n\n")
    self.go_to_assignment_page()  
    
    test_cases = TService.read_csv_data(self.set_time_test_case_file_path, self.set_time_column_list)
    test_results = []
    setting_assignment_page = SettingAssignmentPage(self.driver)
    
    for data in test_cases:
      with self.subTest(data=data):
        date_object_array = self.prepare_date_object(data)
        setting_assignment_page.input_date_to_form(*date_object_array)
        setting_assignment_page.click_save_and_display_button()
        test_result = setting_assignment_page.is_match_expected_result(data['expected_result'], SetType.SET_TIME)
        assert test_result
        
        if data['expected_result'] == '':
          AssignmentPage(self.driver).click_setting_button()
        
        test_results.append({"Id": data['Id'], 'Passed': ('Passed' if test_result == True else 'Failed')})
        print("Test " + data["Id"] + " " + ('Passed' if test_result == True else 'Failed'))
        time.sleep(2)
    
    TService.write_test_results(self.set_time_result_file_path, test_results, ['Id', 'Passed'])
    print("\n\n-------------End set time tests-----------------\n\n")

    
  def test_set_assignment_grade(self):
    print("\n\n-------------Start set grade tests-----------------\n\n")
    self.go_to_assignment_page()
    setting_assignment_page = SettingAssignmentPage(self.driver)
    test_cases = TService.read_csv_data(self.set_grade_test_case_file_path, self.set_grade_column_list)
    setting_assignment_page.click_expand_grade_section_button()
    test_results = []
    
    for data in test_cases:
      with self.subTest(data=data):
        setting_assignment_page.maxmium_grade_field = data[self.MAXIMUM_GRADE_COLUMN]
        setting_assignment_page.grade_pass_field = data[self.GRADE_PASS_COLUMN]
        total_reponse_time = setting_assignment_page.click_save_and_display_button()
        test_result = setting_assignment_page.is_match_expected_result(data['expected_result'], SetType.SET_GRADE)
        assert test_result
          
        if data['expected_result'] == '' or "Recalculating grades" in self.driver.page_source:
          AssignmentPage(self.driver).click_setting_button()
          setting_assignment_page.click_expand_grade_section_button()
          
        response_time_test = total_reponse_time < float(data['max_response_time'])*1000
        test_results.append({"Id": data['Id'], 'UI_Passed': ('Passed' if test_result == True else 'Failed'), "RT_Passed": ('Passed' if response_time_test else 'Failed')})
        print("Test " + data["Id"] + " " + ('Passed' if test_result == True else 'Failed'))
        time.sleep(3)
        
    TService.write_test_results(self.set_grade_result_file_path, test_results, ['Id', 'UI_Passed', 'RT_Passed'])
    print("\n\n-------------End set grade tests-----------------\n\n")
  
  def tearDown(self) -> None:
    print("\n----------End tests------------\n")
    return self.driver.close()
   
if __name__ == "__main__":
  unittest.main()
    