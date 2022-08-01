nested_list1 = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]

nested_list2 = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None],
]
from datetime import datetime

def _logger(path_to_file):

    def logger(some_function):

        def new_function(*args, **kwargs):
            log = []
            f = open(path_to_file, "a", encoding="UTF 8")
            date_and_time = str(datetime.now())
            name_function = str(some_function.__name__)

            result = some_function(*args, **kwargs)

            log.append("дата: " + date_and_time)
            log.append("имя функции: " + name_function)
            log.append("возвращаемое значение: " + str(result))
            log.append("аргументы: " + str(args))

            f.write(str("; ".join(log) + "\n"))

            return result

        return new_function

    return logger

path_to_file = str(input("Введите путь к логам: "))

class FlatIteratoPresent:
    def __init__(self, lst):
        self.lst = sum(lst, [])
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index == len(self.lst):
            raise StopIteration
        else:
            return self.lst[self.index]

@_logger (path_to_file)
def flat_generator_present(my_list):
    for lists in my_list:
        for item in lists:
            yield item

for item in FlatIteratoPresent(nested_list1):
    print(item)
flat_list = [item for item in FlatIteratoPresent(nested_list1)]
print(flat_list)

for item in flat_generator_present(nested_list2):
    print(item)
