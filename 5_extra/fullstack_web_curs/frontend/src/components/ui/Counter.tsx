import { useState } from "react";

export default function Counter1(
  // @ts-ignore
  props = { defaultValue: 0, callbackFunc: any },
) {
  const [count, setCount] = useState(props.defaultValue);

  function Increase() {
    setCount(count + 1);
  }

  function Decrease() {
    setCount(count - 1);
  }

  return (
    <div>
      {count}
      <div
        onClick={() => {
          props.callbackFunc(count);
        }}
        className={"btn btn-lg btn-outline-primary"}
      >
        ==========
      </div>
      <div onClick={Increase} className={"btn btn-lg btn-outline-danger"}>
        +
      </div>
      <div onClick={Decrease} className={"btn btn-lg btn-outline-danger"}>
        -
      </div>
    </div>
  );
}
