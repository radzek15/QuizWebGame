<template>
  <div>
    <h1>Questions</h1>
    <ul>
      <li v-for="question in questions" :key="question.id">
        {{ question }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      questions: []
    };
  },
  created() {
    axios.get('http://localhost:8080/api/questions/')
      .then(response => {
        if (response.data.results && response.data.results.length > 0) {
          this.questions = response.data.results;
        }
      })
      .catch(error => {
        console.error('Error fetching questions:', error);
      });
  }
};
</script>

<style scoped>

</style>
