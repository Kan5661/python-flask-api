from peewee import *
from flask import Flask, request, jsonify
from playhouse.shortcuts import model_to_dict, dict_to_model
from datetime import date

db = PostgresqlDatabase('person_but_more', user='kanlin', password='12345',
                        host='localhost', port=5432)

db.connect()

class BaseModel(Model):
    class Meta:
        database = db

class Person(BaseModel):
    name = CharField()
    birthday = DateField()
    nationality = CharField()
    age = IntegerField()
    likes_chocolate = BooleanField()

db.drop_tables([Person])
db.create_tables([Person])

kan = Person(name='kan', birthday=date(2002, 7, 18), nationality='Chinese American', age=20, likes_chocolate=True)
kan.save()

app = Flask(__name__) 


#Get/Read functionalities 
@app.route('/person/', methods=['GET', 'POST'])
@app.route('/person/<id>', methods=['GET', 'PUT', 'DELETE'])
def person(id=None):
    if request.method == 'GET':
        if id:
            return jsonify(model_to_dict(Person.get(Person.id == id)))
        else:
            people_list = []
            for person in Person.select():
                people_list.append(model_to_dict(person))
            return jsonify(people_list)

    if request.method == 'POST':
        new_person = dict_to_model(Person, request.get_json())
        new_person.save()
        return jsonify({"success": True})
    
    if request.method == 'DELETE':
        Person.delete().where(Person.id == id).execute()
        return f"person {id} deleted"


app.run(debug=True, port=1234)