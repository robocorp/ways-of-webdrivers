from RPA.Browser.Selenium import Selenium
from SeleniumLibrary.base import keyword

class ExtendedSelenium(Selenium):

    def __init__(self, *args, **kwargs):
        Selenium.__init__(self, *args, **kwargs)

    @keyword
    def looking_at_element(self, locator):
        element = self.get_webelement(locator)
        self.logger.warn(dir(element))