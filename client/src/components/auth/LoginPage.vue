<template>
  <div class="container">
    <form @submit.prevent="login">
      <div class="form-group">
        <label for="exampleInputEmail1">Email address</label>
        <input v-model="email" type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter email">
      </div>
      <div class="form-group">
        <label for="exampleInputPassword1">Password</label>
        <input v-model="password" type="password" class="form-control" id="exampleInputPassword1" placeholder="Password">
      </div>
      <button type="submit" class="btn btn-primary">Login</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      email: '',
      password: ''
    };
  },
  methods: {
    async login() {
      try {
        const response = await axios.post('http://localhost:8000/api/auth/login/', {
          email: this.email,
          password: this.password
        });
        console.log(response.data);
        // Redirect or handle successful login
      } catch (error) {
        console.error('Login error:', error.response.data);
        // Handle login error
      }
    }
  }
};
</script>
