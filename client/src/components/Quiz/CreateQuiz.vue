<template>
  <div class="container">
    <h2>Create New Quiz</h2>
    <form @submit.prevent="createQuiz">
      <label for="quizName">Quiz Name:</label>
      <input type="text" id="quizName" v-model="quizName" required>

      <label for="quizDescription">Quiz Description:</label>
      <input type="text" id="quizDescription" v-model="quizDescription" required>

      <label for="availableQuestions">Available Questions:</label>
      <select id="availableQuestions" v-model="selectedQuestions" multiple>
        <option v-for="question in availableQuestions" :key="question.id" :value="question.id">
          {{ question.question_description }}
        </option>
      </select>

      <label for="selectedQuestions">Selected Questions:</label>
      <ul>
        <li v-for="questionId in selectedQuestions" :key="questionId">
          {{ getQuestionById(questionId).question_description }}
        </li>
      </ul>

      <button type="submit">Create Quiz</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'CreateQuiz',
  data() {
    return {
      quizName: '',
      quizDescription: '',
      selectedQuestions: [],
      availableQuestions: [],
      csrfToken: ''
    };
  },
  created() {
    this.fetchCSRFToken();
    this.fetchAvailableQuestions();
  },
  methods: {
    fetchCSRFToken() {
      this.csrfToken = this.getCookie('csrftoken');
    },
    getCookie(name) {
      const value = `; ${document.cookie}`;
      const parts = value.split(`; ${name}=`);
      if (parts.length === 2) return parts.pop().split(';').shift();
    },
    fetchAvailableQuestions() {
      axios.get('http://localhost:8080/api/question/')
        .then(response => {
          this.availableQuestions = response.data.results;
        })
        .catch(error => {
          console.error('Error fetching available questions:', error);
        });
    },
    getQuestionById(questionId) {
      return this.availableQuestions.find(question => question.id === questionId);
    },
    createQuiz() {
      const quizData = {
        quiz_name: this.quizName,
        quiz_description: this.quizDescription,
        questions: this.selectedQuestions
      };

      axios.post('http://localhost:8080/api/quiz/', quizData, {
        headers: {
          'X-CSRFToken': this.csrfToken
        }
      })
      .then(response => {
        console.log('Quiz created:', response.data);
      })
      .catch(error => {
        console.error('Error creating quiz:', error);
      });
    }
  }
};
</script>

<style scoped>

</style>
