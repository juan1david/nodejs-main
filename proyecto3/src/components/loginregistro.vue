<template>
    <div class="aut-container">
        <h1 class="title">{{ frmlogin ? 'Iniciar Sesión' : 'Registrar Usuario' }}</h1>
        <form @submit.prevent="loginUsuario" class="form">
            <div class="frminput" v-if="!frmlogin">
                <label for="documento">Documento</label>
                <select v-model="documento" id="documento" required>
                    <option value="">Seleccionar documento</option>
                    <option v-for="doc in documentos" :key="doc" :value="doc">
                        {{ doc }}
                    </option>
                </select>
            </div>

            <div class="frminput">
                <label for="nombreUsuario">Nombre Usuario</label>
                <input type="text" id="nombreUsuario" v-model="nombreUsuario" required />
            </div>

            <div class="frminput">
                <label for="Password">Contraseña</label>
                <input type="password" id="Password" v-model="password" required />
            </div>

            <div class="frminput" v-if="!frmlogin">
                <label for="confirmPassword">Confirmar Contraseña</label>
                <input type="password" id="confirmPassword" v-model="confirmPassword" required />
            </div>

            <div class="frminput" v-if="!frmlogin">
                <label for="rol">Rol</label>
                <select v-model="rol" id="rol" required>
                    <option value="">Seleccionar rol</option>
                    <option value="padre">Padre</option>
                    <option value="docente">Docente</option>
                    <option value="estudiante">Estudiante</option>
                </select>
            </div>

            <button type="submit">{{ frmlogin ? 'Iniciar Sesión' : 'Registrarse' }}</button>
            <div v-if="menError" class="error-message">{{ menError }}</div>
            <button type="button" @click="cambioForm">{{ frmlogin ? 'Crear Cuenta' : 'Iniciar Sesión' }}</button>
        </form>
    </div>
</template>

<script setup>
import Swal from 'sweetalert2';
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';

const nombreUsuario = ref('');
const password = ref('');
const confirmPassword = ref('');
const rol = ref('');
const documento = ref('');
const documentos = ref([]);
const frmlogin = ref(true);
const menError = ref('');
const router = useRouter();

const cambioForm = async () => {
    frmlogin.value = !frmlogin.value;
    if (!frmlogin.value) {
        await fetchDocumentos();
    }
};

const fetchDocumentos = async () => {
    try {
        const response = await axios.get('http://127.0.0.1:8000/clientes/documento/');
        documentos.value = response.data;
    } catch (error) {
        console.error("Error en la consulta de documentos: ", error);
        menError.value = "Error al consultar documentos";
    }
};

const loginUsuario = async () => {
    if (frmlogin.value) {
        try {
            const response = await axios.post('http://127.0.0.1:8000/login', {
                nombre_usuario: nombreUsuario.value,
                password: password.value,
            });
            const { rol: userRol, mensaje } = response.data;

            Swal.fire({
                icon: 'success',
                title: mensaje,
                text: 'Bienvenido a tu cuenta',
            });

            router.push(userRol === "estudiante" ? '/estudiante' : (userRol === "docente" ? '/docente' : '/padre'));
        } catch (error) {
            console.error("Error de inicio de sesión", error);
            menError.value = error.response?.data?.detail || "Error de inicio de sesión";
            Swal.fire({
                icon: 'error',
                title: 'Error de inicio de sesión',
                text: menError.value,
            });
        }
    } else {
        if (password.value !== confirmPassword.value) {
            menError.value = "Las contraseñas no coinciden";
            return;
        }
        try {
            const response = await axios.post('http://127.0.0.1:8000/registrousuario', {
                nombre_usuario: nombreUsuario.value,
                password: password.value,
                rol: rol.value,
                documento: documento.value,
            });
            Swal.fire({
                icon: 'success',
                title: response.data.mensaje,
                text: 'Usuario registrado con éxito',
            });
            cambioForm();
        } catch (error) {
            console.error("Error al registrar usuario: ", error);
            menError.value = error.response?.data?.detail || "Error al registrar usuario";
            Swal.fire({
                icon: 'error',
                title: 'Error en el registro',
                text: menError.value,
            });
        }
    }
};

onMounted(() => {
    if (!frmlogin.value) {
        fetchDocumentos();
    }
});
</script>

<style scoped>
.aut-container {
  height: 100vh; /* Full height of the viewport */
  width: 105%; /* Full width */
  margin: 0; /* Remove margin */
  padding: 20px;
  font-family: Arial, sans-serif;
  background-image: url('./icons/59214359-de-vuelta-a-la-escuela-texturas-para-fondos-de-escritorio-rellenos-de-fondo-página-web (1).jpg');
  background-size: cover; /* Cover the entire container */
  background-position: center;
  background-repeat: no-repeat;
  border-radius: 0; /* Remove border radius for full-screen effect */
  box-shadow: none; /* Remove box shadow for cleaner look */
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

.frminput {
  margin-bottom: 10px;
}

.frminput label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

.frminput input,
.frminput select {
  width: 100%; /* Full width of the form */
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  box-sizing: border-box;
}

button {
  background-color: #007bff;
  color: #fff;
  border: none;
  padding: 10px 15px;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s;
  display: block;
  margin: 10px auto; /* Center the button */
  width: 100%; /* Full width for button */
}

button:hover {
  background-color: #0056b3;
}

.error-message {
  color: #dc3545;
  margin-top: 10px;
  text-align: center; /* Center the error message */
}
</style>
