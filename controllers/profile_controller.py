from models.user import User
from services.UserService import UserService


class ProfileController:
    def __init__(self, view, main_window, user):
        self.view = view
        self.main_window = main_window
        self.user = user
        self.load_user_data()
        self.view.save_button.clicked.connect(self.save_user_data)
        self.user_service = UserService()

    def load_user_data(self):
        self.view.email_input.setText(self.user.email)
        self.view.full_name_input.setText(self.user.full_name)
        self.view.phone_input.setText(self.user.phone)
        self.view.address_input.setText(str(self.user.address))
        #self.view.key_input.setText(self.user.key) TODO

    def save_user_data(self):
        self.user.full_name = self.view.full_name_input.text()
        self.user.phone = self.view.phone_input.text()
        self.user.address = int(self.view.address_input.text()) #TODO

        try:
            self.user = self.user_service.update_user(self.user)
            if self.user:
                self.view.message_label.setText('Profile updated successfully')
            else:
                raise Exception('Error while saving')
        except Exception as e:
            self.view.message_label.setText(f'Error updating profile: {str(e)}')