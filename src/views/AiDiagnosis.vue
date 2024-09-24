<template>
  <div>
    <el-container style="display: flex; justify-content: space-between;">
      <el-main style="flex: 2; margin-right: 20px;">
        <ChatWindow :messages="messages" />
        <InputArea @sendMessage="sendMessage" />
      </el-main>
      <el-aside width="300px" style="flex: 1;">
        <AiRecommendation :recommendations="recommendations" />
        <el-button type="primary" @click="getRecommendation">分析科室</el-button>
      </el-aside>
</el-container>

  </div>
</template>

<script>
import ChatWindow from '@/components/ChatWindow.vue';
import InputArea from '@/components/InputArea.vue';
import AiRecommendation from '@/components/AiRecommendation.vue';

export default {
  components: {
    ChatWindow,
    InputArea,
    AiRecommendation,
  },
  data() {
    return {
      messages: [],          // 聊天记录
      recommendations: [], // 科室推荐结果
      sessionId: null,      // 会话 ID
      selectedSymptoms: ['头晕','咳嗽'],
    };
  },
  methods: {
    async sendMessage(userMessage) {
      // 添加用户的消息到聊天窗口
      this.messages.push({
        sender: 'user',
        text: userMessage,
      });

      // 显示正在处理的系统消息
      this.messages.push({
        sender: 'system',
        text: '正在分析您的症状，请稍候...',
      });

      try {
        // 构建请求数据
        const payload = {
          prompt: userMessage,
        };
        if (this.sessionId) {
          payload.session_id = this.sessionId;
        }

        // 发送后端API请求
        const response = await this.$axios.post('/chat/chat', payload);

        // 移除加载消息
        this.messages.pop();

        // 更新会话 ID
        if (!this.sessionId) {
          this.sessionId = response.data.session_id;
        }

        // 显示系统的回复
        this.messages.push({
          sender: 'system',
          text: response.data.response,
        });

        // 更新推荐科室
        if (response.data.recommendation) {
          this.recommendation = response.data.recommendation;
        }
      } catch (error) {
        // 移除加载消息
        this.messages.pop();

        // 错误处理
        this.messages.push({
          sender: 'system',
          text: '系统错误，请稍后重试。',
        });
      }
    },
    async getRecommendation() {
      this.$axios.post('/fast/recommend', {symptoms: this.selectedSymptoms}).then(res => {
        this.recommendations = res.data.departments;
      }).catch(err => {
        console.log(err);
        this.recommendations = [];
      })
    }
  },
};
</script>

<style scoped>
el-container {
  margin: 20px;
  padding: 20px;
  background-color: #f7f7f7; /* 增加页面整体的背景色 */
}

el-main {
  background-color: #ffffff; /* 白色背景让聊天窗口看起来更干净 */
  padding: 20px;
  border-radius: 10px; /* 圆角边框 */
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1); /* 阴影效果 */
}

el-aside {
  background-color: #fafafa;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
}

button {
  background-color: #409EFF; /* 按钮使用更鲜艳的颜色 */
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #66b1ff; /* 悬停效果 */
}

input[type="text"] {
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
  width: 80%;
  margin-right: 10px;
}

.input-area {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-top: 20px;
}

</style>