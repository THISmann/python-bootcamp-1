import React from "react";
import "./home.css"; 
import Navbar from "../../components/navbar/Navbar";
import Header from "../../components/header/Header";
import Service from "../../components/services/Service";
import Contact from "../../components/contact/Contact";
import Form from "../../components/form/FormContact";

function Home(props) {
    return (
        <>
            <Navbar className="nav" />
            <Header className="header" />
            <Service />
            <Form />
            <Contact />
        </>
    );
}

export default Home;