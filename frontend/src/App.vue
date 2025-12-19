<script setup>
import { ref, provide } from 'vue'
import Home from './components/Home.vue'
import MessageBoard from './components/MessageBoard.vue'
import Showcase from './components/Showcase.vue'
import AIAvatar from './components/AIAvatar.vue'

const currentPage = ref('home')

// 权限管理状态
const isAdmin = ref(false)
const password = ref('')
const showPasswordInput = ref(false)

// 密码验证函数
const verifyPassword = () => {
  if (password.value === 'admin123') { // 示例密码，实际应用应加密存储
    isAdmin.value = true
    showPasswordInput.value = false
    password.value = ''
  } else {
    alert('密码错误，请重试')
    password.value = ''
  }
}

// 隐藏密码输入框
const hidePasswordInput = () => {
  showPasswordInput.value = false
  password.value = ''
}

// 提供全局状态和方法
provide('isAdmin', isAdmin)
provide('password', password)
provide('showPasswordInput', showPasswordInput)
provide('verifyPassword', verifyPassword)
provide('hidePasswordInput', hidePasswordInput)
</script>

<template>
  <div class="app-container">
    <!-- 导航栏 -->
    <nav class="navbar">
      <h1 class="blog-title">个人博客</h1>
      <div class="nav-links">
        <button 
          @click="currentPage = 'home'" 
          :class="{ active: currentPage === 'home' }"
        >
          首页
        </button>
        <button 
          @click="currentPage = 'message'" 
          :class="{ active: currentPage === 'message' }"
        >
          留言板
        </button>
        <button 
          @click="currentPage = 'showcase'" 
          :class="{ active: currentPage === 'showcase' }"
        >
          展示柜
        </button>
        <button 
          @click="currentPage = 'ai'" 
          :class="{ active: currentPage === 'ai' }"
        >
          AI分身
        </button>
        <!-- 管理员状态 -->
        <span v-if="isAdmin" class="admin-status">
          管理员模式
        </span>
      </div>
    </nav>

    <!-- 主内容区 -->
    <main class="main-content">
      <component :is="
        currentPage === 'home' ? Home : 
        currentPage === 'message' ? MessageBoard : 
        currentPage === 'showcase' ? Showcase : 
        AIAvatar
      " />
    </main>

    <!-- 密码输入模态框 -->
    <div v-if="showPasswordInput" class="password-modal">
      <div class="password-content">
        <h3>管理员登录</h3>
        <input 
          type="password" 
          v-model="password" 
          placeholder="请输入密码" 
          @keyup.enter="verifyPassword"
        />
        <div class="password-buttons">
          <button @click="verifyPassword">确认</button>
          <button @click="hidePasswordInput">取消</button>
        </div>
      </div>
    </div>

    <!-- 页脚 -->
    <footer class="footer" @dblclick="showPasswordInput = true">
      <p>&copy; 2025 个人博客. All rights reserved.</p>
    </footer>
  </div>
</template>

<style>
/* 全局样式 */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Arial', sans-serif;
  line-height: 1.6;
  color: #333;
  background-color: #f5f5f5;
}

.app-container {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

/* 导航栏样式 */
.navbar {
  background-color: #333;
  color: white;
  padding: 1rem 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.blog-title {
  font-size: 1.8rem;
  font-weight: bold;
}

.nav-links {
  display: flex;
  gap: 1.5rem;
}

.nav-links button {
  background: none;
  border: none;
  color: white;
  font-size: 1rem;
  cursor: pointer;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  transition: background-color 0.3s;
}

.nav-links button:hover {
  background-color: #555;
}

.nav-links button.active {
  background-color: #42b883;
}

/* 管理员状态样式 */
.admin-status {
  color: #42b883;
  font-weight: bold;
  margin-left: 1rem;
  padding: 0.5rem 1rem;
  background-color: rgba(66, 184, 131, 0.1);
  border-radius: 4px;
  font-size: 0.9rem;
}

/* 主内容区样式 */
.main-content {
  flex: 1;
  padding: 2rem;
  max-width: 1200px;
  margin: 0 auto;
  width: 100%;
}

/* 页脚样式 */
.footer {
  background-color: #333;
  color: white;
  text-align: center;
  padding: 1rem;
  margin-top: auto;
  cursor: pointer;
  transition: opacity 0.3s;
}

.footer:hover {
  opacity: 0.8;
}

/* 密码模态框样式 */
.password-modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.password-content {
  background-color: white;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
  width: 90%;
  max-width: 400px;
  text-align: center;
}

.password-content h3 {
  margin-bottom: 1.5rem;
  color: #333;
}

.password-content input {
  width: 100%;
  padding: 0.8rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 1rem;
  margin-bottom: 1.5rem;
}

.password-buttons {
  display: flex;
  gap: 1rem;
  justify-content: center;
}

.password-buttons button {
  padding: 0.8rem 1.5rem;
  border: none;
  border-radius: 4px;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.3s;
}

.password-buttons button:first-child {
  background-color: #42b883;
  color: white;
}

.password-buttons button:first-child:hover {
  background-color: #359e6f;
}

.password-buttons button:last-child {
  background-color: #666;
  color: white;
}

.password-buttons button:last-child:hover {
  background-color: #555;
}
</style>
