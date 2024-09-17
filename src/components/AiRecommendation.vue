<template>
  <div class="recommendation">
    <h3>推荐科室</h3>
    <el-card v-if="recommendations && recommendations.length > 0">
      <div v-for="(rec, index) in recommendations" :key="index" class="recommendation-item">
        <p><strong>科室 {{ index + 1 }}：</strong>{{ rec.department }}</p>
        <p><strong>建议：</strong>{{ rec.advice }}</p>
        <hr v-if="index < recommendations.length - 1"/> <!-- 增加分隔线，区分多个科室 -->
      </div>
    </el-card>
    <p v-else>请描述您的症状，系统将为您推荐合适的科室。</p>
  </div>
</template>

<script>
export default {
  props: {
    recommendations: {
      type: Array,
      default: () => [],
    },
  },
};
</script>

<style scoped>
.recommendation {
  padding: 20px;
}

.recommendation-item {
  margin-bottom: 10px;
}

hr {
  margin: 10px 0;
}
</style>
