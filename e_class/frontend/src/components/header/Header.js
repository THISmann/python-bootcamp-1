import React from "react";
import "./header.css";
//import head1 from './assets/head1.png';
import head2 from './assets/head2.png';

function Header(props) {
    return (
        <>
            <div className="header">
                <div className="left">
                    <h1> test</h1>
                </div>
                <div className="rigth">
                    <img src={head2} className="head2" alt="illustration" srcset="" />
                </div>
            </div>
        </>
    )
}

export default Header;