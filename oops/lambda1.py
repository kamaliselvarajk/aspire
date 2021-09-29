from functools import reduce
b = [
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
        

print('filter the student whose average is grater than 40')
avg = list(filter(lambda x:sum(x['marks'])/len(x['marks'])>40, b))
for i in range(len(avg)):
    print(avg[i])
print('------------------------------')

print('filter the student who got pass mark in all the subjects (pass mark 30)')
mark = list(filter(lambda x:x['marks'][0]>30 and x['marks'][1]>30 and x['marks'][2]>30 and x['marks'][3]>30 and x['marks'][4]>30, b))
for i in range(len(mark)):             
    print(mark[i]['name'])
print('------------------------------')

print('filter the student who got pass mark in all the subjects and whose parents are not-educated')
for i in range(5):
    mark = list(filter(lambda x:(x['marks'][i])>30 and x["parents_details"]["parents_qualification"] == "non-educated", b))     
for i in range(len(mark)):
    print(mark[i]) 
print('------------------------------')  

print('Find the student who got top most mark irrespective of all the subject and whose parents are not educated')
'''maxmark = []
for i in range(len(b)):
    maxmark.append(sum(b[i]['marks']))
def max():  
    maxi = maxmark[0]
    for i in range(1,len(b)):    
        if maxmark[i]  > maxi:
            maxi = maxmark[i]
            max.index = i
    if b[max.index]["parents_details"]["parents_qualification"] == "non-educated":
        print(b[max.index]['name'])
    else:
        maxmark[max.index] = 0
        max()        
max()'''
sum=[]
for i in range(len(b)):
    sum.append(reduce(lambda a,b:a+b,b[i]['marks']))
def fun():
    maxList = reduce(lambda v1, v2: max(v1, v2), sum)
index = sum.index(max(sum))
if b[index]["parents_details"]["parents_qualification"] == "non-educated":
    print(b[index]['name'])
else:
    sum[index] = 0
    fun()
print('------------------------------') 

print('Find the student who got top most mark irrespective of all the subject in tamil medium')
sum=[]
for i in range(len(b)):
    sum.append(reduce(lambda a,b:a+b,b[i]['marks']))
def fun():
    maxList = reduce(lambda v1, v2: max(v1, v2), sum)
index = sum.index(max(sum))
print(index)
if b[index]["medium"] == "tamil":
    print(b[index]['name'])
else:
    sum[index] = 0    
    fun()
print('------------------------------') 

print('Find the no of the studetns passed: pass mark (30)')
mark = list(filter(lambda x:x['marks'][0]>30 and x['marks'][1]>30 and x['marks'][2]>30 and x['marks'][3]>30 and x['marks'][4]>30, b))
print(len(mark))  
print('------------------------------') 

print('Display sundar\'s 4th subject mark')
mark = list(filter(lambda x:(x['name']== 'sundar'), b))
print(mark[0]['marks'][3])
print('------------------------------') 

print('Display 2nd subject mark of the student whose father name is "Rajeev"')
mark = list(filter(lambda x:(x["parents_details"]["father_name"]== "rajeev"), b))
print(mark[0]['marks'][1])
print('------------------------------') 

print('Display students name whose father names are same')
samefather = [] 
for i in range(len(b)):
    for j in range(1, len(b)):
        if(b[i]["parents_details"]["father_name"] == b[j]["parents_details"]["father_name"]):
            samefather.append(b[i]['name'])
print(samefather)            
print('------------------------------') 

print('Display students name whose father name ends with h')
mark = list(filter(lambda x:(x["parents_details"]["father_name"].endswith('h')), b))
for i in range(len(mark)):
    print(mark[i]['name'])
print('------------------------------') 

print('Delete the student from the array who got less than 30 in the second subject')
c = b   
d = b
mark = list(filter(lambda x:(x["marks"][1]) < 30, c)) 
for i in mark:
    if i in c:
        c.remove(i)
print(c)
print('------------------------------') 

