// libraries
import React, { Component } from 'react';

// components
import Login from './login';
import Register from './register';

class Account extends Component {

    constructor(props) {
        super(props);
    
        this.state = {
          login: true,
          register: false,
          error: ""
        };
    
        this.handler = this.accountHandler.bind(this)
    }
    
    accountHandler = (name, id) => {
        this.props.accountHandler(name, id);
    }

    render() {
        return(
            <div>
                { this.props.action === "Login" ? <Login handler={this.handler} /> : <Register handler={this.handler} /> }
            </div>
        );
    }
}

export default Account;