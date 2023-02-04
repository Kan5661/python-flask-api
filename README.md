person API with peewee

Person Model:
```
{
  name: CharField(),
  birthday = DateField()
  nationality = CharField()
  age = IntegerField()
  likes_chocolate = BooleanField()
  }
```
GET & POST request endpoint -> /person

endpoint /person/:id to GET, UPDATE, DELETE person by ID
