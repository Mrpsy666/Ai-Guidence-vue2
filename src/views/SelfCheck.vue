<template>
  <div>
    <h1>疾病自查</h1>
    <el-input v-model="searchQuery" placeholder="请输入疾病名称..." clearable></el-input>
    <el-button @click="searchDisease">搜索</el-button>

    <el-table :data="diseases">
      <el-table-column prop="name" label="疾病名称"></el-table-column>
      <el-table-column>
        <template slot-scope="scope">
          <el-button @click="viewDetails(scope.row.id)">查看详情</el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  data() {
    return {
      searchQuery: '',
      diseases: [],
    };
  },
  methods: {
    searchDisease() {
      this.$axios.get(`/disease/search?query=${this.searchQuery}`).then(res => {
        this.diseases = res.data;
      });
    },
    filterByLetter(letter) {
      this.$axios.get(`/disease/search?letter=${letter}`).then(res => {
        this.diseases = res.data;
      });
    },
    viewDetails(id) {
      this.$router.push(`/disease/${id}`);
    },
  },
};
</script>

<style scoped>
h2 {
  margin-top: 20px;
}
</style>
