import React from 'react';
// import Nav from './Nav'

// constructor, render, componentdidmount,state change render called, willUnmount 
// class App extends React.Component {
//   constructor() {
//     super();
//     this.state={
//       show:true
//     }
//     console.log("Constructor"); 
//   }

//   componentDidMount(){
//     console.log("ComponentDidMount");
//   }
//   render() {
//     console.log("Render"); 
//     return (
//       <div>
//       <h1>React Life Cycle Method</h1>
//       {
//         this.state.show ?
//         <Nav />
//         :null
//       }
//       <button onClick={()=>{this.setState({show:!this.state.show})}}>Toggle Navbar</button>
//     </div>
//     )
    
//   }
// }
// export default App;

//componentDidMount
// export default class App extends React.Component {
//   constructor() {
//     super();
//     console.log("constructor");
//     this.state={
//       data:false
//     }
//   }

//   componentDidMount() {
//     console.log("componentDidMount");
//     this.setState({data:true})
//   }

//   render() {
//     console.log("render");

//     return (
//       <div>
//         <h1>ComponentDidMount Lifecycle</h1>
//       </div>
//     )
//   }
// } 

// componentWillUnmount
// export default class App extends React.Component {
//   constructor() {
//     super();
//     this.state={
//       show:false
//     }
//   }
//   render() {
//     console.log("render");
//     return (
//       <div>
//         <h1>Component Will Unmount</h1>
//       {this.state.show? <Child /> :null}
//       <button onClick={() =>{this.setState({show:!this.state.show})}}>Toggle Child</button>
//       </div>
//     )
//   }
// }

// class Child extends React.Component {
//   componentWillUnmount(){
//     console.log("Component is hidden now-unmount");
//   }
//   render() {
//     return (
//       <div>
//         <h2>Child Component</h2>
//       </div>
//     )
//   }
// }

// //componentDidUpdate(when state or props changes)
// export default class App extends React.Component {
//   constructor() {
//     super();
//     this.state={
//       counter:0
//     }
//   }

// // componentDidUpdate(prevProps, prevState, snapShot) {
// //   console.log("componentDidUpdate called", prevState);

// //  //use condition else setState results infinite loop
// //  if(prevState.counter<3){
// //   this.setState({counter:this.state.counter +1})
// // }
// // }

//   render() {
//     console.log("render");
//     return (
//       <div>
//         <h1>ComponentDidUpdate Lifecycle Method</h1>
//         <Child data={this.state.counter} />
//         <button
//   onClick={()=>{this.setState({counter:this.state.counter +1})}}
//         > Update Counter: {this.state.counter}</button>
//       </div>
//     )
//   }
// }

// //child component
//  class Child extends React.Component {
//   constructor() {
//     super();
//     this.state={
//       counter:0
//     }
//   }

//   componentDidUpdate(prevProps, prevState, snapShot) {
//     console.log("componentDidUpdate called", prevProps, this.props.data);

   
//   }

//   render() {
//     console.log("render");
//     return (
//       <div>
//         <h2>Child Component {this.props.data}</h2>
        
//       </div>
//     )
//   }
// }

//getDerived State from Props
import Home from './Home';
export default class App extends React.Component {
  constructor() {
    super();
    this.state={
      data:0
    }
  }

  render() {
    return (
      <div>
        <h1>Get Derived State From Props:  {this.state.data}</h1>
        <Home data={this.state.data}/>
        <button onClick={()=>{this.setState({data:this.state.data+1})}}>Increment</button>
      </div>
    )
  }
}

