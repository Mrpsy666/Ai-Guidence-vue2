<template>
  <div>
    <h1>{{ disease.name }}</h1>
    <el-tabs v-model="activeTab">
      <el-tab-pane label="概述" name="overview">{{ disease.overview }}</el-tab-pane>
      <el-tab-pane label="症状" name="symptoms">{{ disease.symptoms.join(', ') }}</el-tab-pane>
      <el-tab-pane label="病因" name="causes">{{ disease.causes.join(', ') }}</el-tab-pane>
      <!-- 其他标签同理 -->
    </el-tabs>
  </div>
</template>

<script>
export default {
  data() {
    return {
      activeTab: 'overview',
      disease: {},
    };
  },
  created() {
    const id = this.$route.params.id;
    this.$axios.get(`/disease/${id}`).then(res => {
      this.disease = res.data;
    });
  },
};
</script>
