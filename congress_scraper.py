import requests
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import urllib, http.client

class Bill:
	def __init__(self, name, description, status):
		self.name = name
		self. description = description
		self.status = status

def main():
	driver = webdriver.Chrome()


	urls_of_statuses = {"Introduced": "https://www.congress.gov/search?searchResultViewType=expanded&q={%22congress%22:%22111%22,%22source%22:%22legislation%22,%22bill-status%22:%22introduced%22}&pageSize=250",
						"Passed One Chamber": "https://www.congress.gov/search?searchResultViewType=expanded&pageSize=250&q=%7B%22congress%22%3A%22111%22%2C%22source%22%3A%22legislation%22%2C%22bill-status%22%3A%22passed-one%22%7D",
						"Passed Both Chambers": "https://www.congress.gov/search?searchResultViewType=expanded&pageSize=250&q=%7B%22congress%22%3A%22111%22%2C%22source%22%3A%22legislation%22%2C%22bill-status%22%3A%22passed-both%22%7D",
						"Vetoed": "https://www.congress.gov/search?searchResultViewType=expanded&pageSize=250&q=%7B%22congress%22%3A%22all%22%2C%22source%22%3A%22legislation%22%2C%22bill-status%22%3A%22veto%22%7D",
						"Became Law": "https://www.congress.gov/search?searchResultViewType=expanded&pageSize=250&q=%7B%22congress%22%3A%22111%22%2C%22source%22%3A%22legislation%22%2C%22bill-status%22%3A%22law%22%7D"
						}

	key_status_words = [['Introduced'],
						['Passed House', 'Passed Senate'],
						['Failed to Pass Over Veto', 'Vetoed By President']]

	driver.get(urls_of_statuses["Introduced"])

	list_of_all_bills = driver.find_elements_by_xpath("//div[@id='main']/ol/li[@class='expanded']")

	bills_in_this_status = []
	for item in list_of_all_bills:
		if 'Introduced' in item.find_element_by_xpath(".//span[@class='result-item result-tracker']/p[@class='hide_fromsighted']").text:
			name = item.find_element_by_xpath(".//span[@class='result-heading']/a").text
			desc = item.find_element_by_xpath(".//span[@class='result-title']").text
			status = 'Introduced'
			temp_bill = Bill(name, desc, status)
			bills_in_this_status.append(temp_bill)
		
		
	
	print("bills listed under Introduced one website:", len(list_of_all_bills))
	print("bills actually in Introduced status:", len(bills_in_this_status))



if __name__ == '__main__':
	main()