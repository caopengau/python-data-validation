from pydantic import BaseModel, ValidationError
 
class Person(BaseModel):
    age: int
    name: str
    is_married: bool
 
data = {
    'name': 'John',
    'age': 20,
    'is_married': False
}

try:
    person = Person(**data)
    print(person.dict())
 
except ValidationError as e:
    print(e)


invalidData = {
    'age': "test",
    'is_married': False
}
try:
    person = Person(**invalidData)
    print(person.dict())
 
except ValidationError as e:
    print(e)