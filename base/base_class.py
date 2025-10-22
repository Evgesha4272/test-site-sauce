import datetime

class Base:

    def __init__(self, driver):
        self.driver = driver

    # Method get current URL
    def get_current_url(self):
        get_url = self.driver.current_url
        print('Current url:', get_url)

    # Method check word
    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print('Good value word')

    # Method screenshot
    def get_screenshot(self):
        now_date = datetime.datetime.now().strftime('%Y-%m-%d')
        name_screenshot = 'screenshot' + now_date + '.png'

    # Method check URL
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print('Good url')