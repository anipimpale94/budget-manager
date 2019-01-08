// libraries
import React, { Component } from 'react';

// components
import Login from './login';
import Register from './register';

class Account extends Component {

    constructor(props) {
        super(props);
    
        this.state = {
          email: "",
          name: "",
          login: true,
          register: false
        };
    
        this.handler = this.accountHandler.bind(this)
    }
    
    accountHandler = (email, name) => {
        this.setState({
          email: email,
          name: name,
        })

        this.props.accountHandler(true, name);
    }

    render() {
        return(
            <div>
                { this.props.action == "Login" ? <Login handler={this.handler} /> : <Register handler={this.handler} /> }
            </div>
        );
    }
}

export default Account;