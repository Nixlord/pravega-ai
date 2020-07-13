import React from "react";
import {Button} from "@material-ui/core";
import helloAPI from "../../../api/samples/helloAPI";

export interface HomeProps {
    prompt: string,
    defaultName: string
}
export interface HomeState {
    name: string
}

export default class Home extends React.Component<HomeProps, HomeState> {
    constructor(props: HomeProps) {
        super(props);
        this.state = {
            name: "Developer"
        }
    }

    componentDidMount(): void {
        const name = this.props.defaultName
        helloAPI({ name })
            .then(res => res.developer)
            .then(name => this.setState({ name }))
    }

    render() {
        return (
            <>
                <h2>Home</h2>
                <Button variant = "contained" color="primary">
                    {this.props.prompt} {this.state.name}
                </Button>
            </>
        )
    }
}