from datetime import datetime

class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.created_at = datetime.now()

class Chat:
    def __init__(self, chat_id, name):
        self.id = chat_id
        self.name = name
        self.users = []
        self.created_at = datetime.now()

    def add_user(self, user):
        self.users.append(user)

class Message:
    def __init__(self, message_id, chat, author, text):
        self.id = message_id
        self.chat = chat
        self.author = author
        self.text = text
        self.created_at = datetime.now()

class ChatServer:
    def __init__(self):
        self.users = []
        self.chats = []
        self.messages = []

    def add_user(self, username):
        user_id = len(self.users) + 1
        user = User(user_id, username)
        self.users.append(user)
        return user_id

    def create_chat(self, chat_name, user_ids):
        chat_id = len(self.chats) + 1
        chat = Chat(chat_id, chat_name)
        for user_id in user_ids:
            user = self.get_user_by_id(user_id)
            if user:
                chat.add_user(user)
        self.chats.append(chat)
        return chat_id

    def send_message(self, user_id, chat_id, text):
        user = self.get_user_by_id(user_id)
        chat = self.get_chat_by_id(chat_id)
        if user and chat:
            message_id = len(self.messages) + 1
            message = Message(message_id, chat, user, text)
            self.messages.append(message)
            return message_id

    def get_user_by_id(self, user_id):
        for user in self.users:
            if user.id == user_id:
                return user
        return None

    def get_chat_by_id(self, chat_id):
        for chat in self.chats:
            if chat.id == chat_id:
                return chat
        return None

    def get_user_chats(self, user_id):
        user_chats = []
        for chat in self.chats:
            if any(user.id == user_id for user in chat.users):
                user_chats.append(chat)
        sorted_chats = sorted(user_chats, key=lambda c: c.created_at, reverse=True)
        return sorted_chats

    def get_chat_messages(self, chat_id):
        chat_messages = []
        for message in self.messages:
            if message.chat.id == chat_id:
                chat_messages.append(message)
        sorted_messages = sorted(chat_messages, key=lambda m: m.created_at)
        return sorted_messages

chat_server = ChatServer()

user1_id = chat_server.add_user("Маша")
user2_id = chat_server.add_user("Петя")
user3_id = chat_server.add_user("Саша")
user4_id = chat_server.add_user("Вася")

chat_id = chat_server.create_chat("Chat 1", [user1_id, user2_id, user3_id, user4_id])

messages = [
    "Привет, как дела?",
    "Что делали сегодня?",
    "Есть планы на выходные?",
    "Какая погода у вас?"
]

for message_text in messages:
    message_id = chat_server.send_message(user1_id, chat_id, message_text)
    reply_text = "Привет, готовился к сессии!"
    chat_server.send_message(user2_id, chat_id, reply_text, in_reply_to=message_id)

chat_messages = chat_server.get_chat_messages(chat_id)
for message in chat_messages:
    print("Message: {}, Created At: {}".format(message.text, message.created_at))


