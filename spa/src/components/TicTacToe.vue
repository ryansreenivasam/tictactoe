<!-- 
  Author: Ryan Sreenivasam
  Description: Vue component that contains board UI and frontend logic.
-->
<template>
  <div>
    <h1 style="font-size: 40pt;"> Tic Tac Toe </h1>
    <h3> By: Ryan Sreenivasam </h3>
    <h1 v-show="dialogVisible">{{ dialog }}</h1>
    <br>
    <!--
      This table element is the tic tac toe board.  Each place on the board is 
      a button and when the button is pressed the updateGame method is called 
      with the index of that button.
    -->
    <div class="board">
      <table>
        <tr>
          <td>
            <button class="boardButton" v-on:click="updateGame(0)"> 
              {{ gameBoard.board.substr(0,1) }} 
            </button>
          </td>
          <td>
            <button class="boardButton" v-on:click="updateGame(1)"> 
              {{ gameBoard.board.substr(1,1) }} 
            </button>
          </td>
          <td>
            <button class="boardButton" v-on:click="updateGame(2)"> 
              {{ gameBoard.board.substr(2,1) }} 
            </button>
          </td>
        </tr>
        <tr>
          <td>
            <button class="boardButton" v-on:click="updateGame(3)"> 
              {{ gameBoard.board.substr(3,1) }} 
            </button>
          </td>
          <td>
            <button class="boardButton" v-on:click="updateGame(4)"> 
              {{ gameBoard.board.substr(4,1) }} 
            </button>
          </td>
          <td>
            <button class="boardButton" v-on:click="updateGame(5)"> 
              {{ gameBoard.board.substr(5,1) }} 
            </button>
          </td>
        </tr>
        <tr>
          <td>
            <button class="boardButton" v-on:click="updateGame(6)"> 
              {{ gameBoard.board.substr(6,1) }} 
            </button>
          </td>
          <td>
            <button class="boardButton" v-on:click="updateGame(7)"> 
              {{ gameBoard.board.substr(7,1) }} 
            </button>
          </td>
          <td>
            <button class="boardButton" v-on:click="updateGame(8)"> 
              {{ gameBoard.board.substr(8,1) }} 
            </button>
          </td>
        </tr>
      </table>
    </div>
    <br>
    <!-- This is a button that sends a POST request with an empty game board -->
    <button v-on:click="newGame"> NewGame </button>
  </div>
</template>

<script>
// Axios is a tool to handle HTTP requests
import axios from "axios"; 
// Config file to ensure uniformity of URL during API requests
import { djangoURL } from "../config.js";

export default {
  name: 'TicTacToe',
  props: {
  },
  data() {
    return {
      // Contents of game throughout play
      gameBoard: {
        'board': '_________',
        'response': false, 
        'winner': "0" 
      },
      // The dialog that is displayed when a player wins
      dialog: "",
      // Boolean that governs if dialog is visible or not
      dialogVisible: false
    }
  },
  // Immediately create a new game when the page loads.
  mounted: function () {
      this.newGame();
  },
  methods: {
    /**
    * This method is called by the system to start a new game after a game 
    * is completed.  The POST request contains an empty board.
    */
    newGame: function () {
      var board = {
        'board': '_________',
        'response': false, 
        'winner': "0" 
      };
      // Add a new game to database with an empty board
      axios.post(`${djangoURL}api/`, board) 
        .then( response => {
          // POST response contains the new game object
          this.gameBoard = response.data
          // Check for winner here to reset the dialog from any previous game
          this.checkForWinner();
        })
        .catch(e => {
          this.errors.push(e)
        });
    },

    /**
    * This method will update the board with a user's new move.  The index in
    * the board string that corresponds to the placement of the user's move is 
    * updated with an X.  The game object's response field is set to true 
    * signaling that a new AI move has been requested. A PUT request is then sent 
    * to the server with the updated information. The PUT request response will 
    * contain the new AI move.
    */
    updateGame: function (index) {
      // Strings in Javascript are immutable so a copy must be made
      var currBoard = this.gameBoard.board;
      // Add X to the string in the index that the user requested
      currBoard = currBoard.substring(0, index) + "X" + currBoard.substring(index+1);
      //Update the game board here so the UI is updated immediately
      this.gameBoard.board = currBoard;
      // Create a board object with the new string and response set to true
      var board = { 'board': currBoard, 'response': true};
      // Send a PUT request with the new player move and request for an AI move
      axios.put(`${djangoURL}api/${this.gameBoard.id}/`, board) 
        .then( response => {
          this.gameBoard = response.data  // PUT response contains new AI move
          // Check for a winner here after the response has been received
          this.checkForWinner();
        })
        .catch(e => {
          this.errors.push(e)
        });
    },

    /**
    * This method will check the winner field of the game object and add a 
    * prompt on the screen if a player has won. The prompt will disappear 
    * after 5 seconds and the game will be reset.
    */
    checkForWinner: function () {
      // Check if the user has won
      if(this.gameBoard.winner == "X") {
        // Set dialog to something descriptive
        this.dialog = "Holy Cow! Somehow You Won!";
        this.flashDialog();
      }
      // Check if the computer has won
      else if(this.gameBoard.winner == "O") {
        // Set dialog to be something descriptive
        this.dialog = "The Computer Wins Again!";
        this.flashDialog();
      }
      else {
        this.dialog = ""
      }
    },

    /**
    * This method will make the winner dialog visible for 5 seconds then make 
    * it invisible again.  After 5 seconds, a new game will begin.
    */
    flashDialog: function () {
      // Set dialog to be visible
      this.dialogVisible = true;
      // Dialog will disappear and a new game will be created after 5 seconds
      setTimeout(() => {
        this.dialogVisible = false;
        this.newGame();
      }, 5000);
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
table {
  margin: 5px auto;
}
td {
  width: 100px;
  height: 100px;
}
button {
  width: 150px;
  height: 50px;
  font-size: 15pt;
}
.boardButton {
  width: 100px;
  height: 100px;
  font-size: 30pt;
}
</style>
