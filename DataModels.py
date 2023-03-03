import pandas as pd
import cryptpandas as crp


class dataModel:
    """
    class data models to stored to Data Base
    """
    def __init__(self):
        self.salt = b"\x18\xc9R\x0b\x04NCVYS\x97\xed\x1b!\xf6v\x8d3a\x9c\xd3\xf6w*\xa5\x82\x05\x8a\x9ek\x1c\x08\x10:\xa8\xe9\xbb\xbf|`{7\xf5^r\xd2\x86lG&\xac\x19\x03\x1b\xe0\xcd\x1bnz\xe4\xac\xcf\x0c\x07\x97\x07s\x15M5\xc3t:|-\xd7i\x87hZ%\xf6M[\x9a\x908Z\xfc\x15\xa3\xce\xac\xa69\xfe\x1c\xe0\xccu"
        self.users_file = "resource/users.crypt"
        self.listPasswordFile = "resource/listPassword.crypt"
        self.mainPassword = "({@XnSJ>8w2}y(]7w;u'p4H"
        self.users = self.initData()
        self.listPassword = self.initData1()

    def initData(self):
        """
        check password users models, and create it if not exists
        """
        try:
            # print('debug piye yo')
            users = crp.read_encrypted(
                path=self.users_file, password=self.mainPassword, salt=self.salt
            )
            return users
        except FileNotFoundError:
            df = pd.DataFrame(
                {
                    "users": [
                        "admin",
                    ],
                    "passwords": [
                        "admin",
                    ],
                }
            )
            crp.to_encrypted(
                df,
                password=self.mainPassword,
                path=self.users_file,
                salt=self.salt,
            )
            users = crp.read_encrypted(
                path=self.users_file, password=self.mainPassword, salt=self.salt
            )
            return users

    def initData1(self):
        """
        check List Password and if not exists, create it
        """
        try:
            users = crp.read_encrypted(
                path=self.listPasswordFile,
                password=self.mainPassword,
                salt=self.salt,
            )
            return users
        except FileNotFoundError:
            df = pd.DataFrame(
                {
                    "user": [
                        "admin",
                    ],
                    "site": [
                        "admin",
                    ],
                    "passwords": [
                        "admin",
                    ],
                }
            )
            crp.to_encrypted(
                df,
                password=self.mainPassword,
                path=self.listPasswordFile,
                salt=self.salt,
            )
            user = crp.read_encrypted(
                path=self.listPasswordFile,
                password=self.mainPassword,
                salt=self.salt,
            )
            return user

    def check_exist_data_login(self, user):
        """Check data user forlogin"""
        df = self.users[self.users["users"] == user]
        if len(df) > 0:
            return True
        else:
            return False

    def get_password_login(self, user):
        """get users password"""
        return self.users[self.users["users"] == user].iloc[0, 1]

    def add_data_user(self, user, pwd):
        """Register new user"""
        # print(type(self.users))
        self.users = self.users.append(
            {"users": user, "passwords": pwd}, ignore_index=True
        )
        # print('add data',self.users)
        self.commitData(data="users")

    def commitData(self, data="users"):
        """save data to file"""
        # print('debug users',self.users)
        if data == "users":
            crp.to_encrypted(
                self.users,
                password=self.mainPassword,
                path=self.users_file,
                salt=self.salt,
            )
        elif data == "site":
            crp.to_encrypted(
                self.listPassword,
                password=self.mainPassword,
                path=self.listPasswordFile,
                salt=self.salt,
            )

    def check_exist_data(self, site, user):
        """check data site password for current user"""
        df = self.listPassword[self.listPassword["user"] == user]
        try:
            df1 = df[df["site"] == site]
        except:
            df1 = None
        if df1 is not None:
            if len(df1) > 0:
                return True
            else:
                return False
        else:
            return False

    def get_password(self, site, user):
        """get site password from current user"""
        # print('list', self.listPassword)
        df = self.listPassword[self.listPassword["user"] == user]
        # print('df', df)
        df = df[df["site"] == site]
        # print(df)
        return df.iloc[0, 2]

    def add_password(self, site, pwd, user):
        """add site password for current user"""
        self.listPassword = self.listPassword.append(
            {"user": user, "site": site, "passwords": pwd}, ignore_index=True
        )
        self.commitData(data="site")

    def update_password(self, user, site, newPwd):
        """Update site password for current user"""
        self.listPassword.loc[
            (self.listPassword.user == user) & (self.listPassword.site == site),
            "passwords",
        ] = newPwd
        self.commitData(data="site")

    def deletePassword(self, site, user):
        """delete site password for current user"""
        self.listPassword = self.listPassword[
            (self.listPassword.user != user) & (self.listPassword.site != site)
        ]
        self.commitData(data="site")

    def change_password_user(self, user, newPwd):
        """Change current user password"""
        self.users.loc[self.users.users == user, "passwords"] = newPwd
        self.commitData(data="users")
