import React from 'react';
import ReactDOM from 'react-dom';
import {HashRouter as Router, Route, Switch} from 'react-router-dom';
import Home from './components/Home';
import Login from './components/Login';
import NotFound from './components/NotFound';


ReactDOM.render(
    <Router>
    <div>
      <Switch>
        <Route exact path="/" component={Home}/>
        <Route exact path="/login" component={Login}/>
        <Route component={NotFound}/>
      </Switch>
    </div>
    </Router>,
    document.getElementById('root')
)