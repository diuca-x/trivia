import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import "../syles/trivia.css"

const Trivia = () =>{
    const [questions, setQuestions] = useState()
    const [question, setQuestion] = useState()
    const[index, setIndex] = useState(0) 
    const navigate = useNavigate()

    useEffect(() => {
        (async () => {
          try {
            
            const response = await fetch(import.meta.env.VITE_BACKEND_URL +`api/startGame/10`,
              {
                method: "GET",
                headers: {
                  "Content-Type": "application/json",
                },
              }
            );
            const result = await response.json();
            setQuestions(result)
            setQuestion(result[index])
          } catch (error) {
            console.log("Error loading message from backend");
          }
        })();
      }, []);

    useEffect(() => {
      if(Array.isArray(questions)){
        if(index == questions.length ){
          alert("finished")
          let c = 0
          for (let i of questions){
              if(i.correct == true){
                  c+=1
              }
          }
          alert(`number of correct answers: ${c}`)
          navigate('/', { replace: true })
        }
      }
      
    },[])
   
            
    const option_selectionator = async (option) => {
        let new_questions = questions
        let actual_question = new_questions[index]
        actual_question["answered"] = true
        if(option == question.answer){
            alert("exito")
            actual_question["correct"] = true
        } else{
            alert("no exito")
            actual_question["correct"] = false
        }
        new_questions[index] = actual_question 
        setQuestions(new_questions)
        setQuestion(questions[index+1])
        setIndex(index+1)
    }

    return(
        <>
            <div className="container-fluid text-center ">
                <div className="row "> <h1>Trivia</h1></div>
                <div className="row">
                    {question && (<>
                            <h2>{question.question}</h2>
                            {question.options.map((x,index) => {
                                return(
                                    <>
                                    <div className="col" key={index}><button className="custom-btn btn-14 my-3" onClick={() =>{option_selectionator(x)}}>{x}</button></div>
                                    </>
                                )
                            })}
                            
                            </>)}
                </div>
                <div className="row  mt-5">
                  <div class="progress_bar justify-content-center">
                  {question && (<>
                            {questions.map((x,index) => {
                              
                                return(
                                    <>
                                    <div class={`circle ${x.correct != null? x.correct == false? "incorrect":"correct" :"" }`}></div>
                                    </>
                                )
                            })}
                            
                            </>)}
                    
                    
                  </div>
                </div>
                
            </div>

        </>
    )
}


export default Trivia
