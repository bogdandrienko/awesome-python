import Button from "react-bootstrap/Button";
import React from "react";
import ReactPlayer from "react-player";
import { Link } from "react-router-dom";
import * as bases from "../components/ui/bases";

export default function Page() {
  return (
    <bases.Base1 pageName={"Домашняя страница"}>
      <div>
        <ReactPlayer
          url="https://www.youtube.com/watch?v=ysz5S6PUM-U"
          controls={false}
        />
        <div>
          <Button variant="primary">Primary</Button>
          <Button variant="secondary">Secondary</Button>
          <Button variant="success">Success</Button>
          <Button variant="warning">Warning</Button>
          <Button variant="danger">Danger</Button>
          <Button variant="info">Info</Button>
          <Button variant="light">Light</Button>
          <Button variant="dark">Dark</Button>
          <Button variant="link">Link</Button>
        </div>
      </div>
    </bases.Base1>
  );
}
