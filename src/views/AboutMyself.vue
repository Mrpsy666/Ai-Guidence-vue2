<template>
  <div class="about-myself">
    <!-- 个人信息部分 -->
    <div class="personal-info">
      <h2>个人信息</h2>
      <el-card class="box-card">
        <div>
          <p><strong>姓名：</strong>{{ userInfo.name }}</p>
          <p><strong>年龄：</strong>{{ userInfo.age }}</p>
          <p><strong>性别：</strong>{{ userInfo.gender }}</p>
          <p><strong>联系电话：</strong>{{ userInfo.phone }}</p>
          <p><strong>邮箱：</strong>{{ userInfo.email }}</p>
        </div>
      </el-card>
    </div>

    <!-- 已预约信息部分 -->
    <div class="appointments">
      <h2>我的预约</h2>
      <el-table :data="appointments" style="width: 100%">
        <el-table-column prop="doctor" label="医生" width="180"></el-table-column>
        <el-table-column prop="date" label="预约日期" width="180"></el-table-column>
        <el-table-column prop="timeSlot" label="时间段" width="180"></el-table-column>
        <el-table-column prop="department" label="科室"></el-table-column>
        <el-table-column prop="status" label="状态" width="120"></el-table-column>
        <el-table-column label="操作" width="150">
          <template v-slot="scope">
            <el-button
              type="danger"
              size="mini"
              @click="cancelAppointment(scope.row)">
              取消预约
            </el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>

    <!-- 取消确认弹窗 -->
    <el-dialog :visible.sync="dialogVisible" title="取消预约">
      <p>您确定要取消这次预约吗？</p>
      <span slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible = false">取消</el-button>
        <el-button type="primary" @click="confirmCancel">确认</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
export default {
  data() {
    return {
      dialogVisible: false,  // 控制弹窗显示
      appointmentToCancel: null,  // 需要取消的预约
    };
  },
  computed: {
    // 从 Vuex 中获取用户信息
    userInfo() {
      return this.$store.getters.getUserInfo;
    },
    // 从 Vuex 中获取预约信息
    appointments() {
      return this.$store.getters.getAppointments;
    }
  },
  methods: {
    // 用户点击取消预约时，弹出确认框
    cancelAppointment(appointment) {
      this.appointmentToCancel = appointment;  // 存储要取消的预约
      this.dialogVisible = true;  // 显示弹窗
    },
    // 确认取消操作
    confirmCancel() {
      this.$store.dispatch('cancelAppointment', this.appointmentToCancel);  // 通过 Vuex 进行取消
      this.dialogVisible = false;  // 关闭弹窗
      this.appointmentToCancel = null;  // 重置状态
    },
  },
};
</script>

<style scoped>
.about-myself {
  padding: 20px;
}

.personal-info {
  margin-bottom: 30px;
}

.personal-info h2,
.appointments h2 {
  margin-bottom: 10px;
}

.el-card {
  padding: 10px;
  background-color: #f9f9f9;
  border-radius: 10px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);
}

.el-table {
  background-color: #ffffff;
  border-radius: 10px;
  overflow: hidden;
}

.el-table th,
.el-table td {
  text-align: center;
}

.appointments {
  margin-top: 30px;
}

.dialog-footer {
  text-align: right;
}
</style>
