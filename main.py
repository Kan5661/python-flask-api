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

class Chair(BaseModel):
    chair_type = CharField()
    material = CharField()
    color = CharField()
    price = IntegerField()
    rating = DecimalField(max_digits=2, decimal_places=1)



db.drop_tables([Person, Chair])
db.create_tables([Person, Chair])

chair_1 = Chair(chair_type='rocking chair', material='wood', color='red', price=2, rating=5)
chair_1.save()
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


@app.route('/chair/', methods=['GET', 'POST'])
@app.route('/chair/<id>', methods=['GET'])
def chair(id=None):
    if request.method == 'GET':
        if id:
            return jsonify(model_to_dict(Chair.get(Chair.id == id)))
        else:
            chair_list = []
            for chair in Chair.select():
                chair_list.append(model_to_dict(chair))
            return jsonify(chair_list)

    if request.method == 'POST':
        new_chair = dict_to_model(Chair, request.get_json())
        new_chair.save()
        return jsonify({"success": True})

app.run(debug=True, port=1234)