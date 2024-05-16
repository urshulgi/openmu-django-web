# from bcrypt import gensalt, hashpw
from bcrypt import checkpw

from openmu.models.data import Account as AccountModel


class Account:

    def __init__(self, login_name):
        self.login_name = login_name

    def is_correct_password(self, password: str) -> bool:
        """
        Passwords in OpenMU project are encrypted with bcrypt.

        :param password:
            Plain text password
        """
        bpassword = password.encode("utf-8")
        account_hash = self.account.passwordhash.encode("utf-8")
        return checkpw(bpassword, account_hash)

    def update_password(self):
        return

    @property
    def account(self) -> AccountModel:
        """
        :return:
            If there are no results that match the query, get() will raise a DoesNotExist exception.
            https://docs.djangoproject.com/en/5.0/topics/db/queries/#retrieving-a-single-object-with-get
        """
        account_object = AccountModel.objects.get(loginname=self.login_name)
        return account_object
