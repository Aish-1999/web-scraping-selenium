from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium
from selenium.webdriver.common.keys import Keys
import pandas as pd

driver = webdriver.Chrome('/Users/aishwaryas/Desktop/chromedriver')

driver.get('https://www.ebay.com/')

search_box = driver.find_element(By.ID , 'gh-ac')
search_box.clear()
search_box.send_keys('apple phones')
search_button = driver.find_element(By.ID , 'gh-btn').click()
# search_button
# driver.back()

#we also create xpath when we want multiple postings or items

#looking for name , rating , price and place from each posting and we are going to get all the postings
#cretae a list for all these 

phone_names = []
phone_prices = []
phone_type = []
phone_rating = []
phone_place = []
phone_reviews =[]

#HERE I AM INDIVIDUALLY GETTING THE POST ELEMENTS SO WE USE DRIVER
 # names = driver.find_elements(By.XPATH , "//div[@class = 's-item__title']")
 #    for name in names:
 #        phone_names.append(name.text)
    
 #    prices = driver.find_elements(By.XPATH , "//span[@class = 's-item__price']")
 #    for price in prices:
 #        phone_prices.append(price.text)
        
 #    types = driver.find_elements(By.XPATH , "//span[@class = 'SECONDARY_INFO']")
 #    for type_ in types:
 #        phone_type.append(type_.text)
        
 #    ratings = driver.find_elements(By.XPATH , "//div[@class = 'x-star-rating']")
 #    for rating in ratings:
 #        phone_rating.append(rating.text)
        
 #    places = driver.find_elements(By.XPATH , "//span[@class = 's-item__location s-item__itemLocation']")
 #    for place in places:
 #        phone_place.append(place.text)
        
 #    reviews = driver.find_elements(By.XPATH , "//span[@class = 's-item__reviews-count']")
 #    for review in reviews:
 #        phone_reviews.append(review.text)

#HERE I AM GETTING EACH POST AND FROM THOSE POST THEIR CONTENT HENCE IN PLACE OF DRIVER WE USE POST
postings = driver.find_elements(By.XPATH , "//div[@class = 's-item__wrapper clearfix']")
for post in postings:

    names = post.find_elements(By.XPATH , "//div[@class = 's-item__title']")
    for name in names:
        phone_names.append(name.text)
    
    prices = post.find_elements(By.XPATH , "//span[@class = 's-item__price']")
    for price in prices:
        phone_prices.append(price.text)
        
    types = post.find_elements(By.XPATH , "//span[@class = 'SECONDARY_INFO']")
    for type_ in types:
        phone_type.append(type_.text)
        
    ratings = post.find_elements(By.XPATH , "//div[@class = 'x-star-rating']")
    for rating in ratings:
        phone_rating.append(rating.text)
        
    places = post.find_elements(By.XPATH , "//span[@class = 's-item__location s-item__itemLocation']")
    for place in places:
        phone_place.append(place.text)
    try:
        if len(post.find_elements(By.XPATH , "//span[@class = 's-item__reviews-count']"))>0:
            reviews = post.find_elements(By.XPATH , "//span[@class = 's-item__reviews-count']")
            for review in reviews:
                phone_reviews.append(review.text)
        else:
            phone_reviews.append('0')
    except:
        pass
    
            
        
#checking lengthlen(phone_names)
len(phone_prices)
len(phone_type)
len(phone_rating)
len(phone_place)
len(phone_reviews)

#creating a dataframe
df = pd.DataFrame(zip(phone_names,phone_prices,phone_type,phone_rating,phone_place,phone_reviews) ,columns =['phone_names','phone_prices','phone_type','phone_rating','phone_place','phone_reviews'])

df.to_csv('/Users/aishwaryas/Desktop/python web scarpaing/project3selenium.csv', index=False)
