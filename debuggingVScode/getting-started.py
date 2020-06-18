
def define_best_name(name1, name2):
    if len(name1) > len(name2):
        return name1
    return name2

my_name = "Tom Thompsom"
your_name = "Lauretius Maximus"

the_best_name = define_best_name(my_name, your_name)