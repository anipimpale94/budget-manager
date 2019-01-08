// libraries
import React, { Component } from 'react';
import { Button, FormGroup, FormControl, ControlLabel } from "react-bootstrap";
import axios from 'axios';

// css
import '../css/login.css';


class Login extends Component {

    constructor(props) {
        super(props);
    
        this.state = {
          email: "",
          password: "",
          error: "",
        };
    }
    
    validateForm() {
        return this.state.email.length > 0 && this.state.password.length > 5;
    }
    
    handleChange = event => {
        this.setState({
            [event.target.id]: event.target.value
        });
    }
    
    handleSubmit = event => {
        event.preventDefault();         
        axios({
            method: 'POST',
            // later change to public IP
            url: 'http://localhost:5000/login',
            data: {
                email: this.state.email,
                password: this.state.password
            },
            config: { headers: {'content-type': 'application/json' }}      
        })
        .then(res => {
            console.log(res.data);
            if(res.data.Email != null) {
                this.props.handler(res.data.Email, res.data.Name)
            } else {
                this.setState({
                    error: res.data.error
                });
            }
            
        }).catch(err => {
            console.warn('error:', err)
            this.setState({
                error: err
            });
        });
    }
    
    render() {
        return (
            <div className="loginForm">
                <form onSubmit={this.handleSubmit}>
                    <FormGroup controlId="email" bsSize="large">
                        <ControlLabel>Email</ControlLabel>
                        <FormControl
                            autoFocus
                            type="email"
                            value={this.state.email}
                            onChange={this.handleChange}
                        />
                    </FormGroup>
                    <FormGroup controlId="password" bsSize="large">
                        <ControlLabel>Password</ControlLabel>
                        <FormControl
                            value={this.state.password}
                            onChange={this.handleChange}
                            type="password"
                        />
                    </FormGroup>
                    { this.state.error === "" ? null : <div className="error">*{this.state.error}</div> }
                    <Button
                        block
                        bsSize="large"
                        disabled={!this.validateForm()}
                        type="submit"
                    >
                        Login
                    </Button>
                </form>
            </div>
        );
    }
}

export default Login;
