import { createApp } from 'vue'
import { createRouter, createWebHistory } from "vue-router";

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap/dist/js/bootstrap.js'
import '@fortawesome/fontawesome-free/css/all.css'

import App from './App.vue'
import HomePage from "@/components/HomePage.vue";
import DemoQuiz from "@/components/Quiz/DemoQuiz.vue";
import NewQuiz from "@/components/NewQuiz.vue";
import RegisterPage from "@/components/auth/RegisterPage.vue";
import LoginPage from "@/components/auth/LoginPage.vue";

const router = createRouter({
	history: createWebHistory(),
	routes: [
		{ path: '/', component: HomePage},
		{ path: '/demo-quiz', component: DemoQuiz},
		{ path: '/create-quiz', component: NewQuiz},
		{ path: '/register', component: RegisterPage},
		{ path: '/login', component: LoginPage},
	],
});

const app = createApp(App)

app.use(router);

app.mount('#app');
