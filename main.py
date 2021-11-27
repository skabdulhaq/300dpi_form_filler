from selenium import webdriver
from selenium.webdriver.common import by


browser = webdriver.Edge("D:/development/msedgedriver.exe")

browser.get("https://docs.google.com/forms/d/e/1FAIpQLSf_KgrkmoondPW1bFBvugp_a-TcGgJFkNqg0KXpQfZXjMZRTQ/viewform")
email_ = "sk.abdulhaq2004@gmail.com"
name_ = "Shaik Abdul Haq"
number_ = 7416167631
reg = 125004384
sas_id = "125004384@sastra.ac.in"
describe = """This Form Is Filled By Python!!!
I like Developing, My  daily routine was used to be Eat, Code, Sleep, Repeat before November 23 Because CIA Schedule released. Since I was a child I used to be very passionate about learning new technology's. I am presently a intermediate python programmer Done projects using beautifulsoup, Selenium,  Leaning Flask, JavaScript and Flutter. If I get a chance to explore video editing I will definitely do it too. I am a fast learner I can  learn new technology quickly, so I am very much confident that I will adopt to your environment very quickly. So, please check projects on GitHub. Thankyou for reading in ADVANCE!!"""
# browser.quit()
projects = """300dpi form filler : https://github.com/skabdulhaq/Password_Manager
Password Manager: https://github.com/skabdulhaq/Password_Manager
KBC: https://github.com/skabdulhaq/KBC
Movie links scraper: https://github.com/skabdulhaq/Movie_links_scraper
"""
email = browser.find_element(by.By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div[1]/input')
email.send_keys(email_)
name = browser.find_element(by.By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
name.send_keys(name_)
number = browser.find_element(by.By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
number.send_keys(number_)
regnum = browser.find_element(by.By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
regnum.send_keys(reg)
first_year = browser.find_element(by.By.XPATH, '//*[@id="i21"]/div[3]/div')
first_year.click()
email_sastra = browser.find_element(by.By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input')
email_sastra.send_keys(sas_id)
id_ = 45
for _ in range(3):
    intrest = browser.find_element(by.By.XPATH, f'//*[@id="i{id_}"]/div[2]')
    intrest.click()
    id_ = id_ + 3
WHY_WE_HAVE_TO_SELECT = browser.find_element(by.By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div[2]/textarea')
WHY_WE_HAVE_TO_SELECT.send_keys(describe)

projects_ = browser.find_element(by.By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div[1]/div[2]/textarea')
projects_.send_keys(projects)
submit_button = browser.find_element(by.By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
submit_button.click()
