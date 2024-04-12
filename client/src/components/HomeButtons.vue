<script>
export default {
  name: "HomeButtons"
}
</script>

<template>
  <div class="d-flex justify-content-center align-items-center" style="height: calc(100vh);">
    <router-link to="/demo-quiz" class="btn btn-primary custom-btn">DEMO QUIZ</router-link>
    <router-link to="/create-quiz" class="btn btn-primary custom-btn">CREATE QUIZ</router-link>
  </div>
</template>

<style scoped>
.custom-btn {
  margin: 20px;
  font-size: 4em;
  padding: 10px 10px;
  border-radius: 50px;
  max-width: 300px;
  font-family: 'Cursive', 'Lucida Handwriting';
}
</style>
