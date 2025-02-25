import React from "react";

export default class App extends React.Component {
  constructor() {
    super();
    this.state = {
      count: 0,
    };
    console.log("Constructor Initialized");
  }

  componentDidMount() {
    console.log("Component Mounted");
    console.log("Current State: ", this.state.count);
  }

  componentDidUpdate(prevProps, prevState) {
    console.log("Component Updated");
    console.log("Previous State: ", prevState.count);
    console.log("Current State: ", this.state.count);
  }

  componentWillUnmount() {
    console.log("Component Unmounted");
  }

  handleIncrement = () => {
    this.setState((prevState) => ({
      count: prevState.count + 1,
    }));
  };

  handleDecrement = () => {
    this.setState((prevState) => ({
      count: prevState.count - 1,
    }));
  };

  render() {
    console.log("Component Rendered");
    return (
      <div>
        <h1>React LifeCycle Method</h1>
        <h2>Counter: {this.state.count}</h2>
        <button onClick={this.handleIncrement}>Increase</button>
        <button onClick={this.handleDecrement}>Decrease</button>
      </div>
    );
  }
}
