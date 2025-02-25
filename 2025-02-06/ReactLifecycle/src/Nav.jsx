import React from 'react';

export default class Nav extends React.Component{
    componentWillUnmount(){
        console.log("Unmount");
    }
    render() {
        return <h3>navbar</h3>
    }

}