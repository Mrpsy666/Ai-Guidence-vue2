<template>
  <div class="departments">
    <div class="department-list">
      <div
        v-for="dept in departments"
        :key="dept.id"
        class="department-card"
        @click="goToDepartmentDetails(dept.id)"gi
      >
        <div class="department-name">{{ dept.name }}</div>
      </div>
    </div>
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
.departments {
  padding: 20px;
  background-color: #f0f2f5;
}

.department-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  grid-gap: 20px;
}

.department-card {
  background-color: #fff;
  border-radius: 12px;
  padding: 30px 20px;
  text-align: center;
  cursor: pointer;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.department-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
}

.department-name {
  font-size: 20px;
  font-weight: bold;
  color: #333;
}

@media (max-width: 768px) {
  .department-card {
    padding: 20px 15px;
  }
  .department-name {
    font-size: 18px;
  }
}
</style>
