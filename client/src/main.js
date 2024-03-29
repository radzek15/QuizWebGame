import { createApp } from 'vue'
import { createRouter, createWebHistory } from "vue-router";

import 'bootstrap/dist/css/bootstrap.css'

import App from './App.vue'
import HomePage from "@/components/HomePage.vue";
import DemoQuiz from "@/components/Quiz/DemoQuiz.vue";


const router = createRouter({
	history: createWebHistory(),
	routes: [
		{ path: '/', component: HomePage},
		{ path: '/demo-quiz', component: DemoQuiz}
	],
});

const app = createApp(App)

app.use(router);

app.mount('#app');
