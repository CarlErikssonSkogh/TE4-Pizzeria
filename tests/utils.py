import unittest
from playwright.sync_api import sync_playwright
from os import path

#
#  Test class template
#
class TemplateTest(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        self.playwright = sync_playwright().start()
        browserType = self.playwright.chromium
        launchOptions = {"headless": True}
        self.browser = browserType.launch(**launchOptions)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()

    @classmethod
    def tearDownClass(self) -> None:
        self.context.close()
        self.browser.close()
        self.playwright.stop()

    def setUp(self, fileToTest) -> None:
        # file name is relative to the root directory of the project
        relativePath = path.join(path.dirname(__file__), "..", fileToTest)
        absolutePath = path.abspath(relativePath)
        self.page.goto(f"file://{absolutePath}")

    def tearDown(self) -> None:
        self.page.goto("about:blank")

    #
    # Helper functions
    #

    # run assertIn for every string in the list
    def assertInAll(self, matches: list[str], source) -> None:
        for match in matches:
            self.assertIn(match, source)
