a = [
{
"name":"rakesh",
"age":12,
"academics":{
"sslc":40,
"hsc":70
}
},
{
"name":"rakesh",
"age":12,
"academics":{
"sslc":60,
"hsc":70
}
},
{
"name":"rakesh",
"age":12,
"academics":{
"sslc":40,
"hsc":90
}
},
{
"name":"rakesh",
"age":12,
"academics":{
"sslc":80,
"hsc":70
}
},
{
"name":"rakesh",
"age":12,
"academics":{
"sslc":59,
"hsc":20
}
},
{
"name":"rajesh",
"age":12,
"academics":{
"sslc":100,
"hsc":70
}
}
]

print('both mark should be more than 60')
first = list(filter(lambda x:x['academics']['sslc']>60 and x['academics']['hsc']>60, a))
for i in range(len(first)):
    print(first[i])
print('------------------------------')

print('average should be 60')
avg = list(filter(lambda x:(x['academics']['sslc'] + x['academics']['hsc'])/2>60, a))    
for i in range(len(avg)):
    print(avg[i])
print('------------------------------')

print('Should double and display age who got more than 60 as average')
avg = list(filter(lambda x:(x['academics']['sslc'] + x['academics']['hsc'])/2>60, a))    
for i in range(len(avg)):
    print(avg[i]['name'], avg[i]['age']*2)
print('------------------------------')

