import Vue from 'vue';
import VueRouter from 'vue-router';
import Diagnosis from './views/AiDiagnosis.vue';  // 智能导诊模块
import SelfCheck from './views/SelfCheck.vue';  // 疾病自查模块
import DiseaseDetail from "@/views/DiseaseDetail.vue";
import FastDiagnosis from "@/views/FastDiagnosis.vue";
import AppointmentPage from "@/views/AppointmentPage.vue";
import DoctorDetails from "@/views/DoctorDetails.vue";
import SearchDepartment from "@/views/SearchDepartment.vue";
import SearchDoctor from "@/views/SearchDoctor.vue";
import AppointPage from "@/views/AppointPage.vue";
import DepartmentDetail from "@/views/DepartmentDetail.vue";
import AboutMyself from "@/views/AboutMyself.vue";

Vue.use(VueRouter);

const routes = [
  { path: '/', redirect: '/diagnosis' },  // 默认跳转到智能导诊
  { path: '/diagnosis', component: Diagnosis },
  { path: '/self-check', component: SelfCheck },
  { path: '/disease/:id', component: DiseaseDetail},
  { path: '/fastDiagnosis', component: FastDiagnosis},
  { path: '/appointment', component: AppointmentPage},
  { path:'/search-doctor', component: SearchDoctor},
  { path: '/search-department', component: SearchDepartment},
  { path: '/doctor/:id', component: DoctorDetails},
  { path: '/appoint-doctor/:id', component: AppointPage},
  { path: '/department/:id', component: DepartmentDetail},
  { path: '/myself', component: AboutMyself}
];

const router = new VueRouter({
  mode: 'history',
  routes,
});

export default router;

