import React from 'react';
import logo from './logo.svg';
import './App.css';

interface AppState {
  name: string
};

export default class App extends React.Component<{}, AppState> {
  constructor(props: {}) {
    super(props);

    this.state = {
      name: "Developer"
    };
  }

  componentDidMount() {
    fetch('/api/hello/Diksha')
    .then(res => res.json())
    .then(res => this.setState({name: res.developer}))
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p>
            Hello {this.state.name}
          </p>
          <a
            className="App-link"
            href="https://reactjs.org"
            target="_blank"
            rel="noopener noreferrer"
          >
            Learn React
          </a>
        </header>
      </div>
    );
  }
}
