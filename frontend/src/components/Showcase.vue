<script setup>
import { ref, onMounted, inject } from 'vue'
import axios from 'axios'

// 注入全局权限状态
const isAdmin = inject('isAdmin')

// 项目列表
const projects = ref([])
// 新项目
const newProject = ref({
  title: '',
  description: '',
  image_url: ''
})
// 加载状态
const loading = ref(false)
// 错误信息
const error = ref('')

// 获取项目列表
const fetchProjects = async () => {
  try {
    loading.value = true
    const response = await axios.get('http://localhost:8000/projects')
    projects.value = response.data
  } catch (err) {
    error.value = '获取项目失败，请稍后重试'
    console.error('Error fetching projects:', err)
  } finally {
    loading.value = false
  }
}

// 提交新项目
const submitProject = async () => {
  if (!newProject.value.title || !newProject.value.description) {
    error.value = '请填写项目标题和描述'
    return
  }

  try {
    loading.value = true
    const response = await axios.post('http://localhost:8000/projects', newProject.value)
    projects.value.push(response.data)
    // 重置表单
    newProject.value = {
      title: '',
      description: '',
      image_url: ''
    }
    error.value = ''
  } catch (err) {
    error.value = '提交项目失败，请稍后重试'
    console.error('Error submitting project:', err)
  } finally {
    loading.value = false
  }
}

// 删除项目
const deleteProject = async (id) => {
  try {
    await axios.delete(`http://localhost:8000/projects/${id}`)
    projects.value = projects.value.filter(project => project.id !== id)
  } catch (err) {
    error.value = '删除项目失败，请稍后重试'
    console.error('Error deleting project:', err)
  }
}

// 组件挂载时获取项目
onMounted(() => {
  fetchProjects()
})
</script>

<template>
  <div class="showcase">
    <h2>项目展示柜</h2>
    
    <!-- 错误提示 -->
    <div v-if="error" class="error-message">
      {{ error }}
    </div>

    <!-- 添加项目表单 -->
    <div class="project-form">
      <h3>添加项目</h3>
      <form @submit.prevent="submitProject">
        <div class="form-group">
          <label for="title">项目标题：</label>
          <input 
            type="text" 
            id="title" 
            v-model="newProject.title"
            placeholder="请输入项目标题"
          />
        </div>
        <div class="form-group">
          <label for="description">项目描述：</label>
          <textarea 
            id="description" 
            v-model="newProject.description"
            placeholder="请输入项目描述"
            rows="4"
          ></textarea>
        </div>
        <div class="form-group">
          <label for="image_url">图片URL（可选）：</label>
          <input 
            type="text" 
            id="image_url" 
            v-model="newProject.image_url"
            placeholder="请输入图片URL"
          />
        </div>
        <button type="submit" :disabled="loading">
          {{ loading ? '提交中...' : '提交项目' }}
        </button>
      </form>
    </div>

    <!-- 项目列表 -->
    <div class="projects-list">
      <h3>项目列表</h3>
      <div v-if="loading" class="loading">加载中...</div>
      <div v-else-if="projects.length === 0" class="empty">暂无项目</div>
      <div v-else class="projects-grid">
        <div 
          v-for="project in projects" 
          :key="project.id"
          class="project-card"
        >
          <div v-if="project.image_url" class="project-image">
            <img :src="project.image_url" :alt="project.title" />
          </div>
          <div class="project-content">
            <h4>{{ project.title }}</h4>
            <p class="project-description">{{ project.description }}</p>
            <p class="project-date">{{ project.created_at }}</p>
            <button 
              class="delete-btn"
              @click="deleteProject(project.id)"
              :disabled="loading"
              v-if="isAdmin"
            >
              删除
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.showcase {
  max-width: 1000px;
  margin: 0 auto;
}

.showcase h2 {
  text-align: center;
  margin-bottom: 2rem;
  color: #333;
}

/* 错误提示 */
.error-message {
  background-color: #ffebee;
  color: #c62828;
  padding: 1rem;
  border-radius: 4px;
  margin-bottom: 1.5rem;
}

/* 添加项目表单 */
.project-form {
  background-color: white;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  margin-bottom: 2rem;
}

.project-form h3 {
  margin-bottom: 1.5rem;
  color: #333;
}

.form-group {
  margin-bottom: 1.5rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: bold;
  color: #555;
}

.form-group input,
.form-group textarea {
  width: 100%;
  padding: 0.8rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 1rem;
}

.form-group textarea {
  resize: vertical;
}

.project-form button {
  background-color: #42b883;
  color: white;
  border: none;
  padding: 0.8rem 1.5rem;
  border-radius: 4px;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.3s;
}

.project-form button:hover {
  background-color: #359e6f;
}

.project-form button:disabled {
  background-color: #b5d8c6;
  cursor: not-allowed;
}

/* 项目列表样式 */
.projects-list h3 {
  margin-bottom: 1.5rem;
  color: #333;
}

.loading,
.empty {
  text-align: center;
  padding: 2rem;
  color: #666;
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.projects-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1.5rem;
}

.project-card {
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  overflow: hidden;
  transition: transform 0.3s;
}

.project-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
}

.project-image {
  height: 200px;
  overflow: hidden;
}

.project-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.project-content {
  padding: 1.5rem;
}

.project-content h4 {
  font-size: 1.2rem;
  margin-bottom: 0.8rem;
  color: #333;
}

.project-description {
  color: #555;
  line-height: 1.6;
  margin-bottom: 0.8rem;
  min-height: 80px;
}

.project-date {
  font-size: 0.8rem;
  color: #999;
  margin-bottom: 1rem;
}

.delete-btn {
  background-color: #e53935;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  font-size: 0.9rem;
  cursor: pointer;
  transition: background-color 0.3s;
}

.delete-btn:hover {
  background-color: #c62828;
}
</style>