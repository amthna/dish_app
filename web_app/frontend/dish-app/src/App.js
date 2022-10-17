// Import dependencies
import React from 'react';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import { useState } from 'react';

// Import Components, styles, media
import Navigation from './components/Navigation';
import './App.css';

// Import Pages
import HomePage from './pages/HomePage';
import Directory, { DirectoryPage } from './pages/Directory';
import DishDetail from './pages/DishDetail';

// Define the function that renders the content in routes using State.
function App() {

  return (
    <>
      <Router>

          <header>
            <h1>Dishy</h1>
            <p>Explore the textures of global cuisine</p>
          </header>

          <Navigation />

          <main>
          <Route path="/directory">
              <DirectoryPage />
            </Route>
            <Route path="/dish_detail">
              <DishDetail />
            </Route>
          </main>

          <footer>
            <p>© 2022 Andrew Mathena</p>
          </footer>

      </Router>
    </>
  );
}

export default App;