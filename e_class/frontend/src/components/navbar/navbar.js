import React from "react";
import "./navbar.css";

function Navbar(props) {
    return (
        <>
            <div className="navbar" >
                <ul className="navbar-list">
                    <li> logo </li>
                    <li>home</li>
                    <li>about</li>
                    <li>service</li>
                </ul>
            </div>
        </>
    );
}

export default Navbar;