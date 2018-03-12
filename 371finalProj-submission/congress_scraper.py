import requests
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import urllib, http.client
import parser

class Bill:
	def __init__(self, name, description, status):
		self.name = name
		self. description = description
		self.status = status

def makeLispPhrase(billName, beenVotedOnHouse=False, beenVotedOnSenate=False, passedHouse=False, passedSenate=False, isSigned=False, isVetoed=False, hadOverturn=False, isOverturned=False):
	lispParse=[]
	lispParse.append("(isa "+billName+" Bill-Idea)")
	lispParse.append("(writtenSponsored "+billName+")")
	count=0
	if beenVotedOnHouse: 
		lispParse.append("(houseVoteResult "+ billName+ " "+str(passedHouse) + ")")
		count+=1
	if beenVotedOnSenate: 
		lispParse.append("(senateVoteResult "+billName+" "+str(passedSenate)+")")
		count+=1
	if isSigned:
		lispParse.append("(presidentSigned " +billName+")")
		count+=1
	if isVetoed:
		lispParse.append("(presidentVeto " +billName+")")
		count+=1
	if hadOverturn:
		lispParse.append("(vetoOverTurn "+billName+" "+ str(isOverturned)+")")
	# for item in lispParse:
	# 	print(item)
	# print("\n")
	lispParse.append('\n')
	lispParse = '\n'.join(lispParse)
	return lispParse

# def handleChambersSeparately(webel):
# 	if 'Passed House' in webel.find_element_by_xpath(".//span[@class='result-item result-tracker']/p[@class='hide_fromsighted']").text:
# 		if 'S' in item.find_element_by_xpath(".//span[@class='result-heading']/a").text:

def failedHouse(driver, urls, bills_counted):
	driver.get(urls['Failed House'])
	time.sleep(1)
	try:
		stupid_modal = driver.find_element_by_xpath("//div[@class='modal-dialog modal-lg']/div/div[@class='modal-header']/button").click()
		print('exited modal')
	except NoSuchElementException:
		print("modal wasn't there")

	for i in range(5):
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		time.sleep(1)
	print('getting all elements')
	all_elements = driver.find_elements_by_xpath("//div[@class='result_item']/div[1]/div[2]/div[1]/a")

	print(all_elements)

	running_lisp = ''
	for item in all_elements:
		bill_name = item.text
		if bill_name != ' ' and bill_name != '':
			if '(' in bill_name:
				whole_name=bill_name
				bill_name = whole_name[:bill_name.find('(')-1]
				bill_name += '-' + whole_name[whole_name.find('(')+1:whole_name.find(')')-2]
				bill_name = bill_name.replace('.','').lower()
			else:
				bill_name = bill_name[:bill_name.find(':')]
				bill_name = bill_name.replace('.','').lower()
			
			running_lisp += makeLispPhrase(bill_name.replace(' ', ''), beenVotedOnHouse=True) + '\n'
			bills_counted += 1

	print("house bills counted")
	return running_lisp, bills_counted

def failedSenate(driver, urls, bills_counted):
	driver.get(urls['Failed Senate'])
	time.sleep(1)
	try:
		stupid_modal = driver.find_element_by_xpath("//div[@class='modal-dialog modal-lg']/div/div[@class='modal-header']/button").click()
		print('exited modal')
	except NoSuchElementException:
		print("modal wasn't there")

	for i in range(6):
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		time.sleep(1)
	print('getting all elements')
	all_elements = driver.find_elements_by_xpath("//div[@class='result_item']/div[1]/div[2]/div[1]/a")

	print(all_elements)

	running_lisp = ''
	for item in all_elements:
		bill_name = item.text
		if bill_name != ' ' and bill_name != '':
			if '(' in bill_name:
				whole_name=bill_name
				bill_name = whole_name[:bill_name.find('(')-1]
				bill_name += '-' + whole_name[whole_name.find('(')+1:whole_name.find(')')-2]
				bill_name = bill_name.replace('.','').lower()
			else:
				bill_name = bill_name[:bill_name.find(':')]
				bill_name = bill_name.replace('.','').lower()
			
			running_lisp += makeLispPhrase(bill_name.replace(' ', ''), beenVotedOnSenate=True) + '\n'
			bills_counted += 1

	print("senate bills counted")
	return running_lisp, bills_counted

def vetoedNoOverride(driver, urls, bills_counted):
	driver.get(urls['Vetoed No Override'])
	time.sleep(1)
	try:
		stupid_modal = driver.find_element_by_xpath("//div[@class='modal-dialog modal-lg']/div/div[@class='modal-header']/button").click()
		print('exited modal')
	except NoSuchElementException:
		print("modal wasn't there")

	for i in range(5):
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		time.sleep(1)
	print('getting all elements')
	all_elements = driver.find_elements_by_xpath("//div[@class='result_item']/div[1]/div[2]/div[1]/a")

	print(all_elements)

	running_lisp = ''
	for item in all_elements:
		bill_name = item.text
		if bill_name != ' ' and bill_name != '':
			if '(' in bill_name:
				whole_name=bill_name
				bill_name = whole_name[:bill_name.find('(')-1]
				bill_name += '-' + whole_name[whole_name.find('(')+1:whole_name.find(')')-2]
				bill_name = bill_name.replace('.','').lower()
			else:
				bill_name = bill_name[:bill_name.find(':')]
				bill_name = bill_name.replace('.','').lower()
			
			running_lisp += makeLispPhrase(bill_name.replace(' ', ''), beenVotedOnHouse=True, passedHouse=True, beenVotedOnSenate=True, passedSenate=True,isVetoed=True,hadOverturn=True) + '\n'
			bills_counted += 1

	print("vetoed bills counted")
	return running_lisp, bills_counted

def vetoOverridden(driver, urls, bills_counted):
	driver.get(urls['Veto Overridden'])
	time.sleep(1)
	try:
		stupid_modal = driver.find_element_by_xpath("//div[@class='modal-dialog modal-lg']/div/div[@class='modal-header']/button").click()
		print('exited modal')
	except NoSuchElementException:
		print("modal wasn't there")

	for i in range(3):
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		time.sleep(1)
	print('getting all elements')
	all_elements = driver.find_elements_by_xpath("//div[@class='result_item']/div[1]/div[2]/div[1]/a")

	print(all_elements)

	running_lisp = ''
	for item in all_elements:
		bill_name = item.text
		if bill_name != ' ' and bill_name != '':
			if '(' in bill_name:
				whole_name=bill_name
				bill_name = whole_name[:bill_name.find('(')-1]
				bill_name += '-' + whole_name[whole_name.find('(')+1:whole_name.find(')')-2]
				bill_name = bill_name.replace('.','').lower()
			else:
				bill_name = bill_name[:bill_name.find(':')]
				bill_name = bill_name.replace('.','').lower()
			
			running_lisp += makeLispPhrase(bill_name.replace(' ', ''), beenVotedOnHouse=True, passedHouse=True, beenVotedOnSenate=True, passedSenate=True,isVetoed=True,hadOverturn=True,isOverturned=True) + '\n'
			bills_counted += 1

	print("veto overriden bills counted")
	return running_lisp, bills_counted

def main():
	driver = webdriver.Chrome()
	
	running_lisp = ''
	# bills_counted = 0
	urls = {'Failed House':'https://www.govtrack.us/congress/bills/browse?current_status[]=16&congress=__ALL__#current_status[]=16&congress=__ALL__',
			'Failed Senate':'https://www.govtrack.us/congress/bills/browse?current_status[]=16&congress=__ALL__#current_status[]=17&congress=__ALL__',
			'Vetoed No Override': 'https://www.govtrack.us/congress/bills/browse?current_status[]=16&congress=__ALL__#current_status[]=15&congress=__ALL__',
			'Veto Overridden':'https://www.govtrack.us/congress/bills/browse?current_status[]=16&congress=__ALL__#current_status[]=29&congress=__ALL__'}

	bills_counted = 0
	temp_lisp, bills_counted = failedHouse(driver, urls, bills_counted)
	running_lisp += temp_lisp

	driver.quit()
	driver = webdriver.Chrome()
	temp_lisp, bills_counted = failedSenate(driver, urls, bills_counted)
	running_lisp += temp_lisp

	driver.quit()
	driver = webdriver.Chrome()
	temp_lisp, bills_counted = vetoedNoOverride(driver,urls,bills_counted)
	running_lisp += temp_lisp

	driver.quit()
	driver = webdriver.Chrome()
	temp_lisp, bills_counted = vetoOverridden(driver,urls,bills_counted)
	running_lisp += temp_lisp

	print(running_lisp)
	print('bills_counted =', bills_counted)

	f = open('testHolder.meld', 'a')
	f.write(running_lisp)
	# print("bills_counted=", bills_counted)




if __name__ == '__main__':
	main()

def ifCongressDotGovWorking():

	driver = webdriver.Chrome()

	urls_of_statuses = {"Introduced": "https://www.congress.gov/search?searchResultViewType=expanded&q={%22congress%22:%22111%22,%22source%22:%22legislation%22,%22bill-status%22:%22introduced%22}&pageSize=250",
						"Passed One Chamber": "https://www.congress.gov/search?searchResultViewType=expanded&pageSize=250&q=%7B%22congress%22%3A%22111%22%2C%22source%22%3A%22legislation%22%2C%22bill-status%22%3A%22passed-one%22%7D",
						"Passed Both Chambers": "https://www.congress.gov/search?searchResultViewType=expanded&pageSize=250&q=%7B%22congress%22%3A%22111%22%2C%22source%22%3A%22legislation%22%2C%22bill-status%22%3A%22passed-both%22%7D",
						"Vetoed": "https://www.congress.gov/search?searchResultViewType=expanded&pageSize=250&q=%7B%22congress%22%3A%22all%22%2C%22source%22%3A%22legislation%22%2C%22bill-status%22%3A%22veto%22%7D",
						"Became Law": "https://www.congress.gov/search?searchResultViewType=expanded&pageSize=250&q=%7B%22congress%22%3A%22111%22%2C%22source%22%3A%22legislation%22%2C%22bill-status%22%3A%22law%22%7D"
						}

	key_status_words = {'Introduced' : ['Introduced'],
						'Passed One Chamber' : ['Passed House', 'Passed Senate'],
						'Passed Both Chambers' : ['Passed House', 'Passed Senate'],
						'Vetoed' : ['Failed to Pass Over Veto', 'Vetoed By President'],
						'Became Law' : ['Became Law']}

	running_lisp = ''

	# driver.get(urls_of_statuses['Introduced'])
	# list_of_all_bills = driver.find_elements_by_xpath("//div[@id='main']/ol/li[@class='expanded']")
	# for item in list_of_all_bills:
	# 	if 'Introduced' in item.find_element_by_xpath(".//span[@class='result-item result-tracker']/p[@class='hide_fromsighted']").text:
	# 		name = item.find_element_by_xpath(".//span[@class='result-heading']/a").text
	# 		desc = item.find_element_by_xpath(".//span[@class='result-title']").text
	# 		status = 'Introduced'
	# 		temp_bill = Bill(name, desc, status)
	# 		running_lisp += makeLispPhrase(name)


	# driver.get(urls_of_statuses['Passed One Chamber'])
	# list_of_all_bills = driver.find_elements_by_xpath("//div[@id='main']/ol/li[@class='expanded']")
	# for item in list_of_all_bills:
	# 	this_status = item.find_element_by_xpath(".//span[@class='result-item result-tracker']/p[@class='hide_fromsighted']").text
	# 	name = item.find_element_by_xpath(".//span[@class='result-heading']/a").text
	# 	if ('Passed House' in this_status and name[0] == 'H'):
	# 		desc = item.find_element_by_xpath(".//span[@class='result-title']").text
	# 		status = 'Passed House Only'
	# 		temp_bill = Bill(name, desc, status)
	# 		running_lisp += makeLispPhrase(name, beenVotedOnHouse=True, passedHouse=True)
	# 	elif ('Passed Senate' in this_status and name[0] == 'S'):
	# 		desc = item.find_element_by_xpath(".//span[@class='result-title']").text
	# 		status = 'Passed House Only'
	# 		temp_bill = Bill(name, desc, status)
	# 		running_lisp += makeLispPhrase(name, beenVotedOnSenate=True, passedSenate=True)


	driver.get(urls_of_statuses['Passed Both Chambers'])
	list_of_all_bills = driver.find_elements_by_xpath("//div[@id='main']/ol/li[@class='expanded']")
	for item in list_of_all_bills:
		this_status = item.find_element_by_xpath(".//span[@class='result-item result-tracker']/p[@class='hide_fromsighted']").text
		name = item.find_element_by_xpath(".//span[@class='result-heading']/a").text
		if ('Passed House' in this_status and name[0] == 'S'):
			desc = item.find_element_by_xpath(".//span[@class='result-title']").text
			status = 'Passed Both'
			temp_bill = Bill(name, desc, status)
			running_lisp += makeLispPhrase(name, beenVotedOnHouse=True, passedHouse=True, beenVotedOnSenate=True, passedSenate=True)
		elif ('Passed Senate' in this_status and name[0] == 'H'):
			desc = item.find_element_by_xpath(".//span[@class='result-title']").text
			status = 'Passed House Only'
			temp_bill = Bill(name, desc, status)
			running_lisp += makeLispPhrase(name, beenVotedOnHouse=True, passedHouse=True, beenVotedOnSenate=True, passedSenate=True, )

	print(running_lisp)