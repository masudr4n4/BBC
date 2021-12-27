from selenium.webdriver.common.by import By
from time import sleep
from src.utils.BasePage import BasePage
import allure
from datetime import datetime


class HomePage(BasePage):
    link_xpath = "//h3/a"
    topic_title = "//h3[@class='media__title']"


    @allure.step("Find all the links")
    def get_all_links(self):
        links = []
        elements = self.driver.find_elements(By.XPATH, self.link_xpath)
        for i in elements:
            link = i.get_attribute("href")
            links.append(link)
        return links

    @allure.step("clicking digit {1}")
    def click_digit(self, digit):
        self.driver.find_element("id", self.DIGIT_ID + str(digit)).click()

    @allure.step("Collecting all the topics title")
    def get_topics_title_and_desc(self, links):
        time = datetime.now()
        data = {}
        for url in links[:10]:
            self.driver.get(url)
            title = self.driver.title
            description = self.driver.find_element(By.XPATH, "//article").text
            data[title] = description
            print(title)
            print("\n")
            print(description)
            with open("reports.txt", 'a') as f:
                f.write(f"{title},{description},{str(time)}\n")

        sleep(5)

    def go_to_bbc(self):
        self.driver.get("https://bbc.com/")
