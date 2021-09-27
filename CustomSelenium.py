from RPA.core.webdriver import cache, download, start
import logging
from selenium import webdriver



class CustomSelenium:

    def __init__(self):
        self.driver = None
        self.logger = logging.getLogger(__name__)

    def set_chrome_options(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-gpu")
        options.add_argument('--disable-web-security')
        options.add_argument("--start-maximized")
        options.add_argument('--remote-debugging-port=9222')
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        return options

    def set_webdriver(self, browser="Chrome"):
        options = self.set_chrome_options()
        executable_driver_path = cache(browser)
        if not executable_driver_path:
            executable_driver_path = download(browser)
            self.logger.warning("Using downloaded driver: %s" % executable_driver_path)
        else:
            self.logger.warning("Using cached driver: %s" % executable_driver_path)

        self.driver = start("Chrome", executable_path=str(executable_driver_path), options=options)

    def open_url(self, url:str, screenshot:str=None):
        self.driver.get(url)
        if screenshot:
            self.driver.get_screenshot_as_file(screenshot)

    def driver_quit(self):
        if self.driver:
            self.driver.quit()
