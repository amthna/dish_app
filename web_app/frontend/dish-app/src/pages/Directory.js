import React, { useState } from 'react';
import { useHistory } from "react-router-dom";
// import { createExercise } from '../../../backend/model.mjs';
import CountryTable from '../components/CountryTable';


export const DirectoryPage = () => {

    return (
        <>
        <article>
            <h1>Directory</h1>
            <h2>Select a nation to explore its most popular traditional dishes, or <a href="https://www.w3schools.com">discover a random dish.</a></h2>
          
            </article>

            <CountryTable />
        </>
    );
}

export default DirectoryPage;