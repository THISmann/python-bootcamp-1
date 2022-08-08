import React from "react";
import "./navbar.css";
import logo from './assets/logo.png'
import { FaUser } from 'react-icons/fa'
//import {BiUser} from 'react-icons/bi'

function Navbar(props) {
    return (
        <>
            <div className="navbar" >
                <div className="logo">
                    <img src={logo} className="logo-img" alt="logo" />
                </div>
                <ul className="navbar-list">
                    <li>home</li>
                    <li>about</li>
                    <li>service</li>
                    <li> <FaUser /> Sign-in </li>
                    <li className="getStarted"> Get Started</li>
                </ul>
            </div>
        </>
    );
}

export default Navbar;