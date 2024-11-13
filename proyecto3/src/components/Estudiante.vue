<template>
  <div class="student-view">
    <div class="content-overlay">
    <h1 class="student-title">Área de Estudiantes</h1>
    <p class="student-welcome">
      Bienvenido al área de estudiantes. Aquí puedes ver tus materias, consultar tus calificaciones y acceder a tus tareas.
    </p>

    <div class="actions">
      <div class="action-item">
        <h2>Mis Materias</h2>
        <p>Consulta las materias en las que estás inscrito y revisa el contenido.</p>
        <button class="action-button">Ver Materias</button>
      </div>
      <div class="action-item">
        <h2>Calificaciones</h2>
        <p>Consulta tus calificaciones y realiza un seguimiento de tu progreso académico.</p>
        <button class="action-button">Ver Calificaciones</button>
      </div>
      <div class="action-item">
        <h2>Tareas</h2>
        <p>Accede a tus tareas y revisa los plazos y detalles.</p>
        <button class="action-button">Ver Tareas</button>
      </div>
    </div>

    <div class="menu-container">
      <h2>Menú Principal</h2>
      <div class="accordion">
        <details>
          <summary>Buscar Materia</summary>
          <p class="description">Aquí puedes buscar una materia específica dentro de la lista.</p>
          <div class="search-subject">
            <input type="text" placeholder="Escribe el nombre de la materia" id="buscarMateriaInput">
            <button class="action-button">Buscar</button>
          </div>
        </details>
        <details>
          <summary>Mostrar Lista de Materias</summary>
          <p class="description">Esta sección te permitirá ver la lista completa de materias disponibles.</p>
          <div class="subject-list">
            <div class="subject" v-for="subject in subjects" :key="subject.name">
              <div class="subject-details">
                <h3 class="subject-name">{{ subject.name }}</h3>
                <p class="subject-grade">Nota: {{ subject.grade }}</p>
              </div>
            </div>
          </div>
        </details>
        <details>
          <summary>Salir</summary>
          <p class="description">Haz clic en el botón para salir del sistema.</p>
          <button class="action-button">Salir</button>
        </details>
      </div>
    </div>
  </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

// Definir datos para la lista de materias
const subjects = ref([
  { name: 'Matemáticas', grade: '9.5' },
  { name: 'Historia', grade: '8.9' },
  { name: 'Ciencias', grade: '9.2' },
  { name: 'Inglés', grade: '8.9' },
  { name: 'Lenguaje', grade: '8.7' },
]);
</script>

<style scoped>
/* Estilo para el contenedor principal de la vista de estudiantes */
.student-view {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  min-height: 100vh;
  text-align: center;
  width: 105%;
  padding: 20px;
  background-image: url('./icons/59214359-de-vuelta-a-la-escuela-texturas-para-fondos-de-escritorio-rellenos-de-fondo-página-web (1).jpg');
  font-family: 'Arial', sans-serif;
}

.content-overlay {
  background-color: rgba(255, 255, 255, 0.9); /* Fondo blanco con opacidad */
  border-radius: 8px;
  padding: 20px;
  width: 100%;
  max-width: 1200px;
}

/* Estilo para el título */
.student-title {
  font-size: 2.5rem;
  color: #333;
  margin-bottom: 15px;
  font-weight: bold;
}

/* Estilo para la bienvenida */
.student-welcome {
  font-size: 1rem;
  color: #666;
  margin-bottom: 30px;
  max-width: 80%;
  line-height: 1.6;
}

/* Estilo para la sección de acciones */
.actions {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  margin-top: 30px;
  width: 100%;
}

.action-item {
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 20px;
  margin: 15px;
  max-width: 300px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s;
}

.action-item:hover {
  transform: translateY(-5px);
}

.action-item h2 {
  font-size: 1.4rem;
  color: #007bff;
  margin-bottom: 10px;
  font-weight: bold;
}

.action-item p {
  font-size: 0.9rem;
  color: #666;
  line-height: 1.5;
}

/* Estilo para el botón de acción */
.action-button {
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 5px;
  padding: 12px 25px;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.3s, transform 0.2s;
}

.action-button:hover {
  background-color: #0056b3;
  transform: scale(1.05);
}

/* Estilos adaptativos para pantallas pequeñas */
@media (max-width: 768px) {
  .student-title {
    font-size: 2rem;
  }

  .student-welcome {
    font-size: 0.9rem;
    max-width: 90%;
  }

  .action-item {
    width: 90%;
    margin: 10px 0;
  }
}

@media (max-width: 480px) {
  .student-title {
    font-size: 1.5rem;
  }

  .student-welcome {
    font-size: 0.8rem;
    max-width: 100%;
  }

  .action-item {
    width: 100%;
  }
}

/* Estilo para la sección de menú */
.menu-container {
  margin-top: 30px;
  width: 100%;
}

.accordion {
  background-color: #fff;
  border-radius: 8px;
  border: 1px solid #ddd;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  padding: 20px;
}

.accordion details {
  margin-bottom: 15px;
}

.accordion summary {
  font-size: 1.2rem;
  cursor: pointer;
  color: #007bff;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
  background-color: #f9f9f9;
}

.accordion div {
  padding: 15px;
}

.add-subject, .search-subject, .update-subject, .delete-subject {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.input, .action-button {
  width: 100%;
}

/* Estilo para la lista de materias */
.subject-list {
  display: flex;
  flex-direction: column;
  gap: 10px;
  padding: 0;
}

.subject {
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.subject-details {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.subject-grade {
  font-size: 1rem;
  color: #333;
}

.subject-name {
  font-size: 1.2rem;
  color: #007bff;
  margin: 0;
}
</style>
