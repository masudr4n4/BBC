import allure
import pytest
import random
from src.pages.HomePage import HomePage
from time import sleep


def test_home_page(driver):
    page = HomePage(driver)
    page.go_to_bbc()
    links = page.get_all_links()
    page.get_topics_title_and_desc(links)
