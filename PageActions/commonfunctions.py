from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class Automation_texting:


    def __init__(self):
        self.browser = webdriver.Chrome("/home/vinay/selenium/chromedriver")

    def open_url(self, url):
        """

        :param url:
        :return:
        """
        self.browser.get(url)

    def maximize(self):
        """

        :return:
        """
        self.browser.maximize_window()

    def getpage_title(self):
        """

        :return:
        """
        return self.browser.title

    def click_on_inputs_send_keys(self, x_path, value):
        """

        :param x_path:
        :param value:
        :return:
        """
        self.browser.find_element_by_xpath(x_path).send_keys(value)

    def click_on_elements(self, x_path):
        """

        :param x_path:
        :return:
        """
        time.sleep(2)
        self.browser.find_element(By.XPATH, x_path).click()

    def select_on_element(self, x_path):
        """

        :param x_path:
        :return:
        """
        self.browser.find_element(By.XPATH, x_path)

    def arlts(self):
        """

        :return:
        """
        self.browser.switch_to.alert.accept()

    def switch_to_frame(self, xpath):
        """
            This function will do -
                - switch the frame
        :return:
        """
        try:
            self.browser.switch_to.frame(self.browser.find_element_by_xpath(xpath))
        except NoSuchElementException:
            raise Exception("No element found")

    def double_click(self, xpath):
        """

        :param xpath:
        :return:
        """
        action_chains = ActionChains(self.browser)
        action_chains.double_click(xpath).perform()

    def drag_and_drop(self, source, target):
        """
        :param source:
        :param target:
        :return:
        """
        action_chains = ActionChains(self.browser)
        action_chains.drag_and_drop(source, target).perform()

    def click_hold_move(self, source, target):
        """
        :param target:
        :param source:
        :param
        :return:
        """

        action_chains = ActionChains(self.browser)
        action_chains.click_and_hold(source).move_to_element(target).release().perform()

    def slider_element(self, source, x_offset, y_offset):
        """

        :param source:
        :param x_offset:
        :param y_offset:
        :return:
        """
        acions_chains = ActionChains(self.browser)
        acions_chains.drag_and_drop_by_offset(source, x_offset, y_offset).perform()

    def scrollDown(self):
        """
        :return:
        """

        ActionChains(self.browser).send_keys(Keys.PAGE_DOWN).perform()

    def scrollUp(self):
        """
        :return:
        """
        ActionChains(self.browser).send_keys(Keys.PAGE_UP).perform()

    def close(self):
        """

        :return:
        """
        self.browser.close()

    def move_element(self, xpath, x_offset, y_offset):
        """

        :param xpath:
        :param x_offset:
        :param y_offset:
        :return:
        """
        time.sleep(2)
        move_action = ActionChains(self.browser)
        move_action.click_and_hold(xpath).move_by_offset(x_offset, y_offset).release().perform()


