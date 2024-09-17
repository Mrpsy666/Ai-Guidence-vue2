<template>
  <div class="chat-window">
    <div v-for="(message, index) in messages" :key="index" :class="['message', message.sender]">
      <div class="message-content">{{ message.text }}</div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    messages: {
      type: Array,
      required: true,
    },
  },
};
</script>

<style scoped>
.chat-window {
  height: 400px;
  overflow-y: auto;
  padding: 20px;
  background-color: #f5f5f5;
  border: 1px solid #ddd;
}

.message {
  display: flex;
  margin: 15px 0;
}

.message.user {
  justify-content: flex-end; /* 用户消息靠右显示 */
}

.message.user .message-content {
  background-color: #409eff;
  color: white;
  padding: 10px 20px;
  border-radius: 10px;
  max-width: 60%;
  margin-left: auto; /* 将气泡整体右对齐 */
  text-align: left;  /* 文本内容左对齐 */
  word-wrap: break-word; /* 允许长单词换行 */
  white-space: pre-wrap; /* 保持空格和换行 */
}

.message.system .message-content {
  background-color: #e0e0e0;
  color: #333;
  padding: 10px 20px;
  border-radius: 10px;
  max-width: 60%;
  text-align: left; /* 文本内容左对齐 */
}

.message-content {
  word-wrap: break-word; /* 允许长单词换行 */
  white-space: pre-wrap; /* 保持空格和换行 */
}
</style>
