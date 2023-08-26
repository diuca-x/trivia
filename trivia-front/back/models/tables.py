from extensions import db


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(), unique=False, nullable=False) 
    answer = db.Column(db.String(), unique=False, nullable=False)
    date = db.Column(db.DateTime, unique=False, nullable=False)

    options = db.relationship("Options", backref="question", lazy = True)
    

    def serialize(self):
        serialized_options = [i.serialize()["option"] for i in self.options]
        return {
            "id": self.id,
            "question": self.question, 
            "answer": self.answer,
            "options" : serialized_options,
            "date" : self.date.strftime("%d/%m/%Y")
        }
    
class Options(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False) 
    option = db.Column(db.String(), unique=False, nullable=False)
    
    #cliente = db.relationship("Cliente", backref="usuario", lazy = True)
    

    def serialize(self):
        
        return {
            "id": self.id,
            "question_id": self.question_id, 
            "option": self.option,
            
        }