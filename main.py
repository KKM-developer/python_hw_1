"""
Написать программу для работы пользователя со списком.

Пользовательский интерфейс должен представлять из себя консольное меню из четырех пунктов:

1 - Демонстрация списка

2 - Добавление элемента в конец списка

3 - Удаление последнего элемента из списка

4 - Выход

Программа ожидает ввод от пользователя числа от 1 до 4 для перехода к соответствующему действию.
Реагировать на ввод любых других чисел программа не должна. При переходе к каждому из действий пункты
меню стираются. Изначально список пуст.

К вышеописанному ТЗ добавить пункт меню, осуществляющий сортировку массива, а также добавить ко 2 и 3
пунктам возможность добавлять(удалять) элемент по индексу, отдельно запрашиваемому у пользователя в соотв. подменю.
"""
from typing import List, Any

from myFunk import *

if __name__ == '__main__':
    userList: list[Any] = []
    while True:
        userInsert: int = showMenu()
        if userInsert == 1: showList(userList)
        if userInsert == 2: addItem(userList)
        if userInsert == 3: delItem(userList)
        if userInsert == 4: break