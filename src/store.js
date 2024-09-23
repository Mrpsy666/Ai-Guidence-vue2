import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    userInfo:{
      name: 'admin',
      age: 29,
      gender: '男',
      phone: '13812345678',
      email: 'zhangsan@example.com',
    },
    appointments: [
        {
      doctor: '张医生',
      date: '2024-09-25',
      timeSlot: '上午',
      department: '心脏内科',
      status: '待确认',
    },
    {
      doctor: '李医生',
      date: '2024-09-30',
      timeSlot: '下午',
      department: '消化内科',
      status: '已确认',
    }
    ]  // 存储预约信息
  },
  mutations: {
    UPDATE_USER_INFO(state, newUserInfo){
      state.userInfo = newUserInfo;
    },
    CANCEL_APPOINTMENT(state, appointmentToCanel){
      state.appointments = state.appointments.filter(
          (appointment) => appointment !== appointmentToCanel
      );
    },
    ADD_APPOINTMENT(state, appointment) {
      state.appointments.push(appointment);
    }
  },
  actions: {
    addAppointment({ commit }, appointment) {
      commit('ADD_APPOINTMENT', appointment);
    },
    cancelAppointment({commit }, appointmentToCancel){
      commit('CANCEL_APPOINTMENT', appointmentToCancel);
    }
  },
  getters: {
    getUserInfo: (state) => state.userInfo,
    getAppointments: state => state.appointments
  }
});
