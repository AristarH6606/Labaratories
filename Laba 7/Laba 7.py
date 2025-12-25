class Employee:
    def __init__(self, name: str, id: int):
        self.name = name
        self.__id = id

    def get_info(self) -> str:
        return f'Сотрудник: {self.name}, ID: {self.__id}'

    def __str__(self):
        return self.get_info()

    def get_id(self):
        return self.__id


class Manager(Employee):
    def __init__(self, name: str, id: int, department: str):
        Employee.__init__(self, name, id)
        self.department = department
        self.team = []

    def manager_project(self, project_name: str) -> str:
        return f"Менеджер {self.name} управляет проектом {project_name} в отделе {self.department}"

    def get_info(self):
        return (f'{super().get_info()}, Должность: менеджер,'
                f'Отдел: {self.department}')

    def add_employee(self, employee: Employee):
        self.team.append(employee)
        return f"Сотрудник {employee.name} добавлен в команду"

    def get_team_info(self) -> list:
        return [emp.get_info() for emp in self.team]

    def get_team_detail(self) -> str:
        if not self.team:
            return 'В команде нет сотрудников'
        team_info = '\n'.join([f'- {emp.get_info()}' for emp in self.team])
        return f'Команда менеджера {self.name}: \n{team_info}'


class Technician(Employee):
    def __init__(self, name: str, id: int, specialization: str):
        super().__init__(name, id)
        self.specialization = specialization

    def perform_maintenance(self) -> str:
        return f"Техник {self.name} выполняет обслуживание в области {self.specialization}"

    def get_info(self) -> str:
        return (f"{super().get_info()}, Должность: Техник,"
                f"Специализация:{self.specialization}")


class TechManager(Manager, Technician):
    def __init__(self, name: str, id: int, department: str, specialization: str):
        Manager.__init__(self, name, id, department)
        Technician.__init__(self, name, id, specialization)

    def get_info(self) -> str:
        base_info = Manager.get_info(self)
        return f'{base_info}, Специализация {self.specialization}'

    def __str__(self):
        return f"Техменеджер: {self.get_info()}"


class EmployeeSystem:
    def __init__(self):
        self.employees = []
        self.managers = []
        self.technicians = []
        self.techmanagers = []

    def input_employee(self):
        print('Добавление обычного сотрудника')
        name = input('Введите имя сотрудника:')
        while True:
            try:
                emp_id = int(input('Введите ID сотрудника: '))
                break
            except (ValueError):
                print('Ошибка: ID должно быть числом. Попробуйте ещё раз')
                continue

        employee = Employee(name, emp_id)
        self.employees.append(employee)
        print(f'Сотрудник {name} успешно добавлен')
        return employee

    def input_manager(self):
        print("Добавление менеджера")
        name = input("Введите имя менеджера:")
        while True:
            try:
                emp_id = int(input('Введите ID сотрудника:'))
                break
            except (ValueError):
                print("Ошибка: ID должно быть числом. Попробуйте ещё раз")
                continue

        department = input('Введите отдел менеджера:')
        manager = Manager(name, emp_id, department)
        self.employees.append(manager)
        self.managers.append(manager)
        print(f'Менеджер {name} успешно добавлен')
        return manager

    def input_technician(self):
        print('Добавление техника')
        name = input('Введите имя техника: ')
        while True:
            try:
                emp_id = int(input('Введите ID техника: '))
                break
            except (ValueError):
                print("Ошибка: ID = число")
                continue
        specialization = input('Введите специализацию техника: ')
        technician = Technician(name, emp_id, specialization)
        self.employees.append(technician)
        self.technicians.append(technician)
        print(f'Техник{name} успешно добавлен')
        return technician

    def input_techmanager(self):
        print("Добавление технического менеджера")
        name = input('Введите имя технического менеджера: ')
        while True:
            try:
                emp_id = int(input("Введите ID технического менеджера: "))
                break
            except (ValueError):
                print("Ошибка: ID должно быть числом. Попробуйте ещё раз")
                continue

        department = input("Введите отдел: ")
        specialization = input("Введите специализацию: ")
        techmanager = TechManager(name, emp_id, department, specialization)
        self.employees.append(techmanager)
        self.techmanagers.append(techmanager)
        print(f"Технический менеджер {name} успешно добавлен")
        return techmanager

    def add_employee_to_manager(self):
        print("Добавление сотрудника в команду менеджера")
        if not self.managers:
            print("Нет свободных менеджеров")
            return

        if not self.employees:
            print("Нет свободных сотрудников")
            return

        print("Выбор менеджера")
        for i, manager in enumerate(self.managers, 1):
            print(f'{i}. {manager.name} (ID: {manager.get_id()})')

        try:
            mgr_choice = int(input('Выбери номер менеджера: ')) - 1
            selected_manager = self.managers[mgr_choice]
        except (ValueError, IndexError):
            print("Неверный выбор")
            return

        print("Выбор сотрудника для добавления в команду")
        available_employees = [emp for emp in self.employees if emp != selected_manager]
        for i, emp in enumerate(available_employees, 1):
            print(f'{i}. {emp.get_info()}')

        try:
            emp_choice = int(input("Введите номер сотрудника: ")) - 1
            selected_employee = available_employees[emp_choice]
        except (ValueError, IndexError):
            print('Неверный выбор')
            return

        result = selected_manager.add_employee(selected_employee)
        print(f'{result}')

    def show_all_employees(self):
        """ПОКАЗАТЬ ВСЕХ СОТРУДНИКОВ"""
        print("Все сотрудники")
        if not self.employees:
            print("нет сотрудников")
            return

        for i, employee in enumerate(self.employees, 1):
            print(f'{i}. {employee.get_info()}')

    def show_team_info(self):
        """"ПОКАЗАТЬ ИНФОРМАЦИЮ О КОМАНДАХ МЕНЕДЖЕРОВ"""
        if not self.managers:
            print("Нету менеджеров")
            return

        print("Информация о командах")
        for manager in self.managers:
            print(manager.get_team_detail())
            print('-' * 30)


    def main_menu(self):
        """Главное меню"""
        while True:
            print("\n" + "=" * 30)
            print("СИСТЕМА УПРАВЛЕНИЯ СОТРУДНИКАМИ")
            print("=" * 30)
            print("1. Добавить обычного сотрудника")
            print("2. Добавить менеджера")
            print("3. Добавить техника")
            print("4. Добавить технического менеджера")
            print("5. Добавить сотрудника в команду менеджера")
            print("6. Показать всех сотрудников")
            print("7. Показать информацию о командах")
            print("8. Выполнить действия для сотрудника")
            print("9. Выход")

            choice = input("\nВыберите действие (1-9): ")

            if choice == '1':
                self.input_employee()
            elif choice == '2':
                self.input_manager()
            elif choice == '3':
                self.input_technician()
            elif choice == '4':
                self.input_techmanager()
            elif choice == '5':
                self.add_employee_to_manager()
            elif choice == '6':
                self.show_all_employees()
            elif choice == '7':
                self.show_team_info()
            elif choice == '8':
                self.perform_actions()
            elif choice == '9':
                print("Выход из программы...")
                break
            else:
                print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    system = EmployeeSystem()
    system.main_menu()