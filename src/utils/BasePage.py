import time

class BasePage:
    PAGE_LOAD_WAIT = 10
    SYNC_LOAD_TIME = 15

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(self.PAGE_LOAD_WAIT)
    #
    # def go_back(self):
    #     self.driver.back()
    #
    # def wait_sync(self):
    #     """
    #     Some actions require a brief period for items to appear in src across both api and mobile.
    #     """
    #     # TODO: replace with explicit wait
    #     time.sleep(self.SYNC_LOAD_TIME)
    #
    # def click_acc_id(self, id):
    #     """
    #     Use this function when only click on element with accessibility id
    #     :param id:
    #     :return:
    #     """
    #     self.driver.find_element(MobileBy.ACCESSIBILITY_ID, id).click()
