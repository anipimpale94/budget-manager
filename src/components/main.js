// libraries
import React, { Component } from 'react';
// import axios from 'axios';

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
        // axios.get(`http://localhost:5000/budget/`)
        // .then(res => {
        //     console.log(res.data)
        // })
    }

    handleLogOut = () => {
        this.props.Logout();
    }

    render() {
        return(
            <div>
                <h1>Hello, {this.state.name}!</h1>
            </div>        
        );
    }
}

export default Main;
