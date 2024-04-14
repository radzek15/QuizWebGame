<template>
  <NavBar />
  <router-view />
  <PageFooter />
</template>

<script>
import NavBar from "@/components/Bars/NavBar.vue";
import PageFooter from "@/components/Bars/PageFooter.vue";

export default {
  name: 'App',
  components: {PageFooter, NavBar},
}
</script>

<style>

</style>
