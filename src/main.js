import Vue from 'vue'
import App from './App.vue'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import axios from 'axios'
import router from './router'


Vue.config.productionTip = false;
Vue.use(ElementUI);

axios.defaults.baseURL = 'http://127.0.0.1:8000'
Vue.prototype.$axios = axios;

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
