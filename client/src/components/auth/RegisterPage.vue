<template>
  <div class="container">
    <form class="col-lg-4" @submit.prevent="submitForm">
      <div class="form-group">
        <label for="exampleInputEmail1">Email address</label>
        <input type="email" class="form-control" v-model="email" placeholder="Enter email">
        <small class="form-text text-muted">We'll never share your email with anyone else.</small>
      </div>
      <div class="form-group">
        <label for="exampleInputPassword1">Password</label>
        <input type="password" class="form-control" v-model="password1" placeholder="Password">
      </div>
      <div class="form-group">
        <label for="exampleInputPassword2">Confirm Password</label>
        <input type="password" class="form-control" v-model="password2" placeholder="Confirm Password">
      </div>
      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: "RegisterPage",
  data() {
    return {
      email: '',
      password1: '',
      password2: ''
    };
  },
  methods: {
    async submitForm() {
      if (this.password1 !== this.password2) {
        alert('Passwords do not match');
        return;
      }

      try {
        await axios.post('http://localhost:8080/api/auth/registration/', {
          email: this.email,
          password1: this.password1,
          password2: this.password2
        });

        alert('Registration successful');
        // Optionally, redirect to another page or perform other actions
      } catch (error) {
        console.error('Error during registration:', error.message);
        alert('Registration failed. Please try again later.');
      }
    }
  }
};
</script>

<style scoped>
/* Add custom component styles here if needed */
</style>
