from selenium import webdriver
import time
class PopBot:

	def __init__(self):
		self.driver = webdriver.Firefox()
		self.driver.get("https://www.popcat.click/")
		time.sleep(3)
	def click(self):
		for i in range(0,2000):
	
			self.driver.find_element_by_xpath("/html/body/div[1]/div").click()
			time.sleep(0.01)
bot = PopBot()
bot.click()
time.sleep(1)
bot.driver.quit()
