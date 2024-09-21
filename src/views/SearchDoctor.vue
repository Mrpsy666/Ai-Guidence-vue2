<template>
  <div>
    <el-input placeholder="搜索医生" v-model="searchText" @input="filterDoctors"></el-input>
    <el-list>
      <el-list-item v-for="doctor in filteredDoctors" :key="doctor.id" @click="goToDoctorDetails(doctor.id)">
        <el-card>
          <div class="doctor-info">
            <p><strong>{{ doctor.name }}</strong> - {{ doctor.title }}</p>
            <p>{{ doctor.specialty }}</p>
          </div>
        </el-card>
      </el-list-item>
    </el-list>
  </div>
</template>

<script>
export default {
  data() {
    return {
      searchText: '',
      doctors: [], // 医生列表
      filteredDoctors: [],
    };
  },
  created() {
    this.getDoctors();
  },
  methods: {
    getDoctors() {
      this.$axios.get('/api/doctors').then(response => {
        this.doctors = response.data;
        this.filteredDoctors = this.doctors;
      });
    },
    filterDoctors() {
      this.filteredDoctors = this.doctors.filter(doctor =>
        doctor.name.includes(this.searchText)
      );
    },
    goToDoctorDetails(doctorId) {
      this.$router.push(`/doctor/${doctorId}`);
    },
  },
};
</script>

<style scoped>
.doctor-info {
  text-align: left;
}
</style>
