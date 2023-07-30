import React from "react";
import * as navbars from "./navbars";

// @ts-ignore
export function Base1(props = { children: any, pageName: str }) {
  return (
    <div>
      <div>
        <navbars.Navbar1 />
      </div>
      <main>
        <h1 className="custom-div">{props.pageName}</h1>
        {props.children}
      </main>
      <main>FOOTER</main>
    </div>
  );
}

// @ts-ignore
export function Base2(props = { children: any }) {
  return (
    <div>
      <div>NAVBAR 2</div>
      <main>{props.children}</main>
      <main>FOOTER 2</main>
    </div>
  );
}
