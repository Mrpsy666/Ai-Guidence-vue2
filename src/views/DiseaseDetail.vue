<template>
  <div>
    <h1>{{ disease.name }}</h1>
    <el-tabs v-model="activeTab">
      <el-tab-pane label="概述" name="overview">{{ disease.overview }}</el-tab-pane>
      <el-tab-pane label="症状" name="symptoms">{{ disease.symptoms.join(', ') }}</el-tab-pane>
      <el-tab-pane label="病因" name="causes">{{ disease.causes.join(', ') }}</el-tab-pane>
      <el-tab-pane label="检查方法" name="tests">{{disease.tests.join(', ')}}</el-tab-pane>
      <el-tab-pane label="治疗" name="treatments">{{disease.treatments.join(', ')}}</el-tab-pane>
      <el-tab-pane label="药物" name="medications">{{disease.medications.join(', ')}}</el-tab-pane>
      <el-tab-pane label="预后" name="prognosis">{{disease.prognosis}}</el-tab-pane> <!-- 无需join -->
      <el-tab-pane label="护理" name="care">{{disease.care}}</el-tab-pane> <!-- 无需join -->
      <el-tab-pane label="预防措施" name="prevention">{{disease.prevention}}</el-tab-pane> <!-- 无需join -->
      <el-tab-pane label="传播途径" name="transmission">{{disease.transmission}}</el-tab-pane> <!-- 无需join -->
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
