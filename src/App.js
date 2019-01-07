import React, { Component } from 'react';
// import logo from './logo.svg';

// components
import Login from './components/login';
import Register from './components/register'

// css
import './css/App.css';

class App extends Component {

  constructor(props) {
    super(props);

    this.state = {
      email: "",
      password: "",
      login: false,
      register: true
    };
  }

  formSwtich = (word) => {
    var register,login;
    if(word === "register") {
      register = true;
      login = false;
    }
    else {
      login = true;
      register = false;
    }    
    this.setState({
      login: login,
      register: register
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
            <p id="signupButton" onClick={(word) => this.formSwtich("register")} className={this.state.register ? "contentForm selected":"contentForm"}>Register</p>
            <p id="loginButton" onClick={(word) => this.formSwtich("login")} className={this.state.login ? "contentForm selected":"contentForm"}>Login</p>
          </div>
        </div>
          
        <div>
          { this.state.register?<Register /> : null }
          { this.state.login? <Login /> : null }
        </div>
      </div>
    );
  }
}

export default App;
