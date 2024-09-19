<template>
  <el-header>
    <div class="header-content">
      <img src="@/assets/logo.png" alt="MediGenius Logo" class="logo" />
      <h1>MediGenius 智能导诊系统</h1>
    </div>
  </el-header>
</template>

<script>
export default {
  name: 'AiHeader',
};
</script>

<style scoped>
.header-content {
  display: flex;
  align-items: center; /* 垂直方向居中 */
  justify-content: flex-start; /* 水平方向对齐 */
  background-color: #3a8ee6;
  padding: 10px;

}

.logo {
  width: 39px;  /* 设置logo的宽度 */
  height: auto; /* 高度自适应 */
  margin-right: 10px; /* 给logo和标题之间增加间距 */
}

h1 {
  color: white;
  font-size: 24px;
  margin: 0;
}
</style>
