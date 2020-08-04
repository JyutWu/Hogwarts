from Selenium_Company_Wecat.test_wework_login.index import Index


class TestRegister:
    def setup(self):
        self.index = Index()

    def test_register(self):
        result = self.index.goto_register().register()
        return result
