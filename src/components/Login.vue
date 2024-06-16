<template>
  <div class="login-container">
    <section id="login" class="login-box">
      <h2>{{ showRegister ? '注册' : '登录' }}</h2>
      <div v-if="!isLoggedIn">
        <div v-if="showRegister">
          <div class="form-group">
            <label for="username">用户名</label>
            <input type="text" v-model="registerForm.username">
          </div>
          <div class="form-group">
            <label for="account">账号</label>
            <input type="text" v-model="registerForm.account">
          </div>
          <div class="form-group">
            <label for="password">密码</label>
            <input type="password" v-model="registerForm.password">
          </div>
          <div class="form-group">
            <label for="confirmPassword">确认密码</label>
            <input type="password" v-model="registerForm.confirmPassword">
          </div>
          <div class="form-group">
            <label for="captcha">验证码</label>
            <input type="text" v-model="registerForm.captcha">
            <img :src="captchaSrc" @click="refreshCaptcha">
          </div>
          <button class="button" @click="register">注册</button>
          <button class="button" @click="toggleForm">已有账号？登录</button>
        </div>
        <div v-else>
          <div class="form-group">
            <label for="account">账号</label>
            <input type="text" v-model="loginForm.account">
          </div>
          <div class="form-group">
            <label for="password">密码</label>
            <input type="password" v-model="loginForm.password">
          </div>
          <button class="button" @click="login">登录</button>
          <button class="button" @click="toggleForm">没有账号？注册</button>
        </div>
      </div>
      <div v-else>
        <h2>欢迎，{{ currentUser }}</h2>
        <button class="button" @click="logout">退出登录</button>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'LoGin',
  data() {
    return {
      isLoggedIn: false,
      showRegister: false,
      currentUser: '',
      registerForm: {
        username: '',
        account: '',
        password: '',
        confirmPassword: '',
        captcha: ''
      },
      loginForm: {
        account: '',
        password: ''
      },
      captchaSrc: 'https://dummyimage.com/100x30/000/fff.png&text=1234'
    };
  },
  methods: {
    toggleForm() {
      this.showRegister = !this.showRegister;
    },
    refreshCaptcha() {
      this.captchaSrc = 'https://dummyimage.com/100x30/000/fff.png&text=' + Math.random().toString(36).substring(7);
    },
    register() {
      if (this.registerForm.password !== this.registerForm.confirmPassword) {
        alert('密码和确认密码不匹配');
        return;
      }
      localStorage.setItem(this.registerForm.account, JSON.stringify({
        username: this.registerForm.username,
        account: this.registerForm.account,
        password: this.registerForm.password
      }));
      alert('注册成功');
      this.toggleForm();
    },
    login() {
      const user = JSON.parse(localStorage.getItem(this.loginForm.account));
      if (user && user.password === this.loginForm.password) {
        this.isLoggedIn = true;
        this.currentUser = user.username;
        this.$emit('updateUser', this.currentUser);
        localStorage.setItem('currentUser', JSON.stringify({ username: this.currentUser }));
        this.$router.push('/');
      } else {
        alert('账号或密码错误');
      }
    },
    logout() {
      this.isLoggedIn = false;
      this.currentUser = '';
      this.$emit('updateUser', '');
      localStorage.removeItem('currentUser');
    }
  },
  created() {
    const savedUser = JSON.parse(localStorage.getItem('currentUser'));
    if (savedUser) {
      this.isLoggedIn = true;
      this.currentUser = savedUser.username;
    }
  }
};
</script>

<style scoped>
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background: url('#') no-repeat center center fixed;
  background-size: cover;
  width:100%
}

.login-box {
  display: flex;
  justify-content: center;
  background: rgba(0, 0, 0, 0.8);
  padding: 20px;
  border-radius: 8px;
  width: 300px;
  color: white;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}

.form-group {
  margin-bottom: 15px;
  width: 100%;

}

.form-group label {
  display: block;
  margin-bottom: 5px;
}

.form-group input {
  width: 100%;
  padding: 8px;
  box-sizing: border-box;
  border: none;
  border-radius: 4px;
  background: white;
  color: black;
}

.button {
  width: 100%;
  padding: 10px;
  margin: 5px 0;
  border: none;
  border-radius: 4px;
  background: #333;
  color: white;
  cursor: pointer;
}

.button:hover {
  background: #555;
}
</style>
