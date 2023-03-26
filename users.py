# Define a class for storing user information
class User:
    def __init__(self, name, profession):
        self.name = name
        self.profession = profession
        self.subscriptions = []
        self.questions = []
        self.answers = []
        self.logged_in = True
