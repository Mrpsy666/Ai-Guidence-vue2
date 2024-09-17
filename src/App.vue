<template>
  <div id="app">
    <AiHeader />
    <div class="content">
      <el-row>
        <el-col :span="4">
          <el-menu :default-active="activeIndex" @select="handleSelect" class="el-menu-vertical">
            <el-menu-item index="1">智能导诊</el-menu-item>
            <el-menu-item index="2">疾病自查</el-menu-item>
            <el-menu-item index="3">快捷分诊</el-menu-item>
          </el-menu>
        </el-col>
        <el-col :span="20">
          <router-view></router-view> <!-- 路由视图，动态渲染模块 -->
        </el-col>
      </el-row>
    </div>
    <AiFooter />
  </div>
</template>

<script>
import AiHeader from '@/components/AiHeader.vue';
import AiFooter from '@/components/AiFooter.vue';

export default {
  components: {
    AiHeader,
    AiFooter,
  },
  data() {
    return {
      activeIndex: '1',
    };
  },
  methods: {
    handleSelect(key) {
      if (key === '1') {
        this.$router.push('/diagnosis');
      } else if (key === '2') {
        this.$router.push('/self-check');
      } else if (key === '3') {
        this.$router.push('/fastDiagnosis');
      }
    },
  },
};
</script>

<style>
/* 设置最小高度为视口高度，并使用 flex 布局 */
#app {
  min-height: 100vh; /* 视口高度的最小值 */
  display: flex;
  flex-direction: column;
}

.content {
  flex: 1; /* 主内容区域填满剩余空间 */
  display: flex;
  flex-direction: column;
}

el-row {
  flex: 1; /* 让 el-row 也占据可用空间 */
  margin: 20px;
}

el-col {
  background-color: #f5f5f5;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);
}

AiFooter {
  background-color: #f8f8f8;
  padding: 20px;
  text-align: center;
}
</style>
