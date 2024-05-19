<script>
export default {
  name: "NavBar"
}
</script>

<template>
  <nav class="navbar navbar-expand-lg bg-transparent">
    <div class="container d-flex align-items-center justify-content-between">
      <a class="text-red navbar-brand" href="/"><i class="fa-sharp fa-solid fa-code"></i> QuizWebGame</a>
      <div class="collapse navbar-collapse" id="navbarScroll">
        <ul class="navbar-nav me-auto my-2 my-lg-0 navbar-nav-scroll" style="--bs-scroll-height: 100px;">
          <li class="nav-item dropdown dropdown-hover">
            <a class="nav-link active dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
              Quizzes
            </a>
            <ul class="dropdown-menu bg-transparent">
              <li><router-link class="dropdown-item" to="/quiz-name">Quiz Name</router-link></li>
<!--              <li><hr class="dropdown-divider"></li>-->
            </ul>
          </li>
          <li><router-link to="/login" class="nav-item m-3">Sign In</router-link></li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<style scoped>
.navbar {
  backdrop-filter: blur(10px);
}

.text-red{
  color: #AD1705;
}

.text-light:hover {
  color: #AD1705 !important;
  background-color: transparent;
}

.dropdown-menu {
  display: none;
}

.dropdown-hover:hover .dropdown-menu {
  display: block;
}
</style>
