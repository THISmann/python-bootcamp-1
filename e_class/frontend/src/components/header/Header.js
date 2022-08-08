import React from "react";
import "./header.css";
//import head1 from './assets/head1.png';
import head2 from './assets/head2.png';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';

function Header(props) {
    return (
        <>
            <Container>
                <Row>
                    <Col className="rigth" xs={6}>
                        <h1> Study management System </h1>
                        <p className="" > Lorem ipsum dolor sit amet consectetur adipisicing elit.
                            Mollitia aspernatur aperiam eum earum natus error ratione,
                            ut perspiciatis omnis? Quod sapiente dolorum fugit sint ipsum
                            quasi at sed! Blanditiis, nobis.Lorem ipsum dolor sit amet
                            consectetur adipisicing elit. Mollitia aspernatur aperiam eum
                            earum natus error ratione, ut perspiciatis omnis? Quod sapiente
                            dolorum fugit sint ipsum quasi at sed! Blanditiis, nobis. </p>
                        <button> Get Started Now </button>
                    </Col>
                    <Col xs={6}>
                        <img src={head2} className="head2" alt="illustration" srcset="" />
                    </Col>
                </Row>
            </Container>
        </>
    )
}

export default Header;