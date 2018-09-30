<template>
  <div id="app">
    <Frontend />
  </div>
</template>

<script>
import Frontend from './components/Frontend.vue'

export default {
  name: 'app',
  components: {
    Frontend
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background-color: black;
}
</style>
