from extensions import db


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(), unique=False, nullable=False) 
    answer = db.Column(db.String(), unique=False, nullable=False)

    options = db.relationship("Option", backref="question", lazy = True)
    

    def serialize(self):
        return {
            "id": self.id,
            "question": self.question, 
            "answer": self.answer
        }
    
class Option(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False) 
    option = db.Column(db.String(), unique=False, nullable=False)

    #cliente = db.relationship("Cliente", backref="usuario", lazy = True)
    

    def serialize(self):
        return {
            "id": self.id,
            "question_id": self.question_id, 
            "option": self.option
        }