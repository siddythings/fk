# Define a class for storing user information
class User:
    def __init__(self, name, profession):
        self.name = name
        self.profession = profession
        self.subscriptions = []
        self.questions = []
        self.answers = []
        self.logged_in = True


# Define a class for storing question information
class Question:
    def __init__(self, text, topics, user):
        self.text = text
        self.topics = topics
        self.user = user
        self.answers = []
        self.commnet = []


# Define a class for storing answer information
class Answer:
    def __init__(self, text, user, question):
        self.text = text
        self.user = user
        self.question = question
        self.accepted = False
        self.upvote = 0
        self.commnet = []


# Define a class for storing comment information
class Comment:
    def __init__(self, text, user, question_or_answer):
        self.text = text
        self.user = user
        self.question_or_answer = question_or_answer


# Define a dictionary to store all users
users = {}
user_name = ""
# Define a dictionary to store all questions
questions = {}

# Define a function for creating a new user
def user_signup(name, profession):
    global user_name
    user_name = name
    user = User(name, profession)
    users[user_name] = user


# Define a function for login into profile
def login(name):
    global user_name
    user_name = name
    user = users[user_name]
    return user


# Define a function for display to profile
def show_profile(name):
    return users[name]


# Define a function for logging a user out
def logout():
    global user_name
    users[user_name].logged_in = False


# Define a function for subscribing a user to one or more topics
def subscribe(*topics):
    for topic in topics:
        users[user_name].subscriptions.append(topic)


# Define a function for UNsubscribing a user to one or more topics
def unsubscribe(*topics):
    for topic in topics:
        try:
            topic_index = users[user_name].subscriptions.index(topic)
            users[user_name].subscriptions.pop(topic_index)
        except:
            pass


# Define a function for adding a new question
def add_questions(text, topic):
    global user_name
    user = users[user_name]
    if not user.logged_in:
        raise Exception("Login First")
    question = Question(text, topic, user)
    questions[text] = question
    users[user_name].questions.append(question)


# Define a function for showing the details of a single question
def show_question(text):
    return questions[text]


topic = ["java", "python"]
question = ["java", "jdk"]

["java"]

# Define a function for showing the user's feed
def show_feed(topics=None, answered=None):
    # Create a list of questions to show

    user = users[user_name]

    show_questions = []
    for question in user.questions:
        if (
            topics
            and answered
            and list(set(topics) & set(question.topics))
            and question.answers
        ):
            show_questions.append(question)

        if topics and list(set(topics) & set(question.topics)):
            show_questions.append(question)

        if answered and question.answers:
            show_questions.append(question)

        if not topics and not answered:
            show_questions.append(question)

    # return show_questions
    print(
        [
            {
                "question": obj.text,
                "topics": obj.topics,
                user_name: obj.user.name,
                "answered": obj.answers,
            }
            for obj in show_questions
        ]
    )


# Define a function for answering a question
def answer_question(text, answer):
    global user_name
    user = users[user_name]

    if not user.logged_in:
        raise Exception("Login First")

    question = questions[text]
    answer = Answer(answer, user, question)
    question.answers.append(answer)


def upvote_answer(text, answer):
    question = questions[text]
    for answer in question.answers:
        if answer.text == answer.text:
            answer.upvote = answer.upvote + 1


# Define a function for accepting an answer to a question
def accept_answer(text, answer):
    question = questions[text]
    for answer in question.answers:
        if answer.text == answer.text:
            answer.accepted = True


user_signup("Sachin", "Developer")  # name, Developer
subscribe("jdk", "java")  # list of topics to subscribe
add_questions("What are new open source jdks?", topic=["java", "jdk"])
add_questions("Does Hadoop work on JDK 11?", topic=["hadoop", "jdk"])
# show_feed()
# show_feed(topics=["java"])  # only shows 1st question
# show_feed(topics=["jdk"])  # shows both questions
# show_feed(answered=True)  # shows no question as no one has answer
# logout()

# user_signup("Kalyan", "Developer")
# subscribe("apache", "hadoop")
show_feed()  # shows 2 questions added by Sachin
# add_questions(
#     "Does Apache Spark support streaming of data from hdfs?", topic=["apache", "hadoop"]
# )
answer_question(
    "Does Hadoop work on JDK 11?", answer="Yeah Hadoop 3 and above supports it."
)  # shows 3 questions
# logout()

# user_signup("Lokesh", "Developer")
# subscribe("apache", "hadoop", "java")
# show_feed()
# show_question("Does Hadoop work on JDK 11?")  # show the question with 1 response
accept_answer(
    "Does Hadoop work on JDK 11?", answer="Yeah Hadoop 3 and above supports it."
)  #
# login("Sachin")

upvote_answer(
    "Does Hadoop work on JDK 11?", answer="Yeah Hadoop 3 and above supports it."
)
upvote_answer(
    "Does Hadoop work on JDK 11?", answer="Yeah Hadoop 3 and above supports it."
)
# # show_feed(answered=True)
# print(
#     [
#         (obj.upvote, obj.text)
#         for obj in show_question("Does Hadoop work on JDK 11?").answers
#     ]
# )  # show the question with 1 response
# logout()

# login("Sachin")
# show_feed()
# show_profile("Kalyan")
# show_question("Does Hadoop work on JDK 11?")
# accept_answer(
#     "Does Hadoop work on JDK 11?", answer="Yeah Hadoop 3 and above supports it."
# )
# show_profile("Kalyan")
# show_feed(answered=True)
# logout()

# unsubscribe("java")
show_feed(topics=["java"])
print(show_profile("Sachin").subscriptions)
