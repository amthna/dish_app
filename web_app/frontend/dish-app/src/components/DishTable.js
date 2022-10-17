import React from 'react';
import countries from '../data/countries.js'
import { Link } from 'react-router-dom';

  

function DishTable() {
    return (

        <div>
            <ol>
           <li> <Link to="../dish_detail">Hamburger</Link></li>
           <li> <Link to="../dish_detail">Hotdog</Link></li>
           <li> <Link to="../dish_detail">Salad</Link></li>
           <li> <Link to="../dish_detail">Lasagna</Link></li>
           <li> <Link to="../dish_detail">Buffalo Wings</Link></li>
            </ol>
          
        </div>

    );
}

export default DishTable