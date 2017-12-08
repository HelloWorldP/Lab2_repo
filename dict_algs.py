ivan = {
    "name": "Ivan",
    "age": 28,
    "children": [{
        "name": "Andrey",
        "age": 12,
    }, {
        "name": "Alina",
        "age": 10,
    }],
}
darja = {
    "name": "Darja",
    "age": 35,
    "children": [{
        "name": "Olya",
        "age": 19,
    }, {
        "name": "Pavel",
        "age": 7,
    }],
}
emps = [ivan, darja]
for n in emps:
    for n1 in n["children"]:
        if n1["age"]>18:
            print ("4.Имена сотрудников, у которых дети старше 18 ->", n["name"])