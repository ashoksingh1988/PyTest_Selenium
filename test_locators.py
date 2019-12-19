import selenium.webdriver.common.by

# for maintainability we can seperate web objects by page name


class MainPageLocatars(object):
    SEARCH = (selenium.webdriver.common.by.By.CLASS_NAME, 'search-toggle')
    SEARCHLIST = (selenium.webdriver.common.by.By.CSS_SELECTOR, '#search')
    HealthIT = (selenium.webdriver.common.by.By.XPATH,"//*[@class='topics menu-bar js-menu-bar-transition']//a[contains(text(),'Health IT')]")
    Finance = (selenium.webdriver.common.by.By.XPATH,"//*[@class='topics menu-bar js-menu-bar-transition']//a[contains(text(),'Finance')]")
    Menu = (selenium.webdriver.common.by.By.XPATH,"//button[contains(text(),'Menu')]")
    ListMenu = (selenium.webdriver.common.by.By.CLASS_NAME, 'mm-list list-no-bullets')
    EmailInput= (selenium.webdriver.common.by.By.NAME, 'email')
    signup =  (selenium.webdriver.common.by.By.XPATH,"//*[@class='page-inner-wrapper']//button[1]")