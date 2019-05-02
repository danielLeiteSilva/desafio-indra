class passagem:

    def __init__(self,driver):

        self.SEARCH='Salvador, Bahia, Brasil'
        self.URL='https://www.decolar.com/'
        self.driver=driver

    def go_passagem(self):
        self.driver.get(self.URL)

    def search_passagem(self, value):
        element = self.driver.find_element_by_name(self.SEARCH)
        element.send_keys(value)
        element.submit()