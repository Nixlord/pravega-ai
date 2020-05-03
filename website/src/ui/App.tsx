import React from 'react';
import './App.css';
import Routes from './common/Routes';
import {BrowserRouter} from "react-router-dom";
import Container from "./common/Container";
import StaggeredGrid from "./common/StaggeredGrid";

const App = () => (
  <>
    <BrowserRouter>
        <Container>
            <Routes />
        </Container>
    </BrowserRouter>
    <StaggeredGrid/>
  </>
)

export default App;