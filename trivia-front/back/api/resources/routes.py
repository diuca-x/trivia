
from flask import jsonify, request, make_response
from api.resources.functions import give_answer
from flask_restful import Resource, abort

#---import models
from models.tables import Question, Options

#--- import db
from extensions import db

import random
#--- for excel reading

from flask import  render_template, request

from datetime import datetime

from flask_jwt_extended import jwt_required

class SingleQuestion(Resource): #to get all questions, or create a new one
    method_decorators=[jwt_required()]
    def get(self):
        all = Question.query.all()
        
        alldic = []
        for i in all:
            question_dic = i.serialize()
            alldic.append(question_dic)
            
        return jsonify(alldic)
    

    def post(self):
        data = request.json

        options = data.get("options")
        
        if not data.get("question") or not data.get("answer") or not options or not data.get("date"):
            return make_response(jsonify({"msg" : "missing data"}),400)
        if len(options) < 2:
            return make_response(jsonify({"msg" : "need to have at least 2 options, coudnt create question " + data.get("question")}),400)

        date_to_add = datetime.strptime(data.get("date"), '%d/%m/%Y')

        question_to_add = Question(question = data.get("question"), answer= data.get("answer"), date = date_to_add)
        db.session.add(question_to_add)
        db.session.commit()
        

        for i in options:
            option_to_add = Options(option = i, question_id=question_to_add.id)
            db.session.add(option_to_add)
        db.session.commit()

        return jsonify({"msg": "Question created", "question": question_to_add.serialize(), "options": options})
    
class specificQuestion(Resource): # to get a specific question, modify an existen one (not the options) or delete one
    def get(self, question_id):
        question = Question.query.get_or_404(question_id)
        return jsonify(question.serialize())

    def put(self, question_id):
        data = request.json
        question = Question.query.get_or_404(question_id)

        if not data.get("question") or not data.get("answer"):
            return make_response(jsonify({"msg" : "missing data"}),400)
        
        
        question.answer = data.get("answer")
        question.question = data.get("question")
        db.session.commit()

        options = question.serialize()["options"]

        if data.get("answer") in options:
            return jsonify({"msg": "question updated, but answer already in options", "result": question.serialize()})
        else :
            return jsonify({"msg": "question updated", "result": question.serialize()})

    def delete(self, question_id): #deletes a question and all options
        question = Question.query.get_or_404(question_id)
        
        options = Options.query.filter_by(question_id = question_id).all()
        if len(options) > 0: 
            for i in options:
                db.session.delete(i)
        db.session.delete(question)

        

        db.session.commit()

        return jsonify({"msg": "question deleted"})
    
class addOptions(Resource): # to get the options for a question or add an option for an existing question
    def get(self,question_id):
        options = Options.query.filter_by(question_id = question_id)
        serialized_options = [i.serialize() for i in options]

        return jsonify(serialized_options)
    def post(self,question_id):
        data  = request.json
        option = data.get("option")
        question = Question.query.get_or_404(question_id)

        option_to_add = Options(question_id = question_id,option = option )
        db.session.add(option_to_add)

        question.options.append(option_to_add)
        db.session.commit()

        if not option:
            return make_response(jsonify({"msg" : "missing data"}),400)
        return  jsonify({"msg": "option added", "question" : question.serialize()})
    
class handleOption(Resource): #to get a specific option, delete an option or modify it
    def get(self,option_id):
        option = Options.query.get_or_404(option_id)
        result = option.serialize()
        result["question"] = option.question.serialize()["question"]
        return jsonify(result)
    
    def put(self,option_id):
        data = request.json
        new_option = data.get("option")
        old_option = Options.query.get_or_404(option_id)

        if not new_option:
            return make_response(jsonify({"msg" : "missing data"}),400)

        old_option.option = new_option

        db.session.commit()
        
        result = old_option.serialize()
        result["question"] = old_option.question.serialize()["question"]

        return jsonify({"msg":"question modified", "result": result})
    
    def delete(self, option_id):
        option = Options.query.get_or_404(option_id)
        
        print(option.question_id)
        question = Question.query.get(option.question_id)

        if len(question.options) <= 3: 
            return make_response(jsonify({"msg" : "A question can't have less than 3 options!"}),400)
        

        db.session.delete(option) 
        db.session.commit()

        return jsonify({"msg": "question deleted"})

class startGame(Resource): #to start the game
    def get(self,ammount):

        today_questions = Question.query.filter_by(date = datetime.today().replace(hour=0, minute=0, second=0,microsecond=0 )).all()
        random.shuffle(today_questions) 
        
        

        if(ammount > len(today_questions)):
            return jsonify({"msg": "not enough questions!"})   
         
        alldic = []
        if(ammount == 0):
            ammount = len(today_questions)
        c = 0
        
         
        while c < ammount:     
            question_dic = today_questions[c].serialize()
            question_result = give_answer(question_dic)
            alldic.append(question_result)

            c+=1
            
        
        return jsonify(alldic)            
        

class asd(Resource): #to test
    def get(self):


        questions = Question.query.filter_by(date = datetime.today().replace(hour=0, minute=0, second=0,microsecond=0 )).all()

        questions = Question.query.all()
        for i in questions:
            print(i.date)
        
        print(questions)

        return jsonify({"msg":"asd"})