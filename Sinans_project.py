from datetime import date
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
PATH = "C:\SeleniumChromeDriver\chromedriver.exe"
today = date.today()
d1 = today.strftime("%Y/%m/%d")
driver = webdriver.Chrome(PATH)


def daily_expess():
    driver.get("https://www.express.co.uk")
    driver.maximize_window()
    driver.find_element(By.XPATH, '//button[text()="I accept"]').click()
    heading1 = driver.find_element_by_tag_name("h2")
    with open("DailyExpress.txt", "w") as file:
        file.write(d1)
        file.write("\n\n")
        file.write("https://www.express.co.uk")
        file.write("\n\n")
        file.write(heading1.text)
        file.write("\n\n\n")

    heading_click = driver.find_element_by_tag_name("h2").click()
    time.sleep(5)
    article = driver.find_elements_by_class_name("text-description")
    for ch in article:
        with open("DailyExpress.txt", "a", encoding="utf-8") as file:
            file.write(ch.text)


def daily_mail():
    driver.get("https://www.dailymail.co.uk")
    driver.maximize_window()
    time.sleep(5)
    driver.find_element(By.XPATH, '//button[text()="Got it"]').click()
    heading2 = driver.find_element_by_tag_name("h2")

    with open("DailyMail.txt", "w") as file:
        file.write(d1)
        file.write("\n\n")
        file.write("https://www.dailymail.co.uk")
        file.write("\n\n")
        file.write(heading2.text)
        file.write("\n\n\n")

    heading_click1 = driver.find_element_by_tag_name("h2").click()
    time.sleep(5)
    bullets = driver.find_element_by_class_name("mol-bullets-with-font")
    article1 = driver.find_elements_by_class_name("mol-para-with-font")
    for ch in article1:
        with open("DailyMail.txt", "a", encoding="utf-8") as file:
            file.write(ch.text + "\n")

def the_independent():
    driver.get("https://www.independent.co.uk")
    driver.maximize_window()
    driver.find_element(By.XPATH, '//button[text()="AGREE"]').click()
    content_title = driver.find_element_by_class_name("content").find_element_by_css_selector('a.title')
    with open("TheIndependent.txt", "w") as file:
        file.write(d1)
        file.write("\n\n")
        file.write("https://www.independent.co.uk")
        file.write("\n\n")
        file.write(content_title.text)
        file.write("\n\n\n")

    driver.execute_script("arguments[0].click();", content_title)
    time.sleep(5)
    main_content = driver.find_element_by_id("main").find_elements_by_tag_name("p")
    for ch in main_content:
        with open("TheIndependent.txt", "a", encoding="utf-8") as file:
            file.write(ch.text + "\n")
    driver.close()

daily_expess()
daily_mail()
the_independent()