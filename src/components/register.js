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
            confirm_password: ""
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
        event.preventDefault();         
        console.log(this.state.email + "\n" + this.state.password);
        axios({
            method: 'POST',
            url: 'http://127.0.0.1:5000/register',
            data: {
                name: this.state.name,                
                email: this.state.email,
                password: this.state.password,
                // confirm_password: this.state.confirm_password
            },
            config: { headers: {'content-type': 'application/json' }}      
        })
        .then(res => {
            console.log(res.data);
        }).catch(err => console.warn('error:', err));
    }
    
    render() {
        
        return (
            <div className="registerForm">
                {/* <h2>Register</h2>
                <div id="register">
                    <input type="text" id="first" placeholder="Name"/>
                    <input type="email" id="email" placeholder="Email"/>
                    <input type="password" id="password" placeholder="Password"/>
                    <input type="password" id="confirm" placeholder="Confirm Password"/>
                    <button id="submit">Submit</button>
                </div> */}
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
                        autoFocus
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