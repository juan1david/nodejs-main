<template>
  <header>
    <nav>
      <div class="container">
        <div class="logo">
          <a href="#"><img src="./icons/ecd1ca2f-8962-4397-b9b3-df04d1343138.jpeg" alt="Logo de la aplicación"></a>
        </div>
        <div class="title">
          <h1>PROCESSCHOOL</h1>
        </div>
        <div class="menu-toggle" @click="toggleMenu">
          <span class="bar"></span>
          <span class="bar"></span>
          <span class="bar"></span>
        </div>
        <ul :class="{ 'show': menuOpen }">
          <li><router-link to="/Home">Home</router-link></li>
          <li><router-link to="/">Consultar</router-link></li>
          <li><router-link to="/Registrar">Registrar</router-link></li>
          <li><router-link to="/login">Login</router-link></li>
          <li><router-link to="/Docente">Docente</router-link></li>
          <li><router-link to="/Estudiante">Estudiante</router-link></li>
        </ul>
      </div>
    </nav>
  </header>
</template>

<script setup>
import { ref } from 'vue';

const menuOpen = ref(false);

const toggleMenu = () => {
  menuOpen.value = !menuOpen.value;
};
</script>

<style scoped>
/* Estilo para el encabezado */
header {
  background-color: #007bff; /* Color de fondo azul */
  color: #fff; /* Color del texto blanco */
  padding: 15px 20px; /* Padding alrededor del contenido */
  position: relative; /* Posicionamiento relativo */
}

/* Estilo para el contenedor del encabezado */
.container {
  display: flex; /* Usa Flexbox */
  justify-content: space-between; /* Espacio entre el logo, título y menú */
  align-items: center; /* Centra verticalmente */
}

/* Estilo para el logo */
.logo a {
  color: #fff; /* Color del texto blanco */
  text-decoration: none; /* Elimina subrayado */
}

/* Estilo para la imagen del logo */
.logo img {
  height: 100px; /* Aumenta el tamaño del logo */
  width: 180px; /* Asegura que no sea demasiado grande */
}

/* Estilo para el título */
.title h1 {
  margin: 0;
  font-size: 2rem; /* Tamaño de fuente un poco más grande para el título */
}

/* Botón de alternancia de menú */
.menu-toggle {
  display: none; /* Oculto por defecto en pantallas grandes */
  flex-direction: column;
  cursor: pointer;
}

.menu-toggle .bar {
  background-color: #fff;
  height: 3px;
  width: 25px;
  margin: 3px 0;
  transition: 0.3s;
}

/* Estilo para la lista de navegación */
nav ul {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  align-items: center;
}

nav ul li {
  margin-left: 20px;
}

nav ul li a {
  color: #fff;
  text-decoration: none;
  font-size: 1rem;
  transition: color 0.3s;
}

nav ul li a:hover {
  color: #e0e0e0;
}

/* Adaptativo para pantallas pequeñas */
@media (max-width: 768px) {
  .menu-toggle {
    display: flex;
  }

  nav ul {
    display: none;
    flex-direction: column;
    width: 100%;
    position: absolute;
    top: 60px;
    right: 0;
    background-color: #007bff;
    border-radius: 5px;
    padding: 10px 0;
    z-index: 10;
  }

  nav ul.show {
    display: flex;
  }

  nav ul li {
    margin: 10px 0;
    text-align: center;
  }
}

/* Adaptativo para pantallas más pequeñas */
@media (max-width: 480px) {
  .title h1 {
    font-size: 1.5rem; /* Ajusta el tamaño de la fuente para pantallas pequeñas */
  }

  .logo img {
    height: 60px; /* Ajusta el tamaño del logo para pantallas pequeñas */
    max-width: 100px; /* Asegura que el logo no se vea demasiado grande */
  }

  nav ul li a {
    font-size: 0.9rem; /* Tamaño de fuente para enlaces en pantallas pequeñas */
  }
}
</style>
