import React from "react";
import "./home.css";
import Navbar from "../../components/navbar/Navbar";
import Header from "../../components/header/Header";

function Home(props) {
    return (
        <>
            <Navbar className="nav" />
            <Header className="header" />
        </>
    );
}

export default Home;