import addressbook_pb2
person = addressbook_pb2.Person()
person.id = 1234
person.name = "John Doe"
person.email = "jdoe@example.com"
phone = person.phones.add()
phone.number = "555-4321"
phone.type = addressbook_pb2.Person.HOME
#print(person.__str__())
# write to a file
f = open('person', 'wb')
f.write(person.SerializeToString())
f.close()

# read from a file
person = addressbook_pb2.Person()
f = open('person', "rb")
person.ParseFromString(f.read())
print(person.__str__())
f.close()