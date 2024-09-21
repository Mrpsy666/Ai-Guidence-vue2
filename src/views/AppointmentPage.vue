<template>
  <div class="home">
    <el-row :gutter="20">
      <el-col :span="12">
        <el-card @click="goToDoctorSearch" class="box-card">
          <div slot="header" class="clearfix">
            <span>按医师查找</span>
          </div>
          <div>
            <img src="@/assets/doctor-icon.png" class="icon"/>
          </div>
        </el-card>
      </el-col>
      <el-col :span="12">
        <el-card @click="goToDepartmentSearch" class="box-card">
          <div slot="header" class="clearfix">
            <span>按科室查找</span>
          </div>
          <div>
            <img src="@/assets/department-icon.png" class="icon"/>
          </div>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  methods: {
    goToDoctorSearch() {
      this.$router.push('/search-doctor');
    },
    goToDepartmentSearch() {
      this.$router.push('/search-department');
    }
  }
}
</script>

<style scoped>
.home {
  padding: 20px;
}

.box-card {
  cursor: pointer;
}

.icon {
  width: 100px;
  height: 100px;
  margin: 20px auto;
}
</style>
