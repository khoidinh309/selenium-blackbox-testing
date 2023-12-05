from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from xpaths import *

class ChangProfile:
    def __init__(self, driver : webdriver):
            self.driver = driver

    def refresh(self):
        self.driver.refresh()
        
    def login(self, usr, pw):
        print("[+] Login")
        username = self.driver.find_element(By.XPATH, txt_usr())
        password = self.driver.find_element(By.XPATH, txt_pass())
        username.clear()
        password.clear()
        username.send_keys(usr)
        password.send_keys(pw)
        self.driver.find_element(By.XPATH, txt_login()).click()
        
    def test_change_profile(self, fname, lname, email):
        print("[Step] Change Profile")
        wait = WebDriverWait(self.driver, 5)
        account = ["student", "moodle"]
        
        self.driver.find_element(By.XPATH, txt_continue_profile()).click()
        
        self.login(account[0], account[1])
        try:
            wait.until(EC.presence_of_element_located((By.XPATH, txt_edit_profile_btn())))
        except TimeoutException:
            print("[-] Load Page Fail")
            
        self.driver.find_element(By.XPATH, txt_edit_profile_btn()).click()
        self.change_profile(fname, lname, email) 
        result_fname = self.check_fname(fname) 
        result_lname = self.check_lname(lname)
        result_email = self.check_email(email)
        result = result_fname and result_lname and result_email
        if fname == "" or lname == "" or ((email.find("@")==-1 and email.find(".com")==-1) and email!="unchanged") or email == "":        
            return result
        else:
            self.driver.find_element(By.XPATH, txt_update()).click()
            if email != "" and email != "unchanged":
                self.driver.find_element(By.XPATH, txt_continue_email()).click()
            try:
                self.driver.find_element(By.XPATH, txt_profile())
                return True
            except:
                return False
            
    def change_profile(self, fname, lname, email):
        if email != "unchanged":
            try:
                self.driver.find_element(By.LINK_TEXT, "Cancel email change").click()
            except NoSuchElementException:
                pass
            email_field = self.driver.find_element(By.XPATH, txt_email())          
            print("[+] Input email")
            email_field.clear()
            email_field.send_keys(email)
        if fname != "unchanged":
            first_name = self.driver.find_element(By.XPATH, txt_fname())
            print("[+] Input First name")
            first_name.clear()
            first_name.send_keys(fname)
        if lname != "unchanged":
            last_name = self.driver.find_element(By.XPATH, txt_lname())
            print("[+] Input Last name")
            last_name.clear()
            last_name.send_keys(lname)   
        self.driver.find_element(By.XPATH, txt_city()).click() 
        
    def check_fname(self, fname):
        if fname == "unchanged":
            return True
        elif fname == "":
            try:
                self.driver.find_elements(By.XPATH, txt_error_fname())
                print("[-] Change first name fail")
                return True
            except:
                print("[+] Change first name success")
                return False
        else:
            return True
        
    def check_lname(self, lname):
        if lname == "unchanged":
            return True
        elif lname == "":
            try:
                self.driver.find_elements(By.XPATH, txt_error_lname())
                print("[-] Change last name fail")
                return True
            except:
                print("[+] Change last name success")
                return False
        else:
            return True
        
    def check_email(self, email):
        if email == "unchanged":
            return True
        elif email == "" or (email.find("@")==-1 and email.find(".com")==-1):
            try :
                self.driver.find_elements(By.XPATH, txt_error_email())
                print("[-] Change email fail")
                return True
            except:
                print("[+] Change email success")
                return False
        else:
            return True
 
class CreateEvent:
    def __init__(self, driver : webdriver):
            self.driver = driver

    def refresh(self):
        self.driver.refresh()    
        
    def test_create_event(self, title, start_date, start_month, duration_date, duration_month, duration_min):
        print("[Step] Create Event")
        self.driver.get("https://sandbox.moodledemo.net/login/index.php")

        self.driver.implicitly_wait(5)
        
        self.driver.find_element(By.ID, "username").send_keys("admin")
        self.driver.find_element(By.ID, "password").send_keys("sandbox")
        self.driver.find_element(By.ID, "loginbtn").click()
            
        dashboard_link = self.driver.find_element(By.CSS_SELECTOR, 'a[href="https://sandbox.moodledemo.net/my/"]')
        dashboard_link.click()

        self.driver.find_element(By.CSS_SELECTOR, 'button[data-action="new-event-button"]').click()
        self.create_event(title, start_date, start_month, duration_date, duration_month, duration_min) 
        
        result_title = self.check_title(title) 
        result = result_title
        self.driver.find_element(By.XPATH,"//button[@data-action='save']").click()
        
        if duration_date != "":
            result_starttime = self.check_starttime(start_date, start_month, duration_date, duration_month)
            result = result_title and result_starttime
        if duration_min != "":
            result_durationmin = self.check_durationmin(duration_min)
            result = result_title and result_durationmin
        return result
            
    def create_event(self, title, start_date, start_month, duration_date, duration_month, duration_min):
        event_title = self.driver.find_element(By.ID, "id_name")
        if title != "":
            print("[+] Input Event Title")
            event_title.clear()
            event_title.send_keys(title)
        if start_date != "":
            print("[+] Choose Start date for event")
            self.driver.find_element(By.XPATH,"//select[@id='id_timestart_day']/option[@value='%s']" %start_date).click()
        if start_month != "":
            print("[+] Choose Start month for event")
            self.driver.find_element(By.XPATH,"//select[@id='id_timestart_day']/option[@value='%s']" %start_month).click()
        if duration_date != "":
            print("[+] Set duration for event")
            self.driver.find_element(By.CLASS_NAME,"moreless-toggler").click()
            self.driver.find_element(By.XPATH,"//label//input[@id='id_duration_1']").click()
            self.driver.find_element(By.XPATH,"//select[@id='id_timedurationuntil_day']/option[@value='%s']" %duration_date).click()
            if duration_month != "":
                self.driver.find_element(By.XPATH,"//select[@id='id_timedurationuntil_month']/option[@value='%s']" %duration_month).click()
        if duration_min != "":
            print("[+] Set duration for event")
            self.driver.find_element(By.CLASS_NAME,"moreless-toggler").click()
            self.driver.find_element(By.XPATH,"//label//input[@id='id_duration_2']").click()
            self.driver.find_element(By.XPATH,"//input[@id='id_timedurationminutes']").send_keys(duration_min)
    
    def check_title(self, title):
        if title != "":
            return True
        elif title == "":
            if self.driver.find_elements(By.ID, "id_error_name"): 
                print("[-] Named event title failed")
                return True
            print("[+] Named event title success")
            return False
        
    def check_starttime(self, start_date, start_month, duration_date, duration_month):
        if int(start_month) < int(duration_month):
            return True
        elif int(start_month) > int(duration_month):
            if self.driver.find_elements(By.ID, "fgroup_id_error_durationgroup"): 
                print("[-] Choose event date failed")
                return True
            print("[+] Choose event date success")
            return False
        else:
            if int(start_date) < int(duration_date):
                return True
            elif int(start_date) > int(duration_date):
                if self.driver.find_elements(By.ID, "fgroup_id_error_durationgroup"): 
                    print("[-] Choose event date failed")
                    return True
                print("[+] Choose event date success")
                return False
            else:
                return True

    def check_durationmin(self, duration_min):
        if int(duration_min) > 0:
            return True
        else:
            if self.driver.find_elements(By.ID, "fgroup_id_error_durationgroup"): 
                print("[-] Choose duration time failed")
                return True
            print("[+] Choose duration time success")
            return False