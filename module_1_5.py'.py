immutable_var=(1,2,3,4,5, "я иду искать" , True)
print(immutable_var)
#immutable_var=[0]# выдает ошибку, т.к кортежи не изменяемы
mutable_list =[1,2,3,4,5, "я иду искать" , True]
print(mutable_list)
mutable_list[0]=10
print(mutable_list)


