import base
from base.base_action import BaseAction

class SettingPage(BaseAction):
    def __init__(self,driver):
        BaseAction.__init__(self,driver)

    def input_search_text(self,content):
        self.input_element_content(base.input_src_textid,content)

    def click_back(self):
        self.


