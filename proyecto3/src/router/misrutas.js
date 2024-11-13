import { createRouter, createWebHistory } from "vue-router";
import Consultafb from "@/components/consultafb.vue";
import Registrar from "@/components/registrar.vue";
import Home from "@/components/home.vue";
import Loginregistro from "@/components/loginregistro.vue";
import Docente from "@/components/Docente.vue";
import Estudiante from "@/components/Estudiante.vue";


const routes = [
    {
        path: '/Home',
        name: 'Home',
        component: Home
    },
    {
        path: '/Registrar',
        name: 'Registrar',
        component: Registrar
    },
    {
        path: '/',
        name: 'Consultar',
        component: Consultafb
    },
    {   
        path: '/login',
        name: 'loginregistro',
        component: Loginregistro 
    },
    {   
        path: '/Estudiante',
        name: 'Estudiante',
        component: Estudiante 
    },
    {   
        path: '/Docente',
        name: 'Docente',
        component: Docente 
    },
];

const router = createRouter({
    history: createWebHistory(),
    routes
});

export default router;
