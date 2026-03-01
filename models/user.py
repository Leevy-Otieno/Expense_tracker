class User:

    def __init__(self, username, password, role):
        self._username = username
        self._password = password
        self._role = role

    def get_username(self):
        return self._username

    def get_role(self):
        return self._role

    def get_password(self):
        return self._password

    def __str__(self):
        return f"Username: {self._username} | Role: {self._role}"


class Founder(User):
    
    def __init__(self, username, password):
        super().__init__(username, password, role="founder")


class Accountant(User):
    
    def __init__(self, username, password):
        super().__init__(username, password, role="accountant")



class Investor(User):
   
    def __init__(self, username, password):
        super().__init__(username, password, role="investor")