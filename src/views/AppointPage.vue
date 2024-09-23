<template>
  <div>
    <h2>预约医生：{{ doctor.name }}</h2>
    <el-form :model="form" label-width="120px">
      <el-form-item label="选择日期">
        <el-date-picker
            v-model="form.date"
            type="date"
            placeholder="选择预约日期"
            value-format="yyyy-MM-dd"
        ></el-date-picker>
      </el-form-item>

      <el-form-item label="选择时间段">
        <el-select v-model="form.timeSlot" placeholder="请选择时间段">
          <el-option label="上午" value="morning"></el-option>
          <el-option label="下午" value="afternoon"></el-option>
        </el-select>
      </el-form-item>

      <el-form-item label="姓名">
        <el-input v-model="form.name" placeholder="请输入姓名"></el-input>
      </el-form-item>

      <el-form-item label="电话号码">
        <el-input v-model="form.phone" placeholder="请输入电话号码"></el-input>
      </el-form-item>

      <el-form-item>
        <el-button type="primary" @click="submitAppointment">提交预约</el-button>
      </el-form-item>
    </el-form>

    <el-dialog :visible.sync="dialogVisible" title="预约结果">
      <p>预约成功！</p>
      <span slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible = false">确认</el-button>
      </span>
    </el-dialog>


  </div>
</template>

<script>
export default {
  data() {
    return {
      form: {
        doctorId: '',
        date: '',
        timeSlot: '',
        name: '',
        phone: '',
      },
      dialogVisible: false,
      appointmentSuccess: false,
      doctor: {}
    };
  },
  created() {
    const doctorId = this.$route.params.id;
    this.form.doctorId = doctorId;
    this.getDoctorInfo(doctorId);
  },
  methods: {
    getDoctorInfo(doctorId) {
      this.$axios.get(`/appoint/doctor/${doctorId}`).then(response => {
        this.doctor = response.data;
      });
    },
    submitAppointment() {
      // 将 doctorId 转换为整数类型，确保一致性
      this.form.doctorId = Number(this.form.doctorId);

      // 将预约信息存储到 Vuex store 中
      this.$store.dispatch('addAppointment', this.form);

      // 标记预约成功并显示对话框
      this.appointmentSuccess = true;
      this.dialogVisible = true;
  }
}
}
</script>

<style scoped>
.dialog-footer {
  text-align: right;
}
</style>
