#===========Login======================
def txt_usr():
    return "//input[@id='username']"
def txt_pass():
    return "//input[@id='password']"
def txt_login():
    return "//button[@id='loginbtn']"

#============Change Profile===============
def txt_continue_profile():
    return "/html[1]/body[1]/div[2]/div[3]/div[1]/div[2]/div[1]/section[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/form[1]/button[1]"
def txt_edit_profile_btn():
    return "//a[contains(text(),'Edit profile')]"
def txt_fname():
    return "//input[@id='id_firstname']"
def txt_lname():
    return "//input[@id='id_lastname']"
def txt_email():
    return "//input[@id='id_email']"
def txt_update():
    return "//input[@id='id_submitbutton']"
def txt_city():
    return "//input[@id='id_city']"
def txt_error_fname():
    return "//div[@id='id_error_firstname']"
def txt_error_lname():
    return "//div[@id='id_error_lastname']"
def txt_error_email():
    return "//div[@id='id_error_email']"
def txt_continue_email():
    return "/html[1]/body[1]/div[2]/div[3]/div[1]/div[2]/div[1]/section[1]/div[1]/div[2]/form[1]/button[1]"
def txt_profile():
    return "//h3[contains(text(),'User details')]"