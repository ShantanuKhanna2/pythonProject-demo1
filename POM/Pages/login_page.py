from Test import login_test

class Login_page():

    def __int__(self, driver):
        self.driver = driver

        self.username_textname_id = "txtUsername"
        self.password_textname_id = "txtPassword"
        self.loginbutton_id       = "btnLogin"

    def username_textbox(self,username):
        self.driver.find_element(By.ID, self.username_textname_id).clear()
        self.driver.find_element(By.ID,self.username_textname_id).send_keys(username)

    def password_textbox(self,password):
        self.driver.find_element(By.ID, self.password_textname_id).clear()
        self.driver.find_element(By.ID, self.password_textname_id).send_keys(password)

    def password_textbox(self):
        self.driver.find_element(By.ID, self.password_textname_id).click()


