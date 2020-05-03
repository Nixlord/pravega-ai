import React, {Component} from "react";
import "./Square.css"

export interface SquareProps {}

export interface SquareState {
  value: string
}

export default class Square extends React.Component<SquareProps, SquareState> {
  constructor(props: SquareProps) {
    super(props)
    this.state = {
      value: ""
    }
  }
  render() {
    return (
      <button 
        className="square" 
        onClick={ () => this.setState({value: 'X'}) }
        >
        {this.state.value}
      </button>
    );
  }
}