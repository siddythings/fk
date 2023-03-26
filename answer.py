# Define a class for storing answer information
class Answer:
    def __init__(self, text, user, question):
        self.text = text
        self.user = user
        self.question = question
        self.accepted = False
        self.upvote = 0
        self.commnet = []
