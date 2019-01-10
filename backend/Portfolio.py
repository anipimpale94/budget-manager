from datetime import datetime

class Portfolio(object):
    id = 0
    subject = ""
    estimate = 0.0
    user_id = 0
    create_date = datetime.now
    modify_date = datetime.now

    def __init__(self, id, user_id, subject, estimate):
        self.id = id
        self.user_id = user_id
        self.subject = subject
        self.estimate = estimate
        create_date = datetime.now
        modify_date = datetime.now
