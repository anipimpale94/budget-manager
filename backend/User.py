from datetime import datetime

class User(object):
    id = 0
    name = ""
    email = ""
    password = ""
    create_date = datetime.now

    def __init__(self, id, name, email, password):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        create_date = datetime.now
