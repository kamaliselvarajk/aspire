a = [
 {
 "name":"rakesh",
 "age":"12",
 "academics":{
 "sslc":40,
 "hsc":70
 }
 },
 {
 "name":"raj",
 "age":"12",
 "academics":{
 "sslc":60,
 "hsc":70
 }
 },
 {
 "name":"kumar",
 "age":"12",
 "academics":{
 "sslc":40,
 "hsc":90
 }
 },
 {
 "name":"sathish",
 "age":"12",
 "academics":{
 "sslc":80,
 "hsc":70
 }
 },
 {
 "name":"ragu",
 "age":"12",
 "academics":{
 "sslc":59,
 "hsc":20
 }
 },
 {
 "name":"sundar",
 "age":"12",
 "academics":{
 "sslc":100,
 "hsc":70
 }
 }
]

#Both mark should be more than 60
print('Students who secured more than 60 in both sslc and hsc')
mark = list(filter(lambda x: x['academics']['sslc'] > 60 and x['academics']['hsc'] >60, a))
for i in range(len(mark)):
    print(mark[i]['name'])


#Average should be 60
print('Students whose average sholud be 60')
mark = list(filter(lambda x: (x['academics']['sslc'] + x['academics']['hsc'])/2 >= 60, a))
for i in range(len(mark)):
    print(mark[i]['name'])

#Should double and display age who got more than 60 as average (doubt)
print("Student's doubled age who got more than 60 as average")
mark = list(filter(lambda x: x['academics']['sslc'] > 60 and x['academics']['hsc'] >60, a))
b = 2
for i in range(len(mark)):
    x = int(mark[i]['age'])
    print(x + x)

#Total the sslc mark and display who got more than 60 as average
print('Sum of sslc mark of students whot got more than 60 as average')
mark = list(filter(lambda x: x['academics']['sslc'] > 60 and x['academics']['hsc'] >60, a))
sum = 0
for i in range(len(mark)):
    sum += mark[i]['academics']['sslc']
print(sum)











