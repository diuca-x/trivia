import { useEffect, useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'


import { BrowserRouter, Route, Routes } from "react-router-dom";
import injectContext from "./store/appContext";

import Home from './pages/home';
import Trivia from './pages/trivia';

function App() {

  const basename = import.meta.env.BASENAME || "";
  
  
  return (
    <div className='cont'>
        <BrowserRouter basename={basename}>
            
                
                <Routes>
                    <Route element={<Home />} path="/" />    
                    <Route element={<Trivia />} path="/trivia" />   
                    <Route element={<h1>Not found!</h1>} />
                </Routes>
                
            
        </BrowserRouter>
    </div>
);
}

export default injectContext(App)
