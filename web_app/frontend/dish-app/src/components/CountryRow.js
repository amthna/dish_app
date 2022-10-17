import React from 'react';
import Collapse from './Collapse';
import DishTable from'./DishTable';

function CountryRow({ country }) {
    return (
        <Collapse country={country}>
            <h2>Here are {country.name}'s most popular traditional dishes</h2>
            <h3>Select a recipe to view its unique flavors and cooking methods.</h3>
            <DishTable />
        </Collapse>

    );
}

export default CountryRow