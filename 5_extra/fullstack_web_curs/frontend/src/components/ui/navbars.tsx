import React from "react";
import { AppBar, Toolbar, IconButton, Typography } from "@mui/material";
import DeleteIcon from "@mui/icons-material/Delete";
import { Link } from "react-router-dom";

// @ts-ignore
export function Navbar1(props = {}) {
  return (
    <div>
      <AppBar position="static">
        <Toolbar variant="dense">
          <IconButton
            edge="start"
            color="inherit"
            aria-label="menu"
            sx={{ mr: 2 }}
          >
            <DeleteIcon />
          </IconButton>
          <Typography variant="h6" color="inherit" component="div">
            Photos
          </Typography>
        </Toolbar>
      </AppBar>

      <div>
        <Link to={"/"} className={"btn btn-md btn-warning"}>
          home
        </Link>
        <Link to={"/about"} className={"btn btn-md btn-primary"}>
          about
        </Link>
        <Link to={"/custom"} className={"btn btn-md btn-primary"}>
          custom
        </Link>
      </div>
    </div>
  );
}

// @ts-ignore
export function Navbar2(props = { children: any, pageName: str }) {
  return <div className={"custom-navbar"}></div>;
}
