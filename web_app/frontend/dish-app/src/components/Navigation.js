import React from 'react';
import { Link } from 'react-router-dom';


function Navigation() {
  return (
    <nav>
        <Link to="/">Home</Link>
        <Link to="../directory">Discover a dish</Link>
    </nav>
  );
}

export default Navigation;
