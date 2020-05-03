import React from 'react';
import './App.css';
import Routes from './common/Routes';
import {BrowserRouter} from "react-router-dom";
import Container from "./common/Container";
import StaggeredGrid from "./common/StaggeredGrid";
import SimpleCard from "./common/Card";

const App = () => (
  <>
    <div className="pageHeader">
        <h1 className="title">Pravega Documentation</h1>
    </div>
    <BrowserRouter>
        <Container>
            <Routes />
        </Container>
    </BrowserRouter>
    <SimpleCard/>
    <StaggeredGrid/>
  </>
)

export default App;