import sqlite3
# Создаем глобальные константы для контроля выбора пользователя.
UC_MIN = 1
UC_MAX = 8
EXIT = 8
class Population: # Данный класс работает с базой данных которую
    # мы предварительно создали для вывода данных которые выбирает пользователь
    # при взаимодействии с меню.
  def __init__(self):
    with sqlite3.connect('cities.db') as self.__conn:
      cur = self.__conn.cursor()
      self.__user_choice = 0

      while self.__user_choice != EXIT: # Создаем цикл который
          # управляется в соответсвии с выбором пользователя.

        self.__show_menu()
        self.__user_choice = int (input('Введите пункт меню: ')) # Здесь создаем
          # атрибут данных который просит пользователя выбрать нужный ему пункт меню.

        if self.__user_choice == 1:
          cur.execute(''' Select * From Cities ORDER BY Population ''')
          results = cur.fetchall()
          self.__show_results(results)

        if self.__user_choice == 2:
          cur.execute(''' Select * From Cities ORDER BY Population DESC ''')
          results = cur.fetchall()
          self.__show_results(results)

        if self.__user_choice == 3:
          cur.execute(''' Select * From Cities ORDER BY CityName ''')
          results = cur.fetchall()
          self.__show_results(results)

        if self.__user_choice == 4:
          cur.execute(''' Select SUM (Population) From Cities ''')
          results = cur.fetchall()
          self.__show_results(results)

        if self.__user_choice == 5:
          cur.execute(''' Select AVG (Population) From Cities ''')
          results = cur.fetchall()
          self.__show_results(results)

        if self.__user_choice == 6:
          cur.execute(''' Select CityID,CityName,MAX (Population) From Cities''')
          results = cur.fetchall()
          self.__show_results(results)

        if self.__user_choice == 7:
          cur.execute(''' Select CityID,CityName,MIN (Population) From Cities''')
          results = cur.fetchall()
          self.__show_results(results)

        if self.__user_choice < UC_MIN or self.__user_choice > UC_MAX:
          print('Введите Пункт Меню от 1 до 8.')
          print()

  def __show_menu(self): # Создаем меню.
    print()
    print('Добро пожаловать в программу "SHOW_CITY_POPULATION V.1.0"')
    print('1. Показать список городов отсортированных по возрастанию населения')
    print('2. Показать список городов отсортированных по убыванию населения')
    print('3. Показать список городов отсортированных по названию')
    print('4. Показать общую численность населения городов ')
    print('5. Показать среднюю численность населения городов')
    print('6. Показать город с наибольшей численностью населения')
    print('7. Показать город с наименьшей численностью населения')
    print('8. Выйти из программы')
    print()

  def __show_results(self,results): # Данный метод выводит нам результаты
      # изьятые из базы данных.

      if len(results[0]) > 1:

        for row in results:
          print(f'{row[0]} {row[1]} {row[2]:,.0f}')

      else:
        for row in results:
          print(f'{row[0]:,.0f} Человек.')

# Создаем точку входа.
if __name__ == '__main__':
  population = Population()