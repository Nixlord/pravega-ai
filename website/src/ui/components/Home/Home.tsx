import React from "react";
import {Button} from "@material-ui/core";

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
        fetch(`/api/hello/${this.props.defaultName}`)
            .then(response => response.json())
            .then(json => this.setState({
                name: json.developer
            }))
            .catch(console.error)
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