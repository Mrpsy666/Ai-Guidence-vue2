<template>
  <div class="home">
    <div class="row">
      <div class="col" @click="goToDoctorSearch">
        <div class="box-card hover-effect">
          <div class="header">
            <span>按医师查找</span>
          </div>
          <div class="icon-wrapper">
            <img src="@/assets/doctor-icon.png" class="icon" />
          </div>
        </div>
      </div>
      <div class="col" @click="goToDepartmentSearch">
        <div class="box-card hover-effect">
          <div class="header">
            <span>按科室查找</span>
          </div>
          <div class="icon-wrapper">
            <img src="@/assets/department-icon.png" class="icon" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    goToDoctorSearch() {
      console.log("Navigating to /search-doctor");
      this.$router.push('/search-doctor');
    },
    goToDepartmentSearch() {
      console.log("Navigating to /search-department");
      this.$router.push('/search-department');
    }
  }
}
</script>

<style scoped>
.home {
  padding: 20px;
}

.row {
  display: flex;
  justify-content: space-between;
  gap: 20px; /* 间距 */
}

.col {
  flex: 1;
  cursor: pointer;
}

.box-card {
  background-color: #fff;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  text-align: center;
  padding: 20px;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.box-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.header {
  font-size: 16px;
  font-weight: bold;
  margin-bottom: 10px;
}

.icon-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 20px;
}

.icon {
  width: 100px;
  height: 100px;
  margin: 0 auto;
}

.hover-effect {
  transition: all 0.3s ease-in-out;
}

.hover-effect:hover {
  box-shadow: 0 6px 18px rgba(0, 0, 0, 0.15);
  transform: scale(1.02);
}
</style>
