class UserManager:
    def __init__(self):
        self.users = {}
        self.next_id = 1

    # addUser добавляет пользователя с заданным именем.
    # Пользователю присваивается уникальный идентификатор.
    # Возвращает идентификатор добавленного пользователя.
    def addUser(self, name):
        user_id = self.next_id
        self.users[user_id] = name
        self.next_id += 1
        return user_id

    # getUser возвращает имя пользователя по его идентификатору.
    # Если пользователь с таким идентификатором не найден, возвращает null.
    def getUser(self, user_id):
        return self.users.get(user_id, None)

    # deleteUser удаляет пользователя по его идентификатору.
    # Возвращает true, если пользователь был успешно удален,
    # и false, если пользователь с таким идентификатором не найден.
    def deleteUser(self, user_id):
        if user_id in self.users:
            del self.users[user_id]
            return True
        return False

    # findUseryName возвращает список идентификаторов пользователей с данным именем.
    # Если таких пользователей нет, возвращает пустой список.
    def findUserByName(self, name):
        return [user_id for user_id, user_name in self.users.items() if user_name == name]

def main():
    manager = UserManager()
    while True:
        print("\n1. Добавить пользователя")
        print("2. Найти пользователя по ID")
        print("3. Удалить пользователя по ID")
        print("4. Найти пользователя по имени")
        print("5. Выйти")

        choice = input("Выберите опцию: ")
        if choice == '1':
            name = input("Введите имя нового пользователя: ")
            user_id = manager.addUser(name)
            print(f"Пользователь добавлен с ID: {user_id}")
        elif choice == '2':
            try:
                user_id = int(input("Введите ID пользователя для поиска: "))
                user = manager.getUser(user_id)
                if user:
                    print(f"Имя пользователя с ID {user_id}: {user}")
                else:
                    print(f"Пользователь не найден: {user}")
            except ValueError:
                print("Пожалуйста, введите правильный ID")
        elif choice == '3':
            try:
                user_id = int(input("Введите ID пользователя для удаления: "))
                user = manager.getUser(user_id)
                if manager.deleteUser(user_id):
                    print(f"Пользователь {user} успешно удален")
                else:
                    print(f"Пользователь {user} не найден")
            except ValueError:
                print("Пожалуйста, введите правильный ID")
        elif choice == '4':
            name = input("Введите имя пользователя для поиска: ")
            user_ids = manager.findUserByName(name)
            if user_ids:
                print(f"Пользователи с именем {name} - {user_ids}")
            else:
                print(f"Пользователи с таким именем не найдены: {name} - {user_ids}")
        elif choice == '5':
            print("Выход из программы")
            break
        else:
            print("Неверный выбор, попробуйте снова")

if __name__ == "__main__":
    main()
