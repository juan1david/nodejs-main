<template>
  <div id="app">
    <Header v-if="visible" />
    
    <router-view />
    
    <footer>
      <p>© 2024 mi aplicación</p>
    </footer>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue';
import { useRoute } from 'vue-router';
import Header from './components/Header.vue'; // Asegúrate de importar el componente Header correctamente

const rutasnomostar = ['/cliente'];

const ruta = useRoute();
const visible = ref(true);

watch(
  () => ruta.path,
  (nuevaRuta) => {
    visible.value = !rutasnomostar.includes(nuevaRuta);
  },
  { immediate: true }
);
</script>

<style>
/* Estilo general del contenedor de la aplicación */
#app {
  display: flex; /* Usa flexbox para organizar los elementos */
  flex-direction: column; /* Organiza los elementos en una columna */
  min-height: 100vh; /* Asegura que el contenedor tenga al menos la altura de la ventana */
  width: 100%;
}

/* Estilo para el pie de página */
footer {
  background-color: #000000; /* Color de fondo del pie de página */
  padding: 10px; /* Espaciado interno */
  text-align: center; /* Centra el texto */
  border-top: 1px solid #d30000; /* Línea superior de separación */
  margin-top: auto; /* Empuja el pie de página al fondo del contenedor */
  color: #ffffff;
  width: 1;
  width: 105%;
}

/* Ajustes responsive */
@media (max-width: 368px) {
  /* Ajustes para pantallas de tamaño medio */
  footer {
    padding: 8px; /* Reduce el padding para pantallas más pequeñas */
  }
}

@media (max-width: 280px) {
  /* Ajustes para pantallas pequeñas, como móviles */
  footer {
    padding: 6px; /* Reduce el padding aún más para pantallas muy pequeñas */
    font-size: 0.9rem; /* Reduce el tamaño de la fuente para pantallas pequeñas */
  }
}

/* Asegúrate de que el Header y los componentes principales también se adapten a pantallas pequeñas */
header, .home-container, .login-container, .register-container, .consult-container {
  width: 105%;
  padding: 10px;
}

@media (max-width: 368px) {
  header, .home-container, .login-container, .register-container, .consult-container {
    padding: 15px; /* Ajusta el padding para pantallas más pequeñas */
  }
}
</style>
