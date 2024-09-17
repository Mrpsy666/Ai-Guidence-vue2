<template>
  <div class="input-area">
    <el-input
      v-model="inputText"
      placeholder="请描述您的症状..."
      @keyup.enter="sendInput"
      clearable
      class="input-box"
    ></el-input>
    <el-button type="primary" @click="sendInput" class="send-button">发送</el-button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      inputText: '',
    };
  },
  methods: {
    sendInput() {
      if (this.inputText.trim()) {
        this.$emit('sendMessage', this.inputText);
        this.inputText = ''; // 清空输入框
      }
    },
  },
};
</script>

<style scoped>
.input-area {
  display: flex;
  align-items: center; /* 垂直居中 */
  margin-top: 10px;
  padding: 10px 0;
}

.input-box {
  flex-grow: 1;
  margin-right: 10px; /* 为按钮预留空间 */
}

.send-button {
  flex-shrink: 0;
  padding: 8px 16px;
  font-size: 16px;
}
</style>
