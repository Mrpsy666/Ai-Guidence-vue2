<template>
  <div class="appointment-page">
    <h1>预约挂号</h1>

    <!-- 科室选择 -->
    <el-form :model="form" label-width="120px">
      <el-form-item label="选择科室">
        <el-select v-model="form.department" placeholder="请选择科室">
          <el-option v-for="dept in departments" :key="dept" :label="dept" :value="dept"></el-option>
        </el-select>
      </el-form-item>

      <!-- 预约日期选择 -->
      <el-form-item label="选择日期">
        <el-date-picker v-model="form.date" type="date" placeholder="选择预约日期"></el-date-picker>
      </el-form-item>

      <!-- 预约时间选择 -->
      <el-form-item label="选择时间段">
        <el-select v-model="form.timeSlot" placeholder="请选择时间段">
          <el-option v-for="slot in timeSlots" :key="slot" :label="slot" :value="slot"></el-option>
        </el-select>
      </el-form-item>

      <!-- 用户信息 -->
      <el-form-item label="姓名">
        <el-input v-model="form.name" placeholder="请输入姓名"></el-input>
      </el-form-item>

      <el-form-item label="电话号码">
        <el-input v-model="form.phone" placeholder="请输入电话号码"></el-input>
      </el-form-item>

      <!-- 提交按钮 -->
      <el-form-item>
        <el-button type="primary" @click="submitAppointment">确认预约</el-button>
      </el-form-item>
    </el-form>

    <!-- 预约结果反馈 -->
    <el-dialog :visible.sync="dialogVisible" title="预约结果">
      <p v-if="appointmentSuccess">预约成功！</p>
      <p v-else>预约失败，请稍后再试。</p>
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
        department: '',
        date: '',
        timeSlot: '',
        name: '',
        phone: '',
      },
      departments: ['心脏内科', '呼吸内科', '泌尿外科', '消化内科', '骨科'], // 模拟科室数据
      timeSlots: ['上午', '下午'], // 模拟时间段
      dialogVisible: false,
      appointmentSuccess: false, // 预约成功状态
    };
  },
  methods: {
  submitAppointment() {
    // 确保日期格式为 YYYY-MM-DD
    const appointmentData = {
      department: this.form.department,
      date: this.form.date ? this.form.date.toISOString().split('T')[0] : '', // 将日期转换为 YYYY-MM-DD 格式
      timeSlot: this.form.timeSlot,
      name: this.form.name,
      phone: this.form.phone,
    };

    // 提交预约请求
    this.$axios.post('/appoint/appointments', appointmentData)
      .then((response) => {
        if (response.data.success) {
          this.appointmentSuccess = true;
        } else {
          this.appointmentSuccess = false;
        }
        this.dialogVisible = true;
      })
      .catch((error) => {
        alert(error.response.data.message);
        this.appointmentSuccess = false;
        this.dialogVisible = true;
      });
  },
}

};
</script>

<style scoped>
.appointment-page {
  padding: 20px;
}

.el-form {
  max-width: 600px;
  margin: 0 auto;
}

.dialog-footer {
  text-align: right;
}
</style>
