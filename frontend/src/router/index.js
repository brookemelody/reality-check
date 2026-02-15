import { createRouter, createWebHistory } from 'vue-router'
import HomeComponent from '@/components/HomeComponent.vue'
import EvidenceComponent from '@/components/EvidenceComponent.vue'
import CaseTimelineComponent from '@/components/CaseTimelineComponent.vue'

const router = createRouter({
    history: createWebHistory(),
    routes: [
        { path: '/', component: HomeComponent },
        { path: '/timeline', component: CaseTimelineComponent },
        { path: '/evidence', component: EvidenceComponent }
    ],
})
export default router