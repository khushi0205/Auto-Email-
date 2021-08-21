from selenium import webdriver

usnm = "prank.trials123"
pwd = "Prank321"
email = "khushi.sali2002@gmail.com"
msg = "Hello Ma'am/Sir, \n Your Order has been confirmed. Thank you for your support. \n\n\n\nThanks and Regards,\nUrban Jungle"
driver = webdriver.Edge(r'C:\Users\khushi\OneDrive\Desktop\edgedriver_win64\msedgedriver.exe')
driver.get(
    "https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")

driver.find_element_by_name("identifier").send_keys(usnm)
driver.find_element_by_xpath("//*[@id=\"identifierNext\"]/div/button").click()

driver.implicitly_wait(15)
driver.find_element_by_name("password").send_keys(pwd)
driver.find_element_by_xpath("//*[@id=\"passwordNext\"]/div/button").click()

driver.implicitly_wait(25)
driver.find_element_by_xpath("//*[@id=\":36\"]/div/div").click()
driver.implicitly_wait(15)

driver.find_element_by_name("to").send_keys(email)
driver.find_element_by_class_name("aoT").send_keys("Order confirmation")
driver.find_element_by_xpath("//*[@id=\":9o\"]").send_keys(msg)
driver.find_element_by_id(":88").click()
