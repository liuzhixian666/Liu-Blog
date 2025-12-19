<script setup>
import { ref } from 'vue'

// 聊天消息列表
const messages = ref([
  {
    id: 1,
    content: '你好！我是刘治鲜的AI分身，有什么可以帮助你的吗？',
    sender: 'ai'
  }
])

// 新消息输入
const newMessage = ref('')
// 加载状态
const loading = ref(false)

// 发送消息
const sendMessage = async () => {
  if (!newMessage.value.trim()) return

  // 添加用户消息
  const userMessage = {
    id: Date.now(),
    content: newMessage.value,
    sender: 'user'
  }
  messages.value.push(userMessage)

  // 清空输入框
  newMessage.value = ''

  // 模拟AI思考
  loading.value = true
  
  try {
    // 这里可以替换为实际的AI API调用
    await new Promise(resolve => setTimeout(resolve, 1000))
    
    // 添加AI回复
    const aiResponse = {
      id: Date.now() + 1,
      content: '感谢你的提问！目前我正在学习中，更多功能即将上线。你可以告诉我你的需求，我会尽力帮助你。',
      sender: 'ai'
    }
    messages.value.push(aiResponse)
  } catch (error) {
    console.error('AI回复失败:', error)
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <div class="ai-avatar">
    <h2>AI分身</h2>
    
    <div class="ai-container">
      <!-- AI头像 -->
      <div class="ai-header">
        <div class="ai-avatar-img">
          <img src="https://picsum.photos/id/237/100/100" alt="AI Avatar" />
        </div>
        <div class="ai-info">
          <h3>刘治鲜的AI助手</h3>
          <p class="ai-status">在线</p>
        </div>
      </div>

      <!-- 聊天窗口 -->
      <div class="chat-window">
        <div 
          v-for="message in messages" 
          :key="message.id"
          :class="['message', message.sender]"
        >
          <div class="message-content">
            {{ message.content }}
          </div>
        </div>
        
        <div v-if="loading" class="loading-message">
          <span class="loading-dots">AI正在思考...</span>
        </div>
      </div>

      <!-- 消息输入 -->
      <div class="message-input-area">
        <input
          type="text"
          v-model="newMessage"
          @keyup.enter="sendMessage"
          placeholder="输入消息..."
          :disabled="loading"
        />
        <button @click="sendMessage" :disabled="loading">
          {{ loading ? '发送中...' : '发送' }}
        </button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.ai-avatar {
  max-width: 800px;
  margin: 0 auto;
}

.ai-avatar h2 {
  text-align: center;
  margin-bottom: 2rem;
  color: #333;
  font-size: 2.5rem;
  font-weight: bold;
}

.ai-container {
  background-color: white;
  border-radius: 12px;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
  overflow: hidden;
}

/* AI头像和信息 */
.ai-header {
  display: flex;
  align-items: center;
  gap: 1.5rem;
  padding: 2rem;
  background-color: #42b883;
  color: white;
}

.ai-avatar-img {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  overflow: hidden;
  border: 3px solid white;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
}

.ai-avatar-img img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.ai-info h3 {
  margin: 0 0 0.5rem 0;
  font-size: 1.8rem;
}

.ai-status {
  margin: 0;
  font-size: 1rem;
  opacity: 0.9;
}

/* 聊天窗口 */
.chat-window {
  padding: 2rem;
  height: 500px;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  gap: 1rem;
  background-color: #f8f9fa;
}

.message {
  max-width: 70%;
  padding: 1rem;
  border-radius: 12px;
  position: relative;
}

.message.user {
  align-self: flex-end;
  background-color: #42b883;
  color: white;
  border-bottom-right-radius: 4px;
}

.message.ai {
  align-self: flex-start;
  background-color: white;
  color: #333;
  border-bottom-left-radius: 4px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.message-content {
  margin: 0;
  line-height: 1.6;
}

.loading-message {
  align-self: flex-start;
  padding: 1rem;
  color: #666;
}

.loading-dots::after {
  content: '';
  animation: dots 1.5s infinite;
}

@keyframes dots {
  0%, 20% { content: '.'; }
  40% { content: '..'; }
  60%, 100% { content: '...'; }
}

/* 消息输入区域 */
.message-input-area {
  display: flex;
  gap: 1rem;
  padding: 2rem;
  background-color: white;
  border-top: 1px solid #e9ecef;
}

.message-input-area input {
  flex: 1;
  padding: 1rem;
  border: 2px solid #e9ecef;
  border-radius: 8px;
  font-size: 1rem;
  transition: border-color 0.3s;
}

.message-input-area input:focus {
  outline: none;
  border-color: #42b883;
}

.message-input-area button {
  background-color: #42b883;
  color: white;
  border: none;
  padding: 1rem 2rem;
  border-radius: 8px;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.3s;
  min-width: 100px;
}

.message-input-area button:hover {
  background-color: #359e6f;
}

.message-input-area button:disabled {
  background-color: #b5d8c6;
  cursor: not-allowed;
}

/* 响应式设计 */
@media (max-width: 768px) {
  .message {
    max-width: 85%;
  }
  
  .ai-header {
    padding: 1.5rem;
    gap: 1rem;
  }
  
  .ai-avatar-img {
    width: 60px;
    height: 60px;
  }
  
  .ai-info h3 {
    font-size: 1.5rem;
  }
  
  .chat-window {
    height: 400px;
    padding: 1.5rem;
  }
  
  .message-input-area {
    padding: 1.5rem;
  }
}
</style>