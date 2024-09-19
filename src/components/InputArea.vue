<template>
  <div class="input-area">
    <el-input
      v-model="inputText"
      placeholder="请描述您的症状..."
      @keyup.enter="handleSend"
    />
    <el-button type="primary" @click="handleSend">发送</el-button>
    <el-button icon="el-icon-microphone" @click="startVoiceInput">语音输入</el-button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      inputText: "", // 用户输入的文本
      recognition: null, // 语音识别对象
    };
  },
  mounted() {
    // 检查浏览器是否支持 Web Speech API
    if ('webkitSpeechRecognition' in window) {
      this.recognition = new window.webkitSpeechRecognition();
      this.recognition.lang = 'zh-CN'; // 设置语言为中文
      this.recognition.continuous = false; // 是否持续监听
      this.recognition.interimResults = false; // 是否返回临时结果

      // 识别成功后，将语音结果赋值给输入框，并自动发送
      this.recognition.onresult = (event) => {
        const transcript = event.results[0][0].transcript;
        this.inputText = transcript; // 将语音识别结果输入到文本框中
        this.handleSend(); // 识别完成后自动发送消息
      };

      // 处理识别错误
      this.recognition.onerror = (event) => {
        console.error('语音识别出错: ', event.error);
        this.$message.error('语音识别出错，请重试');
      };
    } else {
      this.$message.error('当前浏览器不支持语音输入');
    }
  },
  methods: {
    handleSend() {
      if (this.inputText.trim() === "") return;
      this.$emit("sendMessage", this.inputText); // 发送输入内容
      this.inputText = ""; // 清空输入框
    },
    startVoiceInput() {
      if (this.recognition) {
        this.recognition.start(); // 开始语音识别
        this.$message.info('正在监听，请开始说话...');
      } else {
        this.$message.error('当前浏览器不支持语音输入');
      }
    }
  }
};
</script>

<style scoped>
.input-area {
  display: flex;
  align-items: center;
  gap: 10px; /* 设置按钮与输入框之间的间距 */
}

.el-input {
  flex: 1;
}
</style>
