import React from "react";
import Counter from "../components/ui/Counter";
import { Link } from "react-router-dom";
import * as bases from "../components/ui/bases";

export default function Page() {
  function printValue(value: number) {
    // callback function
    console.log(value);
  }

  return (
    <bases.Base1 pageName={"Общая информация"}>
      <div>
        <div>
          <Link to={"/"} className={"btn btn-md btn-warning"}>
            home
          </Link>
          <Link to={"/about"} className={"btn btn-md btn-primary"}>
            about
          </Link>
        </div>
        <Counter defaultValue={666} callbackFunc={printValue} />
      </div>
    </bases.Base1>
  );
}
