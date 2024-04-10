<template>
  <div>
    <h2>Create New Question</h2>
    <form @submit.prevent="createQuestion">
      <label for="questionDescription">Question Description:</label>
      <input type="text" id="questionDescription" v-model="questionDescription" required>

      <label for="correctAnswer">Correct Answer:</label>
      <input type="text" id="correctAnswer" v-model="correctAnswer" required>

      <label for="wrongAnswer1">Wrong Answer 1:</label>
      <input type="text" id="wrongAnswer1" v-model="wrongAnswer1" required>

      <label for="wrongAnswer2">Wrong Answer 2:</label>
      <input type="text" id="wrongAnswer2" v-model="wrongAnswer2">

      <label for="wrongAnswer3">Wrong Answer 3:</label>
      <input type="text" id="wrongAnswer3" v-model="wrongAnswer3">

      <button type="submit">Create Question</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'CreateQuestion',
  data() {
    return {
      questionDescription: '',
      correctAnswer: '',
      wrongAnswer1: '',
      wrongAnswer2: '',
      wrongAnswer3: ''
    };
  },
  methods: {
    createQuestion() {
      const questionData = {
        question_description: this.questionDescription,
        correct_answer: this.correctAnswer,
        wrong_answer1: this.wrongAnswer1,
        wrong_answer2: this.wrongAnswer2,
        wrong_answer3: this.wrongAnswer3
      };

      axios.post('http://localhost:8080/api/question/', questionData)
        .then(response => {
          console.log('Question created:', response.data);
        })
        .catch(error => {
          console.error('Error creating question:', error);
        });
    }
  }
};
</script>

<style scoped>

</style>
