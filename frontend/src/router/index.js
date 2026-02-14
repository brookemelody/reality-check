import { createRouter, createWebHistory } from 'vue-router'
import HomeComponent from '@/components/HomeComponent.vue'
import AboutComponent from '@/components/AboutComponent.vue'
import EvidenceComponent from '@/components/EvidenceComponent.vue'

const router = createRouter({
    history: createWebHistory(),
    routes: [
        { path: '/', component: HomeComponent },
        { path: '/about', component: AboutComponent },
        { path: '/evidence', component: EvidenceComponent }
    ],
})
export default router