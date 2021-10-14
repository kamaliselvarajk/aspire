a = [
 {
 "name": "raj",
 "marks": [50,20,30,52,90],
 "medium": "english",
 "parents_details": {
 "parents_qualification": "educated",
 "father_name": "ramu"
 }
 },
 {
 "name": "regho",
 "marks": [70,35,50,60,90],
 "medium": "english",
 "parents_details": {
 "parents_qualification": "non-educated",
 "father_name": "ranjith"
 }
 },
 {
 "name": "ragu",
 "marks": [50,50,35,50,100],
 "medium": "tamil",
 "parents_details": {
 "parents_qualification": "non-educated",
 "father_name": "rajeev"
 }
 },
 {
 "name": "kumar",
 "marks": [50,30,30,52,100],
 "medium": "english",
 "parents_details": {
 "parents_qualification": "educated",
 "father_name": "rajesh"
 }
 },
 {
 "name": "sathesh",
 "marks": [49,19,30,40,12],
 "medium": "tamil",
 "parents_details": {
 "parents_qualification": "non-educated",
 "father_name": "ramu"
 }
 },
 {
 "name": "sundar",
 "marks": [70,70,40,40,80],
 "medium": "tamil",
 "parents_details": {
 "parents_qualification": "non-educated",
 "father_name": "remo"
 }
 }
]
#Students whose average is greater than 40
final_list = list(filter(lambda x: ((sum(x["marks"])/len(x["marks"]))>40) ,a))
print('Students whose average is greater than 40')
for i in final_list:
    print(i["name"])

#Students who got pass mark in all subjects
for i in range(0,5):
    pass_mark = list(filter(lambda x: ((x['marks'][i])>30), a))
print("Students who got pass mark in all subjects")
for i in pass_mark:
    print(i["name"])

#Students who got pass mark in all subjects and whose parents are not educated
for i in range(0,5):
    pass_mark = list(filter(lambda x: ((x['marks'][i])>30 and x['parents_details']['parents_qualification']== 'non-educated'), a))
print("Students who got pass mark in all subjects and whose parents are not educated")
for i in pass_mark:
    print(i["name"])

#Number of students passed
for i in range(0,5):
    pass_mark = list(filter(lambda x: ((x['marks'][i])>30), a))
print("Number of students passed")
print(len(pass_mark))

#Sundar's 4th subject mark
sundar = list(filter(lambda x: (x['name']=='sundar'), a))
sundar_mark = sundar[0]['marks'][3]
print("Sundar's 4th subject mark")
print(sundar_mark)

#Second subject mark of student whose father's name is Rajeev
rajeev = list(filter(lambda x: (x['parents_details']['father_name']=='rajeev'), a))
stu_mark = rajeev[0]['marks'][1]
print("Second subject mark of student whose father's name is Rajeev")
print(stu_mark)

#Display students name whose father's name ends with h
name = list(filter(lambda x: ((x['parents_details']['father_name']).endswith("h")), a))
print("Student's name whose father's name ends with h")
for i in range(len(name)):
    print(name[i]['name'])
    
#Students who got top mark irrespective of all subject and whose parents are not educated
print('Students who got top mark irrespective of all subject and whose parents are not educated')
max_mark = []
for i in range(0,6):
    max_mark.append(sum(a[i]['marks']))
print(max_mark)
def fun():
    maxi = max_mark[0]
    for i in range(1,6):
        if(max_mark[i]>maxi):
            maxi = max_mark[i]
            fun.n = i
fun()
if(a[fun.n]['parents_details']['parents_qualification'] == 'non-educated'):
    print(a[fun.n]['name'])
else:
    max_mark[fun.n] = 0
    fun()

#Students who got top mark irrespective of all subject in tamil medium
print('Students who got top mark irrespective of all subject in tamil medium')
max_mark = []
for i in range(0,6):
    max_mark.append(sum(a[i]['marks']))
print(max_mark)
def fun():
    maxi = max_mark[0]
    for i in range(1,6):
        if(max_mark[i]>maxi):
            maxi = max_mark[i]
            fun.n = i
fun()
if(a[fun.n]['medium'] == 'tamil'):
    print(a[fun.n]['name'])
else:
    max_mark[fun.n] = 0
    print(max_mark)
    fun()

#Delete the student from the array who got less than 30 in second subject
print('Delete the student from the array who got less than 30 in second subject')
b = a
less_in_sec = list(filter(lambda x: (x['marks'][1]<30) , b))
for element in less_in_sec:
    if element in b:
        b.remove(element)
print(b)

#Display students name whose fathers name are same
print('Display students name whose fathers name are same')
new_list = []
for i in range(6):
    for j in range(1,6):
        if(a[i]['parents_details']['father_name'] == a[j]['parents_details']['father_name']):
            new_list.append(a[i]['name'])
print(new_list)

    
