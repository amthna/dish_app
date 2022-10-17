import React from 'react';
import Collapse from './Collapse';
import DishTable from'./DishTable';

function CountryRow({ country }) {
    return (
        <Collapse country={country}>
            <h1>Here are {country.name}'s most popular traditional dishes:</h1>
            <DishTable />
        </Collapse>

    );
}

export default CountryRow