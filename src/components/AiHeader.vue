<template>
  <el-header>
    <div class="header-content">
      <div class="left-content">
        <img src="@/assets/logo.png" alt="MediGenius Logo" class="logo" />
        <h1>MediGenius 智能导诊系统</h1>
      </div>
      <div class="right-content">
        <!-- 检查是否已登录，未登录显示登录和注册按钮，已登录显示用户名 -->
        <template v-if="!isLoggedIn">
          <el-button type="primary" @click="showLogin = true" class="login-btn">登录</el-button>
          <el-button type="success" @click="handleRegister" class="register-btn">注册</el-button>
        </template>
        <template v-else>
          <span class="username">{{ username }}</span>
        </template>
      </div>
    </div>

    <!-- 登录弹窗 -->
    <el-dialog title="登录" :visible.sync="showLogin">
      <el-form :model="loginForm">
        <el-form-item label="用户名">
          <el-input v-model="loginForm.username"></el-input>
        </el-form-item>
        <el-form-item label="密码">
          <el-input type="password" v-model="loginForm.password"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="showLogin = false">取消</el-button>
        <el-button type="primary" @click="handleLogin">登录</el-button>
      </div>
    </el-dialog>
  </el-header>
</template>

<script>
export default {
  name: 'AiHeader',
  data() {
    return {
      isLoggedIn: false, // 用于跟踪登录状态
      username: '', // 用于存储用户名
      showLogin: false, // 控制登录弹窗显示
      loginForm: {
        username: '',
        password: ''
      }
    };
  },
  methods: {
    handleLogin() {
      const { username, password } = this.loginForm;
      // 简单的用户名和密码验证
      if (username === 'admin' && password === '123456') {
        this.isLoggedIn = true; // 登录成功
        this.username = username; // 保存用户名
        this.showLogin = false; // 关闭登录弹窗
        this.loginForm.password = ''; // 清空密码
      } else {
        this.$message.error('用户名或密码错误');
      }
    },
    handleRegister() {
      // 注册逻辑（这里可以跳转到注册页面）
      console.log('注册按钮点击');
    }
  }
};
</script>

<style scoped>
.header-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #3a8ee6;
  padding: 10px 20px;
}

.left-content {
  display: flex;
  align-items: center;
}

.logo {
  width: 39px;
  height: auto;
  margin-right: 10px;
}

h1 {
  color: white;
  font-size: 24px;
  margin: 0;
}

.right-content {
  display: flex;
  align-items: center;
}

.login-btn {
  margin-right: 10px;
}

.username {
  color: white;
  font-size: 20px;
}

.el-button {
  font-size: 14px;
  padding: 8px 20px;
}
</style>
