from unittest import TestCase


from selenium import  webdriver



class Test(TestCase):
    def test_test(self):
        webdriver.Chrome()
        self.fail()
