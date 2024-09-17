<template>
  <div>
    <el-container>
      <el-main>
        <ChatWindow :messages="messages" />
        <InputArea @sendMessage="sendMessage" />
      </el-main>
      <el-aside width="300px">
        <AiRecommendation :recommendation="recommendation" />
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
      recommendation: null, // 科室推荐结果
      sessionId: null,      // 会话 ID
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
        const response = await this.$axios.post('http://localhost:8000/chat/chat', payload);

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
  },
};
</script>

<style scoped>

el-container {
  margin: 20px;
  padding: 20px;
}

el-main {
  background-color: #f5f5f5;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);
}
</style>