<template>
  <div class="consulta-container">
    <h1>Consulta de Clientes</h1>

    <!-- Campo de búsqueda -->
    <input
      type="text"
      v-model="searchQuery"
      placeholder="Buscar cliente..."
      class="search-input"
    />

    <div v-if="filteredData.length > 0" class="table-container">
      <table>
        <thead>
          <tr>
            <th>Documento</th>
            <th>Nombre</th>
            <th>Apellido</th>
            <th>Correo</th>
            <th>Rol</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(cliente, index) in filteredData" :key="index">
            <td>{{ cliente.documento }}</td>
            <td>{{ cliente.nombre }}</td>
            <td>{{ cliente.apellido }}</td>
            <td>{{ cliente.correo }}</td>
            <td>{{ cliente.rol }}</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div v-else class="no-data">
      <p>No se encontraron datos.</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { ref, onMounted, computed } from 'vue';

export default {
  setup() {
    const data = ref([]);
    const searchQuery = ref('');

    const consultaDatosClientes = async () => {
      try {
        const respuesta = await axios.get('http://127.0.0.1:8000/consultaclientes');
        if (Array.isArray(respuesta.data)) {
          data.value = respuesta.data;
        } else {
          console.error('No se cargaron los datos', respuesta.data);
        }
      } catch (error) {
        console.error("Error no hay respuesta", error);
      }
    };

    const filteredData = computed(() => {
      return data.value.filter(cliente =>
        Object.values(cliente).some(val =>
          String(val).toLowerCase().includes(searchQuery.value.toLowerCase())
        )
      );
    });

    onMounted(consultaDatosClientes);

    return { data, searchQuery, filteredData };
  }
}
</script>

<style scoped>
/* Estilo general del contenedor de consulta */
.consulta-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 100vh; /* Ocupa todo el alto de la pantalla */
  width: 112%; /* Ajusta al 100% */
  max-width: 1800px; /* Ajusta el contenedor a un ancho máximo */
  margin: 0 auto; /* Centra el contenedor horizontalmente */
  padding: 20px;
  font-family: Arial, sans-serif;
  text-align: center;
  background-image: url('./icons/59214359-de-vuelta-a-la-escuela-texturas-para-fondos-de-escritorio-rellenos-de-fondo-página-web (1).jpg');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}

/* Estilo para el encabezado */
h1 {
  color: #000000;
  margin-bottom: 20px;
}

/* Estilo para el campo de búsqueda */
.search-input {
  padding: 10px;
  margin-bottom: 20px;
  width: 100%;
  max-width: 400px;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 16px;
  box-shadow: 0px 3px 6px rgba(0, 0, 0, 0.1);
}

/* Estilo para el contenedor de la tabla */
.table-container {
  background: rgba(255, 255, 255, 0.9);
  border-radius: 10px;
  padding: 20px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  width: 100%;
  max-width: 800px;
  margin: 0 auto;
}

/* Estilo para la tabla */
table {
  width: 100%;
  border-collapse: collapse;
}

/* Estilo para los encabezados de la tabla */
th {
  background-color: #007bff;
  color: #fff;
  padding: 12px;
  text-align: left;
}

/* Estilo para las celdas de la tabla */
td {
  padding: 12px;
  border-bottom: 1px solid #ddd;
  text-align: left;
}

/* Estilo para las filas */
tr {
  transition: background-color 0.3s ease;
}
tr:hover {
  background-color: rgba(0, 123, 255, 0.1);
}

/* Estilo para el mensaje de sin datos */
.no-data {
  color: #fff;
  font-size: 18px;
}

/* Media Queries para pantallas pequeñas */
@media (max-width: 768px) {
  .consulta-container {
    width: 90%;
  }

  table {
    font-size: 0.9rem;
  }

  th, td {
    padding: 8px;
  }

  .no-data {
    font-size: 16px;
  }
}

@media (max-width: 480px) {
  .consulta-container {
    width: 100%;
  }

  table {
    font-size: 0.8rem;
  }

  th, td {
    padding: 6px;
  }

  .no-data {
    font-size: 14px;
  }
}
</style>
