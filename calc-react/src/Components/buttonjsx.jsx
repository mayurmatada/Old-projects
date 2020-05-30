import "./buttoncss.css";
import React, { Component } from "react";

class Buttonjsx extends Component {
  render() {
    return (
      <div
        className="bttnCSS"
        onClick={() => this.props.handleclick(this.props.children)}
      >
        {this.props.children}
      </div>
    );
  }
}

export default Buttonjsx;
