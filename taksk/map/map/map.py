

Sergo   =["Sergo",300,"have_esse","in_process"       ]
Ivan    =["Ivan",260,"have_esse","in_process"        ]
Katya   =["Katya",250,"no_have_esse","in_process"    ]

threshold_value_to_join_univer=270

Point_of_future_student=[Sergo,Ivan,Katya]
def point_check(student):

    if student[2]=="have_esse":
        student[1]+=10
    return student

Point_of_future_student=list(map(point_check,Point_of_future_student))

arr_int=[1,2,3]
print(arr_int)
arr_int=list(map(lambda x:x**2,arr_int))
print(arr_int)