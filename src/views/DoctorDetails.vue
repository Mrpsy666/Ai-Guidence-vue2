<template>
  <div>
    <el-card>
      <h2>{{ doctor.name }}</h2>
      <p>{{ doctor.title }}</p>
      <p>{{ doctor.specialty }}</p>

      <el-table :data="doctor.schedule">
        <el-table-column prop="date" label="日期" />
        <el-table-column prop="timeSlot" label="时间段" />
        <el-table-column prop="status" label="预约情况" />
      </el-table>

      <el-button type="primary" @click="goToAppointment">预约</el-button>
    </el-card>
  </div>
</template>

<script>
export default {
  data() {
    return {
      doctor: {}  // 医生详细信息
    };
  },
  created() {
    const doctorId = this.$route.params.id;
    this.$axios.get(`/api/doctor/${doctorId}`).then(response => {
      this.doctor = response.data;
    });
  },
  methods: {
    goToAppointment() {
      this.$router.push(`/appointment/${this.doctor.id}`);
    }
  }
};
</script>

<style scoped>
.el-card {
  text-align: left;
}
</style>
