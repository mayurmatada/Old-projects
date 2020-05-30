import React, { Component } from "react";
import "./App.css";
import Buttonjsx from "./Components/buttonjsx.jsx";
import Input from "./Components/Input.jsx";
import Equal from "./Components/equalbutton.jsx";
import Parenthesis from "./Components/parenthesis.jsx";
import * as math from "mathjs";

class App extends Component {
  constructor(props) {
    super(props);

    this.state = {
      input: "",
      parenthesis: false
    };
    this.appender = this.appender.bind(this);
    this.solve = this.solve.bind(this);
    this.clear = this.clear.bind(this);
    this.check = this.check.bind(this);
  }

  appender(val) {
    this.setState({ input: this.state.input + val });
  }

  solve() {
    this.setState({ input: math.evaluate(this.state.input) });
  }
  clear() {
    this.setState({ input: "" });
  }

  check() {
    console.log("Hello2");
    return <div>Hi</div>;
  }

  render() {
    return (
      <div className="App">
        <div className="calc-wrapper">
          <div className="row">
            <Input>{this.state.input}</Input>
          </div>
          <div className="row">
            <Buttonjsx handleclick={this.clear}>C</Buttonjsx>
            <Buttonjsx handleclick={this.appender}>^</Buttonjsx>
            <Parenthesis name={this.check} handleclick={this.appender}>
              ()
            </Parenthesis>
          </div>
          <div className="row">
            <Buttonjsx handleclick={this.appender}>1</Buttonjsx>
            <Buttonjsx handleclick={this.appender}>2</Buttonjsx>
            <Buttonjsx handleclick={this.appender}>3</Buttonjsx>
            <Buttonjsx handleclick={this.appender}>/</Buttonjsx>
          </div>
          <div className="row">
            <Buttonjsx handleclick={this.appender}>4</Buttonjsx>
            <Buttonjsx handleclick={this.appender}>5</Buttonjsx>
            <Buttonjsx handleclick={this.appender}>6</Buttonjsx>
            <Buttonjsx handleclick={this.appender}>*</Buttonjsx>
          </div>
          <div className="row">
            <Buttonjsx handleclick={this.appender}>7</Buttonjsx>
            <Buttonjsx handleclick={this.appender}>8</Buttonjsx>
            <Buttonjsx handleclick={this.appender}>9</Buttonjsx>
            <Buttonjsx handleclick={this.appender}>+</Buttonjsx>
          </div>
          <div className="row">
            <Buttonjsx handleclick={this.appender}>.</Buttonjsx>
            <Buttonjsx handleclick={this.appender}>0</Buttonjsx>
            <Buttonjsx handleclick={this.appender}>sqrt</Buttonjsx>
            <Equal handleclick={this.solve}>=</Equal>
          </div>
        </div>
      </div>
    );
  }
}

export default App;
