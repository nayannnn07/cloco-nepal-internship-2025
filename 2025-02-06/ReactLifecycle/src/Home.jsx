import React from 'react'

export default class Home extends React.Component {
    constructor() {
        super();
        this.state={
          currentValue:0
        }
      }

    static getDerivedStateFromProps(props, state) {
        console.log("hooks-derived state",props,state);
        return {
            // eslint-disable-next-line react/prop-types
            currentValue: props.data*10
        };
    }
  render() {
    console.log("render");
    return (
      <div>
        <h1>Current Value: {this.state.currentValue}</h1>
      </div>
    )
  }
}
