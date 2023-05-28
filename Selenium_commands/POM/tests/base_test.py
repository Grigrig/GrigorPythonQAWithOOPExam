import pytest

@pytest.mark.usefixtures("get_driver")
class BaseTest:

    def navigate_to_widget_part_from_home_page(self):
        self.home_page.click_on_widget_part_btn()

    def select_dropdown_items_from_select_page_select_menu(self, text="Green"):
        self.select_menu_page.click_on_select_btn()
        self.select_menu_page.select_item_from_select_menu_and_assert_text(text)

    def navigate_to_widget_part_and_select_item(self, text="Green"):
        self.navigate_to_widget_part_from_home_page()
        self.select_dropdown_items_from_select_page_select_menu(text)


