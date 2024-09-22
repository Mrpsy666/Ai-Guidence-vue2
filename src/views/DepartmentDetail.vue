<template>
  <div class="department-doctors">
    <!-- 左侧医生列表 -->
    <div class="doctor-list">
      <div v-for="doctor in doctors" :key="doctor.id" class="doctor-card">
        <div class="doctor-info" @click="selectDoctor(doctor)">
          <div class="doctor-name">{{ doctor.name }}</div>
          <div class="doctor-title">{{ doctor.title }}</div>
        </div>
        <button class="appointment-button" @click.stop="bookAppointment(doctor)">预约</button>
      </div>
    </div>

    <!-- 右侧医生排班 -->
    <div class="doctor-schedule" v-if="selectedDoctor">
      <h2>{{ selectedDoctor.name }}的预约</h2>
      <div v-for="schedule in doctorSchedule" :key="schedule.date" class="schedule-card">
        <h3>{{ schedule.date }} ({{ schedule.weekday }})</h3>
        <div class="time-slot" v-for="slot in schedule.timeSlots" :key="slot.timeSlot">
          <span>{{ slot.timeSlot }} - {{ slot.fee }}元/次</span>
          <span>{{ slot.status }}</span>
          <span v-if="slot.status === '可预约'">余{{ slot.remaining }}个</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      doctors: [],            // 医生列表
      selectedDoctor: null,   // 当前选中的医生
      doctorSchedule: []      // 选中医生的排班信息
    };
  },
  created() {
    const departmentId = this.$route.params.id;
    this.getDoctors(departmentId);
  },
  methods: {
    getDoctors(departmentId) {
      // 获取科室医生数据
      this.$axios.get(`/appoint/department/${departmentId}/doctors`).then(response => {
        this.doctors = response.data;
      });
    },
    selectDoctor(doctor) {
      this.selectedDoctor = doctor;
      // 获取选中医生的排班信息
      this.$axios.get(`/appoint/schedule/${doctor.id}`).then(response => {
        const scheduleData = response.data;
        // 处理排班数据，按日期分组
        const groupedSchedule = {};
        scheduleData.forEach(entry => {
          if (!groupedSchedule[entry.date]) {
            // 获取星期几
            const dateObj = new Date(entry.date);
            const weekdays = ['星期日', '星期一', '星期二', '星期三', '星期四', '星期五', '星期六'];
            const weekday = weekdays[dateObj.getDay()];
            groupedSchedule[entry.date] = {
              date: entry.date,
              weekday: weekday,
              timeSlots: []
            };
          }
          groupedSchedule[entry.date].timeSlots.push({
            timeSlot: entry.timeSlot,
            status: entry.status,
            remaining: entry.remaining,
            fee: entry.fee
          });
        });
        // 转换为数组
        this.doctorSchedule = Object.values(groupedSchedule);
      });
    },
    bookAppointment(doctor) {
      const id = doctor.id;
      this.$router.push(`/appoint-doctor/${id}`);
    }
  }
}
</script>

<style scoped>
.department-doctors {
  display: flex;
  padding: 20px;
}

/* 左侧医生列表样式 */
.doctor-list {
  width: 30%;
  margin-right: 20px;
  border-right: 1px solid #ddd;
}

.doctor-card {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 15px;
  margin-bottom: 10px;
  background-color: #f9f9f9;
  border: 1px solid #ddd;
  border-radius: 8px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.doctor-card:hover {
  background-color: #eaeaea;
}

.doctor-info {
  flex-grow: 1; /* 让医生信息部分占据剩余空间 */
}

.doctor-name {
  font-size: 16px;
  font-weight: bold;
}

.doctor-title {
  font-size: 14px;
  color: #666;
}

.appointment-button {
  background-color: #4caf50;
  color: white;
  border: none;
  border-radius: 4px;
  padding: 8px 12px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.appointment-button:hover {
  background-color: #45a049;
}


/* 右侧医生排班样式 */
.doctor-schedule {
  width: 70%;
  padding-left: 20px;
}

.schedule-card {
  background-color: #fafafa;
  border: 1px solid #eee;
  border-radius: 8px;
  padding: 15px;
  margin-bottom: 15px;
}

.time-slot {
  display: flex;
  justify-content: space-between;
  padding: 10px 0;
  border-top: 1px solid #eee;
}

h2 {
  margin-bottom: 20px;
  font-size: 24px;
}

h3 {
  margin-bottom: 10px;
  font-size: 20px;
  color: #333;
}
</style>
