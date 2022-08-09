import React from "react";
import "./service.css";
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import img1 from './assets/2.png';
import img2 from './assets/3.png';
import img3 from './assets/4.png';
import img4 from './assets/5.png'
//import Alert from 'react-bootstrap/Alert';

export default function Service(props) {
    return (

        <>
            <Container>
                <Row>
                    {[
                        {
                            'source': img1,
                            'title': 'data virsualisation',
                            'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elits'
                        },
                        {
                            'source': img2,
                            'title': 'student record',
                            'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elits'
                        },
                        {
                            'source': img4,
                            'title': 'parent reccord',
                            'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elits'
                        },
                        {
                            'source': img3,
                            'title': 'teacher management',
                            'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elits'
                        }
                    ].map((variant) => (
                        <Col className="service" xs={3} key={variant} variant={variant}>
                            <img className="img" src={variant.source} alt="img"/>
                            <h3> {variant.title} </h3>
                            <p> {variant.description}   </p>
                        </Col>
                    ))}
                </Row>
            </Container>

        </>
    );
}
