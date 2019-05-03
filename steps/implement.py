import time

@given(u'que estou na tela principal do Carrefour')
def step_impl(context):
    context.driver.get('https://www.carrefour.com.br')


@when(u'pesquiso moto x4')
def step_impl(context):
    element=context.driver.find_element_by_xpath('//*[@id="js-site-search-input"]')
    element.send_keys('moto x4')
    element.submit()
    time.sleep(5)

@then(u'o resultado moto x4 ira aparecer')
def step_impl(context):
    element2=context.driver.find_element_by_xpath('/html/body/main/div/div[6]/div[4]/div[1]/ul/li[1]/div/form/div[2]/a/div[1]/div/div/div/img')
    element2.click()
    

'''@then(u'clica em comprar')
def step_impl(context):
    element3=context.driver.find_element_by_xpath('//*[@id="buyProductButtonBottom"]')
    element3.click()
    time.sleep(10)'''


@then(u'finaliza a Pesquisa')
def step_impl(context):
   pass
