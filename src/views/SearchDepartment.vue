<template>
  <div>
    <el-row :gutter="20">
      <el-col v-for="dept in departments" :key="dept.id" :span="12">
        <el-card @click="goToDepartmentDetails(dept.id)" class="box-card">
          <div>{{ dept.name }}</div>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  data() {
    return {
      departments: []  // 科室列表
    };
  },
  created() {
    this.getDepartments();
  },
  methods: {
    getDepartments() {
      this.$axios.get('/appoint/departments').then(response => {
        this.departments = response.data;
      });
    },
    goToDepartmentDetails(departmentId) {
      this.$router.push(`/department/${departmentId}`);
    }
  }
}
</script>

<style scoped>
.box-card {
  cursor: pointer;
  text-align: center;
}
</style>
