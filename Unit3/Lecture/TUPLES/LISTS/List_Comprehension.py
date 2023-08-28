list1 = [i for i in range(15) if i % 2 == 0]
#print(list1)
list2 = [e for e in range(20) if e < 8]
#print(list2)
list3 = [i * 3 for i in range(15) if i % 2 == 0]
#print(list3)
names_dict = {"Nora": 56, "Lulu": 15, "Gino": 31}
odd_values = [value for value in names_dict.values() if value % 2 != 0]
#print(odd_values)
grades = {"Nora": 90, "Lulu": 15, "Gino": 60}
double_grades = {key: value * 2 for (key, value) in grades.items()}
#print(double_grades)
age = {"Peter": 17, "Izabela": 8, "Sofija": 35, "Filip": 25, "Nusa": 30}
new_age = {key: value *3 for (key, value) in age.items() if value % 2 == 0}
print(new_age)
