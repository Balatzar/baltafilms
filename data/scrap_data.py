from selenium import webdriver
from selenium.webdriver.common.keys import Keys

firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
firefox_capabilities['marionette'] = True

file = open("storage/my_movies.txt", "w")
count = 101

driver = webdriver.Firefox(capabilities=firefox_capabilities)
driver.get("http://www.imdb.com/user/ur22079630/ratings")
for x in range(0, 18):
  movies = driver.find_elements_by_class_name("rating.rating-list")
  for m in movies:
    print(m.get_attribute("id"))
    file.write(m.get_attribute("id") + '\n')

  driver.get("http://www.imdb.com/user/ur22079630/ratings?start=" + str(count) + "&view=detail&sort=ratings_date:desc")
  count = count + 100

driver.close()
