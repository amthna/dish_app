import React from 'react';
import countries from '../data/countries.js'
import CountryList from './CountryList';

function CountryTable() {
    return (
        <>
        
            <ol id="directory">


                    <CountryList countries={countries}></CountryList>

            </ol>
        </>
    );
}

export default CountryTable