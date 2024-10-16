from ui_auto_structure.base.base_2 import Base
from ui_auto_structure import page


class PageLogin(Base):
    def page_go_to_login(self):
        self.driver.get("https://dev.acucloud.accuenergy.com")

    def page_input_username(self, username):
        self.base_input(page.login_username, username)

    def page_input_password(self, password):
        self.base_input(page.login_password, password)

    def page_click_login_button(self):
        self.base_click(page.submit)

    def page_get_error(self):
        self.base_get_text(page.login_error)

    def page_login(self, username, password):
        self.page_input_username(username)
        self.page_input_password(password)
        self.page_click_login_button()
