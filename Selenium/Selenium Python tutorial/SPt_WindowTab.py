from selenium import webdriver

exec_path = r"C:\Users\USER\Documents\Selenium\chromedriver.exe"
URL = r"https://www.wikipedia.org/"
# English language URL: https://en.wikipedia.org/
# English language URL: https://tr.wikipedia.org/
# English language URL: hhttps://de.wikipedia.org/

languages = ["en", "tr", "de"]
driver = webdriver.Chrome(executable_path=exec_path)
driver.get(URL)
driver.maximize_window()
print("Window handle of the current window is:", driver.current_window_handle)

for i in range(len(languages)):
    driver.execute_script("window.open()")
    driver.switch_to.window(driver.window_handles[i+1])
    languages_URL = r"https://" + languages[i] + ".wikipedia.org/"
    driver.get(languages_URL)
    print(languages_URL, driver.window_handles[i+1], driver.title, driver.current_url)
