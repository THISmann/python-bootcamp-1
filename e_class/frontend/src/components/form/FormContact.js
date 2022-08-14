import React from 'react';
import "./form.css";
import FloatingLabel from 'react-bootstrap/FloatingLabel';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
//import phone from './assets/phone.png';
import contact from './assets/contact.png';

export default function FormContact() {
    return (
        <>
            <Container>
                <Row>
                    <Col className='FormContact_form' xs={6}>
                        <Form>
                            <FloatingLabel
                                controlId="floatingInput"
                                label="Email address"
                                className="mb-3"
                            >
                                <Form.Control type="email" placeholder="name@example.com" />
                            </FloatingLabel>

                            <FloatingLabel
                                controlId="floatingInput"
                                label="title"
                                className="mb-3"
                            >
                                <Form.Control type="text" placeholder="name@example.com" />
                            </FloatingLabel>

                            <FloatingLabel controlId="floatingTextarea2" label="Comments">
                                <Form.Control
                                    as="textarea"
                                    placeholder="Leave a comment here"
                                    style={{ height: '100px' }}
                                />
                            </FloatingLabel>


                            <Form.Group>
                                <Button className='mt-3' variant="outline-success">Success</Button>
                            </Form.Group>

                        </Form>
                    </Col>

                    <Col className='FormContact_img' xs={6}>
                        <img className="Form_img" src={contact} alt="img" />
                    </Col>
                </Row>
            </Container>
        </>
    );
}
