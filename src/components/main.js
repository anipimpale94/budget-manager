// libraries
import React, { Component } from 'react';
import axios from 'axios';
import { Button } from "react-bootstrap";

// css
import '../css/main.css';

class Main extends Component {
    constructor(props) {
        super(props);
    
        this.state = {
            Name: this.props.Name,
            id: this.props.Id
        };    
    }

    componentDidMount() {
        axios.get(`http://localhost:5000/budget/` + this.state.id)
        .then(res => {
            // const persons = res.data;
            // this.setState({ persons });
            console.log(res.data)
        })
    }

    handleLogOut = () => {
        this.props.Logout();
    }

    render() {
        return(
            <div>
                <h1>Hello, {this.state.Name}!</h1>
            </div>        
        );
    }
}

export default Main;
