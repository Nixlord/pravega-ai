import React, {Component} from "react";
import { Theme, createStyles, makeStyles } from '@material-ui/core/styles';
import GridList from '@material-ui/core/GridList';
import GridListTile from '@material-ui/core/GridListTile';
import tileData from './tileData';

interface StaggeredGridProps {}

interface StaggeredGridState {}

export default class StaggeredGrid extends React.Component<StaggeredGridProps, StaggeredGridState> {
    render(): React.ReactNode {
        return (
            <GridList cellHeight={350} cols={5}>
                {tileData.map((tile) => (
                    <GridListTile key={tile.title} cols={tile.cols || 1}>
                        <img src={tile.img} alt={tile.title} />
                    </GridListTile>
                ))}
            </GridList>
        )
    }
}