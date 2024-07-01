class User:
    users = {}

    def __init__(self, telegram_id):
        self.telegram_id = telegram_id
        self.tokens = 0

    @classmethod
    def get_or_create(cls, telegram_id):
        if telegram_id not in cls.users:
            cls.users[telegram_id] = cls(telegram_id)
        return cls.users[telegram_id]

    @classmethod
    def get(cls, telegram_id):
        return cls.users.get(telegram_id)

    def save(self):
        User.users[self.telegram_id] = self
