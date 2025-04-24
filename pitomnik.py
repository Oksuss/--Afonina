class Animal:
    def __init__(self, name):
        self.name = name

    def show_commands(self):
        print(f"{self.name}: {', '.join(self.commands)}")

    def learn_command(self, command):
        if command not in self.commands:
            self.commands.append(command)
            print(f'{self.name} успешно научился команде "{command}"!')
        else:
            print(f'{self.name} уже знает команду "{command}".')

class Dog(Animal):
    commands = ["сидеть", "лежать", "дай лапку"]
    
    def __init__(self, name):
        super().__init__(name)

class Cat(Animal):
    commands = ["принести игрушку"]  
    
    def __init__(self, name):
        super().__init__(name)

# Основной класс-реестр всех животных
class Registry:
    def __init__(self):
        self.animals = []
        
    # Добавление нового животного в реестр
    def add_animal(self, animal_type, name):
        if animal_type.lower() == 'собака':
            new_animal = Dog(name)
        elif animal_type.lower() == 'кошка':
            new_animal = Cat(name)
        else:
            raise ValueError("Такой вид животного не поддерживается.")
            
        self.animals.append(new_animal)
        print(f'Животное {animal_type}, {name}, зарегистрировано.')

    # Просмотреть список зарегистрированных животных
    def list_animals(self):
        for i, animal in enumerate(self.animals):
            print(f"{i+1}. {type(animal).__name__}: {animal.name}")

    # Показать доступные команды конкретного животного
    def show_commands(self, index):
        try:
            animal = self.animals[index]
            animal.show_commands()
        except IndexError:
            print('Нет такого животного в реестре.')

    # Обучить выбранное животное новой команде
    def teach_command(self, index, command):
        try:
            animal = self.animals[index]
            animal.learn_command(command)
        except IndexError:
            print('Нет такого животного в реестре.')

def main():
    registry = Registry()
    while True:
        print("\nМеню:")
        print("1. Зарегистрировать новое животное")
        print("2. Посмотреть список зарегистрированных животных")
        print("3. Узнать известные команды животного")
        print("4. Научить животное новой команде")
        print("5. Выход")
        
        choice = input("Выберите пункт меню: ")
        
        if choice == '1':
            type_name = input("Вид животного (Собака / Кошка): ").strip().lower()
            name = input("Имя животного: ").strip()
            registry.add_animal(type_name, name)
        elif choice == '2':
            registry.list_animals()
        elif choice == '3':
            idx = int(input("Укажите номер животного: "))
            registry.show_commands(idx-1)
        elif choice == '4':
            idx = int(input("Укажите номер животного: "))
            cmd = input("Введите новую команду: ").strip()
            registry.teach_command(idx-1, cmd)
        elif choice == '5':
            break
        else:
            print("Неверный выбор пункта меню!")

if __name__ == "_main_":
    main()