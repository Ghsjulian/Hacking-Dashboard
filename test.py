import time
import os
import sys
import requests
from threading import Thread
import mechanize


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
browser.open("https://m.facebook.com/friends/center/suggestions/")

links = browser.links()
for link in browser.links():
  if link.text == "Add friend":
      print(link)
  
  






"""
f = open("data.html", "w")
dat = browser.response().read()
f.write(str(dat,"UTF-8"))
f.close()
"""
