<script>
import CreateQuestion from "@/components/Quiz/CreateQuestion.vue";
import CreateQuiz from "@/components/Quiz/CreateQuiz.vue";

export default {
  name: "NewQuiz",
  components: {CreateQuiz, CreateQuestion}
}
</script>

<template>
  <div class="container">
    <CreateQuestion />
    <CreateQuiz />
  </div>
</template>

<style scoped>

</style>
