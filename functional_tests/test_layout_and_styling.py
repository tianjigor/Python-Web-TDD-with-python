# -*- coding:utf-8 -*-
from .base import FunctionalTest


# class LayoutAndStylingTest(FunctionalTest):
    # def test_layout_adn_styling(self):
    #     self.browser.get(self.live_server_url)
    #     self.browser.set_window_size(1024, 768)
    #
    #     inputbox = self.get_item_input_box()
    #     inputbox.send_keys('testing\n')
    #     self.assertAlmostEqual(
    #         inputbox.location['x'] + inputbox.size['width']/2,
    #         512,
    #         delta=5
    #     )