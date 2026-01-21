#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """Divides element by element two lists safely"""
    result = []
    for i in range(list_length):
        try:
            val1 = my_list_1[i]
            val2 = my_list_2[i]
            try:
                res = val1 / val2
            except ZeroDivisionError:
                print("division by 0")
                res = 0
            except TypeError:
                print("wrong type")
                res = 0
        except IndexError:
            print("out of range")
            res = 0
        finally:
            result.append(res)
    return result
