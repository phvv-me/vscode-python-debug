
def define_best_name(name1, name2):
    length1 = len(name1)
    length2 = len(name2)

    print(length1, length2)

    if length1 > length2:
        return name1
    return name2


my_name = "Tom Thompsom"
your_name = "Lauretius Maximus"
the_best_name = define_best_name(my_name, your_name)

print(the_best_name)


def updated_define_best_name(name1: str, name2: str):
    if len(name1) > len(name2):
        return name1
    return name2
