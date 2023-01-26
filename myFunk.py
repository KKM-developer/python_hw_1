def showMenu() -> int:
    """
Запрос на выбор пункта меню
    :return: Пункт меню
    :rtype: int
    """
    print(f'1 - Демонстрация списка\n2 - Добавление элемента в список'
          f'\n3 - Удаление элемента из списка\n4 - Выход')
    userInput: int = int(input())
    return userInput


def showList(userList: list) -> list:
    """
Демонстрация списка
    :rtype: None
    :type userList: list
    """
    print(userList)


def addItem(userList: list) -> None:
    """
Добавление элемента в список
    :rtype: None
    :param userList: list
    :return: обновленный список
    """
    listIndex: int = int(input('Укажите индекс добавляемого элемента: '))
    userItem: str = input('Элемент: ')
    return userList.insert(listIndex, userItem)


def delItem(userList: list) -> list:
    """
Удаление элемента из списка
    :rtype: list
    :return: обновленный список
    :type userList: list
    """
    listIndex = int(input('Укажите индекс удаляемого элемента: '))
    del userList[listIndex]
    return userList

