from datetime import datetime

def _logger(path_to_file):

    def logger(some_function):

        def new_function(*args, **kwargs):
            log = []
            f = open(path_to_file, "a", encoding="UTF 8")
            date_and_time = str(datetime.now())
            name_function = str(some_function.__name__)

            result = some_function(*args, **kwargs)
            result = str(result)

            log.append("дата: " + date_and_time)
            log.append("имя функции: " + name_function)
            log.append("возвращаемое значение: " + result)
            log.append("аргументы: " + str(args))

            f.write(str("; ".join(log) + "\n"))

            return result

        return new_function

    return logger

path_to_file = str(input("Введите путь к логам: "))
@_logger (path_to_file)
def old_function(a, b):
    print("Я создал функцию, которая считает сумму")
    return a + b

old_function(8, 9)