from selenium import webdriver
from Pyautomators.contrib.scenario_autoretry import scenario_retry

def before_all(context):
	context.driver=webdriver.Chrome('driver/Chromedriver.exe')

def after_all(context):
	context.driver.quit()

