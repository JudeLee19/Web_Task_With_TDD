from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase


class PostTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('/Users/judelee/Downloads/chromedriver')
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_show_web(self):
        self.browser.get(self.live_server_url)
        self.assertIn('Board', self.browser.title)