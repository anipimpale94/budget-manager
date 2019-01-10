// libraries
import React, { Component } from 'react';

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
      Name: "",
      Id: 0, 
      logAction: "Login"
    };

    this.accountHandler = this.accountHandler.bind(this);
    // this.accountLogOut = this.accountLogOut.bind(this);
  }

  accountLogOut = () => {
    this.setState({
      userActive: false,
      Name: "",
    });
  }

  accountHandler = (name, id) => {
    this.setState({
      userActive: true,
      Name: name,
      Id: id
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
              <p id="signupButton" onClick={(word) => this.formSwtich("Register")} className={this.state.logAction == "Register" ? "contentForm selected":"contentForm"}>Register</p>
              <p id="loginButton" onClick={(word) => this.formSwtich("Login")} className={this.state.logAction == "Login" ? "contentForm selected":"contentForm"}>Login</p>
            </div>
          }
          
          </div>
        </div>
        
        { this.state.userActive ? <Main Name={this.state.Name} /> : <Account accountHandler={this.accountHandler} action={this.state.logAction} /> }
        
      </div>
    );
  }
}

export default App;
