<template>
  <div class="container">
    <h1>Demo Quiz</h1>
    <div v-for="q in questions" :key="q.id">
      <p>{{q.id}}. {{q.question_description}}</p>
      <div v-for="(choice, index) in getChoices(q)" :key="index">
        <input
          type="radio"
          :name="'question_' + q.id"
          :value="choice"
          v-model="q.selectedChoice"
        >
        <label>{{ choice }}</label>
      </div>
    </div>
    <button @click="submitQuiz">Submit Quiz</button>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "DemoQuiz",
  data() {
    return {
      questions: [],
      showResult: false,
      correctAnswers: 0
    };
  },
  created() {
    axios.get('http://localhost:8080/api/questions/')
      .then(response => {
        if (response.data.results && response.data.results.length > 0) {
          this.questions = response.data.results.map(question => ({
            ...question,
            selectedChoice: null
          }));
        }
      })
      .catch(error => {
        console.error('Error fetching questions:', error);
      });
  },
  methods: {
    getChoices(question) {
      return [question.correct_answer, question.wrong_answer1, question.wrong_answer2, question.wrong_answer3];
    },
    submitQuiz() {
      this.correctAnswers = this.questions.reduce((count, question) => {
        return question.selectedChoice === question.correct_answer ? count + 1 : count;
      }, 0);
      alert(`Your score: ${this.correctAnswers}`);
    },
  }
};
</script>

<style scoped>

</style>
