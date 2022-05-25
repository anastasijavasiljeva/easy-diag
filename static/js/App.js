import React, { useState } from "react";
import { createRoot } from 'react-dom/client';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import MainForm from './MainForm';
import AboutUs from './AboutUs';
import '../css/app.css';
import { Navbar, NavbarBrand } from 'react-bootstrap';
import FormControlLabel from '@mui/material/FormControlLabel';
import Switch from '@mui/material/Switch';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faSun } from '@fortawesome/free-solid-svg-icons'

const App = () => {
    const [theme, setTheme ] = useState(false);
    var storedTheme = localStorage.getItem('theme') || (window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");
    if (storedTheme) document.documentElement.setAttribute('data-theme', storedTheme);  
    function toggleTheme() {
        var currentTheme = document.documentElement.getAttribute("data-theme");
        var targetTheme = (currentTheme === "light") ? "dark" : "light";
        document.documentElement.setAttribute('data-theme', targetTheme)
        localStorage.setItem('theme', targetTheme);
        setTheme(!theme);
    };
    return (
    <BrowserRouter>
        <div className="App">   
        <Navbar>
          <a href='/' className='logoLink'><NavbarBrand className = "brand">EasyDiag</NavbarBrand></a>
          <FormControlLabel aria-label="Toggle dark mode" aria-hidden="true" control={ <Switch checked={theme == "light"} name="theme-toggle" onChange={toggleTheme} className=''/> } label={<FontAwesomeIcon icon={faSun} size="2x"/>} />
        </Navbar>
          <Routes>
          <Route exact path = '/' element = {<MainForm/>}/>
          <Route exact path="/about-us" element = {<AboutUs/>}/>
          </Routes>
        </div>
      </BrowserRouter>
      );
};

createRoot(document.getElementById("render-react-here")).render(<App/>);
