import time
import os
import sys
import requests
from threading import Thread
import mechanize


def AvtaNone():
  headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
  }
  browser = mechanize.Browser()
  #browser.set_handle_equiv(True)
  #browser.set_handle_gzip(True)
  #browser.set_handle_redirect(True)
  #browser.set_handle_referer(True)
  #browser.addheaders = [('User-Agent',headers['User-Agent'])]
  browser.set_handle_equiv(True)
  browser.set_handle_redirect(True)
  browser.set_handle_referer(True)
  browser.set_handle_robots(False)
  # Follows refresh 0 but not hangs on refresh &gt; 0
  browser.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
  browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
  #browser.set_handle_robots(False)
  browser.open('https://free.facebook.com/login.php')
  browser.select_form(nr=0)
  browser.form['email'] = ""
  browser.form['pass'] = ""
  submit = browser.submit()
  time.sleep(0.5)
  browser.select_form(nr=0)
  submit = browser.submit()
  browser.open("https://m.facebook.com/photo.php/?photo_id=107319812401391")
  """
  response = requests.get(image_url)
  if response.status_code == 200:
        # Open a local file in binary write mode and save the image content
        with open("downloaded_photo.jpg", "wb") as file:
            file.write(response.content)
            print("Photo downloaded successfully.")
    else:
        print(f"Failed to download photo. Status code: {response.status_code}")
  
  """
  image_url = None
  for link in browser.links():
    if link.url.endswith('.jpg') or link.url.endswith('.png'):
        image_url = link.url
        break
    print(image_url)


"""
    if image_url:
        # Download the image
        response = browser.retrieve(image_urlfilename="downloaded_image.jpg")
        print("Image downloaded successfully.")
    else:
        print("Image not found on the web page.")

"""





#Avtar()








def getAvtar(image_url):
    # Send an HTTP GET request to the image URL
    response = requests.get(image_url)
    if response.status_code == 200:
        # Open a local file in binary write mode and save the image content
        with open("downloaded_photo.jpg", "wb") as file:
            file.write(response.content)
            print("Photo downloaded successfully.")
    else:
        print(f"Failed to download photo. Status code: {response.status_code}")













def getUser():
  headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
  }
  browser = mechanize.Browser()
  cj = mechanize.LWPCookieJar()
  browser.set_cookiejar(cj)
  #browser.set_handle_equiv(True)
  #browser.set_handle_gzip(True)
  #browser.set_handle_redirect(True)
  #browser.set_handle_referer(True)
  #browser.addheaders = [('User-Agent',headers['User-Agent'])]
  browser.set_handle_equiv(True)
  browser.set_handle_redirect(True)
  browser.set_handle_referer(True)
  browser.set_handle_robots(False)
  # Follows refresh 0 but not hangs on refresh &gt; 0
  browser.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
  browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
  #browser.set_handle_robots(False)
  browser.open("http://free.facebook.com/login.php")
  browser.select_form(nr=0)
  browser.form['email'] = ""
  browser.form['pass'] = ""
  submit = browser.submit()
  time.sleep(0.7)
  browser.select_form(nr=0)
  submit = browser.submit()
  
  
  for cookie in cj:
    print(f"Cookie: {cookie.name} = {cookie.value}")
  
  for link in browser.links():
    if link.text == "Messages":
       browser.follow_link(link)
       time.sleep(0.3)
       users = browser.links()
       link2 = users[13:18]
       data_list = []
       for user in link2:
           #print(user.attrs[0][1])
           data = {
           "name" : user.text,
           "link" : user.attrs[0][1]
           }
           i = 0
           while i<len(link2):
               data_list.append(data)
               i+=1
       
       
       
       print(data_list)
   
       
  
  """
  #getUrl = str(input("Enter Url : "))
  #browser.open(getUrl)
  
  f = open("data.html", "w")
  dat = browser.response().read()
  f.write(str(dat,"UTF-8"))
  f.close()
  """
  













getUser()





