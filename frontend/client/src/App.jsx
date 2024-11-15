import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Home from './routes/Home';
import About from './routes/About';
import NotFound from './routes/NotFound';

function App() {
  return (
    <div>
      <header>
        <h1>Mi Aplicación React</h1>
        <nav>
          <a href="/">Inicio</a> | <a href="/about">Acerca de</a>
        </nav>
      </header>
      <main>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<About />} />


          <Route path="*" element={<NotFound />} />{/* lo que no se encuentra */}
        </Routes>
      </main>
    </div>
  );
}

export default App;
