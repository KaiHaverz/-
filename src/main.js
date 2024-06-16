import { createApp } from 'vue'  
import App from './App.vue'  
import router from './router' // 引入你创建的路由配置  
  
const app = createApp(App)  
  
app.config.productionTip = false  
  
// 注入路由到Vue实例中  
app.use(router)  
  
// 挂载应用到DOM上  
app.mount('#app')