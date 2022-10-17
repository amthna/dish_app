import React, { useState } from 'react';
import { useHistory } from "react-router-dom";
// import { createExercise } from '../../../backend/model.mjs';
import CountryTable from '../components/CountryTable';


export const DirectoryPage = () => {

    return (
        <>
        <article>
            <h2>Directory</h2>
            <p>Select a nation to explore cuisine</p>
          
            </article>

            <CountryTable />
        </>
    );
}

export default DirectoryPage;