import random
import string
import json
import os
from getpass import getpass

# Список из 500+ самых популярных паролей
COMMON_PASSWORDS = [
    "123456", "password", "123456789", "12345", "12345678", "qwerty", "abc123", "111111",
    "123123", "admin", "letmein", "welcome", "monkey", "dragon", "master", "football",
    "baseball", "login", "shadow", "sunshine", "iloveyou", "princess", "trustno1", "1234567",
    "qwerty123", "1q2w3e4r", "qwertyuiop", "123qwe", "1234", "1234567890", "123321",
    "654321", "987654321", "qwerty12345", "mypassword", "password123", "password1",
    "admin123", "qwerty123", "abc123456", "passw0rd", "password12", "12345qwerty",
    "qwerty123456", "1qaz2wsx", "qwerty12345", "123456789a", "a123456", "11111111",
    "000000", "555555", "666666", "7777777", "88888888", "999999999", "12345678910",
    "superman", "batman", "spiderman", "robert", "jennifer", "amanda", "michael",
    "jordan", "hunter", "thomas", "charlie", "andrew", "daniel", "jessica", "ashley",
    "nicole", "michelle", "samantha", "brittany", "elizabeth", "kimberly", "stephanie",
    "jennifer", "tiffany", "christina", "jasmine", "melissa", "angela", "laura", "lisa",
    "brian", "kevin", "justin", "brandon", "ryan", "jonathan", "nicholas", "anthony",
    "eric", "adam", "kevin", "thomas", "christopher", "jason", "matthew", "john",
    "david", "james", "joseph", "robert", "william", "charles", "richard", "daniel",
    "steven", "timothy", "jeffrey", "george", "mark", "paul", "donald", "kenneth",
    "ronald", "edward", "brian", "jason", "jeff", "jerry", "frank", "scott", "eric",
    "stephen", "larry", "dennis", "raymond", "gregory", "patrick", "peter", "walter",
    "harold", "douglas", "henry", "carl", "arthur", "ryan", "roger", "joe", "juan",
    "jack", "albert", "jonathan", "justin", "terry", "gerald", "keith", "samuel",
    "willie", "ralph", "lawrence", "nicholas", "roy", "benjamin", "bruce", "brandon",
    "adam", "harry", "fred", "wayne", "billy", "steve", "louis", "jeremy", "aaron",
    "randy", "howard", "eugene", "carlos", "russell", "bobby", "victor", "martin",
    "ernest", "phillip", "todd", "jesse", "craig", "alan", "shawn", "clarence", "sean",
    "philip", "chris", "johnny", "earl", "jimmy", "antonio", "danny", "bryan", "tony",
    "luis", "mike", "stanley", "leonard", "nathan", "dale", "manuel", "rodney", "curtis",
    "norman", "allen", "marvin", "vincent", "glenn", "jeffery", "travis", "jeff",
    "chad", "jacob", "lee", "melvin", "alfred", "kyle", "francis", "bradley", "jesus",
    "herbert", "frederick", "ray", "joel", "edwin", "don", "eddie", "ricky", "troy",
    "randall", "barry", "alexander", "bernard", "mario", "leroy", "francisco", "marcus",
    "micheal", "theodore", "clifford", "miguel", "oscar", "jay", "jim", "tom", "calvin",
    "alex", "jon", "ronnie", "bill", "lloyd", "tommy", "leon", "derek", "warren",
    "darrell", "jerome", "floyd", "leo", "alvin", "tim", "wesley", "gordon", "dean",
    "greg", "jorge", "dusty", "pedro", "ian", "rolando", "fabio", "julio", "cesar",
    "hugo", "ruben", "ramon", "felipe", "emilio", "javier", "raul", "enrique", "fernando",
    "pablo", "ignacio", "sergio", "manuel", "andres", "carlos", "mario", "luis", "jose",
    "juan", "francisco", "jesus", "angel", "miguel", "alejandro", "antonio", "jorge",
    "pedro", "david", "daniel", "ricardo", "rafael", "eduardo", "alberto", "roberto",
    "gerardo", "fernando", "arturo", "enrique", "ramiro", "raul", "cristian", "victor",
    "hector", "omar", "saul", "ivan", "jaime", "humberto", "felix", "ruben", "alfredo",
    "julian", "esteban", "diego", "rodrigo", "gabriel", "emiliano", "leonardo", "santiago",
    "mateo", "lucas", "matias", "thiago", "benjamin", "nicolas", "julio", "cesar",
    "martin", "adrian", "pablo", "javier", "andres", "cristopher", "dylan", "ethan",
    "liam", "noah", "oliver", "elijah", "lucas", "logan", "alexander", "henry", "jackson",
    "sebastian", "aiden", "owen", "samuel", "joseph", "john", "david", "wyatt", "matthew",
    "luke", "asher", "carter", "julian", "grayson", "leo", "jayden", "gabriel", "isaac",
    "lincoln", "anthony", "hudson", "ezra", "thomas", "charles", "christopher", "jaxon",
    "mason", "michael", "caleb", "william", "jonah", "oscar", "elias", "colton", "james",
    "andrew", "joshua", "nathan", "nolan", "cameron", "connor", "adrian", "thomas",
    "sophia", "emma", "olivia", "ava", "isabella", "mia", "charlotte", "amelia", "harper",
    "evelyn", "abigail", "emily", "elizabeth", "sofia", "madison", "avery", "ella",
    "scarlett", "grace", "chloe", "victoria", "riley", "aria", "lily", "aubrey", "zoey"
]

# Добавляем еще паролей для достижения 500+
for i in range(50):
    COMMON_PASSWORDS.append(f"password{i}")
    COMMON_PASSWORDS.append(f"pass{i}")
    COMMON_PASSWORDS.append(f"qwerty{i}")
    COMMON_PASSWORDS.append(f"12345{i}")

class PasswordManager:
    def __init__(self, filename="passwords.json"):
        self.filename = filename
        self.accounts = self.load_accounts()
    
    def load_accounts(self):
        """Загрузка аккаунтов из файла"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    return json.load(f)
            except:
                return {}
        return {}
    
    def save_accounts(self):
        """Сохранение аккаунтов в файл"""
        with open(self.filename, 'w') as f:
            json.dump(self.accounts, f, indent=2)
    
    def generate_password(self, length=12):
        """Генерация надежного пароля"""
        if length < 8:
            length = 8
        
        characters = string.ascii_letters + string.digits + "!@#$%^&*"
        password = []
        
        # Гарантируем наличие всех типов символов
        password.append(random.choice(string.ascii_lowercase))
        password.append(random.choice(string.ascii_uppercase))
        password.append(random.choice(string.digits))
        password.append(random.choice("!@#$%^&*"))
        
        # Добавляем остальные символы
        for _ in range(length - 4):
            password.append(random.choice(characters))
        
        # Перемешиваем
        random.shuffle(password)
        return ''.join(password)
    
    def check_password_strength(self, password):
        """Проверка надежности пароля"""
        score = 0
        feedback = []
        
        # Проверка длины
        if len(password) >= 12:
            score += 2
        elif len(password) >= 8:
            score += 1
        else:
            feedback.append("Пароль слишком короткий (минимум 8 символов)")
        
        # Проверка на наличие разных типов символов
        has_lower = any(c.islower() for c in password)
        has_upper = any(c.isupper() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(c in "!@#$%^&*" for c in password)
        
        if has_lower:
            score += 1
        else:
            feedback.append("Добавьте строчные буквы")
        
        if has_upper:
            score += 1
        else:
            feedback.append("Добавьте заглавные буквы")
        
        if has_digit:
            score += 1
        else:
            feedback.append("Добавьте цифры")
        
        if has_special:
            score += 1
        else:
            feedback.append("Добавьте спецсимволы (!@#$%^&*)")
        
        # Проверка на популярность
        if password.lower() in COMMON_PASSWORDS:
            score = 0
            feedback = ["ОПАСНО! Этот пароль в списке самых популярных паролей!"]
        
        # Оценка
        if score <= 2:
            strength = "Очень слабый"
        elif score <= 4:
            strength = "Слабый"
        elif score <= 6:
            strength = "Средний"
        else:
            strength = "Надежный"
        
        return strength, feedback
    
    def add_account(self, service, username, password):
        """Добавление нового аккаунта"""
        if service in self.accounts:
            print(f"\n⚠️  Аккаунт для '{service}' уже существует!")
            overwrite = input("Перезаписать? (y/n): ").lower()
            if overwrite != 'y':
                return False
        
        self.accounts[service] = {
            "username": username,
            "password": password
        }
        self.save_accounts()
        print(f"\n✅ Аккаунт для '{service}' успешно сохранен!")
        return True
    
    def get_account(self, service):
        """Получение данных аккаунта"""
        if service in self.accounts:
            return self.accounts[service]
        return None
    
    def list_accounts(self):
        """Список всех сохраненных сервисов"""
        if not self.accounts:
            print("\n📭 Нет сохраненных аккаунтов")
        else:
            print("\n📋 Сохраненные аккаунты:")
            for i, service in enumerate(self.accounts.keys(), 1):
                print(f"  {i}. {service}")
    
    def delete_account(self, service):
        """Удаление аккаунта"""
        if service in self.accounts:
            del self.accounts[service]
            self.save_accounts()
            print(f"\n🗑️  Аккаунт '{service}' удален!")
            return True
        else:
            print(f"\n❌ Аккаунт '{service}' не найден!")
            return False

def main():
    manager = PasswordManager()
    
    print("=" * 50)
    print("🔐 МЕНЕДЖЕР ПАРОЛЕЙ 🔐")
    print("=" * 50)
    
    while True:
        print("\n📌 Доступные команды:")
        print("  1 - Сгенерировать пароль")
        print("  2 - Проверить надежность пароля")
        print("  3 - Добавить аккаунт")
        print("  4 - Показать все аккаунты")
        print("  5 - Просмотреть данные аккаунта")
        print("  6 - Удалить аккаунт")
        print("  0 - Выход")
        
        choice = input("\n👉 Ваш выбор: ").strip()
        
        if choice == '1':
            try:
                length = int(input("Длина пароля (минимум 8, по умолчанию 12): ") or "12")
                if length < 8:
                    print("⚠️  Длина не может быть меньше 8. Установлено 8.")
                    length = 8
                password = manager.generate_password(length)
                print(f"\n🔑 Сгенерированный пароль: {password}")
                
                # Проверка надежности
                strength, feedback = manager.check_password_strength(password)
                print(f"📊 Надежность: {strength}")
                if feedback and strength != "Очень слабый":
                    for msg in feedback:
                        print(f"   • {msg}")
            except ValueError:
                print("❌ Ошибка: введите число!")
        
        elif choice == '2':
            password = getpass("Введите пароль для проверки: ")
            strength, feedback = manager.check_password_strength(password)
            print(f"\n📊 Надежность пароля: {strength}")
            if feedback:
                for msg in feedback:
                    print(f"   • {msg}")
        
        elif choice == '3':
            print("\n➕ Добавление нового аккаунта:")
            service = input("Название сервиса/сайта: ").strip()
            if not service:
                print("❌ Название не может быть пустым!")
                continue
            
            username = input("Логин/Email: ").strip()
            if not username:
                print("❌ Логин не может быть пустым!")
                continue
            
            print("\nВарианты ввода пароля:")
            print("  1 - Ввести свой пароль")
            print("  2 - Сгенерировать надежный пароль")
            pass_choice = input("Выберите (1/2): ").strip()
            
            if pass_choice == '2':
                try:
                    length = int(input("Длина пароля (минимум 8, по умолчанию 12): ") or "12")
                    if length < 8:
                        length = 8
                    password = manager.generate_password(length)
                    print(f"\n🔑 Сгенерированный пароль: {password}")
                except:
                    password = manager.generate_password(12)
            else:
                password = getpass("Введите пароль: ")
                if not password:
                    print("❌ Пароль не может быть пустым!")
                    continue
            
            # Проверка надежности пароля
            strength, feedback = manager.check_password_strength(password)
            print(f"\n📊 Надежность пароля: {strength}")
            if feedback and strength != "Очень слабый":
                for msg in feedback:
                    print(f"   • {msg}")
            
            if strength == "Очень слабый":
                print("⚠️  ВНИМАНИЕ: Этот пароль небезопасен!")
                proceed = input("Все равно сохранить? (y/n): ").lower()
                if proceed != 'y':
                    continue
            
            manager.add_account(service, username, password)
        
        elif choice == '4':
            manager.list_accounts()
        
        elif choice == '5':
            manager.list_accounts()
            service = input("\nВведите название сервиса: ").strip()
            account = manager.get_account(service)
            if account:
                print(f"\n🔐 Данные аккаунта '{service}':")
                print(f"   Логин: {account['username']}")
                print(f"   Пароль: {account['password']}")
                
                # Проверка надежности сохраненного пароля
                strength, feedback = manager.check_password_strength(account['password'])
                print(f"   Надежность пароля: {strength}")
            else:
                print(f"\n❌ Аккаунт '{service}' не найден!")
        
        elif choice == '6':
            manager.list_accounts()
            service = input("\nВведите название сервиса для удаления: ").strip()
            confirm = input(f"Вы уверены, что хотите удалить '{service}'? (y/n): ").lower()
            if confirm == 'y':
                manager.delete_account(service)
        
        elif choice == '0':
            print("\n👋 До свидания!")
            break
        
        else:
            print("❌ Неверная команда! Попробуйте снова.")

if __name__ == "__main__":
    main()
