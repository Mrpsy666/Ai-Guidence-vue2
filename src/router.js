import Vue from 'vue';
import VueRouter from 'vue-router';
import Diagnosis from './views/AiDiagnosis.vue';  // 智能导诊模块
import SelfCheck from './views/SelfCheck.vue';  // 疾病自查模块
import DiseaseDetail from "@/views/DiseaseDetail.vue";
import FastDiagnosis from "@/views/FastDiagnosis.vue";


Vue.use(VueRouter);

const routes = [
  { path: '/', redirect: '/diagnosis' },  // 默认跳转到智能导诊
  { path: '/diagnosis', component: Diagnosis },
  { path: '/self-check', component: SelfCheck },
  { path: '/disease/:id', component: DiseaseDetail},
  { path: '/fastDiagnosis', component: FastDiagnosis},
];

const router = new VueRouter({
  mode: 'history',
  routes,
});

export default router;

