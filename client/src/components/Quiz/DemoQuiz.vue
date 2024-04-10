<template>
  <div class="container">
    <h1>Demo Quiz</h1>
    <div v-for="q in questions" :key="q.id">
      <label class="mt-4">{{q.id}}. {{q.question_description}}</label>
      <div v-for="(choice, index) in q.choices" :key="index" v-if="choice !== null">
        <input
          type="radio"
          :name="'question_' + q.id"
          :value="choice"
          v-model="q.selectedChoice"
        >
        <label class="mx-1">{{ choice }}</label>
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
    axios.get('http://localhost:8080/api/question/')
      .then(response => {
        if (response.data.results && response.data.results.length > 0) {
          this.questions = response.data.results.map(question => ({
            ...question,
            selectedChoice: null,
            choices: this.shuffleChoices([question.correct_answer, question.wrong_answer1, question.wrong_answer2, question.wrong_answer3].filter(Boolean)), // Filter out null values
            numOptions: this.getNumOptions(question)
          }));
        }
      })
      .catch(error => {
        console.error('Error fetching questions:', error);
      });
  },
  methods: {
    shuffleChoices(choices) {
      for (let i = choices.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * i);
        [choices[i], choices[j]] = [choices[j], choices[i]];
      }
      return choices;
    },
    getNumOptions(question) {
      let count = 0;
      if (question.correct_answer) count++;
      if (question.wrong_answer1) count++;
      if (question.wrong_answer2) count++;
      if (question.wrong_answer3) count++;
      return count;
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
