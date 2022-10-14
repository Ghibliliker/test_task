from collections import deque


def check_relation(net, first, second):

    def add_new(net, first):
        result = []
        for item in net:
            if first in item:
                for name in item:
                    if name != first:
                        result.append(name)
        return result

    search_queue = deque()
    search_queue += add_new(net, first)
    searched = []

    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person == second:
                return True
            else:
                search_queue += add_new(net, person)
                searched.append(person)
    return False


if __name__ == '__main__':

    net = (
    ("Ваня", "Лёша"), ("Лёша", "Катя"),
    ("Ваня", "Катя"), ("Вова", "Катя"),
    ("Лёша", "Лена"), ("Оля", "Петя"),
    ("Стёпа", "Оля"), ("Оля", "Настя"),
    ("Настя", "Дима"), ("Дима", "Маша")
    )

    assert check_relation(net, "Петя", "Стёпа") is True
    assert check_relation(net, "Маша", "Петя") is True
    assert check_relation(net, "Ваня", "Дима") is False
    assert check_relation(net, "Лёша", "Настя") is False
    assert check_relation(net, "Стёпа", "Маша") is True
    assert check_relation(net, "Лена", "Маша") is False
    assert check_relation(net, "Вова", "Лена") is True
    print('OK')
