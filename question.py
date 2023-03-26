# Define a class for storing question information
class Question:
    def __init__(self, text, topics, user):
        self.text = text
        self.topics = topics
        self.user = user
        self.answers = []
        self.commnet = []
