
import React from 'react'
//import ReactDOM from 'react-dom'
//import React, { Component }  from 'react';
import { Routes, Route } from "react-router-dom";
import Home from './containers/home/Home';
import Eleve from './containers/eleves/Eleve';

function App() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/student" element={<Eleve />} />
    </Routes>
  );
}

export default App;
