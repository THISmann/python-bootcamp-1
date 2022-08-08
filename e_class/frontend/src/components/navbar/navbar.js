import React from "react";
import "./navbar.css";
import logo from './assets/logo.png'
import { FaUser } from 'react-icons/fa'
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';


//import {BiUser} from 'react-icons/bi'

function Navbar(props) {
    return (
        <>
            <Container fluid>
                <Row>
                    <Col xs={6}>
                        <img src={logo} className="logo-img" alt="logo" />
                    </Col>
                    <Col xs={6}>
                        <ul className="navbar-list">
                            <li>home</li>
                            <li>about</li>
                            <li>service</li>
                            <li> <FaUser /> Sign-in </li>
                            <li className="getStarted"> Get Started</li>
                        </ul>
                    </Col>
                </Row>
            </Container>
        </>
    );
}

export default Navbar;