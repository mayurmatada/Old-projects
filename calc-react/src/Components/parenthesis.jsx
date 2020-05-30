import React, { Component } from "react";
import "./buttoncss.css";

class Parenthesis extends Component {
  render() {
    return (
      <div
        className="bttnCSS"
        onClick={() => this.props.handleclick(this.props.name)}
      >
        {this.props.children}
      </div>
    );
  }
}

export default Parenthesis;
