import { BrowserRouter, Routes, Route } from "react-router-dom";
import HomePage from "../pages/HomePage";
import AboutPage from "../pages/AboutPage";
import CustomPage from "../pages/CustomPage";

export default function Router() {
  return (
    <BrowserRouter>
      <Routes>
        {/* base */}
        <Route path="/" element={<HomePage />}></Route>
        <Route path="/home" element={<HomePage />}></Route>
        <Route path="/about" element={<AboutPage />}></Route>
        {/* custom */}
        <Route path="/custom" element={<CustomPage />}></Route>
      </Routes>
    </BrowserRouter>
  );
}
