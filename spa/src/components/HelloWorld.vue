<template>
  <div class="hello">
    <h1>{{ msg }}</h1>  
    
    <!-- This is a button that sends a POST request with an empty game board -->
    <button v-on:click="newGame"> NewGame </button>
    <!-- This displays the current contents of the board as it is updated -->
    <h3>currentgame: {{ gameBoard }}</h3>
  </div>
</template>

<script>
import axios from "axios"; //Axios is a tool to handle HTTP requests

export default {
  name: 'HelloWorld',
  props: {
    msg: String, // from default Vue app
    gameBoard: String // Contents of game throughout play
  },
  methods: {
    newGame: function () {
      var board = {'board': 'OOOOOOOOO'};  //TODO: This will be empty board with first player move
      // This adds a new game with the contents of board
      axios.post("http://127.0.0.1:8000/api/", board) 
        .then( response => {
          this.gameBoard = response.data  // Update gameboard prop with state of game
        })
        .catch(e => {
          this.errors.push(e)
        });
    }
  }
}


</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
