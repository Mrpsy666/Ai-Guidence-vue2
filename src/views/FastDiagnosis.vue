<template>
  <div class="quick-diagnosis-page">
    <el-row :gutter="20">
      <!-- 左边部分：症状选择 -->
      <el-col :span="16">
        <h1>快捷分诊</h1>
        <p>请选择您当前的症状，我将为您推荐适合的科室：</p>

        <!-- 乳腺外科 -->
        <el-card class="symptom-category">
          <div class="symptom-buttons">
            <el-checkbox-group v-model="selectedSymptoms">
              <el-checkbox label="乳房肿块">乳房肿块</el-checkbox>
              <el-checkbox label="体重变化">体重变化</el-checkbox>
              <el-checkbox label="尿频">尿频</el-checkbox>
              <el-checkbox label="视力下降">视力下降</el-checkbox>
              <el-checkbox label="咳嗽">咳嗽</el-checkbox>
              <el-checkbox label="咳痰">咳痰</el-checkbox>
              <el-checkbox label="呼吸困难">呼吸困难</el-checkbox>
              <el-checkbox label="胸痛">胸痛</el-checkbox>
              <el-checkbox label="发热">发热</el-checkbox>
            </el-checkbox-group>
          </div>
        </el-card>

        <!-- 心脏内科 -->
        <el-card class="symptom-category">
          <div class="symptom-buttons">
            <el-checkbox-group v-model="selectedSymptoms">
              <el-checkbox label="心悸">心悸</el-checkbox>
              <el-checkbox label="胸闷">胸闷</el-checkbox>
              <el-checkbox label="乏力">乏力</el-checkbox>
              <el-checkbox label="浮肿">浮肿</el-checkbox>
              <el-checkbox label="头晕">头晕</el-checkbox>
              <el-checkbox label="耳鸣">耳鸣</el-checkbox>
              <el-checkbox label="骨折">骨折</el-checkbox>
              <el-checkbox label="关节疼痛">关节疼痛</el-checkbox>
              <el-checkbox label="腰背痛">腰背痛</el-checkbox>
              <el-checkbox label="肿胀">肿胀</el-checkbox>
              <el-checkbox label="活动受限">活动受限</el-checkbox>
            </el-checkbox-group>
          </div>
        </el-card>

        <!-- 神经内科 -->
        <el-card class="symptom-category">
          <div class="symptom-buttons">
            <el-checkbox-group v-model="selectedSymptoms">
              <el-checkbox label="头晕">头晕</el-checkbox>
              <el-checkbox label="消化不良">消化不良</el-checkbox>
              <el-checkbox label="心理问题">心理问题</el-checkbox>
              <el-checkbox label="皮肤瘙痒">皮肤瘙痒</el-checkbox>
              <el-checkbox label="胃痛">胃痛</el-checkbox>
            </el-checkbox-group>
          </div>
        </el-card>


        <!-- 操作按钮 -->
        <div class="action-buttons">
          <el-button type="primary" size="large" @click="getRecommendation">获取推荐</el-button>
          <el-button type="danger" size="large" class="no-symptom-button" @click="clearSelection">以上都没有</el-button>
        </div>
      </el-col>

      <!-- 右边部分：科室推荐 -->
      <el-col :span="8">
        <recommendation :recommendations="recommendations" />
      </el-col>
    </el-row>
  </div>
</template>

<script>
import Recommendation from '@/components/AiRecommendation.vue';

export default {
  components: {
    Recommendation
  },
  data() {
    return {
      selectedSymptoms: [], // 存储用户选择的症状
      recommendations: []  // 存储推荐的科室列表
    };
  },
  methods: {
    // 清空选择的症状
    clearSelection() {
      this.selectedSymptoms = [];
    },

    // 获取推荐科室
    getRecommendation() {
      if (this.selectedSymptoms.length === 0) {
        this.recommendations = [];
        return;
      }

      // 模拟后端请求，返回多个科室推荐
      this.$axios.post('/fast/recommend', { symptoms: this.selectedSymptoms }).then(res => {
        this.recommendations = res.data.departments;  // 接收多个科室
      }).catch(err => {
        console.error("请求失败:", err);
        this.recommendations = [];
      });
    }
  }
};
</script>

<style scoped>
.quick-diagnosis-page {
  padding: 20px;
}

.symptom-category {
  margin-bottom: 20px;
}

.action-buttons {
  margin-top: 30px;
}
</style>
