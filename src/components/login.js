import React, { Component } from 'react';

class Login extends Component {
  render() {
    return (
        <div className="loginForm">
            <div id="login">
                <input type="email" id="email" placeholder="Email"/>
                <input type="password" id="password" placeholder="Password"/>
                <button id="send">Send</button>
            </div>                             
        </div>
    );
  }
}

export default Login;
