import random


def give_answer(question_dic):
    options3 = []

    options = question_dic.get("options")
    random.shuffle(options)
    for i in range(2):
        options3.append(options[i])

    options3.append(question_dic.get("answer"))
    random.shuffle(options3)
    question_dic["options"] = options3

    question_dic["answered"] = False
    
    del question_dic["id"]

    return question_dic