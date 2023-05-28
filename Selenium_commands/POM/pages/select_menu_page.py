from hamcrest import equal_to
from selenium.webdriver.common.by import By
from Selenium_commands.POM.lib.helpers import Helpers
from Selenium_commands.POM.lib.assertions import assert_that

select_btn = (By.XPATH, '(//*[@id="item-8"])[2]')
select_menu = (By.ID, 'oldSelectMenu')


class SelectMenuPage(Helpers):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_on_select_btn(self):
        self.find_and_click(select_btn)

    def select_item_from_select_menu_and_assert_text(self, index=4, value="3", text="Green"):
        self.select_item(select_menu, by_value=True, value=value)
        selected_item = self.select_item(select_menu, by_text=True, text=text)
        assert_that(selected_item, equal_to(text))
        self.select_item(select_menu, by_index=True, text=index)



