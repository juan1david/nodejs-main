<template>
  <div class="home-container">
    <!-- Contenedor para el fondo con opacidad -->
    <div class="content-overlay">
      <header class="header">
        <h1 class="home-title">¡Bienvenido a Processchool!</h1>
        <p class="home-description">
          Descubre nuestras características únicas y explora todas las posibilidades que ofrecemos para tu proceso educativo. ¡Estamos encantados de tenerte aquí! 
          Con Processchool, el aprendizaje se convierte en una experiencia enriquecedora y colaborativa.
        </p>
        <button class="home-button">Comenzar</button>
      </header>

      <section class="features">
        <h2 class="features-title">Nuestras Características</h2>
        <div class="feature-items">
          <div class="feature-item">
            <h3>Clases Interactivas</h3>
            <p>Clases dinámicas y atractivas con actividades prácticas y multimedia para un aprendizaje efectivo.</p>
          </div>
          <div class="feature-item">
            <h3>Soporte Personalizado</h3>
            <p>Asesoría experta para resolver dudas y guiar tu proceso de aprendizaje.</p>
          </div>
          <div class="feature-item">
            <h3>Materiales de Estudio</h3>
            <p>Accede a materiales de estudio actualizados, diseñados para facilitar tu aprendizaje.</p>
          </div>
          <div class="feature-item">
            <h3>Evaluaciones Constantes</h3>
            <p>Mide tu progreso con evaluaciones regulares y obtén retroalimentación inmediata.</p>
          </div>
          <div class="feature-item">
            <h3>Comunidad Colaborativa</h3>
            <p>Comparte ideas y experiencias con otros estudiantes en un ambiente de aprendizaje.</p>
          </div>
          <div class="feature-item">
            <h3>Acceso Móvil</h3>
            <p>Accede a clases y materiales desde cualquier dispositivo, adaptándote a tu estilo de vida.</p>
          </div>
        </div>
      </section>

      <section class="about-us">
        <h2 class="about-title">Sobre Nosotros</h2>
        <p class="about-description">
          En Processchool, nuestra misión es transformar la educación a través de la tecnología y la innovación. 
          Creemos en un aprendizaje accesible y personalizado que se adapte a las necesidades de cada estudiante. 
          Nuestro equipo está comprometido a ofrecer una experiencia de aprendizaje excepcional.
        </p>
        <p class="about-description">
          Únete a nosotros y forma parte de una nueva era educativa donde tu éxito es nuestra prioridad.
        </p>
      </section>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
// No es necesario ningún script adicional por ahora
</script>

<style scoped>
/* Estilo para el contenedor principal */
.home-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  min-height: 100vh;
  text-align: center;
  padding: 40px 20px;
  background-color: rgba(244, 244, 244, 0.8);
  background-image: url('./icons/59214359-de-vuelta-a-la-escuela-texturas-para-fondos-de-escritorio-rellenos-de-fondo-página-web (1).jpg');
  background-size: cover;
  background-position: center;
  font-family: 'Arial', sans-serif;
  color: #000;
}

/* Contenedor para el contenido con fondo blanco semitransparente */
.content-overlay {
  background-color: rgba(255, 255, 255, 0.9); /* Fondo blanco con opacidad */
  border-radius: 8px;
  padding: 20px;
  width: 100%;
  max-width: 1200px;
}

/* Estilo para el encabezado */
.header {
  margin-bottom: 40px;
}

/* Estilo para el título */
.home-title {
  font-size: 2.5rem;
  color: #070707;
  margin-bottom: 15px;
  font-weight: bold;
}

/* Estilo para la descripción */
.home-description {
  font-size: 1rem;
  color: #0a0a0a;
  margin-bottom: 25px;
  max-width: 80%;
  line-height: 1.6;
  text-align: center;
  margin-left: auto;
  margin-right: auto;
}

/* Estilo para el botón */
.home-button {
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 5px;
  padding: 12px 25px;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.3s, transform 0.2s;
}

.home-button:hover {
  background-color: #0056b3;
  transform: scale(1.05);
}

/* Estilo para la sección de características */
.features {
  margin-top: 40px;
  width: 100%;
}

.features-title {
  font-size: 2rem;
  margin-bottom: 20px;
  color: #007bff;
}

.feature-items {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}

.feature-item {
  background-color: #ffffff;
  border: 1px solid #dddddd;
  border-radius: 8px;
  padding: 20px;
  margin: 10px;
  width: calc(33% - 20px);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s;
}

.feature-item:hover {
  transform: translateY(-5px);
}

.feature-item h3 {
  font-size: 1.4rem;
  color: #007bff;
  margin-bottom: 10px;
  font-weight: bold;
}

.feature-item p {
  font-size: 0.9rem;
  color: #333;
  line-height: 1.5;
}

/* Estilo para la sección Sobre Nosotros */
.about-us {
  margin-top: 40px;
  max-width: 800px;
  padding: 20px;
  background-color: rgba(255, 255, 255, 0.9);
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.about-title {
  font-size: 2rem;
  margin-bottom: 20px;
  color: #007bff;
}

.about-description {
  font-size: 0.9rem;
  color: #333;
  line-height: 1.5;
  margin-bottom: 15px;
}

/* Estilos adaptativos para pantallas pequeñas */
@media (max-width: 768px) {
  .home-title {
    font-size: 2rem;
  }

  .home-description {
    font-size: 0.9rem;
    max-width: 95%;
  }

  .home-button {
    font-size: 0.9rem;
    padding: 10px 20px;
  }

  .features {
    flex-direction: column;
    align-items: center;
  }

  .feature-item {
    width: 90%;
    margin: 10px 0;
  }
}

@media (max-width: 480px) {
  .home-title {
    font-size: 1.5rem;
  }

  .home-description {
    font-size: 0.8rem;
  }

  .home-button {
    font-size: 0.8rem;
    padding: 8px 15px;
  }

  .feature-item h3 {
    font-size: 1.2rem;
  }

  .feature-item p {
    font-size: 0.8rem;
  }
}
</style>
