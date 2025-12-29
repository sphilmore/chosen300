from selenium.webdriver.common.by import By

from pages.base_registration_form import BaseForm
from selenium.webdriver.support import expected_conditions as EC

class Donation(BaseForm):

    def __init__(self, driver):
        super().__init__(driver)

    def click_donation_page(self):
        self.wait().until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Clothing Donations']" ))
        ).click()

    def donation_form_fill(self, first= None, last=None, organization=None, email=None, phone=None):
        if first:
         self.driver.find_element(By.ID, "firstName").send_keys(first)
        if last:
         self.driver.find_element(By.ID, "lastName").send_keys(last)
        if organization:
         self.driver.find_element(By.ID, "org").send_keys(organization)
        if email:
         self.driver.find_element(By.ID, "email").send_keys(email)
        if phone:
         self.driver.find_element(By.ID, "phone").send_keys(phone)
    def donation_continue_button(self):
        self.wait().until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Continue']"))
        ).click()
    def click_donation_category(self):
        self.wait().until(
            EC.element_to_be_clickable((By.XPATH, "//label[.//text()[normalize-space()='Clothing']]//button[@role='checkbox']"))
        ).click()
    def enter_number_of_bags(self, text):
        self.wait().until(
            EC.presence_of_element_located((By.ID, "quantity"))
        ).send_keys(text)
    def click_donation_contintue(self):
        self.wait().until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Continue']"))

        ).click()
    def click_drop_off_site(self):
        self.wait().until(
            EC.element_to_be_clickable((By.ID, "dropoff-site"))
        ).click()
        self.wait().until(
            EC.element_to_be_clickable((By.XPATH, "//*[@role='option' and normalize-space()='West Philadelphia']"))
        ).click()
    def continue_to_submit(self):
        self.wait().until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Continue']"))
        ).click()
    def submit_donation_button(self):
        self.wait().until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Submit Donation']"))
        ).click()

