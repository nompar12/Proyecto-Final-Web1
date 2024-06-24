salary = int(input("Ingrese el salario: "))
transport_aid = 160200

flag1 =1300000
flag2 = 2600000

if salary >= flag1 and salary < flag2:

   salary += transport_aid
   
   print(salary)

else:
  print(salary)