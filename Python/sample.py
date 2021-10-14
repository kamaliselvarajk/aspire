a = 'This is Hello World'
b = a.replace('Hello World', 'Aspire System')
print(b)

b = ['name', 'tess', 'ddddd', 'rest', 'raj', 'view', 'louu', 'nea']
vowel = 'aeiou'
lst = list(filter(lambda x: (x[-1] in vowel) , b))
print(lst)

c = 'RAKESH murali'
print(c.swapcase())

ip = 'This is Aspire Systems'
new = list(ip.split(' '))
print(new)
new.reverse()
print(new)
op = " ".join(new)
print(op)

op = [x for x in range(0,11,2)]
print(op)


ip = [1,2,3,4,5,6,7,10]
#for i in range((len(ip)-2)):
d = list(filter(lambda x: ip.index(x)<(len(ip)-1), ip))
print(d)
res = [x*2 for x in d]
print(res)
res.append(ip[-1])
print(res)
op = sum(res)
print(op)

def fun(*arg):
    a = list(filter(lambda x:x!=0 , arg))
    res = sum(a)
    print(res)
fun(1,2,3,4,5,6)

ip = [{
"id": "1",
"name": "Iphone 11",
"product_details": {
"ram": "2 GB",
"processor": "snapdragon",
"screen_size": "4 inch",
},
"cost": "50000",
"currency": "INR",
"category": "mobile",
"colour": "black"
},
{
"id": "2",
"name": "Samsung Galaxy",
"product_details": {
"ram": "2 GB",
"processor": "snapdragon",
"screen_size": "4 inch",
},
"cost": "45000",
"currency": "INR",
"category": "mobile",
"colour": "grey"
},
{
"id": "3",
"name": "Washing Machine",
"product_details": {
"machine_capacity": "6kg",
"machine_rpm": "50",
"type": "top_load"
},
"cost": "25000",
"currency": "INR",
"category": "washing-machine",
"colour": "blue"
},
{
"id": "4",
"name": "Samsung TV",
"product_details": {
"isSmart": "false",
"resolution": "UHD",
"screen_size": "55 inch",
},
"cost": "40000",
"currency": "INR",
"category": "tv",
"colour": "black"
}]

filtered = list(filter(lambda x: (x['product_details']['processor']=='snapdragon'), filter(lambda x: x["category"]=="mobile",ip)))
print(filtered)
#final = list(filter(lambda x: x['name'],filtered))
#print(final)
#print(filtered['name'])