from unittest import TestCase
from selenium import webdriver 
from selenium import WebGeckoDriver
from pages.pages.passagem import passagem

class TestPage(TestCase):

    def setUp(self):
        
        self.driver=WebChromeDriver.Chrome()
        self.page_home = passagem(self.driver)
        self.driver.get('https://www.decolar.com/')

    def test_search(self):
        self.page_home.search_passagem('Salvador, Bahia, Brasil')
        assert 'Salvador, Bahia, Brasil' in self.driver.title

    def tearDown(self):
        self.driver.close()
        
unittest.main()