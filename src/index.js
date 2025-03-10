import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import LandingPage from './components/LandingPage';
import LandingPageHTML from './LANDINGPAGE.HTML'; // This will be linked directly





import './index.css'; // Assuming you have some global styles

ReactDOM.render(
  <Router>
    <React.StrictMode>
      <Switch>
        <Route path="/" exact component={LandingPage} />
        <Route path="/landingpage" component={LandingPage} /> {/* Render LandingPage component */}




      </Switch>
    </React.StrictMode>
  </Router>,

  document.getElementById('root')
);
