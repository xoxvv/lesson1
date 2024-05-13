immutable_var=1,2,3,'age',True
print(immutable_var)
#immutable_var[0]=2  - кортеж относится к неизменяемым типам данных, так как содержит не список данных, а коллекцию данных внутри которой могут быть и элементы в виде списков, которые внтури кортежа можно менять
mutable_list= ["false",2,3,4,"apple"]
mutable_list.append('Koks')
print(mutable_list)