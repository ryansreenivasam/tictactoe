<template>
  <div class="hello">
    <h1>{{ msg }}</h1>  

    <!-- This displays the current contents of the board as it is updated -->
    <h3>currentgame: {{ gameBoard }}</h3>
    
    <!-- This is a button that sends a PUT request with current game board -->
    <button v-on:click="updateGame"> UpdateGame </button>
    
    <!-- This is a button that sends a POST request with an empty game board -->
    <button v-on:click="newGame"> NewGame </button>
  
  </div>
</template>

<script>
import axios from "axios"; //Axios is a tool to handle HTTP requests

export default {
  name: 'HelloWorld',
  props: {
    msg: String, // from default Vue app
  },
  data() {
    return {
      gameBoard: {'board': '_________'} // Contents of game throughout play
    }
  },
  methods: {
    /* This method is called by the system to start a new game after a game 
    is completed.  The POST request contains an empty board and sets the 
    active field to true.
    */
    newGame: function () {
      var board = {'board': '_________', 'active': true};
      // This adds a new game with an empty board and active set to true
      axios.post("http://127.0.0.1:8000/api/", board) 
        .then( response => {
          this.gameBoard = response.data  // POST response contains the new game object
        })
        .catch(e => {
          this.errors.push(e)
        });
    },

    /* This method will update the current game object when the player makes a 
      new move.  The PUT request response will contain the computer's move.
    */
    updateGame: function () {
      var board = {'board': 'updated__'};
      // This updates the current game with the new player move
      axios.put(`http://127.0.0.1:8000/api/${this.gameBoard.id}/`, board) 
        .then( response => {
          this.gameBoard = response.data  // PUT response contains updated game object
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
