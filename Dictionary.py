# Python Dictionary
student = {
"FName": "James",
"Lname": "Bond",
"Phone": 72345532,
"Email": "jamesbond@gmail.com"
}

print(student)
car = {
  "brand":"Lamboghini",
  "model":"Urus",
  "electric":False,
   "year":2015,
}
print(car)

y=car.keys()
print (y)

z=car.values()
print(z)

if "model" in car:
  print ("yes 'model'is one of the keys in the dictionary.")

  car ["year"]=2018
  print(car)

  car["model"]="Aventador"
  print(car)

car["color"]="red"
print(car)

for x in car:
  print(x)
for x in car.values():
  print (x)
  #Nested Dictionary
myFamily= {
 "Child1":{
  "Name":"Emil",
  "year":2004
 },
  "Child2":{
  "name":"Tobius",
  "year":2007
  },
  "Child3":{
  "name":"Linus",
  "year":2011
  ,}
}
