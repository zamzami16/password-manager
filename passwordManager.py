import tkinter as tk
import DataModels
from tkinter import ttk, messagebox


class formManage(ttk.Frame):
    """
    manage window view
    """

    def __init__(self, container, name_form):
        """initialize the view"""
        super().__init__(container)
        self.columnconfigure(2, weight=2)
        self.label_form = []
        self.entry_form = []

        if name_form == "show":
            """SHow Password windows"""
            label = ("Site Name\t", "Password\t")
            for i in range(2):
                lab = ttk.Label(self, text=label[i])
                lab.grid(row=i, column=0, sticky="W")
                ttk.Label(self, text=":").grid(row=i, column=1)
                entry = ttk.Entry(self, width=30)
                entry.grid(row=i, column=2, padx=5, pady=5)
                self.label_form.append(lab)
                self.entry_form.append(entry)
                # self.grid(row=1, column=0, sticky='wnse', pady=5)
            self.show_password_butt = ttk.Button(
                self, text="Show Password", command=self.master.showPassword
            )
            self.show_password_butt.place(x=116, y=69)
            self.quid_butt = ttk.Button(
                self, text="Quit", command=self.master.destroy
            )
            self.quid_butt.place(x=228, y=69)
        elif name_form == "add":
            """Show add password view"""
            label = ("Site Name", "Enter Password", "Re-Enter Password")
            for i in range(3):
                lab = ttk.Label(self, text=label[i])
                lab.grid(row=i, column=0, sticky="W")
                ttk.Label(self, text=":").grid(row=i, column=1)
                entry = ttk.Entry(self, width=30)
                entry.grid(row=i, column=2, padx=5, pady=5)
                self.label_form.append(lab)
                self.entry_form.append(entry)
                # self.grid(row=2, column=0, sticky='wnse', pady=5)
            self.show_password_butt = ttk.Button(
                self, text="Add Password", command=self.master.addPassword
            )
            self.show_password_butt.place(x=117, y=95)
            self.quid_butt = ttk.Button(
                self, text="Quit", command=self.master.destroy
            )
            self.quid_butt.place(x=229, y=95)

        elif name_form == "change":
            """Show change password view"""
            label = (
                "Site Name",
                "Old Password",
                "New Password",
                "Re-New Password",
            )
            for i in range(4):
                lab = ttk.Label(self, text=label[i])
                lab.grid(row=i, column=0, sticky="W")
                ttk.Label(self, text=":").grid(row=i, column=1)
                entry = ttk.Entry(self, width=30)
                entry.grid(row=i, column=2, padx=5, pady=2)
                self.label_form.append(lab)
                self.entry_form.append(entry)
                # self.grid(row=3, column=0, sticky='wnse', pady=5)
            ttk.Label(self).grid(row=4, column=0, pady=2)
            self.show_password_butt = ttk.Button(
                self, text="Change Password", command=self.master.changePassword
            )
            self.show_password_butt.place(x=115, y=99)
            self.quid_butt = ttk.Button(
                self, text="Quit", command=self.master.destroy
            )
            self.quid_butt.place(x=227, y=99)

        elif name_form == "delete":
            """Show delete password view"""
            label = "Site Name\t"
            for i in range(1):
                lab = ttk.Label(self, text=label)
                lab.grid(row=i, column=0, sticky="W", padx=5, pady=5)
                ttk.Label(self, text=":").grid(row=i, column=1, sticky="w")
                entry = ttk.Entry(self, width=30)
                entry.grid(row=i, column=2, padx=5, pady=5)
                self.label_form.append(lab)
                self.entry_form.append(entry)
                # self.grid(row=4, column=0, sticky='wnse', pady=5)
            self.show_password_butt = ttk.Button(
                self, text="Delete Password", command=self.master.deletePassword
            )
            self.show_password_butt.place(x=121, y=39)
            self.quid_butt = ttk.Button(
                self, text="Quit", command=self.master.destroy
            )
            self.quid_butt.place(x=233, y=39)

        elif name_form == "login":
            """Show login view"""
            label = ("Username", "Password")
            for i in range(2):
                lab = ttk.Label(self, text=label[i])
                lab.grid(row=i, column=0, sticky="W", padx=5, pady=5)
                ttk.Label(self, text=":").grid(row=i, column=1)
                entry = ttk.Entry(self, width=30)
                entry.grid(row=i, column=2, padx=5, pady=5)
                self.label_form.append(lab)
                self.entry_form.append(entry)
                # self.grid(row=5, column=0, sticky='wnse', pady=5)
            self.show_password_butt = ttk.Button(
                self, text="Login", command=self.master.login
            )
            self.show_password_butt.place(x=99, y=65)
            self.quid_butt = ttk.Button(
                self, text="Quit", command=self.master.destroy
            )
            self.quid_butt.place(x=211, y=65)
            self.more_butt = ttk.Button(
                self,
                text="More Management",
                command=self.master.launch_management,
            )
            self.more_butt.place(x=99, y=95, width=188)
            """
            self.register_butt = ttk.Button(self, text='Register',
                                            command=self.master.register_user)
            self.register_butt.place(x=115, y=95)
            self.forget_password_butt = ttk.Button(self, text='Forget',
                                                   command=self.master.forget_password)
            self.forget_password_butt.place(x=211, y=95)
            self.login2_butt = ttk.Button(self, text='Login',
                                          command=self.master.login)
            self.login2_butt.place(x=20, y=67, height=53, width=75)
            """

        self.grid(row=1, column=0, sticky="wnse", pady=5)
        # self.pack(fill=tk.BOTH, expand=True)

    def getFromEntry(self):
        """get entry data"""
        value = []
        for entry in self.entry_form:
            value.append(entry.get())
        return value

    def deleteAll(self):
        """delete the entry box"""
        for entry in self.entry_form:
            entry.delete(0, tk.END)


class containerLabel(ttk.Frame):
    """create class container label name"""

    def __init__(self, container, name):
        super().__init__(container)

        self.label = ttk.Label(self, text=name, font=("Arial", 15))
        self.label.pack(padx=5, pady=5)
        self.grid(row=0, column=0, sticky="we")
        # self.pack(expand=True)


class containerButt_opt(ttk.Labelframe):
    """
    Create container button with values:
        - Show Password
        - Add Password
        - Change Password
        - Delete Password
    """

    def __init__(self, container):
        super().__init__(container)
        self.rad_value = tk.IntVar()
        ttk.Radiobutton(
            self,
            text="Show Password\t\t",
            value=0,
            variable=self.rad_value,
            command=self.master.updateContainer2,
        ).grid(row=0, column=0, padx=5, pady=5, sticky="w")
        ttk.Radiobutton(
            self,
            text="Add Password\t\t",
            value=1,
            variable=self.rad_value,
            command=self.master.updateContainer2,
        ).grid(row=1, column=0, padx=5, pady=5, sticky="w")
        ttk.Radiobutton(
            self,
            text="Change Password",
            value=2,
            variable=self.rad_value,
            command=self.master.updateContainer2,
        ).grid(row=0, column=1, padx=5, pady=5, sticky="w")
        ttk.Radiobutton(
            self,
            text="Delete Password",
            value=3,
            variable=self.rad_value,
            command=self.master.updateContainer2,
        ).grid(row=1, column=1, padx=5, pady=5, sticky="w")
        self.grid(row=2, column=0, sticky="nswe")
        # self.pack(2, fill=tk.BOTH)


class managementWindow:
    """
    Add Management windows from base view
    """

    def __init__(self, container):
        self.master = container
        self.master.title("Management App")
        self.master.geometry("325x200")
        self.master.resizable(0, 0)
        # make it show the Main Window when close it
        self.master.protocol(
            "WM_DELETE_WINDOW", self.master.master.onManagementClosed
        )
        title = ttk.Label(
            self.master, text="Management Window", font=("Arial", 14)
        )
        title.pack(padx=5, pady=5)
        self.container_select_val = tk.IntVar()
        self.container_select = ttk.Labelframe(self.master)
        self.tabControl = ttk.Notebook(self.master)
        # add register tab
        self.tab_register = ttk.Frame(self.tabControl)
        self.forget_pass = ttk.Frame(self.tabControl)
        self.change_pass = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab_register, text="Register")
        self.tabControl.add(self.forget_pass, text="Forget Password")
        self.tabControl.add(self.change_pass, text="Change Password")
        # pack tab control
        self.tabControl.pack(expand=1, fill=tk.BOTH)

        # add element in tab register
        ttk.Label(self.tab_register, text="User Name").grid(
            row=0, column=0, padx=5, pady=5, sticky="w"
        )
        ttk.Label(self.tab_register, text="Enter Password").grid(
            row=1, column=0, padx=5, pady=5, sticky="w"
        )
        ttk.Label(self.tab_register, text="Re-Enter Password").grid(
            row=2, column=0, padx=5, pady=5, sticky="w"
        )
        self.register_entry = []
        for i in range(3):
            ttk.Label(self.tab_register, text=":").grid(
                row=i, column=1, sticky="w"
            )
            entry = ttk.Entry(self.tab_register, width=30)
            entry.grid(row=i, column=2, padx=2, pady=2, sticky="w")
            self.register_entry.append(entry)

        self.footer = ttk.Frame(self.tab_register)
        self.cancel_button = ttk.Button(
            self.footer,
            text="Cancel",
            command=self.master.master.onManagementClosed,
        )
        self.cancel_button.grid(row=0, column=2, pady=5, sticky="E", padx=10)
        ttk.Button(
            self.footer, text="Register", command=self.register_user
        ).grid(row=0, column=0, pady=5, sticky="W", padx=10)
        self.footer.grid(row=3, column=2, padx=2, sticky="EW", ipady=20)

        # add element in tab forget password
        ttk.Label(self.forget_pass, text="Still under development").pack(
            expand=1
        )

        # add element in change password tab
        ttk.Label(self.change_pass, text="User Name\t").grid(
            row=0, column=0, padx=5, pady=2, sticky="w"
        )
        ttk.Label(self.change_pass, text="Enter Old Password").grid(
            row=1, column=0, padx=5, pady=2, sticky="w"
        )
        ttk.Label(self.change_pass, text="Enter New Password").grid(
            row=2, column=0, padx=5, pady=2, sticky="w"
        )
        ttk.Label(self.change_pass, text="Re-Enter New Password").grid(
            row=3, column=0, padx=5, pady=2, sticky="w"
        )
        self.change_pass_entry = []
        for i in range(4):
            ttk.Label(self.change_pass, text=":").grid(
                row=i, column=1, sticky="w"
            )
            entry = ttk.Entry(self.change_pass, width=25)
            entry.grid(row=i, column=2, padx=2, pady=2, sticky="w")
            self.change_pass_entry.append(entry)
        self.footer_change = ttk.Frame(self.change_pass)
        self.cancel_button_change = ttk.Button(
            self.footer_change,
            text="Cancel",
            command=self.master.master.onManagementClosed,
        )
        self.cancel_button_change.grid(
            row=0, column=2, pady=5, sticky="E", padx=2
        )
        ttk.Button(
            self.footer_change,
            text="Change Password",
            command=self.change_password_user,
        ).grid(row=0, column=0, pady=5, sticky="W", padx=2)
        self.footer_change.grid(row=4, column=0, columnspan=3, sticky="e")

    def getDataEntry(self, name):
        """Get data entry"""
        if name == "register":
            value = []
            for entry in self.register_entry:
                value.append(entry.get())
            return value
        elif name == "change":
            value = []
            for entry in self.change_pass_entry:
                value.append(entry.get())
            return value

    def register_user(self):
        """Add new user"""
        [user, pwd1, pwd2] = self.getDataEntry("register")
        if pwd1 == pwd2:
            if 7 < len(pwd1) < 51:
                # check existing user
                if not self.master.master.dataModel.check_exist_data_login(
                    user
                ):
                    # print('debug button register')
                    self.master.master.dataModel.add_data_user(user, pwd1)
                    messagebox.showinfo(
                        "Success!",
                        f'Your "{user}" data have been saved in Data Base\nYou can login to add or manage your site password',
                    )
                    self.master.master.onManagementClosed()
                else:
                    messagebox.showerror(
                        "Error!", f'User Name "{user}" already exist!'
                    )
            else:
                messagebox.showerror(
                    "Error!", "Password must contain 8 to 50 character!"
                )
        else:
            messagebox.showerror("Error!", "Please Enter Same Password!")

    def change_password_user(self):
        """Change password window"""
        [user, oldPwd, pwd1, pwd2] = self.getDataEntry("change")
        if pwd1 == pwd2:
            if 7 < len(pwd1) < 51:
                # check existing user
                if self.master.master.dataModel.check_exist_data_login(user):
                    oldPwdDB = self.master.master.dataModel.get_password_login(
                        user
                    )
                    if oldPwd == oldPwdDB:
                        # print('debug button register')
                        self.master.master.dataModel.change_password_user(
                            user, pwd1
                        )
                        messagebox.showinfo(
                            "Success!",
                            f'Your "{user}" data have been changed in Data Base\nYou can login to add or manage your site password',
                        )
                        self.master.master.onManagementClosed()
                else:
                    messagebox.showerror(
                        "Error!", f'User Name "{user}" doesn\'t exist!'
                    )
            else:
                messagebox.showerror(
                    "Error!", "Password must contain 8 to 50 character!"
                )
        else:
            messagebox.showerror("Error!", "Please Enter Same Password!")


# Main app
class App(tk.Tk):
    """Main application"""

    def __init__(self):
        super().__init__()

        self.title("Password Manager")
        self.resizable(False, False)
        self.style = ttk.Style(self)
        self.style.theme_use("vista")
        self.dataModel = DataModels.dataModel()
        self.masterAuth = False
        self.whoami = ""
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=3)
        self.grid_rowconfigure(0, weight=1)
        # self.title_label = ttk.Labelframe(self)
        self.title_label_frame = {}
        for name, label in (
            ("login", "Login"),
            ("show", "Show Password"),
            ("delete", "Delete Password"),
            ("change", "Change Password"),
            ("add", "Add Password"),
        ):
            self.title_label_frame[name] = containerLabel(self, label)
        self.container_frame = dict()
        self.container_frame = {
            "login": formManage(self, "login"),
            "add": formManage(self, "add"),
            "show": formManage(self, "show"),
            "delete": formManage(self, "delete"),
            "change": formManage(self, "change"),
        }
        self.container_frame["login"].tkraise()
        self.updateContainer()
        # print(self.container_frame)
        # self.container_Butt_opt['show'].tkraise()

    def showPassword(self):
        """SHow saved password"""
        # print('debug, password appears')
        [site, _] = self.container_frame["show"].getFromEntry()
        # if len(password) < 1 and len(site):
        #     self.container_frame['show'].deleteAll()
        if self.dataModel.check_exist_data(site, self.whoami):
            pwd = self.dataModel.get_password(site, self.whoami)
            self.container_frame["show"].entry_form[1].delete(0, tk.END)
            self.container_frame["show"].entry_form[1].insert(0, pwd)
        else:
            messagebox.showerror(
                "Error!", "Your data doesn't exist, you can add it first"
            )

    def addPassword(self):
        """add new password"""
        [site, pwd1, pwd2] = self.container_frame["add"].getFromEntry()
        # print('debug add password', val)
        # print()
        if pwd1 == pwd2:
            if 7 < len(pwd1) < 50:
                if not self.dataModel.check_exist_data(site, self.whoami):
                    self.dataModel.add_password(site, pwd1, self.whoami)
                    messagebox.showinfo(
                        "Success!", "Your password have been saved!"
                    )
                    self.container_frame["add"].deleteAll()
                else:
                    messagebox.showerror(
                        "Error!",
                        "Your password didn't saved!\nYour password is currently exist in data base!",
                    )
            else:
                messagebox.showerror(
                    "Error!", "Your password must contain 8 up to 50 character!"
                )
        else:
            messagebox.showerror(
                "Error!",
                "Your password didn't same!/nPlease enter the same password!",
            )

    def deletePassword(self):
        """delete exist password"""
        # print('test delete password button')
        [site] = self.container_frame["delete"].getFromEntry()
        if self.dataModel.check_exist_data(site, self.whoami):
            self.dataModel.deletePassword(site, self.whoami)
            messagebox.showinfo(
                "Success!", f"Data {site} password have been deleted!"
            )
            self.container_frame["delete"].deleteAll()
        else:
            messagebox.showerror("Error!", f"Your {site} site doesn't exists!")

    def changePassword(self):
        """change saved password"""
        # print('debug test change password button')
        [site, oldPass, newPass1, newPass2] = self.container_frame[
            "change"
        ].getFromEntry()
        if newPass1 == newPass2:
            if 7 < len(newPass1) < 50:
                # check existing user and password is dealing with it
                if self.dataModel.check_exist_data(site, self.whoami):
                    if oldPass == self.dataModel.get_password(
                        site, self.whoami
                    ):
                        self.dataModel.update_password(
                            self.whoami, site, newPass1
                        )
                        messagebox.showinfo(
                            "Success!", f"Your {site} password updated."
                        )
                        self.container_frame["change"].deleteAll()
                    else:
                        messagebox.showerror(
                            "Error!", "Please enter correct old password!"
                        )
                else:
                    messagebox.showerror(
                        "Error!", "Your site didn't exist in data base"
                    )
            else:
                messagebox.showerror(
                    "Error!", "Password must have 8 to 50 character"
                )
        else:
            messagebox.showerror(
                "Error!", "Please enter the same new Password correctly!"
            )

    def updateContainer(self):
        """update container view from login"""
        if not self.masterAuth:
            container = self.container_frame["login"]
            label = self.title_label_frame["login"]
            label.tkraise()
            container.tkraise()
        elif self.masterAuth:
            container = self.container_frame["show"]
            label = self.title_label_frame["show"]
            label.tkraise()
            container_opt = containerButt_opt(self)
            self.container_frame_opt = container_opt
            container_opt.tkraise()
            container.tkraise()

    def updateContainer2(self):
        """update container"""
        self.grid_rowconfigure(1, weight=2)
        name = self.container_frame_opt.rad_value.get()
        opt = ""
        if name == 0:
            opt = "show"
            self.container_frame[opt].deleteAll()
        elif name == 1:
            opt = "add"
            self.container_frame[opt].deleteAll()
        elif name == 2:
            opt = "change"
            self.container_frame[opt].deleteAll()
        elif name == 3:
            opt = "delete"
            self.container_frame[opt].deleteAll()

        container = self.container_frame[opt]
        label = self.title_label_frame[opt]
        label.tkraise()
        # container.grid_forget()
        # container.grid(row=1, column=0)
        container.tkraise()
        # print('container', container)

    def login(self):
        [user, password] = self.container_frame["login"].getFromEntry()
        if self.dataModel.check_exist_data_login(user):
            pwd = self.dataModel.get_password_login(user)
            # print('db', pwd, 'form', password)
            if pwd == password:
                self.masterAuth = True
                messagebox.showinfo("Information", "You have been Logged in")
                self.whoami = user
                self.updateContainer()
            else:
                messagebox.showerror(
                    "Error!",
                    "Your Password incorrect!\nPlease Enter Correct Password!",
                )
        else:
            messagebox.showerror(
                "Error!",
                "Your username didn't exist or wrong!,\nPlease enter your correct username or contact developer!",
            )

    def register_user(self):
        pass

    def forget_password(self):
        pass

    def launch_management(self):
        # print('Launch management')
        parent = tk.Toplevel(self)
        self.withdraw()
        self.management = managementWindow(parent)
        # management()

    def onManagementClosed(self):
        self.management.master.destroy()
        self.deiconify()


if __name__ == "__main__":
    app = App()
    # formManage(app, 'show')
    # containerFormLogin(app)
    app.mainloop()
