import React from 'react';
import './Eleve.css';
import Dashhead from '../../components/DashHeard/Dashhead';
import SlideBar from '../../components/SlibeBar/SlideBar';

export default function Eleve() {
  return (
    <>
      <div className='Student'>
        <div>
          <SlideBar />
        </div>

        <div>
          <Dashhead />
        </div>
      </div>


    </>

  )
}
