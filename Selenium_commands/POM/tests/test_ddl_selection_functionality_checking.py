import pytest

from Selenium_commands.POM.tests.base_test import BaseTest

@pytest.mark.smoke
@pytest.mark.parametrize("text", ["Green", "Yellow", "Black"])
class TestSelections(BaseTest):
    def test_select_item_from_select_menu_and_assert_value(self, text):
        self.navigate_to_widget_part_and_select_item(text)
