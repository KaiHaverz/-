<template>  
  <div id="app">  
    <header>  
      <h1>球队俱乐部</h1>  
      <div class="user-info" @click="goToLogin">
        <span v-if="currentUser">{{ currentUser }}</span>
        <span v-else>请登录</span>
      </div>
    </header>  
    <div class="swiper-container">  
     
      <div class="swiper-pagination"></div>  
    </div>  
    <nav>  
      <ul>  
        <li><router-link to="/team-introduction">球队介绍</router-link></li>  
        <li><router-link to="/team-members">球队成员</router-link></li>  
        <li><router-link to="/Highlights">精彩片段</router-link></li>  
        <li><router-link to="/message-board">留言</router-link></li>  
      </ul>  
    </nav>  
  
    <main>  
      <router-view @updateUser="updateCurrentUser"></router-view>  
    </main>  
  
    <footer>  
      <p>&copy; 2024 球队俱乐部</p>  
    </footer>  
  </div>  
</template>  
  
<script>  
import Swiper from 'swiper'; 
import 'swiper/swiper-bundle.css';  

export default {  
  name: 'App',

  data() {
    return {
      currentUser: ''
    };
  },
  mounted() {  
    new Swiper('.swiper-container', {  
      loop: true, // 循环模式选项  
      pagination: {  
        el: '.swiper-pagination',  
        clickable: true, // 允许点击分页器的指示点  
      }   
    });

    // 检查是否已经登录
    const savedUser = JSON.parse(localStorage.getItem('currentUser'));
    if (savedUser) {
      this.currentUser = savedUser.username;
    }
  },
  methods: {
    goToLogin() {
      this.$router.push('/login');
    },
    updateCurrentUser(newUser) {
      this.currentUser = newUser;
      localStorage.setItem('currentUser', JSON.stringify({ username: newUser }));
    }
  }
};  
</script>  
  
<style>  
body, html {
    margin: 0;
    padding: 0;
    font-family: Arial, sans-serif;

}

::-webkit-scrollbar {  
  display: none; 
} 

header {
    background-color: #d60808;
    color: #fff;
    padding: 20px;
}
header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.user-info {
  font-size: 16px;
  cursor: pointer;
}

.swiper-container {  
  width: 100%;  
  height: 50px; /* 设置轮播图的高度 */  
}  
.swiper-slide {  
  background-size: cover;  
  background-position: center;  
  display: flex;  
  justify-content: center;  
  align-items: center;  
}  

nav {
  background-color: #d60808;
}

nav ul {
  list-style-type: none;
  padding: 0;
  margin: 0;
  display: flex;
  justify-content: space-around;
  align-items: center;
  font-size: 1.5em;
}

nav ul li {
  margin: 0;
}

nav ul li a {
  color: white;
  text-decoration: none;
  padding: 10px;
  display: block;
}

nav ul li a:hover {
  color: #ffd700;
}

main {
  display: flex;
  flex-direction: row;
  overflow-x: scroll;
  scroll-snap-type: x mandatory;
  overflow-x: hidden;
  margin: 0;
  padding: 0;
  border: 0;
}

.section {
  flex: 0 0 auto;
  width: 100vw;
  height: 100vh;
  scroll-snap-align: start;
  padding: 0;
  margin:0;
  border: 0;
}

.section h2{
  text-align: center;
}

footer {
  background-color:#d60808;
  color: #fff;
  padding: 20px;
  text-align: center;
}

</style>
