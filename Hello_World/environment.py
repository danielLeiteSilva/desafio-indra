from selenium import webdriver
from Pyautomators.contrib.scenario_autoretry import scenario_retry
from pages.pages.passagem import passagem

from selenium import webdriver

def before_all(context):
	context.driver=webdriver.Chrome('driver/chromedriver.exe')
	context.passagem_page=passagem(context.driver)
	
def after_all(context):
	context.driver.quit()

