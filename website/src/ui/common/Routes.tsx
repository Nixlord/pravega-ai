import React from "react";
import {
    Switch,
    Route
} from "react-router-dom";

import Button from '@material-ui/core/Button';
import ResponsiveDrawer from "../components/samples/Drawer/Drawer";

const Routes = () => (
    <Switch>
        <Route path="/about">
            <About/>
        </Route>
        <Route path="/users">
            <Users/>
        </Route>
        <Route path="/">
            <Home/>
        </Route>
    </Switch>
);

export default Routes;

function Home() {
    return (
        <>
            <h2>Home</h2>
            <Button variant="contained" color="primary">
                Primary
            </Button>
        </>
    );
}

function About() {
    return <ResponsiveDrawer/>;
}

function Users() {
    return <h2>Users</h2>;
}