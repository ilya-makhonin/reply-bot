from telebot import types
from log import log


class Forward:
    def __init__(self, develop_mode: bool):
        """
        :param develop_mode: mode for force debugging
        :type <bool>
        """
        self.message_forward_data = dict()
        self.__develop_mode = develop_mode
        self.logger = log('forward', 'forward.log', 'INFO')

    def add_key(self, message: types.Message):
        """
        Method for adding information about a user to app cache
        :param message: <telebot.types.Message> - standard telegram's message
        :return: nothing
        """
        new_key = {
            'id': message.from_user.id,
            'username': message.from_user.username,
            'first': message.from_user.first_name,
            'last': message.from_user.last_name
        }
        # TODO: I have to find method is better
        self.message_forward_data[message.date] = new_key
        self.logger.info(f"Method add_key. Information: {message.date} => {message.from_user.id}")

    def get_id(self, message: types.Message):
        """
        Method for getting a id of a user from app cache
        :param message: <telebot.types.Message> - standard telegram's message
        :return: <int> - a id of a user
        """
        try:
            result: dict = self.message_forward_data.get(message.reply_to_message.forward_date)
            self.logger.info(f"Method get_id. Information: {result}")
            return result.get('id')
        except Exception as error:
            self.logger.info(f"Error from get_key method. Information {error.with_traceback(None)}")

    def delete_data(self, message: types.Message):
        """
        Method for deleting information about a user from app cache
        :param message: <telebot.types.Message> - standard telegram's message
        :return: nothing
        """
        try:
            result = self.message_forward_data.pop(message.reply_to_message.forward_date)
            self.logger.info(f"Method delete_data. "
                             f"Information: user id {result} was deleted by {message.reply_to_message.date}")
        except Exception as error:
            self.logger.info(f"Error from delete_data method. Information {error.with_traceback(None)}")

    def clear_data(self):
        """
        Method for clearing app cache
        :return: nothing
        """
        self.message_forward_data.clear()
        self.logger.info(f"Method clear_data. Information: self.message_forward_data had cleared")

    def get_mode(self):
        """
        Method for getting state of debugging's mode
        :return: <bool>
        """
        return self.__develop_mode
