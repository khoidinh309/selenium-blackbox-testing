from selenium.webdriver.common.by import By

class FindCoursePageLocator:
    LOGIN_LINK = (By.LINK_TEXT, "Log in")
    USERNAME_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "loginbtn")
    GROUPING_DROPDOWN = (By.ID, "groupingdropdown")
    ALL_OPTION = (By.LINK_TEXT, "All")
    SORTING_DROPDOWN = (By.CSS_SELECTOR, "#sortingdropdown > span")
    SORT_BY_COURSE_NAME_OPTION = (By.LINK_TEXT, "Sort by course name")
    SEARCH_FIELD = (By.NAME, "search")
