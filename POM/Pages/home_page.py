class Home_page():

    def __int__(self, driver):
        self.driver = driver

        self.welcome_page_id = "welcome"
        self.logout_linktext = "Logout"

    def welcome_page(self):
        self.driver.find_element(By.ID, self.welcome_page_id).click()

    def logout_page(self):
        self.driver.find_element(By.ID, self.logout_linktext).click()

