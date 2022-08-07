import './App.css';
import React from 'react'
//import ReactDOM from 'react-dom'
//import React, { Component }  from 'react';
import { Routes, Route } from "react-router-dom";
import Home from './containers/home/Home';

function App() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
    </Routes>
  );
}

export default App;
