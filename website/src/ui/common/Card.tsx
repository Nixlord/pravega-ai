import React, {Component} from "react";
import { makeStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';
import "./Card.css"

export default class SimpleCard extends Component {
    render() {
        // const classes = useStyles();
        const bull = <span className="bullet">•</span>
        return (
            <Card className="root" variant="outlined">
                <CardContent>
                    <Typography className="title" color="textSecondary" gutterBottom>
                        Work of our team
                    </Typography>
                    <Typography variant="h5" component="h2">
                        PRAVEGA
                    </Typography>
                    <Typography className="pos" color="textSecondary">
                        self project
                    </Typography>
                    <Typography className="body" variant="body2" component="p">
                        A library for making coding easy
                    </Typography>
                </CardContent>
                <CardActions>
                    <Button size="small" onClick={() => alert("Going to Github")}>
                        Go To Github
                        </Button>
                </CardActions>
            </Card>
        )
    }
}