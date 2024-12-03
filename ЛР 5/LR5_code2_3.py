from pymongo import MongoClient

class MongoDBConnectionContextManager:
    def __init__(self, host='localhost', port=27017, username='admin', password='admin'):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.connection = None

    def __enter__(self):
        self.connection = MongoClient(
            self.host, self.port,
            username=self.username, password=self.password,
            authSource='myshinynewdb',  # Укажите правильную базу данных для аутентификации
            authMechanism='SCRAM-SHA-1'
        )
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.close()

def main():
    mongo = MongoDBConnectionContextManager(host='some-mongo', port=27017, username='myUserAdmin', password='abc123')
    try:
        with mongo as mongo_connection_context:
            collection = mongo_connection_context.connection['myshinynewdb']['user']

            # Находим запись
            user = collection.find({'age': 205})
            user_record = next(user, None)  # Используем None по умолчанию
            if user_record:
                print(user_record)
            else:
                print("Запись не найдена.")
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == '__main__':
    main()

