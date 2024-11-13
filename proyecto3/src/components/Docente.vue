<template>
  <div class="teacher-view">
    <div class="content-overlay">
    <h1 class="teacher-title">Área de Docentes</h1>

    <p class="teacher-welcome">
      Bienvenido al área de docentes. Aquí puedes gestionar tus clases, ver tu horario, y acceder a los recursos necesarios para tu enseñanza.
    </p>

    <div class="actions">
      <div class="action-item">
        <h2>Gestión de Clases</h2>
        <p>Administra tus clases, asignaciones y recursos de manera eficiente.</p>
        <button class="action-button">Ver Clases</button>
      </div>
      <div class="action-item">
        <h2>Horario</h2>
        <p>Consulta tu horario y planifica tus actividades con facilidad.</p>
        <button class="action-button">Ver Horario</button>
      </div>
      <div class="action-item">
        <h2>Recursos</h2>
        <p>Accede a materiales y recursos para enriquecer tu enseñanza.</p>
        <button class="action-button">Ver Recursos</button>
      </div>
    </div>

    <div class="menu-container">
      <h2>Menú Principal</h2>
      <div class="accordion">
        <details>
          <summary>Agregar Materia</summary>
          <div class="add-subject">
            <input type="text" placeholder="Nombre de la materia" v-model="nombreMateria" />
            <input type="text" placeholder="Nota de la materia" v-model="notaMateria" />
            <button class="action-button" @click="agregarMateria">Agregar Materia</button>
          </div>
        </details>
        <details>
          <summary>Buscar Materia</summary>
          <p class="description">Aquí puedes buscar una materia específica dentro de la lista.</p>
          <div class="search-subject">
            <input type="text" placeholder="Escribe el nombre de la materia" v-model="buscarMateria" />
            <button class="action-button" @click="buscarMateriaFn">Buscar</button>
            <div v-if="materiaEncontrada" class="search-result">
              <h3>Resultado:</h3>
              <p>{{ materiaEncontrada.nombre }} - Nota: {{ materiaEncontrada.nota }}</p>
            </div>
          </div>
        </details>
        <details>
          <summary>Actualizar Materia</summary>
          <div class="update-subject">
            <input type="text" placeholder="Nombre de la materia a actualizar" v-model="nombreMateriaActualizar" />
            <input type="text" placeholder="Nueva nota de la materia" v-model="notaMateriaActualizar" />
            <button class="action-button" @click="actualizarMateria">Actualizar Materia</button>
          </div>
        </details>
        <details>
          <summary>Eliminar Materia</summary>
          <div class="delete-subject">
            <input type="text" placeholder="Nombre de la materia a eliminar" v-model="nombreMateriaEliminar" />
            <button class="action-button" @click="eliminarMateria">Eliminar Materia</button>
          </div>
        </details>
        <details>
          <summary>Mostrar Lista de Materias</summary>
          <p class="description">Esta sección te permitirá ver la lista completa de materias disponibles.</p>
          <div class="subject-list">
            <div v-for="materia in materias" :key="materia.nombre" class="subject">
              <div class="subject-details">
                <h3 class="subject-name">{{ materia.nombre }}</h3>
                <p class="subject-grade">Nota: {{ materia.nota }}</p>
              </div>
            </div>
          </div>
        </details>
        <details>
          <summary>Salir</summary>
          <p class="description">Haz clic en el botón para salir del sistema.</p>
          <button class="action-button" @click="salir">Salir</button>
        </details>
      </div>
    </div>
  </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const nombreMateria = ref('');
const notaMateria = ref('');
const buscarMateria = ref('');
const nombreMateriaActualizar = ref('');
const notaMateriaActualizar = ref('');
const nombreMateriaEliminar = ref('');
const materiaEncontrada = ref(null);

const materias = ref([
  { nombre: 'Matemáticas', nota: 9.5 },
  { nombre: 'Historia', nota: 8.9 },
  { nombre: 'Ciencias', nota: 9.2 },
  { nombre: 'Inglés', nota: 8.9 },
]);

const agregarMateria = () => {
  if (nombreMateria.value && notaMateria.value) {
    materias.value.push({ nombre: nombreMateria.value, nota: parseFloat(notaMateria.value) });
    nombreMateria.value = '';
    notaMateria.value = '';
  } else {
    alert('Por favor, completa todos los campos.');
  }
};

const buscarMateriaFn = () => {
  materiaEncontrada.value = materias.value.find(m => m.nombre.toLowerCase() === buscarMateria.value.toLowerCase());
  if (!materiaEncontrada.value) {
    alert('Materia no encontrada');
  }
};

const actualizarMateria = () => {
  const materia = materias.value.find(m => m.nombre.toLowerCase() === nombreMateriaActualizar.value.toLowerCase());
  if (materia && notaMateriaActualizar.value) {
    materia.nota = parseFloat(notaMateriaActualizar.value);
    nombreMateriaActualizar.value = '';
    notaMateriaActualizar.value = '';
  } else {
    alert('Materia no encontrada o datos inválidos.');
  }
};

const eliminarMateria = () => {
  materias.value = materias.value.filter(m => m.nombre.toLowerCase() !== nombreMateriaEliminar.value.toLowerCase());
  nombreMateriaEliminar.value = '';
};

const salir = () => {
  alert('Saliendo del sistema...');
};
</script>

<style scoped>
/* Estilo para el contenedor principal de la vista de docentes */
.teacher-view {
  display: flex; /* Usa Flexbox para centrar el contenido */
  flex-direction: column; /* Organiza los elementos verticalmente */
  align-items: center; /* Centra los elementos horizontalmente */
  justify-content: flex-start; /* Alinea los elementos en la parte superior */
  min-height: 100vh; /* Altura mínima completa del viewport */
  width: 105%;
  text-align: center; /* Centra el texto */
  padding: 20px; /* Añade padding alrededor del contenido */
  background-image: url('./icons/59214359-de-vuelta-a-la-escuela-texturas-para-fondos-de-escritorio-rellenos-de-fondo-página-web (1).jpg');
  font-family: 'Arial', sans-serif; /* Fuente moderna y profesional */
}

.content-overlay {
  background-color: rgba(255, 255, 255, 0.9); /* Fondo blanco con opacidad */
  border-radius: 8px;
  padding: 20px;
  width: 100%;
  max-width: 1200px;
}

/* Estilo para el título */
.teacher-title {
  font-size: 2.5rem; /* Tamaño de fuente grande para el título */
  color: #333; /* Color oscuro para mejor legibilidad */
  margin-bottom: 15px; /* Espacio debajo del título */
  font-weight: bold; /* Fuente en negrita */
}

/* Estilo para la bienvenida */
.teacher-welcome {
  font-size: 1rem; /* Tamaño de fuente para la bienvenida */
  color: #666; /* Color gris oscuro */
  margin-bottom: 30px; /* Espacio debajo de la bienvenida */
  max-width: 80%; /* Ancho máximo con padding para pantallas pequeñas */
  line-height: 1.6; /* Espaciado de línea para mejor legibilidad */
}

/* Estilo para la sección de acciones */
.actions {
  display: flex; /* Usa Flexbox para el diseño de las acciones */
  flex-wrap: wrap; /* Envuelve los elementos si es necesario */
  justify-content: center; /* Centra los elementos horizontalmente */
  margin-top: 30px; /* Espacio arriba de la sección de acciones */
  width: 100%; /* Ancho completo para la sección de acciones */
}

.action-item {
  background-color: #fff; /* Color de fondo blanco para los elementos de acciones */
  border: 1px solid #ddd; /* Borde gris claro */
  border-radius: 8px; /* Bordes redondeados */
  padding: 20px; /* Padding dentro de cada elemento */
  margin: 15px; /* Espacio alrededor de cada elemento */
  max-width: 300px; /* Ancho máximo para cada elemento */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Sombra sutil para los elementos de acciones */
  transition: transform 0.3s; /* Transición suave para el escalado */
}

.action-item:hover {
  transform: translateY(-5px); /* Eleva ligeramente el elemento al pasar el cursor */
}

.action-item h2 {
  font-size: 1.4rem; /* Tamaño de fuente para los encabezados de acciones */
  color: #007bff; /* Color de texto azul para los encabezados */
  margin-bottom: 10px; /* Espacio debajo del encabezado */
  font-weight: bold; /* Fuente en negrita */
}

.action-item p {
  font-size: 0.9rem; /* Tamaño de fuente para el texto de acciones */
  color: #666; /* Color gris oscuro para el texto */
  line-height: 1.5; /* Espaciado de línea para mejor legibilidad */
}

/* Estilo para el botón de acción */
.action-button {
  background-color: #007bff; /* Color de fondo azul */
  color: #fff; /* Color del texto blanco */
  border: none; /* Sin borde */
  border-radius: 5px; /* Bordes redondeados */
  padding: 12px 25px; /* Padding dentro del botón */
  font-size: 1rem; /* Tamaño de fuente para el texto del botón */
  cursor: pointer; /* Cursor tipo puntero al pasar sobre el botón */
  transition: background-color 0.3s; /* Transición suave para el color de fondo */
}

.action-button:hover {
  background-color: #0056b3; /* Color de fondo más oscuro al pasar el cursor */
}

/* Estilo para el contenedor del menú */
.menu-container {
  width: 100%; /* Ancho completo para el contenedor del menú */
  max-width: 800px; /* Ancho máximo para el contenedor del menú */
  margin: 30px auto; /* Espacio automático alrededor del contenedor del menú */
  padding: 20px; /* Padding dentro del contenedor */
  background-color: #fff; /* Color de fondo blanco para el menú */
  border-radius: 8px; /* Bordes redondeados */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Sombra sutil para el menú */
}

.accordion summary {
  cursor: pointer; /* Cursor tipo puntero para los encabezados del acordeón */
  font-size: 1.2rem; /* Tamaño de fuente para los encabezados del acordeón */
  color: #007bff; /* Color de texto azul para los encabezados */
  margin-bottom: 10px; /* Espacio debajo del encabezado del acordeón */
  border-bottom: 1px solid #ddd; /* Línea inferior sutil */
  padding-bottom: 10px; /* Padding debajo del encabezado */
}

.accordion details {
  margin-bottom: 15px; /* Espacio debajo de cada detalle del acordeón */
}

.accordion details div {
  padding: 15px; /* Padding dentro de cada detalle */
  border: 1px solid #ddd; /* Borde gris claro */
  border-radius: 8px; /* Bordes redondeados */
}

.accordion .add-subject,
.accordion .search-subject,
.accordion .update-subject,
.accordion .delete-subject,
.accordion .subject-list {
  margin-top: 10px; /* Espacio arriba de cada sección dentro del acordeón */
}

.accordion input {
  padding: 10px; /* Padding dentro de los campos de entrada */
  border: 1px solid #ddd; /* Borde gris claro */
  border-radius: 5px; /* Bordes redondeados */
  width: calc(100% - 22px); /* Ancho completo menos padding y borde */
  box-sizing: border-box; /* Incluir padding y borde en el ancho total */
  margin-bottom: 10px; /* Espacio debajo de cada campo de entrada */
}

.accordion .subject {
  margin-bottom: 10px; /* Espacio debajo de cada materia en la lista */
  padding: 10px; /* Padding dentro de cada materia */
  border: 1px solid #ddd; /* Borde gris claro */
  border-radius: 5px; /* Bordes redondeados */
  background-color: #f9f9f9; /* Color de fondo ligero */
}

.accordion .subject-name {
  font-size: 1.1rem; /* Tamaño de fuente para el nombre de la materia */
  color: #333; /* Color oscuro para mejor legibilidad */
  margin-bottom: 5px; /* Espacio debajo del nombre */
}

.accordion .subject-grade {
  font-size: 1rem; /* Tamaño de fuente para la nota de la materia */
  color: #666; /* Color gris oscuro para el texto */
}
</style>
