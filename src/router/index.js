import { createRouter, createWebHistory } from 'vue-router'  
  
// 导入你的Vue组件  
import TeamIntroduction from '../components/TeamIntroduction.vue'  
import TeamMembers from '../components/TeamMembers.vue'  
import HighLights from '../components/Highlights.vue'  
import Login from '../components/Login.vue' // 注意这里将 LoGin 改为 Login 以保持命名一致性  
import MessageBoard from '../components/MessageBoard.vue'  
  
const routes = [  
  {  
    path: '/',  
    redirect: '/team-introduction'  
  },  
  {  
    path: '/team-introduction',  
    name: 'TeamIntroduction',  
    component: TeamIntroduction  
  },  
  {  
    path: '/team-members',  
    name: 'TeamMembers',  
    component: TeamMembers  
  },  
  {  
    path: '/highlights', // 注意这里将 Highlights 改为小写以保持一致性  
    name: 'HighLights',  
    component: HighLights  
  },  
  {  
    path: '/login',  
    name: 'LoGin',  
    component: Login  
  },  
  {  
    path: '/message-board',  
    name: 'MessageBoard',  
    component: MessageBoard  
  }  
]  
  
const router = createRouter({  
  history: createWebHistory(), // 创建历史记录实例  
  routes // 使用routes配置  
})  
  
export default router