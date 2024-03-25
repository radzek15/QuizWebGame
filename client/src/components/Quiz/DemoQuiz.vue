<script>
import axios from "axios";

export default {
  name: "DemoQuiz",
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
}
</script>

<template>
  <div>
    <h1>Demo Quiz</h1>
    <div v-for="q in questions" :key="q.id">
      <p> {{q.id}}. {{q.question_description}} </p>
      <label>
        <input type="radio"> {{q.correct_answer}} <br>
        <input type="radio"> {{q.wrong_answer1}} <br>
        <input type="radio"> {{q.wrong_answer2}} <br>
        <input type="radio"> {{q.wrong_answer3}}
      </label>
    </div>
  </div>
</template>

<style scoped>

</style>
