// libraries
import React, { Component } from 'react';
import axios from 'axios';

// components
import Account from './components/account';
import Main from './components/main';

// css
import './css/App.css';

class App extends Component {

  constructor(props) {
    super(props);

    this.state = {
      userActive: false,
      name: "",
      id: 0, 
      logAction: "Login",
      error: "",
    };

    this.accountHandler = this.accountHandler.bind(this);
  }

  componentWillMount() {
    let token = localStorage.token;
    axios.get(`http://localhost:5000/api/session?jwt=` + token)
    .then(res => {
      if(res.data.active === "true") {
        this.setState({
          userActive: true,
          name: res.data.name,
          id: res.data.id,
        })
      }     
    })
    .catch(err => {
      console.warn('error:', err)
    });
  }

  accountLogOut = () => {
    this.setState({
      userActive: false,
      name: "",
      id: -1
    });
  }

  accountHandler = (name, id) => {
    this.setState({
      userActive: true,
      name: name,
      id: id,
    });
  }

  formSwtich = (action) => {
    this.setState({
      logAction: action
    });
  }

  render() {
    return (
      <div className="body container">

        <div className="header">
          <div>
            <h3 id="appName">Budget Manager</h3>
          </div>   
          <div id="buttons">
          {
            this.state.userActive ?
            <p id="logOutButton" onClick={() => this.accountLogOut()} className="contentForm ">Logout</p> :
            <div>
              <p id="signupButton" onClick={(word) => this.formSwtich("Register")} className={this.state.logAction === "Register" ? "contentForm selected":"contentForm"}>Register</p>
              <p id="loginButton" onClick={(word) => this.formSwtich("Login")} className={this.state.logAction === "Login" ? "contentForm selected":"contentForm"}>Login</p>
            </div>
          }
          
          </div>
        </div>
        
        { this.state.userActive ? <Main name={this.state.name} /> : <Account accountHandler={this.accountHandler} action={this.state.logAction} /> }
        
      </div>
    );
  }
}

export default App;
