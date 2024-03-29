import React, { useState } from 'react';
import './Dashboard.css';
import Container from 'react-bootstrap/Container';
import Table from 'react-bootstrap/Table';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import img1 from './assets/2.png';
import img2 from './assets/3.png';
import img3 from './assets/4.png';
import { Bar } from 'react-chartjs-2';
import { CDBContainer } from 'cdbreact';
import { Chart as ChartJS } from 'chart.js/auto';
import { Chart } from 'react-chartjs-2';
//import img4 from './assets/1.png'


export default function Dashhead() {
    const [data] = useState({
        labels: ['Maths', 'Physic', 'computer science', 'history', 'Coding', 'Arts', 'Music'],
        datasets: [
            {
                label: 'My First dataset',
                backgroundColor: 'rgba(194, 116, 161, 0.5)',
                borderColor: 'rgb(194, 116, 161)',
                data: [35, 25, 40, 75, 56, 55, 40],
            },
            {
                label: 'My Second dataset',
                backgroundColor: 'rgba(71, 225, 167, 0.5)',
                borderColor: 'rgb(71, 225, 167)',
                data: [30, 30, 40, 19, 56, 27, 70],
            },
            {
                label: 'My last dataset',
                backgroundColor: 'rgba(71, 25, 167, 0.5)',
                borderColor: 'rgb(71, 225, 167)',
                data: [25, 35, 14, 29, 56, 17, 70],
            },
        ],
    });
    return (
        <Container className='Dashheads'>
            <Row className='Dashboad_head'>
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
                        'source': img3,
                        'title': 'parent reccord',
                        'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elits'
                    },

                ].map((variant) => (
                    <Col className="dashbord_item" xs={3} key={variant} variant={variant}>
                        <img className="img" src={variant.source} alt="img" />
                        <div>
                            <h6> {variant.title} </h6>
                            <p> price : 23 </p>
                            <p> Hello </p>
                        </div>
                    </Col>
                ))}
            </Row>

            <Row className='m-1'>
                <Table striped bordered hover>
                    <thead>
                        <tr>
                            <th>#</th>
                            <th>First Name</th>
                            <th>Last Name</th>
                            <th>Username</th>
                        </tr>
                    </thead>
                    <tbody>
                        {[{
                            'a': '1',
                            'b': '2',
                            'c': '3',
                            'd': '4'
                        }].map((data) => (
                            <tr>
                                <td>{data.a}</td>
                                <td>{data.b}</td>
                                <td>{data.c}</td>
                                <td>{data.d}</td>
                            </tr>
                        ))}  
                    </tbody>
                </Table>
            </Row>
            <Row>
                <CDBContainer>
                    <h3 className="mt-5">Bar chart</h3>
                    <Bar data={data} options={{ responsive: true }} />
                </CDBContainer>
            </Row>
        </Container>
    );
}
