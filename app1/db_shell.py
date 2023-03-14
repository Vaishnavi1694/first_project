# exec(open(r'D:\Python\Code File\B8_Django\first_project\app1\db_shell.py').read())

# from app1.models import Person
# from django.contrib.auth.models import User
# print(Person.objects.filter(name__contains= "p"))
# output
# <QuerySet [<Person: p1 --pune>, <Person: p3 --mumbai>, <Person: p5 --nashik>, <Person: p6 --Kolhapur>, <Person: p7 --Baramati>, <Person: Pinky --Goa>, <Person: Pinu --Surat>]>

# data = Person.objects.all().values()
# print(data)
# for i in data:
#     print(i)
# output
# <QuerySet [{'id': 1, 'name': 'p1', 'age': 20, 'mobile_num': 8954756214, 'address': 'pune'}, {'id': 4, 'name': 'p3', 'age': 24, 'mobile_num': 9854127777, 'address': 'mumbai'}, {'id': 6, 'name': 'p5', 'age': 26, 'mobile_num': 8456321789, 'address': 'nashik'}, {'id': 7, 'name': 'p6', 'age': 28, 'mobile_num': 9876542584, 'address': 'Kolhapur'}, {'id': 9, 'name': 'p7', 'age': 25, 'mobile_num': 9685475325, 'address': 'Baramati'}, {'id': 10, 'name': 'vaishnavi', 'age': 23, 'mobile_num': 9458467825, 'address': 'Gujrat'}, {'id': 11, 'name': 'Kau', 'age': 21, 'mobile_num': 9458456785, 'address': 'Kerla'}, {'id': 12, 'name': 'Pinky', 'age': 19, 'mobile_num': 9864467286, 'address': 'Goa'}, {'id': 13, 'name': 'Pinu', 'age': 17, 'mobile_num': 9869877582, 'address': 'Surat'}, {'id': 14, 'name': 'Reyu', 'age': 16, 'mobile_num': 8954987785, 'address': 'Karnataka'}, {'id': 15, 'name': 'mau', 'age': 30, 'mobile_num': 9960199875, 'address': 'Nagar'}]>
# {'id': 1, 'name': 'p1', 'age': 20, 'mobile_num': 8954756214, 'address': 'pune'}
# {'id': 4, 'name': 'p3', 'age': 24, 'mobile_num': 9854127777, 'address': 'mumbai'}
# {'id': 6, 'name': 'p5', 'age': 26, 'mobile_num': 8456321789, 'address': 'nashik'}
# {'id': 7, 'name': 'p6', 'age': 28, 'mobile_num': 9876542584, 'address': 'Kolhapur'}
# {'id': 9, 'name': 'p7', 'age': 25, 'mobile_num': 9685475325, 'address': 'Baramati'}
# {'id': 10, 'name': 'vaishnavi', 'age': 23, 'mobile_num': 9458467825, 'address': 'Gujrat'}
# {'id': 11, 'name': 'Kau', 'age': 21, 'mobile_num': 9458456785, 'address': 'Kerla'}
# {'id': 12, 'name': 'Pinky', 'age': 19, 'mobile_num': 9864467286, 'address': 'Goa'}
# {'id': 13, 'name': 'Pinu', 'age': 17, 'mobile_num': 9869877582, 'address': 'Surat'}
# {'id': 14, 'name': 'Reyu', 'age': 16, 'mobile_num': 8954987785, 'address': 'Karnataka'}
# {'id': 15, 'name': 'mau', 'age': 30, 'mobile_num': 9960199875, 'address': 'Nagar'}

# data = Person.objects.all().values("name")
# lst = []
# for i in data:
#     lst.append(i["name"])
# print(lst)
# output
# ['p1', 'p3', 'p5', 'p6', 'p7', 'vaishnavi', 'Kau', 'Pinky', 'Pinu', 'Reyu', 'mau']

# to get all data 
# objs = Person.objects.all()
# print(list(objs))

# Output
# [<Person: p1 --pune>, <Person: p2 --karve nagar>, <Person: p3 --mumbai>, <Person: p4 --nanded>, <Person: p5 --nashik>]

# for person in objs:
#     print(person)
# output
# p1 --pune
# p2 --karve nagar
# p3 --mumbai
# p4 --nanded
# p5 --nashik

# to get first record
# first_record = Person.objects.first()
# print(first_record)
# output
# p1 --pune

# to get record by id
# try:
#     obj = Person.objects.get(id=5)
#     print(obj)
# except Person.DoesNotExist:
#     print("Record does not exist")
# output
# p4 --nanded

# try:
#     obj = Person.objects.get(id=7)
#     print(obj)
# except Person.DoesNotExist:
#     print("Record does not Exist")
# output
# Record does not Exist

# objs = Person.objects.filter(id=1, address="pune")
# print(objs)
# output
# <QuerySet [<Person: p1 --pune>]>

# modifying existing data
# p1 = Person.objects.get(id=4)
# print(p1.__dict__)
# p1.mobile_num = 9854127777
# print(p1.__dict__)
# p1.save()

# p2 = Person(name = "p6", age = 28, mobile_num = 9876542584, address = "Kolhapur")
# p2.save()
# obj = Person.objects.all()
# print(obj)
# output
# <QuerySet [<Person: p1 --pune>, <Person: p2 --karve nagar>, <Person: p3 --mumbai>, <Person: p4 --nanded>, <Person: p5 --nashik>, <Person: p6 --Kolhapur>]>

# Person.objects.create(name = "p7", age = 25, mobile_num = 9685475325, address = "Baramati")
# obj = Person.objects.all()
# print(obj)
# output
# <QuerySet [<Person: p1 --pune>, <Person: p2 --karve nagar>, <Person: p3 --mumbai>, <Person: p4 --nanded>, <Person: p5 --nashik>, <Person: p6 --Kolhapur>, <Person: p7 --Baramati>]>

# bulk create

# p8 = Pers

# obj = Person.objects.all()
# print(obj)
# output
# <QuerySet [<Person: p1 --pune>, <Person: p2 --karve nagar>, <Person: p3 --mumbai>, <Person: p4 --nanded>, <Person: p5 --nashik>, <Person: p6 --Kolhapur>, <Person: p7 --Baramati>, <Person: vaishnavi --Gujrat>, <Person: Kau --Kerla>, <Person: Pinky --Goa>, <Person: Pinu --Surat>, <Person: Reyu --Karnataka>]>

# count
# print(Person.objects.count())
# output
# 12

# Person.objects.filter(name="p2").delete()
# obj = Person.objects.all()
# print(obj)
# output
# <QuerySet [<Person: p1 --pune>, <Person: p3 --mumbai>, <Person: p4 --nanded>, <Person: p5 --nashik>, <Person: p6 --Kolhapur>, <Person: p7 --Baramati>, <Person: vaishnavi --Gujrat>, <Person: Kau --Kerla>, <Person: Pinky --Goa>, <Person: Pinu --Surat>, <Person: Reyu --Karnataka>]>

# print(Person.objects.filter(name__startswith = "p"))
# output
# <QuerySet [<Person: p1 --pune>, <Person: p3 --mumbai>, <Person: p4 --nanded>, <Person: p5 --nashik>, <Person: p6 --Kolhapur>, <Person: p7 --Baramati>, <Person: Pinky --Goa>, <Person: Pinu --Surat>]>

# print(Person.objects.filter(name__endswith="i"))
# output
# <QuerySet [<Person: vaishnavi --Gujrat>]>

# print(Person.objects.filter(name = "p1").exists())
# output
# True

# print(Person.objects.filter(name = "p2"). exists())
# output
# False

# print(Person.objects.all().order_by("name"))
# output
# <QuerySet [<Person: Kau --Kerla>, <Person: Pinky --Goa>, <Person: Pinu --Surat>, <Person: Reyu --Karnataka>, <Person: p1 --pune>, <Person: p3 --mumbai>, <Person: p4 --nanded>, <Person: p5 --nashik>, <Person: p6 --Kolhapur>, <Person: p7 --Baramati>, <Person: vaishnavi --Gujrat>]>

# print(Person.objects.all().order_by("-name"))
# output
# <QuerySet [<Person: vaishnavi --Gujrat>, <Person: p7 --Baramati>, <Person: p6 --Kolhapur>, <Person: p5 --nashik>, <Person: p4 --nanded>, <Person: p3 --mumbai>, <Person: p1 --pune>, <Person: Reyu --Karnataka>, <Person: Pinu --Surat>, <Person: Pinky --Goa>, <Person: Kau --Kerla>]>

# data = Person.objects.all().values()        # output in dictionary
# print(data)

# for i in data:
#     print(i, type(i))

# to get specific info only as we want
# data = Person.objects.all().values("name", "id", "age")
# print(data)
# for i in data:
#     print(i)
# output
# <QuerySet [{'name': 'p1', 'id': 1, 'age': 20}, {'name': 'p3', 'id': 4, 'age': 24}, {'name': 'p4', 'id': 5, 'age': 25}, {'name': 'p5', 'id': 6, 'age': 26}, {'name': 'p6', 'id': 7, 'age': 28}, {'name': 'p7', 'id': 9, 'age': 25}, {'name': 'vaishnavi', 'id': 10, 'age': 23}, {'name': 'Kau', 'id': 11, 'age': 21}, {'name': 'Pinky', 'id': 12, 'age': 19}, {'name': 'Pinu', 'id': 13, 'age': 17}, {'name': 'Reyu', 'id': 14, 'age': 16}]>
# {'name': 'p1', 'id': 1, 'age': 20}
# {'name': 'p3', 'id': 4, 'age': 24}
# {'name': 'p4', 'id': 5, 'age': 25}
# {'name': 'p5', 'id': 6, 'age': 26}
# {'name': 'p6', 'id': 7, 'age': 28}
# {'name': 'p7', 'id': 9, 'age': 25}
# {'name': 'vaishnavi', 'id': 10, 'age': 23}
# {'name': 'Kau', 'id': 11, 'age': 21}
# {'name': 'Pinky', 'id': 12, 'age': 19}
# {'name': 'Pinu', 'id': 13, 'age': 17}
# {'name': 'Reyu', 'id': 14, 'age': 16}

# data = Person.objects.all().values("name", "id", "age")
# lst = []
# for i in data:
#     lst.append(i["name"])
# print(lst)
# output
# ['p1', 'p3', 'p4', 'p5', 'p6', 'p7', 'vaishnavi', 'Kau', 'Pinky', 'Pinu', 'Reyu']

# to get avarage age of total person
# data = Person.objects.all().values()
# lst = list(map(lambda x: x["age"], list(data)))
# print(sum(lst)//len(lst))
# output
# 22

# to get details of person by age
# obj = Person.objects.filter(age = 25)
# print(obj)
# output
# <QuerySet [<Person: p4 --nanded>, <Person: p7 --Baramati>]>

# to get query
# objs = Person.objects.filter(age = 23, address = "Gujrat")
# print(objs.query)
# output
# SELECT "person"."id", "person"."name", "person"."age", "person"."mobile_num", "person"."address" FROM "person" WHERE ("person"."address" = Gujrat AND "person"."age" = 23)

# obj = Person.objects.all()
# print(obj.query)
# output
# SELECT "person"."id", "person"."name", "person"."age", "person"."mobile_num", "person"."address" FROM "person"

# p1 = Person.objects.get(id = 1)
# print(p1.__dict__)
# p1.mobile_num = 8954756214
# print(p1.__dict__)
# p1.save()

# to delete specified id
# p2 = Person.objects.get(id=5)
# p2.delete()

# p3 = Person(name = "mau", age= 30, mobile_num = 9960199875, address = "Nagar")
# p3.save()

# to delete record
# Person.objects.all().delete()
# to delete specific record
# Person.objects.filter(id = 2).delete()

# print(Person.objects.exclude(name__startswith="P"))
# output
# <QuerySet [<Person: vaishnavi --Gujrat>, <Person: Kau --Kerla>, <Person: Reyu --Karnataka>, <Person: mau --Nagar>]>


# print(Person.objects.filter(id = 2).exists())
# print(Person.objects.all().order_by("id"))        # record in ascending order
# print(Person.objects.all().order_by("-id"))       # record in descending order

# introduce in classmethod 
# Person.objects.get(id =1).show_details()
# output
# Person Name:- p1
# Person Age:- 20
# Person Mobile_num:- 8954756214
# Person Address:- pune

# introduce in classmethod 
# for per_obj in Person.objects.all():
#     per_obj.show_details()
# # output
# ----------------------------------
# Person Name:- p1
# Person Age:- 20
# Person Mobile_num:- 8954756214
# Person Address:- pune
# ----------------------------------
# Person Name:- p3
# Person Age:- 24
# Person Mobile_num:- 9854127777
# Person Address:- mumbai
# ----------------------------------
# Person Name:- p5
# Person Age:- 26
# Person Mobile_num:- 8456321789
# Person Address:- nashik
# ----------------------------------
# Person Name:- p6
# Person Age:- 28
# Person Mobile_num:- 9876542584
# Person Address:- Kolhapur
# ----------------------------------
# Person Name:- p7
# Person Age:- 25
# Person Mobile_num:- 9685475325
# Person Address:- Baramati
# ----------------------------------
# Person Name:- vaishnavi
# Person Age:- 23
# Person Mobile_num:- 9458467825
# Person Address:- Gujrat
# ----------------------------------
# Person Name:- Kau
# Person Age:- 21
# Person Mobile_num:- 9458456785
# Person Address:- Kerla
# ----------------------------------
# Person Name:- Pinky
# Person Age:- 19
# Person Mobile_num:- 9864467286
# Person Address:- Goa
# ----------------------------------
# Person Name:- Pinu
# Person Age:- 17
# Person Mobile_num:- 9869877582
# Person Address:- Surat
# ----------------------------------
# Person Name:- Reyu
# Person Age:- 16
# Person Mobile_num:- 8954987785
# Person Address:- Karnataka
# ----------------------------------
# Person Name:- mau
# Person Age:- 30
# Person Mobile_num:- 9960199875
# Person Address:- Nagar
#--------------------------------------------------------------------------------------------------------

# to get person greater than or equal to 25
# introduce in classmethod 
# print(Person.get_data_above_age())
# output
# <QuerySet [<Person: p5 --nashik>, <Person: p6 --Kolhapur>, <Person: p7 --Baramati>, <Person: mau --Nagar>]>
#--------------------------------------------------------------------------------------------------------
# to get only values in list of tuple form
# data = Person.objects.all().values_list()
# print(data)
# output
# <QuerySet [(1, 'p1', 20, 8954756214, 'pune'), (4, 'p3', 24, 9854127777, 'mumbai'), (6, 'p5', 26, 8456321789, 'nashik'), (7, 'p6', 28, 9876542584, 'Kolhapur'), (9, 'p7', 25, 9685475325, 'Baramati'), (10, 'vaishnavi', 23, 9458467825, 'Gujrat'), (11, 'Kau', 21, 9458456785, 'Kerla'), (12, 'Pinky', 19, 9864467286, 'Goa'), (13, 'Pinu', 17, 9869877582, 'Surat'), (14, 'Reyu', 16, 8954987785, 'Karnataka'), (15, 'mau', 30, 9960199875, 'Nagar')]>

#####################################################################################################################################

# to make operation on user
# exec(open(r'D:\Python\Code File\B8_Django\first_project\app1\db_shell.py').read())
# from django.contrib.auth import get_user_model
# user = get_user_model()

# print(user.objects.all())
# output
# <QuerySet [<User: vaishnavi.phadtare2@gmail.com>, <User: Reshma>]>

# create user_name
# user.objects.create_user(username = "rj")        
# print(user.objects.all())
########################################################################################################################################

# now database changes to mysql
# exec(open(r'D:\Python\Code File\B8_Django\first_project\app1\db_shell.py').read())
# from app1.models import Person
# from django.contrib.auth.models import User
# User.objects.create_user(username = "Pooja", password = "Python@123")       # -- always use create_user
# print(User.objects.all())
# print(Person.objects.all())
# output
# <QuerySet [<User: Rajendra>, <User: Pooja>]>
# <QuerySet [<Person: P1 --Pune>, <Person: P2 --KarveRoad>, <Person: P3 --Deccan>, <Person: P4 --Kothrud>, <Person: P5 --Narhe>, <Person: P6 --Nanded City>]>

 

# to make multiple persons id inactive
# data = Person.objects.filter(id__in = [3, 5]).update(is_active=False)
# print(data)
# output
# 2

# to get active person details
# print(Person.objects.filter(is_active=True))
# output
# <QuerySet [<Person: P1 --Pune>, <Person: P2 --KarveRoad>, <Person: P4 --Kothrud>]>

# print(Person.get_active_data())
# output
# <QuerySet [<Person: P1 --Pune>, <Person: P2 --KarveRoad>, <Person: P4 --Kothrud>]>

# print(Person.get_inactive_data())
# output
# <QuerySet [<Person: P3 --Deccan>, <Person: P5 --Narhe>, <Person: P6 --Nanded City>]>

# print(Person.activep.all())
# output
# <QuerySet [<Person: P1 --Pune>, <Person: P2 --KarveRoad>, <Person: P4 --Kothrud>]>

# print(Person.Inactivep.all())
# output
# <QuerySet [<Person: P3 --Deccan>, <Person: P5 --Narhe>, <Person: P6 --Nanded City>]>

# we can define any name in Person class to access all person data
# print(Person.all_data.all())
# output
# <QuerySet [<Person: P1 --Pune>, <Person: P2 --KarveRoad>, <Person: P3 --Deccan>, <Person: P4 --Kothrud>, <Person: P5 --Narhe>, <Person: P6 --Nanded City>]>

# print(Person.objects.all())
# output
# <QuerySet [<Person: P1 --Pune>, <Person: P2 --KarveRoad>, <Person: P3 --Deccan>, <Person: P4 --Kothrud>, <Person: P5 --Narhe>, <Person: P6 --Nanded City>]>


# exec(open(r'D:\Python\Code File\B8_Django\first_project\app1\db_shell.py').read())

from app1.models import *
clgs = College.objects.all()
prnc = Principle.objects.all()
depts = Department.objects.all()
studs = Student.objects.all()
subs = Subject.objects.all()

# print(list(clgs))
# print(list(prnc))
# print(list(depts))
# print(list(studs))
# print(list(subs))
# # output
# [<College: D Y Patil>]
# [<Principle: Kanai>]
# [<Department: EE>, <Department: IT>, <Department: ENTC>]
# [<Student: Vaishnavi>, <Student: Nav>, <Student: Jiv>, <Student: KTN>, <Student: Resh>, <Student: Ashwini>, <Student: priyanka>, <Student: Sanket>, <Student: Wassi>, <Student: Sofi>, <Student: Anisha>, <Student: Jayu>]
# [<Subject: Power System>, <Subject: AC Machine>, <Subject: DC Machine>, <Subject: Control System>, <Subject: Network System>, <Subject: Microprocessor>, <Subject: Digital Electronics>, <Subject: Power Electronics>, <Subject: Operating Systems>, <Subject: IT Networks>, <Subject: Java Programming and Website Design>, <Subject: Foundations of IT Systems>]

# for dept in depts:
    # print(dept)
    # print(dept.__dict__)
# output
# EE
# IT
# ENTC
# {'_state': <django.db.models.base.ModelState object at 0x000002324CBB9910>, 'id': 1, 'name': 'EE', 'dept_str': 60, 'college_id': 1}
# {'_state': <django.db.models.base.ModelState object at 0x000002324CBB9820>, 'id': 2, 'name': 'IT', 'dept_str': 60, 'college_id': 1}
# {'_state': <django.db.models.base.ModelState object at 0x000002324CBB9760>, 'id': 3, 'name': 'ENTC', 'dept_str': 60, 'college_id': 1}

# for stud in studs:
#     print(stud.__dict__)
# output
# {'_state': <django.db.models.base.ModelState object at 0x000002324CBCB8E0>, 'id': 1, 'name': 'Vaishnavi', 'marks': 80, 'age': 25, 'dept_id': 1}
# {'_state': <django.db.models.base.ModelState object at 0x000002324CBCB8B0>, 'id': 2, 'name': 'Nav', 'marks': 82, 'age': 26, 'dept_id': 1}
# {'_state': <django.db.models.base.ModelState object at 0x000002324CBCB820>, 'id': 3, 'name': 'Jiv', 'marks': 84, 'age': 25, 'dept_id': 1}
# {'_state': <django.db.models.base.ModelState object at 0x000002324CBCB790>, 'id': 4, 'name': 'KTN', 'marks': 89, 'age': 26, 'dept_id': 1}
# {'_state': <django.db.models.base.ModelState object at 0x000002324CBCB700>, 'id': 5, 'name': 'Resh', 'marks': 90, 'age': 24, 'dept_id': 2}
# {'_state': <django.db.models.base.ModelState object at 0x000002324CBCB670>, 'id': 6, 'name': 'Ashwini', 'marks': 92, 'age': 25, 'dept_id': 2}
# {'_state': <django.db.models.base.ModelState object at 0x000002324CBCB5E0>, 'id': 7, 'name': 'priyanka', 'marks': 94, 'age': 26, 'dept_id': 2}
# {'_state': <django.db.models.base.ModelState object at 0x000002324CBCB2E0>, 'id': 8, 'name': 'Sanket', 'marks': 99, 'age': 28, 'dept_id': 2}
# {'_state': <django.db.models.base.ModelState object at 0x000002324CBCB250>, 'id': 9, 'name': 'Wassi', 'marks': 98, 'age': 28, 'dept_id': 3}
# {'_state': <django.db.models.base.ModelState object at 0x000002324CBCB1C0>, 'id': 10, 'name': 'Sofi', 'marks': 99, 'age': 27, 'dept_id': 3}
# {'_state': <django.db.models.base.ModelState object at 0x000002324CBCB130>, 'id': 11, 'name': 'Anisha', 'marks': 88, 'age': 29, 'dept_id': 3}
# {'_state': <django.db.models.base.ModelState object at 0x000002324CBCB070>, 'id': 12, 'name': 'Jayu', 'marks': 85, 'age': 24, 'dept_id': 3}

# for sub in subs:
#     print(sub.__dict__)
# output
# {'_state': <django.db.models.base.ModelState object at 0x000002324CB82CD0>, 'id': 1, 'name': 'Power System', 'is_practical': True, 'dept_id': 1}
# {'_state': <django.db.models.base.ModelState object at 0x000002324CB82E20>, 'id': 2, 'name': 'AC Machine', 'is_practical': True, 'dept_id': 1}
# {'_state': <django.db.models.base.ModelState object at 0x000002324CBB92E0>, 'id': 3, 'name': 'DC Machine', 'is_practical': True, 'dept_id': 1}
# {'_state': <django.db.models.base.ModelState object at 0x000002324CBB9D00>, 'id': 4, 'name': 'Control System', 'is_practical': True, 'dept_id': 1}
# {'_state': <django.db.models.base.ModelState object at 0x000002324CBB9DC0>, 'id': 5, 'name': 'Network System', 'is_practical': True, 'dept_id': 3}
# {'_state': <django.db.models.base.ModelState object at 0x000002324CBB9970>, 'id': 6, 'name': 'Microprocessor', 'is_practical': True, 'dept_id': 3}
# {'_state': <django.db.models.base.ModelState object at 0x000002324CBB96A0>, 'id': 7, 'name': 'Digital Electronics', 'is_practical': True, 'dept_id': 3}
# {'_state': <django.db.models.base.ModelState object at 0x000002324CBB9E20>, 'id': 8, 'name': 'Power Electronics', 'is_practical': True, 'dept_id': 3}
# {'_state': <django.db.models.base.ModelState object at 0x000002324CBB9F70>, 'id': 9, 'name': 'Operating Systems', 'is_practical': True, 'dept_id': 2}
# {'_state': <django.db.models.base.ModelState object at 0x000002324CBB9AC0>, 'id': 10, 'name': 'IT Networks', 'is_practical': True, 'dept_id': 2}
# {'_state': <django.db.models.base.ModelState object at 0x000002324CBB9850>, 'id': 11, 'name': 'Java Programming and Website Design', 'is_practical': True, 'dept_id': 2}
# {'_state': <django.db.models.base.ModelState object at 0x000002324CBB9400>, 'id': 12, 'name': 'Foundations of IT Systems', 'is_practical': False, 'dept_id': 2}

# clg =clgs[2]
# print(clg)
# output
# D Y Patil

# from clg input get principle output
# clg = clgs[1]
# print(clg.principle)
# output
# Kanai

# from principle input get college output
# kanai_obj = Principle.objects.first()
# print(kanai_obj.college)
# output
# D Y Patil
# print(kanai_obj.depts)

# to get all department form clg
# print(clg.department_set.all())
# <QuerySet [<Department: EE>, <Department: IT>, <Department: ENTC>]>

# to get college from department
# dept = Department.objects.first()
# print(dept.college)
# Output
# D Y Patil

# from 1st dept fetch all students
# dept = Department.objects.first()
# print(dept.student_set.all())
# <QuerySet [<Student: Vaishnavi>, <Student: Nav>, <Student: Jiv>, <Student: KTN>]>

# dept = Department.objects.get(id = 2)
# print(dept.student_set.all())
# output
# <QuerySet [<Student: Resh>, <Student: Ashwini>, <Student: priyanka>, <Student: Sanket>]>

# dept = Department.objects.get(id = 3)
# print(dept.student_set.all())
# output
# <QuerySet [<Student: Wassi>, <Student: Sofi>, <Student: Anisha>, <Student: Jayu>]>

# dept = Department.objects.get(id = 4)
# print(dept.student_set.all())
# output
# app1.models.Department.DoesNotExist: Department matching query does not exist.

# to get department and student info
# all_dept = Department.objects.all()
# for dept in all_dept:
#     print(f"Department Name:- {dept.name}, student:-{dept.student_set.all()}")
# output
# Department Name:- EE, student:-<QuerySet [<Student: Vaishnavi>, <Student: Nav>, <Student: Jiv>, <Student: KTN>]>
# Department Name:- IT, student:-<QuerySet [<Student: Resh>, <Student: Ashwini>, <Student: priyanka>, <Student: Sanket>]>
# Department Name:- ENTC, student:-<QuerySet [<Student: Wassi>, <Student: Sofi>, <Student: Anisha>, <Student: Jayu>]>

# to get department and student info in dictionary form
# all_dept = Department.objects.all()
# d ={}
# for dept in all_dept:
#     d[dept.name] = list(dept.student_set.all())
# print(d)
# output
# {'EE': [<Student: Vaishnavi>, <Student: Nav>, <Student: Jiv>, <Student: KTN>], 'IT': [<Student: Resh>, <Student: Ashwini>, <Student: priyanka>, <Student: Sanket>], 'ENTC': [<Student: Wassi>, <Student: Sofi>, <Student: Anisha>, <Student: Jayu>]}

# to get department from student
# s1 = Student.objects.get(id = 4)
# print(s1.dept)
# output
# EE

# to get department from all student
# studs = Student.objects.all()
# stud_dept_dict = {}
# for stud in studs:
#     stud_dept_dict[stud.name] = stud.dept
# print(stud_dept_dict)
# output
# {'Vaishnavi': <Department: EE>, 'Nav': <Department: EE>, 'Jiv': <Department: EE>, 'KTN': <Department: EE>, 'Resh': <Department: IT>, 'Ashwini': <Department: IT>, 'priyanka': <Department: IT>, 'Sanket': <Department: IT>, 'Wassi': <Department: ENTC>, 'Sofi': <Department: ENTC>, 'Anisha': <Department: ENTC>, 'Jayu': <Department: ENTC>}

# to get department name only by using student
# studs = Student.objects.all()
# stud_dept_dict = {}
# for stud in studs:
#     stud_dept_dict[stud.name] = stud.dept.name
# print(stud_dept_dict)
# output
# {'Vaishnavi': 'EE', 'Nav': 'EE', 'Jiv': 'EE', 'KTN': 'EE', 'Resh': 'IT', 'Ashwini': 'IT', 'priyanka': 'IT', 'Sanket': 'IT', 'Wassi': 'ENTC', 'Sofi': 'ENTC', 'Anisha': 'ENTC', 'Jayu': 'ENTC'}

# to get department dictionary by using student
# studs = Student.objects.all()
# stud_dept_dict = {}
# for stud in studs:
#     stud_dept_dict[stud.name] = stud.dept.__dict__
# print(stud_dept_dict)
# output
# {'Vaishnavi': {'_state': <django.db.models.base.ModelState object at 0x000002A9C37A4C70>, 'id': 1, 'name': 'EE', 'dept_str': 60, 'college_id': 1}, 'Nav': {'_state': <django.db.models.base.ModelState object at 0x000002A9C37A4A00>, 'id': 1, 'name': 'EE', 'dept_str': 60, 'college_id': 1}, 'Jiv': {'_state': <django.db.models.base.ModelState object at 0x000002A9C37A4460>, 'id': 1, 'name': 'EE', 'dept_str': 60, 'college_id': 1}, 'KTN': {'_state': <django.db.models.base.ModelState object at 0x000002A9C37A4940>, 'id': 1, 'name': 'EE', 'dept_str': 60, 'college_id': 1}, 'Resh': {'_state': <django.db.models.base.ModelState object at 0x000002A9C37A4E50>, 'id': 2, 'name': 'IT', 'dept_str': 60, 'college_id': 1}, 'Ashwini': {'_state': <django.db.models.base.ModelState object at 0x000002A9C37A4AF0>, 'id': 2, 'name': 'IT', 'dept_str': 60, 'college_id': 1}, 'priyanka': {'_state': <django.db.models.base.ModelState object at 0x000002A9C3739CA0>, 'id': 2, 'name': 'IT', 'dept_str': 60, 'college_id': 1}, 'Sanket': {'_state': <django.db.models.base.ModelState object at 0x000002A9C3739430>, 'id': 2, 'name': 'IT', 'dept_str': 60, 'college_id': 1}, 'Wassi': {'_state': <django.db.models.base.ModelState object at 0x000002A9C3739E50>, 'id': 3, 'name': 'ENTC', 'dept_str': 60, 'college_id': 1}, 'Sofi': {'_state': <django.db.models.base.ModelState object at 0x000002A9C3739FA0>, 'id': 3, 'name': 'ENTC', 'dept_str': 60, 'college_id': 1}, 'Anisha': {'_state': <django.db.models.base.ModelState object at 0x000002A9C3739310>, 'id': 3, 'name': 'ENTC', 'dept_str': 60, 'college_id': 1}, 'Jayu': {'_state': <django.db.models.base.ModelState object at 0x000002A9C3739910>, 'id': 3, 'name': 'ENTC', 'dept_str': 60, 'college_id': 1}}


# ###############################################################################################
# Now we can check by making some changes in models.py file
# add after CASCADE related_name = "class name here in small letter"

# to get principle from clg
# clg = College.objects.get(id = 1)
# print(clg.princi)
# output
# Kanai
# print(College.objects.all())
# output
# <QuerySet [<College: D Y Patil>, <College: MIT>, <College: F C>]>

# clg = College.objects.get(id = 1)
# print(clg.depts.all())
# output
# <QuerySet [<Department: EE>, <Department: IT>, <Department: ENTC>]>

# clg = College.objects.get(id = 2)
# print(clg.depts.all())

# dept = Department.objects.get(id = 1)
# print(dept.subs.all())
# output
# <QuerySet [<Subject: Power System>, <Subject: AC Machine>, <Subject: DC Machine>, <Subject: Control System>]>

# dept = Department.objects.get(id = 2)
# print(dept.subs.all())
# output
# <QuerySet [<Subject: Operating Systems>, <Subject: IT Networks>, <Subject: Java Programming and Website Design>, <Subject: Foundations of IT Systems>]>

# dept = Department.objects.get(id = 3)
# print(dept.subs.all())
# output
# <QuerySet [<Subject: Network System>, <Subject: Microprocessor>, <Subject: Digital Electronics>, <Subject: Power Electronics>]>

# to get all subjects from all departments
# depts = Department.objects.all()
# for dept in depts:
#     print(dept.subs.all())
# output
# <QuerySet [<Subject: Power System>, <Subject: AC Machine>, <Subject: DC Machine>, <Subject: Control System>]>
# <QuerySet [<Subject: Operating Systems>, <Subject: IT Networks>, <Subject: Java Programming and Website Design>, <Subject: Foundations of IT Systems>]>
# <QuerySet [<Subject: Network System>, <Subject: Microprocessor>, <Subject: Digital Electronics>, <Subject: Power Electronics>]>

# dept = Department.objects.all()
# print([dept.subs.all() for dept in list(Department.objects.all())])
# output
# [<QuerySet [<Subject: Power System>, <Subject: AC Machine>, <Subject: DC Machine>, <Subject: Control System>]>, <QuerySet [<Subject: Operating Systems>, <Subject: IT Networks>, <Subject: Java Programming and Website Design>, <Subject: Foundations of IT Systems>]>, <QuerySet [<Subject: Network System>, <Subject: Microprocessor>, <Subject: Digital Electronics>, <Subject: Power Electronics>]>]

# dept = Department.objects.all()
# print([list(dept.subs.all()) for dept in Department.objects.all()])

# to get all students from IT dept

# clg = College.objects.get(id = 1)
# print(clg.depts.all()[1].studs.all())
# output
# <QuerySet [<Student: Resh>, <Student: Ashwini>, <Student: priyanka>, <Student: Sanket>]>

# to get all students from ENTC dept
# clg = College.objects.get(id = 1)
# print(clg.depts.all()[2].studs.all())
# output
# <QuerySet [<Student: Wassi>, <Student: Sofi>, <Student: Anisha>, <Student: Jayu>]>.

# to get all students from EE dept
# clg = College.objects.get(id = 1)
# print(clg.depts.all()[0].studs.all())
# output
# <QuerySet [<Student: Vaishnavi>, <Student: Nav>, <Student: Jiv>, <Student: KTN>]>

# to get single students from EE dept
# clg = College.objects.get(id = 1)
# print(clg.depts.all()[0].studs.all()[0])
# output
# Vaishnavi

# clg = College.objects.get(id = 1)
# print(clg.depts.all()[0].studs.all()[1])
# output
# Nav

# clg = College.objects.get(id = 1)
# print(clg.depts.all()[1].studs.all()[0])
# output
# Resh

# clg = College.objects.get(id = 1)
# print(clg.depts.all()[2].studs.all()[0])
# output
# Wassi

# clg = College.objects.get(id = 1)
# for dept in clg.depts.all():
#     print(dept.studs.all())
# output
# <QuerySet [<Student: Vaishnavi>, <Student: Nav>, <Student: Jiv>, <Student: KTN>]>
# <QuerySet [<Student: Resh>, <Student: Ashwini>, <Student: priyanka>, <Student: Sanket>]>
# <QuerySet [<Student: Wassi>, <Student: Sofi>, <Student: Anisha>, <Student: Jayu>]>


# to get all student output in one list
# clg = College.objects.get(id = 1)
# stud_list = []
# for dept in clg.depts.all():
#     stud_list.append(dept.studs.all())
# print(stud_list)
# output
# [<QuerySet [<Student: Vaishnavi>, <Student: Nav>, <Student: Jiv>, <Student: KTN>]>, <QuerySet [<Student: Resh>, <Student: Ashwini>, <Student: priyanka>, <Student: Sanket>]>, <QuerySet [<Student: Wassi>, <Student: Sofi>, <Student: Anisha>, <Student: Jayu>]>]

# clg = College.objects.get(id = 1)
# stud_list = []
# for dept in clg.depts.all():
#     stud_list.extend(dept.studs.all())
# print(stud_list)
# output
# [<Student: Vaishnavi>, <Student: Nav>, <Student: Jiv>, <Student: KTN>, <Student: Resh>, <Student: Ashwini>, <Student: priyanka>, <Student: Sanket>, <Student: Wassi>, <Student: Sofi>, <Student: Anisha>, <Student: Jayu>]


# to get college name from student 
# s1 = Student.objects.get(id = 5)
# print(s1.dept.college)
# output
# D Y Patil

# s2 = Student.objects.get(id = 9)
# print(s2.dept.college.est_date)
# output
# 2022-12-21

# s2 = Student.objects.get(id = 12)
# print(s2.dept.college.adr)
# output
# Akurdi


# studs = Student.objects.all()
# stud_dept_dict = {}
# for stud in studs:
#     stud_dept_dict[stud.name] = stud.dept
# print(stud_dept_dict)

################################################### ADDITION ###################################################


# College.objects.create(name = "", adr = "" )

# to create principle
# c1 = College.objects.get(id = 2)
# p1 = Principle(name ="ABC", exp = 20, qual = "PhD", college = c1)
# another way to create principle p1.save will reflect changes in database
# p1 = Principle(name = "ABC", exp = 20, qual = "PhD", college_id=2)
# p1.save()

# to create department we need to give college instance or college id
# Department.objects.create(name = "Production", dept_str = 120, college_id = 2)
# Department.objects.create(name = "Civil", dept_str = 120, college_id = 2)
# Department.objects.create(name = "Automobile", dept_str = 60, college_id = 1)

# exec(open(r'D:\Python\Code File\B8_Django\first_project\app1\db_shell.py').read())

# Student.objects.create(name = "A", marks = 88, age = 25, dept_id = 6)
# Student.objects.create(name = "B", marks = 80, age = 26, dept_id = 6)
# Student.objects.create(name = "C", marks = 85, age = 24, dept_id = 6)
# Student.objects.create(name = "D", marks = 90, age = 28, dept_id = 6)
# Student.objects.create(name = "E", marks = 81, age = 27)
# Student.objects.create(name = "F", marks = 86, age = 24)
# Student.objects.create(name = "G", marks = 94, age = 26)
# Student.objects.create(name = "H", marks = 75, age = 28)

# s1, s2, s3, s4 = Student.objects.filter(id__gt=16)
# print(s1, s2, s3, s4)
# output
# E F G H

# prod_dept = Department.objects.get(id = 4)
# prod_dept.studs.add(s1, s2)

# civil_dept = Department.objects.get(id = 5)
# civil_dept.studs.add(s3, s4)                    # one to many add students in dept


# here we have set logger in seeting and now we can see the result in query form
# studs = Student.objects.all()
# print(studs)
# output
# (0.000) SELECT `student`.`id`, `student`.`name`, `student`.`marks`, `student`.`age`, `student`.`dept_id` FROM `student` LIMIT 21; args=()
# <QuerySet [<Student: Vaishnavi>, <Student: Nav>, <Student: Jiv>, <Student: KTN>, <Student: Resh>, <Student: Ashwini>, <Student: priyanka>, <Student: Sanket>, <Student: Wassi>, <Student: Sofi>, <Student: Anisha>, <Student: Jayu>, <Student: A>, <Student: B>, <Student: C>, <Student: D>, <Student: E>, <Student: F>, <Student: G>, <Student: H>]>

# to get single student information
# studs = Student.objects.all()[0]
# print(studs)
# output
# (0.000) SELECT `student`.`id`, `student`.`name`, `student`.`marks`, `student`.`age`, `student`.`dept_id` FROM `student` LIMIT 1; args=()
# Vaishnavi

# to get record from zero index to 4
# studs = Student.objects.all()[0:5]
# print(studs)
# output
# (0.000) SELECT `student`.`id`, `student`.`name`, `student`.`marks`, `student`.`age`, `student`.`dept_id` FROM `student` LIMIT 5; args=()
# <QuerySet [<Student: Vaishnavi>, <Student: Nav>, <Student: Jiv>, <Student: KTN>, <Student: Resh>]>

# to get record of index no 5 
# studs = Student.objects.all()[5]
# print(studs)
# output
# (0.000) SELECT `student`.`id`, `student`.`name`, `student`.`marks`, `student`.`age`, `student`.`dept_id` FROM `student` LIMIT 1 OFFSET 5; args=()
# Ashwini
####################################################################################################################################


# to fetch all the students from student table
# studs = Student.objects.all()
# for stud in studs:
#     print(stud)
# this will give all the students from student table
# to get student department
# studs = Student.objects.all()
# for stud in studs:
#     print(stud.dept)
# this will create multiple query for each student which is ideally not correct so to avoid this we will use select related which will create only one query as below
# studs = Student.objects.select_related("dept")
# for stud in studs:
#     print(stud.dept)

# (0.000) SELECT `student`.`id`, `student`.`name`, `student`.`marks`, `student`.`age`, `student`.`dept_id`, `department`.`id`, `department`.`name`, `department`.`dept_str`, `department`.`college_id` FROM `student` LEFT OUTER JOIN `department` ON (`student`.`dept_id` = `department`.`id`); args=()
# EE
# EE
# EE
# EE
# IT
# IT
# IT
# IT
# ENTC
# ENTC
# ENTC
# ENTC
# Automobile
# Automobile
# Automobile
# Automobile
# Production
# Production
# Civil
# Civil

# exec(open(r'D:\Python\Code File\B8_Django\first_project\app1\db_shell.py').read())

# c180 = CarModel.objects.create(name = "c180")
# c200 = CarModel.objects.create(name = "c200")
# print(CarModel.objects.all())

# gas = FuelType.objects.create(name = "gas")
# diesel = FuelType.objects.create(name = "diesel")
# hybrid = FuelType.objects.create(name = "hybrid")
# print(FuelType.objects.all())

# c180 = CarModel.objects.get(name = "c180")
# c200 = CarModel.objects.get(name = "c200")

# gas = FuelType.objects.get(name = "gas")
# diesel = FuelType.objects.get(name = "diesel")
# hybrid = FuelType.objects.get(name = "hybrid")

# c180.fueltype.add(gas)
# c180.fueltype.add(diesel, hybrid)
# print(c180.fueltype.all())

# c200.fueltype.add(gas, diesel, hybrid)
# print(c200.fueltype.all())

# fueltype creation and assign to car model
# c200.fueltype.create(name = "Bio Diesel")
# print(c200.fueltype.all())
# print(c180.fueltype.all())

# print(gas.carmodel_set.all())
# print(diesel.carmodel_set.all())
# print(hybrid.carmodel_set.all())

# Now we are setting related name here

# print(gas.carmodels.all())
# print(c180.fuelmodel.carmodels)

# to fetch carmodels using filter
# print(CarModel.objects.filter(fueltype__name__startswith = "g"))
# output
# <QuerySet [<CarModel: c180>, <CarModel: c200>]>

# print(CarModel.objects.filter(fueltype__name__startswith = "d"))
# output
# <QuerySet [<CarModel: c200>]>

# print(CarModel.objects.filter(fueltype__name__startswith = "h"))
# print(CarModel.objects.filter(fueltype__name__startswith = "B"))
# output
# <QuerySet [<CarModel: c200>]>
# <QuerySet [<CarModel: c200>]>

# print(FuelType.objects.filter(carmodels__name= "c180")) # here we have used related name while comming downward
# output
# <QuerySet [<FuelType: gas>]>

# print(FuelType.objects.filter(carmodels__name__startswith = "c"))
# output will show two times fuel name as two carmodels using gas
# <QuerySet [<FuelType: gas>, <FuelType: gas>, <FuelType: diesel>, <FuelType: hybrid>, <FuelType: Bio Diesel>]>
# to overcome repeatedly gas output we can use distinct function
# print(FuelType.objects.filter(carmodels__name__startswith = "c").distinct())
# output
# <QuerySet [<FuelType: gas>, <FuelType: diesel>, <FuelType: hybrid>, <FuelType: Bio Diesel>]>

# print(FuelType.objects.filter(carmodels__name = "c200"))
# output
# <QuerySet [<FuelType: gas>, <FuelType: diesel>, <FuelType: hybrid>, <FuelType: Bio Diesel>]>

# group_concat - used to give any data in comma seperated value
# select group_concat(id) from student
# '1,2,3,4,5,6,7,8,9,10,11,12,17,18,19,20,13,14,15,16'

# to delete specific car model
# cars = CarModel.objects.filter(fueltype__name__startswith = "B").delete()
# cars.delete()
# print(CarModel.objects.all())

# cars = CarModel.objects.filter(fueltype__name__startswith = "g").delete()
# print(CarModel.objects.all())

# Porsche = CarModel.objects.create(name = "Porsche")
# Tesla = CarModel.objects.create(name = "Tesla")
# Kia =  CarModel.objects.create(name = "Kia")
# Jaguar = CarModel.objects.create(name = "Jaguar")
# Volvo = CarModel.objects.create(name = "Volvo")
# print(CarModel.objects.all())

# Gas = FuelType.objects.create(name = "Gas")
# Diesel = FuelType.objects.create(name = "Diesel")
# Hybrid = FuelType.objects.create(name = "hybrid")
# print(FuelType.objects.all())

# Porsche = CarModel.objects.get(name = "Porsche")
# Tesla = CarModel.objects.get(name = "Tesla")
# Kia = CarModel.objects.get(name = "Kia")
# Jaguar = CarModel.objects.get(name = "Jaguar")
# Volvo = CarModel.objects.get(name = "Volvo")

# Gas = FuelType.objects.get(name = "Gas")
# Diesel = FuelType.objects.get(name = "Diesel")
# Hybrid = FuelType.objects.get(name = "Hybrid")

# Porsche.fueltype.add(Gas)
# Tesla.fueltype.add(Gas)
# Kia.fueltype.add(Hybrid)
# Jaguar.fueltype.add(Diesel, Hybrid)
# Volvo.fueltype.add(Gas, Diesel, Hybrid)

# print(Porsche.fueltype.all())

# relation set cleared
# Porsche.fueltype.clear()
# print(Porsche.fueltype.all())
# output
# <QuerySet []>

# to set relation
# Porsche.fueltype.set([Gas, Diesel, Hybrid])
# print(Porsche.fueltype.all())
#######################################################################################

# print(Student.objects.filter(dept__name = "IT"))
# output
# <QuerySet [<Student: Resh>, <Student: Ashwini>, <Student: priyanka>, <Student: Sanket>]>

# print(Student.objects.filter(dept__name = "ENTC"))
# output
# <QuerySet [<Student: Wassi>, <Student: Sofi>, <Student: Anisha>, <Student: Jayu>]>

# print(Student.objects.filter(dept__name = "Automobile"))
# output
# <QuerySet [<Student: A>, <Student: B>, <Student: C>, <Student: D>]>

# print(Student.objects.filter(dept__name__startswith = "E"))
# output
# <QuerySet [<Student: Vaishnavi>, <Student: Nav>, <Student: Jiv>, <Student: KTN>, <Student: Wassi>, <Student: Sofi>, <Student: Anisha>, <Student: Jayu>]>


# to fetch all student from college id 1
# print(Student.objects.filter(dept__college__id = 1))
# output
# <QuerySet [<Student: Vaishnavi>, <Student: Nav>, <Student: Jiv>, <Student: KTN>, <Student: Resh>, <Student: Ashwini>, <Student: priyanka>, <Student: Sanket>, <Student: Wassi>, <Student: Sofi>, <Student: Anisha>, <Student: Jayu>, <Student: A>, <Student: B>, <Student: C>, <Student: D>]>

# to fetch all student from college id 2
# print(Student.objects.filter(dept__college__id = 2))
# output
# <QuerySet [<Student: E>, <Student: F>, <Student: G>, <Student: H>]>

# to fetch students from MIT AND D Y Patil college
# print(Student.objects.filter(dept__college__name__in =["MIT", "D Y Patil"]))
# output
# <QuerySet [<Student: Vaishnavi>, <Student: Nav>, <Student: Jiv>, <Student: KTN>, <Student: Resh>, <Student: Ashwini>, <Student: priyanka>, <Student: Sanket>, <Student: Wassi>, <Student: Sofi>, <Student: Anisha>, <Student: Jayu>, <Student: A>, <Student: B>, <Student: C>, <Student: D>, <Student: E>, <Student: F>, <Student: G>, <Student: H>]>

# Student id 1 to subject
# p1 = Student.objects.get(id = 1)
# print(p1.dept.subs.all())
# output
# <QuerySet [<Subject: Power System>, <Subject: AC Machine>, <Subject: DC Machine>, <Subject: Control System>]>

# p2 = Student.objects.get(id = 5)
# print(p2.dept.subs.all())
# output
# <QuerySet [<Subject: Operating Systems>, <Subject: IT Networks>, <Subject: Java Programming and Website Design>, <Subject: Foundations of IT Systems>]>

# p3 = Student.objects.get(id = 12)
# print(p3.dept.subs.all())
# output
# <QuerySet [<Subject: Network System>, <Subject: Microprocessor>, <Subject: Digital Electronics>, <Subject: Power Electronics>]>

# from subject id 1 to student
# s1 = Subject.objects.get(id = 1)
# print(s1.student.all())
# output
# <QuerySet [<Student: Vaishnavi>, <Student: Nav>, <Student: Jiv>, <Student: KTN>]>

# create students
# Student.objects.create(name = "Priti", marks = 75, age = 26, dept_id = 5 )
# Student.objects.create(name = "Ravi", marks = 75, age = 28, dept_id = 5)

# to get all student from civil dept
# depts = Departm+s.all())
# output
# <QuerySet [<Student: G>, <Student: H>, <Student: Priti>, <Student: Ravi>]>

# s = Student.objects.get(id = 19)
# s.delete()

# depts = Department.objects.get(id = 5)
# print(depts.studs.all())
# output
# <QuerySet [<Student: H>, <Student: Priti>, <Student: Ravi>]>

# to get all students from procuction dept
# clg = College.objects.get(id = 2)
# print(clg.depts.all()[0].studs.all())
# output
# <QuerySet [<Student: E>, <Student: F>]>

# to get all Students from Civil Dept
# clg = College.objects.get(id = 2)
# print(clg.depts.all()[1].studs.all())
# output
# <QuerySet [<Student: H>, <Student: Priti>, <Student: Ravi>]>

# to fetch single student from production dept
# clg = College.objects.get(id=2)
# print(clg.depts.all()[0].studs.all()[0])
# output
# E

# to fetch single student from Civil dept
# clg = College.objects.get(id=2)
# print(clg.depts.all()[1].studs.all()[1])
# output
# Priti

# to fetch clg name from student id
# a = Student.objects.get(id = 21)
# print(a.dept.college.name)
# output
# MIT

# b = Student.objects.get(id = 21)
# print(b.dept.college.est_date)
# output
# 2022-12-21

# c = Student.objects.get(id=21)
# print(c.dept.college.adr)
# output
# Kothrud

################################################################################################################################
        ########################################  RAW SQL QUERY IN DJANGO ########################################                                                  
################################################################################################################################

# exec(open(r'D:\Python\Code File\B8_Django\first_project\app1\db_shell.py').read())

from django.db import connection
# cursor = connection.cursor()
# cursor.execute('''SELECT * FROM student;''')
# data = cursor.fetchall()            # to get all record in the form of tuple of tuple
# print(data)
# output
# ((1, 'Vaishnavi', 80, 25, 1), (2, 'Nav', 82, 26, 1), (3, 'Jiv', 84, 25, 1), (4, 'KTN', 89, 26, 1), (5, 'Resh', 90, 24, 2), (6, 'Ashwini', 92, 25, 2), (7, 'priyanka', 94, 26, 2), (8, 'Sanket', 99, 28, 2), (9, 'Wassi', 98, 28, 3), (10, 'Sofi', 99, 27, 3), (11, 'Anisha', 88, 29, 3), (12, 'Jayu', 85, 24, 3), (13, 'A', 88, 25, 6), (14, 'B', 80, 26, 6), (15, 'C', 85, 24, 6), (16, 'D', 90, 28, 6), (17, 'E', 81, 27, 4), (18, 'F', 86, 24, 4), (20, 'H', 75, 28, 5), (21, 'Priti', 75, 26, 5), (22, 'Ravi', 75, 28, 5))

# cursor = connection.cursor()
# cursor.execute('''SELECT * FROM student;''')        # raw sql query
# data = cursor.fetchmany(3)
# print(data)
# output
# ((1, 'Vaishnavi', 80, 25, 1), (2, 'Nav', 82, 26, 1), (3, 'Jiv', 84, 25, 1))
# data = cursor.fetchmany(3)      # this will give next 3 record from student table
# print(data)
# output
# ((1, 'Vaishnavi', 80, 25, 1), (2, 'Nav', 82, 26, 1), (3, 'Jiv', 84, 25, 1))
# ((4, 'KTN', 89, 26, 1), (5, 'Resh', 90, 24, 2), (6, 'Ashwini', 92, 25, 2))


# Second method to fetch data
# data = Student.objects.raw('SELECT * FROM student')
# for i in data:
#     print(i)
# output
# Vaishnavi
# Nav
# Jiv
# KTN
# Resh
# Ashwini
# priyanka
# Sanket
# Wassi
# Sofi
# Anisha
# Jayu
# A
# B
# C
# D
# E
# F
# H
# Priti
# Ravi

# (Multiple database) MUlti Tenent- in one application two database


# SECOND_DATABASE = " second_db"
# data = Student.objects.using(SECOND_DATABASE).all()
# print(data)

# c1 = College.objects.using(SECOND_DATABASE).create(name="COEP", adr = "Pune")
# d1 = Department.objects.using(SECOND_DATABASE).create(name = "Mech", dept_str = 120, college = c1 )
# s1 = Student.objects.using(SECOND_DATABASE).create(name = "XYZ", marks = 89, age = 28, dept = d1)
# s2 = Student.objects.using(SECOND_DATABASE).create(name = "PQR", marks = 92, age = 29, dept = d1)
# d1 = Department.objects.using(SECOND_DATABASE).get(id=1)
# subj1 = Subject.objects.using(SECOND_DATABASE).create(name = "Fluid Mechanics", is_practical= True, dept=d1)

# studs = Student.objects.using(SECOND_DATABASE).all()
# print(studs)