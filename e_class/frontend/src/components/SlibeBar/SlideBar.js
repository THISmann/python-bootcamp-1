import React from 'react';
import "./SlideBar.css";
import img1 from './assets/2.png';
import img2 from './assets/3.png';
import img3 from './assets/4.png';
import img4 from './assets/1.png'

export default function SlideBar() {
    return (
        <div className='SlideBar'>
            <h3> Student ....... </h3>
            <ul>
                {[
                    {
                        'source': img1,
                        'title': 'Course',
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
                    {
                        'source': img4,
                        'title': 'Note',
                        'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elits'
                    }
                ].map((list) => (
                    <li className="SlideBar_list" key={list} variant={list}>
                        <img src={list.source} alt={list.description} />
                        <p> {list.title} </p>
                    </li>
                ))}
            </ul>

        </div>
    )
}
