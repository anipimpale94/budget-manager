// libraries
import React, { Component } from 'react';
import { Button, FormGroup, FormControl, ControlLabel } from "react-bootstrap";
import axios from 'axios';

// css
import '../css/register.css';

class Register extends Component {

    constructor(props) {
        super(props);
    
        this.state = {
            name: "",
            email: "",
            password: "",
            confirm_password: "",
            error: "",
        };
    }
    
    validateForm() {
        return this.state.email.length > 0 && this.state.password.length > 5 && this.state.name.length > 0 && this.state.password === this.state.confirm_password;
    }
    
    handleChange = event => {
        this.setState({
            [event.target.id]: event.target.value
        });
    }
    
    handleSubmit = event => {
        this.setState({
            error: ""
        });
        event.preventDefault();         
        axios({
            method: 'POST',
            url: 'http://localhost:5000/api/register',
            data: {
                name: this.state.name,                
                email: this.state.email,
                password: this.state.password,
            },
            config: { headers: {'content-type': 'application/json' }}      
        })
        .then(res => {
            if(res.data.id > 0) {
                localStorage.setItem('token', res.data.access_token);
                this.props.handler(res.data.name, res.data.id, res.data.access_token);
            } else {
                this.setState({
                    error: res.data.error
                });
            }
        }).catch(err => {
            console.warn('error:', err)
        });
    }
    
    render() {      
        return (
            <div className="registerForm">
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
                    <FormGroup controlId="name" bsSize="large">
                        <ControlLabel>Name</ControlLabel>
                        <FormControl
                            type="text"
                            value={this.state.name}
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
                    <FormGroup controlId="confirm_password" bsSize="large">
                        <ControlLabel>Confirm Password</ControlLabel>
                        <FormControl
                            value={this.state.confirm_password}
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
                        Register
                    </Button>
                </form>                             
            </div>
        );
    }
}

export default Register;