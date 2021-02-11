import {useEffect, useState, } from 'react'
import logo from './arjun-logo.png';
import { BrowserRouter as Router, Route, Switch} from 'react-router-dom'

import Navigation from './components/Navigation';
import Home from './components/Home';
import Footer from './footer'
import New from './components/New'
import Exerciseinfo from './components/Exerciseinfo'



function App() {
  return (
    <Router>
    <div className="App">
      <Navigation />
      <div className="webContent">
        <Switch>
          <Route exact path="/">
            <Home />
          </Route>
          <Route  path="/new">
            <New />
          </Route>
          <Route  path="/exercise/:id">
            <Exerciseinfo />
          </Route>
        </Switch>

      </div>
      <Footer />
    </div>
    </Router>

  );

  }


export default App;