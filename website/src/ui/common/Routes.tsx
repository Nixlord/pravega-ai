import React, {useEffect, useState} from "react";
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
    const [name, setName] = useState("Developer")
    useEffect(() => {
        fetch('/api/hello/Diksha')
            .then(response => response.json())
            .then(json => setName(json.developer))
            .catch(error => console.error(error))
    })

    return (
        <>
            <h2>Home</h2>
            <Button variant="contained" color="primary">
                {name}
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