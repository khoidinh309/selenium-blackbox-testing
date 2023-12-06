from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locator import FindCoursePageLocator
from base import BasePage 


class FindCoursePage(BasePage):
    def click_login_link(self):
        self.click_element(FindCoursePageLocator.LOGIN_LINK)
        
    def login(self, username, password):
        self.click_element(FindCoursePageLocator.USERNAME_FIELD)
        self.input_text(FindCoursePageLocator.USERNAME_FIELD, username)
        self.click_element(FindCoursePageLocator.PASSWORD_FIELD)
        self.input_text(FindCoursePageLocator.PASSWORD_FIELD, password)
        self.click_element(FindCoursePageLocator.LOGIN_BUTTON)
        
    def select_all_grouping(self):
        self.click_element(FindCoursePageLocator.GROUPING_DROPDOWN)
        self.click_element(FindCoursePageLocator.ALL_OPTION)
        
    def sort_by_course_name(self):
        self.click_element(FindCoursePageLocator.SORTING_DROPDOWN)
        self.click_element(FindCoursePageLocator.SORT_BY_COURSE_NAME_OPTION)
        
    def search_course(self, course_name):
        self.click_element(FindCoursePageLocator.SEARCH_FIELD)
        self.input_text(FindCoursePageLocator.SEARCH_FIELD, course_name)
