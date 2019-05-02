import time

@given(u'que estou no site do decolar.com')
def step_impl(context):
    context.driver.get('https://www.decolar.com/')


@when(u'pesquiso destino da viagem para Salvador')
def step_impl(context):
    element=context.driver.find_element_by_xpath('//*[@id="searchbox-sbox-box-packages"]/div/div/div[3]/div[2]/div[2]/div[2]/div/div/div/div/input')
    element.send_keys('Salvador, Bahia, Brasil')
    context.driver.implicitly_wait(5)
    context.driver.find_element_by_xpath("/html/body/div[13]/div/div[1]/ul/li[1]")
    element.click()
    element.send_keys("\t")
    element2=context.driver.find_element_by_xpath('//*[@id="searchbox-sbox-box-packages"]/div/div/div[3]/div[2]/span/label')
    element2.click()
    time.sleep(10)
    element3=context.driver.find_element_by_xpath('//*[@id="searchbox-sbox-box-packages"]/div/div/div[3]/div[2]/div[5]/div/a')
    element3.click()



@then(u'o resultado Salvador,Bahia,Brasil irá aparecer')
def step_impl(context):
    
     element.send_keys("\t")
     
     

@then(u'a opçao para nao escolher dia deve ser marcada')
def step_impl(context):
    element2=context.driver.find_element_by_xpath('//*[@id="searchbox-sbox-box-packages"]/div/div/div[3]/div[2]/span/label')
    element2.click()


@then(u'o navegador clica no pesquisar')
def step_impl(context):
    element2=context.driver.find_element_by_xpath('//*[@id="searchbox-sbox-box-packages"]/div/div/div[3]/div[2]/span/label')
    element2.click()

@then(u'o resultado de destino ira aparecer')
def step_impl(context):
    element3=context.driver.find_element_by_xpath('//*[@id="searchbox-sbox-box-packages"]/div/div/div[3]/div[2]/div[5]/div/a')
    element3.click()
