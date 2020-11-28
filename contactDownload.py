from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
import sys 

n = len(sys.argv)
if n < 3:
	print("less number of arguments, expected 2 arguments") 
else:
	gmailId, passWord = sys.argv[1],sys.argv[2]
	try: 
		driver = webdriver.Chrome(ChromeDriverManager().install()) 
		driver.get(r'https://accounts.google.com/signin/v2/identifier?passive=1209600&continue=https%3A%2F%2Fcontacts.google.com%2F&followup=https%3A%2F%2Fcontacts.google.com%2F&flowName=GlifWebSignIn&flowEntry=ServiceLoginpa') 
		driver.implicitly_wait(15) 

		loginBox = driver.find_element_by_xpath('//*[@id ="identifierId"]') 
		loginBox.send_keys(gmailId) 

		nextButton = driver.find_elements_by_xpath('//*[@id ="identifierNext"]') 
		nextButton[0].click() 

		passWordBox = driver.find_element_by_xpath( 
			'//*[@id ="password"]/div[1]/div / div[1]/input') 
		passWordBox.send_keys(passWord) 

		nextButton = driver.find_elements_by_xpath('//*[@id ="passwordNext"]') 
		nextButton[0].click() 

		exportButton = driver.find_elements_by_xpath('//*[text()="Export"]')
		exportButton[0].click()
	
		exportButton2 = driver.find_elements_by_xpath('//span[text()="Export"]')
		exportButton2[0].click()  
	
		print('Login Successful...!!') 
	except: 
		print('Login Failed') 
