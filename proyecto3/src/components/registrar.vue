<template>
  <div class="container">
    <h1 class="title">Registrar Cliente</h1>
    <form @submit.prevent="insertarCliente" class="form">
      <div class="form-group">
        <label for="documento">Documento (solo números)</label>
        <input
          v-model="cliente.documento"
          id="documento"
          type="text"
          required
          class="form-control"
          pattern="\d+"
          title="El documento debe contener solo números"
        />
      </div>
      <div class="form-group">
        <label for="nombre">Nombre (solo letras)</label>
        <input
          v-model="cliente.nombre"
          id="nombre"
          type="text"
          required
          class="form-control"
          pattern="[A-Za-zÀ-ÿ\s]+"
          title="El nombre debe contener solo letras"
        />
      </div>
      <div class="form-group">
        <label for="apellido">Apellido (solo letras)</label>
        <input
          v-model="cliente.apellido"
          id="apellido"
          type="text"
          required
          class="form-control"
          pattern="[A-Za-zÀ-ÿ\s]+"
          title="El apellido debe contener solo letras"
        />
      </div>
      <div class="form-group">
        <label for="correo">Correo</label>
        <input
          v-model="cliente.correo"
          id="correo"
          type="email"
          required
          class="form-control"
        />
      </div>
      <div class="form-group">
        <label for="rol">Rol</label>
        <select v-model="cliente.rol" id="rol" required class="form-control">
          <option value="" disabled selected>Seleccione un rol</option>
          <option value="padre">Padre</option>
          <option value="docente">Docente</option>
          <option value="estudiante">Estudiante</option>
        </select>
      </div>
      <button type="submit" class="submit-button">Registrar</button>
    </form>
    <div v-if="message" :class="messageClass">{{ message }}</div> <!-- Moved here for placement -->
  </div>
</template>

<script>
import axios from 'axios';
import { ref } from 'vue';

export default {
  setup() {
    const cliente = ref({
      documento: "",
      nombre: "",
      apellido: "",
      correo: "",
      rol: ""
    });

    const message = ref('');
    const messageClass = ref('');

    const insertarCliente = async () => {
      try {
        const respuesta = await axios.post('http://127.0.0.1:8000/insertar', cliente.value);

        if (respuesta.status === 200) {
          message.value = 'Registrado exitosamente';
          messageClass.value = 'message-success';
          cliente.value = { documento: "", nombre: "", apellido: "", correo: "", rol: "" };
        } else {
          message.value = 'No se pudo registrar';
          messageClass.value = 'message-error';
        }
      } catch (error) {
        message.value = 'Error al registrar datos';
        messageClass.value = 'message-error';
      }
    };

    return { cliente, insertarCliente, message, messageClass };
  }
};
</script>

<style scoped>
.container {
  max-width: 90%; /* Increased width for more spacious look */
  margin: 0 auto; /* Center the container */
  padding: 20px;
  font-family: Arial, sans-serif;
  background-image: url('./icons/59214359-de-vuelta-a-la-escuela-texturas-para-fondos-de-escritorio-rellenos-de-fondo-página-web (1).jpg');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  border-radius: 8px;
  box-shadow: 0 rgba(0, 0, 0, 0.1);
  backdrop-filter: blur(5px);
}

.title {
  text-align: center;
  margin-bottom: 15px;
  color: #333;
}

.form {
  background: rgba(255, 255, 255, 0.9);
  padding: 15px;
  border-radius: 8px;
  max-width: 50%; /* Set form width to half of the container */
  margin: 0 auto; /* Center the form */
}

.form-group {
  margin-bottom: 10px;
}

.form-group label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

.form-control {
  width: 100%; /* Full width of the form */
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
  box-sizing: border-box;
}

.form-control:focus {
  border-color: #007bff;
  outline: none;
}

.submit-button {
  background-color: #007bff;
  color: #fff;
  border: none;
  padding: 10px 15px;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s;
  display: block;
  margin: 0 auto;
}

.submit-button:hover {
  background-color: #0056b3;
}

.message-success,
.message-warning,
.message-error {
  margin-top: 10px;
}

.message-success {
  color: #28a745;
}

.message-warning {
  color: #ffc107;
}

.message-error {
  color: #dc3545;
}
</style>
