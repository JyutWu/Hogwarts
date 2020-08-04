from Selenium_Company_Wecat.test_wework.index import Index


class TestAddmumber:
    def setup(self):
        self.index = Index()

    def test_addmumber(self):
        self.index.goto_add_member().add_member()
