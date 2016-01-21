# -*- coding: utf-8 -*-
from selenium import webdriver
from fixture.session import SessionHelper
from fixture.project import ProjectHelper
from fixture.james import JamesHelper
from fixture.soap import SoapHelper
from fixture.signup import SignupHelper
from fixture.mail import MailHelper


class Application:

    def __init__(self, browser, config):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.config = config
        self.base_url = config["web"]["baseURL"]
        self.session = SessionHelper(self)
        self.project = ProjectHelper(self)
        self.james = JamesHelper(self)
        self.soap = SoapHelper(self)
        self.signup = SignupHelper(self)
        self.mail = MailHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self, wd):
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()
