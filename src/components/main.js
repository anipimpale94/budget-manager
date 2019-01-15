// libraries
import React, { Component } from 'react';
import axios from 'axios';

// css
import '../css/main.css';

class Main extends Component {
    constructor(props) {
        super(props);
    
        this.state = {
            name: this.props.name,
            error: ""
        };    
    }

    componentDidMount() {
        axios.get(`http://localhost:5000/budget`)
        .then(res => {
            console.log(res.data)
        }).catch(err => {
            console.warn('error:', err)
        });
    }

    handleLogOut = () => {
        this.props.Logout();
    }

    render() {
        return(
            <div>
                <h2>Hello, {this.state.name}!</h2>
            </div>        
        );
    }
}

export default Main;
