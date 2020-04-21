<!-- 
  Author: Ryan Sreenivasam
  Description: The top level of the Vue.js application.  This file dictates how
  components are registered and placed into the overall structure of the page.
-->
<template>
  <div id="app">
    <!--
      Display the contents of the TicTacToe component
    -->
    <TicTacToe/>
  </div>
</template>

<script>
import TicTacToe from './components/TicTacToe.vue'

export default {
  name: 'App',
  components: {
    TicTacToe
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
