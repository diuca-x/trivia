import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import "../syles/trivia.css"

const Trivia = () =>{
    const [questions, setQuestions] = useState()
    const [question, setQuestion] = useState()
    const[index, setIndex] = useState(0) 
    const navigate = useNavigate()

    const[hint, setHint] = useState("") 

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

    
   
            
    const option_selectionator = (option) => {
      
        let new_questions = [...questions]
        let new_question = question
        new_question["answered"] = true
        if(option == question.answer){  
          new_question["correct"] = true
        } else{
          new_question["correct"] = false
        }
        new_questions[index] = new_question 
        setQuestions(new_questions)
        setQuestion(new_question)
      
    }

    const go_nextinator = () =>{
      setQuestion(questions[index+1])
      let new_index = index
      new_index = new_index + 1
      setIndex(new_index)
      setHint("")
    }

    const question_removinator = () =>{
      let remove = question.answer
      while (remove == question.answer){
        remove = question.options[Math.floor(Math.random()*question.options.length)];
      }
      setHint(remove)
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
                                    <div className="row" key={index}>
                                      <div className="col-12"  ><button  className={`custom-btn btn-14 my-3 ${question.correct != null? x != question.answer ? "incorrect":"correct" :"" } ${x == hint? "incorrect":""}`} 
                                      disabled={x == hint} onClick={() =>{question.answered == false? option_selectionator(x):""}}>{x}</button></div>
                                    </div>
                                )
                            })}
                            <div className="row">

                            <button  className={` rounded w-25 me-auto my-3`} disabled={question.answered || hint != ""} onClick={() =>{ question_removinator()}}>Hint</button>
                                <button className=" my-3 rounded w-25 ms-auto " onClick={() =>{go_nextinator()}} disabled={!question.answered} data-bs-toggle = {index +1 == questions.length?"modal":""}
                              data-bs-target= {index +1 == questions.length? "#exampleModal":""}
                              >{index +1 == questions.length? "Finish":"Next"} </button>
                            
                            </div>
                            
                            </>)}
                            
                </div>
                
                <div className="row  mt-5">
                  <div className="progress_bar justify-content-center">
                  {question && (<>
                            {questions.map((x,index) => {
                              
                                return(
                                    <>
                                    <div key={index} className={`circle ${x.correct != null? x.correct == false? "incorrect":"correct" :"" }`}></div>
                                    </>
                                )
                            })}
                            
                            </>)}
                  </div>
                </div>
                
            </div>
            
            <div className="modal fade" id="exampleModal" tabIndex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                              <div className="modal-dialog">
                                <div className="modal-content">
                                  <div className="modal-header">
                                    <h1 className="modal-title fs-5" id="exampleModalLabel">Finished!</h1>
                                    <button type="button" className="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                  </div>
                                  <div className="modal-body">
                                  {`number of correct answers: ${questions? questions.filter(x => x.correct === true).length : ""}`}
                                  <div className="progress_bar justify-content-center">
                                   
                                    {questions && (<>
                                              {questions.map((x,index) => {
                                                
                                                  return(
                                                      <>
                                                      <div key={index} className={`circle my-5 ${x.correct != null? x.correct == false? "incorrect":"correct" :"" }`}></div>
                                                      </>
                                                  )
                                              })}
                                              
                                  </>)}
                  </div>
                                  </div>
                                  <div className="modal-footer">
                                    <button type="button" className="btn btn-secondary" data-bs-dismiss="modal" onClick={() => {navigate('/', { replace: true })}}>Back to menu</button>
                                    
                                  </div>
                                </div>
                              </div>
                            </div>
        </>
    )
}


export default Trivia
