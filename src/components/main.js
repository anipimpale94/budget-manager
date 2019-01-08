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
        };    
    }

    handleLogOut = () => {
        this.props.Logout();
    }

    render() {
        return(
            <div>
                <h1>Hello, {this.state.Name}!</h1>
                <Button
                    block
                    bsSize="large"
                    onClick={this.handleLogOut}
                >Logout</Button>
            </div>        
        );
    }
}

export default Main;
