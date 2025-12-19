<script setup>
import { ref, onMounted, inject } from 'vue'
import axios from 'axios'

// 注入全局权限状态
const isAdmin = inject('isAdmin')

// 留言列表
const messages = ref([])
// 新留言
const newMessage = ref({
  name: '',
  content: ''
})
// 加载状态
const loading = ref(false)
// 错误信息
const error = ref('')

// 获取留言列表
const fetchMessages = async () => {
  try {
    loading.value = true
    const response = await axios.get('http://localhost:8000/messages')
    messages.value = response.data
  } catch (err) {
    error.value = '获取留言失败，请稍后重试'
    console.error('Error fetching messages:', err)
  } finally {
    loading.value = false
  }
}

// 提交新留言
const submitMessage = async () => {
  if (!newMessage.value.name || !newMessage.value.content) {
    error.value = '请填写姓名和留言内容'
    return
  }

  try {
    loading.value = true
    const response = await axios.post('http://localhost:8000/messages', newMessage.value)
    messages.value.push(response.data)
    // 重置表单
    newMessage.value = {
      name: '',
      content: ''
    }
    error.value = ''
  } catch (err) {
    error.value = '提交留言失败，请稍后重试'
    console.error('Error submitting message:', err)
  } finally {
    loading.value = false
  }
}

// 删除留言
const deleteMessage = async (id) => {
  try {
    await axios.delete(`http://localhost:8000/messages/${id}`)
    messages.value = messages.value.filter(msg => msg.id !== id)
  } catch (err) {
    error.value = '删除留言失败，请稍后重试'
    console.error('Error deleting message:', err)
  }
}

// 组件挂载时获取留言
onMounted(() => {
  fetchMessages()
})
</script>

<template>
  <div class="message-board">
    <h2>留言板</h2>
    
    <!-- 错误提示 -->
    <div v-if="error" class="error-message">
      {{ error }}
    </div>

    <!-- 添加留言表单 -->
    <div class="message-form">
      <h3>添加留言</h3>
      <form @submit.prevent="submitMessage">
        <div class="form-group">
          <label for="name">姓名：</label>
          <input 
            type="text" 
            id="name" 
            v-model="newMessage.name"
            placeholder="请输入您的姓名"
          />
        </div>
        <div class="form-group">
          <label for="content">留言内容：</label>
          <textarea 
            id="content" 
            v-model="newMessage.content"
            placeholder="请输入您的留言"
            rows="4"
          ></textarea>
        </div>
        <button type="submit" :disabled="loading">
          {{ loading ? '提交中...' : '提交留言' }}
        </button>
      </form>
    </div>

    <!-- 留言列表 -->
    <div class="messages-list">
      <h3>留言列表</h3>
      <div v-if="loading" class="loading">加载中...</div>
      <div v-else-if="messages.length === 0" class="empty">暂无留言</div>
      <div v-else class="messages">
        <div 
          v-for="message in messages" 
          :key="message.id"
          class="message-item"
        >
          <div class="message-header">
            <span class="message-name">{{ message.name }}</span>
            <span class="message-time">{{ message.created_at }}</span>
          </div>
          <div class="message-content">{{ message.content }}</div>
          <button 
            class="delete-btn"
            @click="deleteMessage(message.id)"
            :disabled="loading"
            v-if="isAdmin"
          >
            删除
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.message-board {
  max-width: 800px;
  margin: 0 auto;
}

.message-board h2 {
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

/* 表单样式 */
.message-form {
  background-color: white;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  margin-bottom: 2rem;
}

.message-form h3 {
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

.message-form button {
  background-color: #42b883;
  color: white;
  border: none;
  padding: 0.8rem 1.5rem;
  border-radius: 4px;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.3s;
}

.message-form button:hover {
  background-color: #359e6f;
}

.message-form button:disabled {
  background-color: #b5d8c6;
  cursor: not-allowed;
}

/* 留言列表样式 */
.messages-list h3 {
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

.messages {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.message-item {
  background-color: white;
  padding: 1.5rem;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  position: relative;
}

.message-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.8rem;
}

.message-name {
  font-weight: bold;
  color: #333;
}

.message-time {
  font-size: 0.8rem;
  color: #999;
}

.message-content {
  color: #555;
  line-height: 1.6;
  margin-bottom: 0.8rem;
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