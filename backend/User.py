class User(object):
    id = ""
    name = ""
    email = ""
    password = ""

    # The class "constructor" - It's actually an initializer 
    def __init__(self, id, name, email, password):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
