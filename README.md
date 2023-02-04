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


Chair model
```
  {
    chair_type = CharField()
    material = CharField()
    color = CharField()
    price = IntegerField()
    rating = DecimalField(max_digits=2, decimal_places=1)
  }
```
/chair enpoint only supports GET & POST