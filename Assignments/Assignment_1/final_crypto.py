# Import libraries

import requests
from datetime import datetime
import matplotlib.pyplot as plt


def scrape_crypto() :
	# Creating a dictionary to provide values as query selectors
	payload = {'fsyms' : 'BTC,ETH', 'tsyms':'USD'}

	for value in range(10):
		# Creating a responce object called url
		r = requests.get("https://min-api.cryptocompare.com/data/pricemulti", params = payload)

		#Converting the bytes format to json
		result = r.json()
		bitcoin = result['BTC']['USD']
		ethereum = result['ETH']['USD']
		now = datetime.now()
		time = now.strftime("%I-%m-%d %H:%M %p")
		write_crypto(bitcoin, ethereum, time)

	read_crypto()


def write_crypto(bitcoin, ethereum, time):
	# Writing data to the file 
	data = str(bitcoin) + ';' + str(ethereum) + ';' + str(time)
	filename = 'crypto.txt'
	file_object = open(filename,'a')
	file_object.write(data + ' ' + '\n')
	file_object.close()

def read_crypto():
	#Reading data from the file
	BTC = []
	ETH = []
	DATES = []
	filename = 'crypto.txt'
	file_object = open(filename,'r')
	for line in file_object :
		fields = line.split(';')
		BTC.append(fields[0])
		ETH.append(fields[1])
		DATES.append(fields[2].strip())
	
	file_object.close()
	graph_crypto(BTC, ETH, DATES)


def graph_crypto(BTC, ETH, DATES):
	# Plotting the graph
	plt.title('Values of Bitcoin and Ethereum')
	plt.ylabel("Price in Dollars")
	plt.xlabel("Date")

	plt.plot(DATES , BTC , linewidth = 1)
	plt.scatter(DATES , BTC ,c = 'red', s = 15)
	plt.xticks(rotation = 45)
	plt.tick_params(axis = 'both',which = 'major' , labelsize = 10)
	plt.show()


scrape_crypto()