#Imports:
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
from pathlib import Path

#Load a text file called stocks.txt if it exsist.
#Count how many lines are in the text file. 
#Each stock takes 10 lines, so divide the number of lines by 10 and we know how many stocks are listed and we know how many loops to update the stocks in the save file.
lines_per_stock = 10

#Check if the stocks.txt file exsists:
stocks_saved = 0
my_file = Path("Stocks.txt")
if my_file.is_file():
    text_file = open("Stocks.txt", "r") #Open the stocks.txt file
    #Splits the element by "\n"
    lines = text_file.readlines()
    stocks_saved = len(lines)/lines_per_stock
    text_file.close()
    open('Stocks.txt', 'w').close()

print("Stock information that you're following:\n===============================")

#Loop through the stocks in the stocks.txt file, find their current stock values, display them on the screen, then resave the text file:
current_stock = 0
while(current_stock < int(stocks_saved)):

    stock_ticker = lines[0+(current_stock*lines_per_stock)]
    user_input = stock_ticker.replace("\n","")
    user_input += " stock"
    company_name = lines[1+(current_stock*lines_per_stock)]
    exchange = lines[2+(current_stock*lines_per_stock)]

    #Open the browser:
    driver = webdriver.Chrome()
    driver.get("http://www.google.com/")
    driver.implicitly_wait(60)
    
    element = driver.find_element_by_xpath("//div[1]/div/div[2]/input")
    time.sleep(1)
    element.send_keys(user_input)
    #time.sleep(3)
    element.send_keys(Keys.ENTER)

    #Update the current price, price range, percentage change, open price, high price and low price of that stock from today, and top 3 news links associated with said stock:
    current_price = driver.find_element_by_xpath("//div/g-card-section/span[1]/span/span[1]").text
    price_change = driver.find_element_by_xpath("//div/g-card-section/span[2]/span[1]").text
    percentage_change = driver.find_element_by_xpath("//div/g-card-section/span[2]/span[2]/span[1]").text
    today_open = driver.find_element_by_xpath("//div[1]/table/tbody/tr[1]/td[2]").text
    today_high = driver.find_element_by_xpath("//div[1]/table/tbody/tr[2]/td[2]").text
    today_low = driver.find_element_by_xpath("//div[1]/table/tbody/tr[3]/td[2]").text
    links = driver.find_elements_by_xpath("//div[@class='g']/div[@class='rc']/div[1]/a")
    
    file = open('Stocks.txt', 'a+')
    file.write(stock_ticker)
    file.write(company_name)
    file.write(exchange)
    file.write("$"+current_price+" "+price_change+" "+percentage_change+"\n")
    file.write("Open Price"+ " $"+today_open+"\n")
    file.write("Today's High Price"+ " $"+today_high+"\n")
    file.write("Today's Low Price"+ " $"+today_low+"\n")
    file.write(links[0].get_attribute("href")+"\n"+links[1].get_attribute("href")+"\n"+links[2].get_attribute("href")+"\n")
    file.close()

    print("Stocks.txt file updated!")
    print(stock_ticker.replace("\n",""))
    print(company_name.replace("\n",""))
    print(exchange.replace("\n",""))
    print("$"+current_price+" "+price_change+" "+percentage_change)
    print("Open Price"+ " $"+today_open)
    print("Today's High Price"+ " $"+today_high)
    print("Today's Low Price"+ " $"+today_low)
    print(links[0].get_attribute("href")+"\n"+links[1].get_attribute("href")+"\n"+links[2].get_attribute("href"))

    current_stock += 1
    driver.quit()

run_again = True

while(run_again == True):

    user_input = input("\nWould you like to look up a new stock? (Y or N)")
    while(user_input.upper() != 'N' and user_input.upper() != 'Y'):
        user_input = input("Please enter a Y or N.\nWould you like to look up a new stock? (Y or N)")
    
    if user_input.upper() == 'N':
        run_again = False
    elif user_input.upper() == 'Y':
        user_input = input("Enter the  stock ticker or stock name you would like to look up: ")
        stock_ticker = user_input
        user_input += " stock"

        #Open the browser:
        driver = webdriver.Chrome()
        driver.get("http://www.google.com/")
        driver.implicitly_wait(60)
        
        element = driver.find_element_by_xpath("//div[1]/div/div[2]/input")
        time.sleep(1)
        element.send_keys(user_input)
        #time.sleep(1)
        element.send_keys(Keys.ENTER)

        #time.sleep(1)
        company_name = driver.find_element_by_xpath("//span[@class='vk_bk']").text
        print(company_name)

        exchange = driver.find_element_by_xpath("//div[@class='HfMth']").text
        print(exchange)

        #Current Stock Price/Price Change/Percentage Change
        #current_price = driver.find_element_by_xpath("//span[@class='IsqQVc NprOob XcVN5d']").text
        current_price = driver.find_element_by_xpath("//div/g-card-section/span[1]/span/span[1]").text
        #price_change = driver.find_element_by_xpath("//span[@jsname='qRSVye']").text
        price_change = driver.find_element_by_xpath("//div/g-card-section/span[2]/span[1]").text
        #percentage_change = driver.find_element_by_xpath("//span[@jsname='rfaVEf']").text
        percentage_change = driver.find_element_by_xpath("//div/g-card-section/span[2]/span[2]/span[1]").text
        print("$"+current_price+" "+price_change+" "+percentage_change)

        #Today's Open Price
        today_open = driver.find_element_by_xpath("//div[1]/table/tbody/tr[1]/td[2]").text
        print("Open Price"+ " $"+today_open)
        #Today's High Price
        today_high = driver.find_element_by_xpath("//div[1]/table/tbody/tr[2]/td[2]").text
        print("Today's High Price"+ " $"+today_high)
        #Today's Low Price
        today_low = driver.find_element_by_xpath("//div[1]/table/tbody/tr[3]/td[2]").text
        print("Today's Low Price"+ " $"+today_low)

        #News articles associated with searched stock (Three Links)
        links = driver.find_elements_by_xpath("//div[@class='g']/div[@class='rc']/div[1]/a")#.get_attribute("href")
        print(links[0].get_attribute("href")+"\n"+links[1].get_attribute("href")+"\n"+links[2].get_attribute("href"))

        user_input = input("Would you like to save the stock info? (Y or N)")
        while(user_input.upper() != 'N' and user_input.upper() != 'Y'):
            user_input = input("Please enter a Y or N.\nWould you like to save the stock info? (Y or N)")

        if user_input.upper() == 'Y':
            #with open("stocks.txt", "a") as myfile:
            file = open('Stocks.txt', 'a+')
            file.write(stock_ticker+"\n")
            file.write(company_name+"\n")
            file.write(exchange+"\n")
            file.write("$"+current_price+" "+price_change+" "+percentage_change+"\n")
            file.write("Open Price"+ " $"+today_open+"\n")
            file.write("Today's High Price"+ " $"+today_high+"\n")
            file.write("Today's Low Price"+ " $"+today_low+"\n")
            file.write(links[0].get_attribute("href")+"\n"+links[1].get_attribute("href")+"\n"+links[2].get_attribute("href")+"\n")
            file.close()
            print("Stocks.txt file updated!")
            #print(os.getcwd())
        driver.quit()