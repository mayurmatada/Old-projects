import React, { Component } from "react";
import "./buttoncss.css";
class Equal extends Component {
  render() {
    return (
      <div className="bttnCSS" onClick={this.props.handleclick}>
        {this.props.children}
      </div>
    );
  }
}

export default Equal;
