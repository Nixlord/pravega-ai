import React, {Component} from "react";
import { Link } from "react-router-dom";

interface ContainerState {

}

interface ContainerProps {

}


export default class Container extends Component<ContainerProps, ContainerState> {
    render(): React.ReactNode {
        return (
            <>
                <ContainerUI />
                {this.props.children}
            </>
        )
    }
}

const ContainerUI = () => (
    <nav>
        <ul>
            <li>
                <Link to="/">Home</Link>
            </li>
            <li>
                <Link to="/about">About</Link>
            </li>
            <li>
                <Link to="/users">Users</Link>
            </li>
        </ul>
    </nav>
)