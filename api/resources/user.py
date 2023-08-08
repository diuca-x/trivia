from flask import jsonify, request
from flask_restful import Resource, abort

from users import users
#---import models
from models.question import Question
#--- import db
from extensions import db


class SingleQuestion(Resource):
    def get(self):
        all = Question.query.all()
        
        alldic = []
        for i in all:
            alldic.append(i.serialize())
        return jsonify({"result": alldic})

    def post(self):
        data = request.json
        to_add = Question(question = data.get("question"), answer= data.get("answer"))
        print(to_add.serialize())
        db.session.add(to_add)
        db.session.commit()

        return jsonify({"msg": "Question created", "added": to_add.serialize()})
    
class ModifyOrGetQuestion(Resource):
    def get(self, question_id):
        question = Question.query.get_or_404(question_id)

        

        return jsonify({"question": question.serialize()})

    def put(self, question_id):
        data = request.json

        question = Question.query.get_or_404(question_id)
        question.answer = data.get("answer")
        question.question = data.get("question")

        db.session.commit()
        

        return jsonify({"msg": "question updated", "question": question.serialize()})

    def delete(self, question_id):
        question = Question.query.get_or_404(question_id)


        db.session.delete(question)
        db.session.commit()



        return jsonify({"msg": "question deleted"})