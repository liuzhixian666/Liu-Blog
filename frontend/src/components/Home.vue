<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

// 点赞数状态
const likeCount = ref(0)
const isLoading = ref(false)
const error = ref('')
const hasLiked = ref(false)

// 后端API地址
const API_URL = 'http://127.0.0.1:8000'

// 获取当前点赞数
const fetchLikeCount = async () => {
  try {
    isLoading.value = true
    const response = await axios.get(`${API_URL}/footprint`)
    likeCount.value = response.data.count
  } catch (err) {
    error.value = '获取点赞数失败'
    console.error(err)
  } finally {
    isLoading.value = false
  }
}

// 增加点赞
const addLike = async () => {
  if (hasLiked.value) return
  
  try {
    isLoading.value = true
    const response = await axios.post(`${API_URL}/footprint/like`)
    likeCount.value = response.data.count
    hasLiked.value = true
  } catch (err) {
    error.value = '点赞失败'
    console.error(err)
  } finally {
    isLoading.value = false
  }
}

// 组件挂载时获取点赞数
onMounted(() => {
  fetchLikeCount()
})
</script>

<template>
  <div class="home-container">
    <!-- 欢迎图片区域 -->
    <section class="welcome-section">
      <div class="welcome-image">
        <img src="https://picsum.photos/id/1036/1200/400" alt="Welcome to Liu's Blog" />
        <div class="welcome-overlay">
          <h1>Welcome to Liu's Blog</h1>
          <p>记录生活，分享知识</p>
          <!-- 点亮足迹功能 -->
          <div class="footprint-section">
            <button 
              class="like-button" 
              @click="addLike" 
              :disabled="isLoading || hasLiked"
            >
              <span class="like-icon">{{ hasLiked ? '❤️' : '🤍' }}</span>
              <span class="like-text">
                {{ isLoading ? '处理中...' : (hasLiked ? '已点亮足迹' : '点亮足迹') }}
              </span>
              <span class="like-count">{{ likeCount }}</span>
            </button>
            <p v-if="error" class="error-message">{{ error }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- 介绍区域 -->
    <section class="intro-section">
      <h2>关于我的博客</h2>
      <p class="intro-text">
        这是一个基于 Vue 3 和 FastAPI 开发的个人博客网站。
        在这里你可以看到我的项目展示，也可以在留言板留下你的足迹。
        我致力于分享技术知识、生活感悟和项目经验。
      </p>
    </section>

    <!-- 功能特性区域 -->
    <section class="features-section">
      <div class="feature-card">
        <div class="feature-icon">💬</div>
        <h3>留言板</h3>
        <p>与我交流，留下你的想法和建议。</p>
      </div>
      <div class="feature-card">
        <div class="feature-icon">📁</div>
        <h3>项目展示</h3>
        <p>查看我参与和开发的项目。</p>
      </div>
      <div class="feature-card">
        <div class="feature-icon">🤖</div>
        <h3>AI分身</h3>
        <p>与我的AI助手进行智能对话。</p>
      </div>
      <div class="feature-card">
        <div class="feature-icon">❤️</div>
        <h3>点亮足迹</h3>
        <p>留下你的访问记录，为博客点赞。</p>
      </div>
    </section>

    <!-- 最新动态区域 -->
    <section class="latest-section">
      <h2>最新动态</h2>
      <div class="latest-content">
        <div class="latest-item">
          <span class="latest-date">2025-12-19</span>
          <p>博客正式上线啦！</p>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
.home-container {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

/* 欢迎图片区域 */
.welcome-section {
  width: 100%;
  margin-bottom: 1rem;
}

.welcome-image {
  position: relative;
  width: 100%;
  height: 400px;
  overflow: hidden;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

.welcome-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
}

.welcome-image:hover img {
  transform: scale(1.05);
}

.welcome-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.3));
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  color: white;
  text-align: center;
}

.welcome-overlay h1 {
  font-size: 3.5rem;
  margin-bottom: 1rem;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
  font-weight: bold;
}

.welcome-overlay p {
  font-size: 1.5rem;
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5);
}

/* 介绍区域 */
.intro-section {
  text-align: center;
  padding: 3rem 2rem;
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.intro-section h2 {
  font-size: 2.5rem;
  margin-bottom: 1.5rem;
  color: #333;
  font-weight: bold;
}

.intro-text {
  font-size: 1.2rem;
  color: #666;
  max-width: 900px;
  margin: 0 auto;
  line-height: 1.8;
}

/* 功能特性区域 */
.features-section {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 2rem;
}

.feature-card {
  background-color: white;
  padding: 2.5rem 2rem;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  text-align: center;
  transition: all 0.3s ease;
}

.feature-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
}

.feature-icon {
  font-size: 3rem;
  margin-bottom: 1.5rem;
}

.feature-card h3 {
  font-size: 1.8rem;
  margin-bottom: 1rem;
  color: #333;
  font-weight: bold;
}

.feature-card p {
  color: #666;
  font-size: 1.1rem;
  line-height: 1.6;
}

/* 最新动态区域 */
.latest-section {
  background-color: white;
  padding: 2.5rem 2rem;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.latest-section h2 {
  font-size: 2rem;
  margin-bottom: 1.5rem;
  color: #333;
  font-weight: bold;
  text-align: center;
}

.latest-content {
  max-width: 800px;
  margin: 0 auto;
}

.latest-item {
  display: flex;
  align-items: center;
  gap: 1.5rem;
  padding: 1.5rem;
  background-color: #f8f9fa;
  border-radius: 8px;
  border-left: 4px solid #42b883;
}

.latest-date {
  font-weight: bold;
  color: #42b883;
  min-width: 120px;
}

.latest-item p {
  color: #666;
  margin: 0;
}

/* 点亮足迹样式 */
.footprint-section {
  margin-top: 2rem;
}

.like-button {
  display: flex;
  align-items: center;
  gap: 0.8rem;
  background-color: rgba(255, 255, 255, 0.2);
  border: 2px solid white;
  color: white;
  padding: 1rem 2rem;
  font-size: 1.2rem;
  border-radius: 50px;
  cursor: pointer;
  transition: all 0.3s ease;
  backdrop-filter: blur(10px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

.like-button:hover:not(:disabled) {
  background-color: rgba(255, 255, 255, 0.3);
  transform: translateY(-3px);
  box-shadow: 0 6px 16px rgba(0, 0, 0, 0.2);
}

.like-button:disabled {
  opacity: 0.7;
  cursor: not-allowed;
  transform: none;
}

.like-icon {
  font-size: 1.8rem;
  transition: transform 0.3s ease;
}

.like-button:not(:disabled):hover .like-icon {
  transform: scale(1.2);
}

.like-text {
  font-weight: bold;
}

.like-count {
  background-color: rgba(255, 255, 255, 0.3);
  padding: 0.4rem 1rem;
  border-radius: 20px;
  font-weight: bold;
  min-width: 50px;
  text-align: center;
}

.error-message {
  color: #ff4444;
  margin-top: 1rem;
  font-size: 1rem;
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5);
}

/* 响应式设计 */
@media (max-width: 768px) {
  .welcome-overlay h1 {
    font-size: 2.5rem;
  }
  
  .welcome-overlay p {
    font-size: 1.2rem;
  }
  
  .like-button {
    font-size: 1rem;
    padding: 0.8rem 1.5rem;
  }
  
  .like-icon {
    font-size: 1.5rem;
  }
  
  .intro-section h2 {
    font-size: 2rem;
  }
  
  .features-section {
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1.5rem;
  }
}
</style>