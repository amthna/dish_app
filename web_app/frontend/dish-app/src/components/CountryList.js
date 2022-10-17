import React from 'react';
import CountryRow from './CountryRow';

function CountryList({ countries }) {
    return (
        <>
            
                {countries.map((country) => <CountryRow country={country} key={country.id} />)}
        
        </>
    );
}

export default CountryList