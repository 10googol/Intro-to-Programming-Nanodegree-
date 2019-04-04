/*
 * Create a list that holds all of your cards
 */

var cardDeck = ["fa fa-diamond", "fa fa-diamond", "fa fa-paper-plane-o", "fa fa-paper-plane-o",
"fa fa-anchor", "fa fa-anchor","fa fa-bolt", "fa fa-bolt", "fa fa-cube", "fa fa-cube",
"fa fa-leaf", "fa fa-leaf", "fa fa-bicycle", "fa fa-bicycle", "fa fa-bomb", "fa fa-bomb"];
var chosenCards = []; // List to hold chosen cards when clicked
var moves = 0; // Variable to count moves
var matches = 0; // Variable to count the number of matches 1 per each pair.
var second = 0; // Keeps the time in seconds and is displayed to the .timer
var firstCardClick = true; // Used to determine when first card is clicked.
var rating;

 // Shuffle function from http://stackoverflow.com/a/2450976
 function shuffle(array) {
     var currentIndex = array.length, temporaryValue, randomIndex;

     while (currentIndex !== 0) {
         randomIndex = Math.floor(Math.random() * currentIndex);
         currentIndex -= 1;
         temporaryValue = array[currentIndex];
         array[currentIndex] = array[randomIndex];
         array[randomIndex] = temporaryValue;
     }
     return array;
 }

 /*
 * startGame function is basically window dressing because it just shows where
 * the games starts in a traditional sense and is only used to call reset function
 */
function startGame() {
   resetGame();
 }

/*
 * End of the game clean up and display Modal
 *
 */
function endGame() {
  endTime();
  displayModal();
}

/*
 * Display game stats
 *
 */
function displayModal() {
  $('.modal')[0].style.display = "block";
  $('#winStats').text('You completed the game in ' + second + ' seconds, with a rating of ' + rating + '. Congragulations!  Click on Game Start/Reset to play again!');
}

/*
 *  When card is matched or not increment moves variable to keep
 *  track of attempts.
 */
function movesCounter() {
 moves++;
 $('.moves').text(moves.toString());
}

/*
 *  Update stars rating at top of the page. Less than 10 moves =
 *  3 stars, 10 to 15 moves = 2 star,15 to 20 moves = 1 stars,
 *  and 20 or > = 0 stars.
 */
function setRating() {
  if (moves <= 12){
    rating = "3 Stars";
  } else if (moves > 12 && moves <= 15) {
    $('.stars i').eq(2).removeClass('fa fa-star').addClass('fa fa-star-o');
    rating = "2 Stars";
  } else if (moves > 15 && moves <= 20) {
    $('.stars i').eq(1).removeClass('fa fa-star').addClass('fa fa-star-o');
    rating = "1 Star";
  } else {
    $('.stars i').eq(0).removeClass('fa fa-star').addClass('fa fa-star-o');
    rating = "0 Stars";
  }
}

// Function to keep track of seconds in game and update .timer container.
function startTime() {
  timeInSeconds = setInterval(function () {
      second = second + 1;
      $('.timer').text(second.toString());
  }, 1000);
}

// Stop the timer to the game that was initiated in the startTime() function.
function endTime() {
  if (timeInSeconds) {
      clearInterval(timeInSeconds);
  }
}

// Initialize each card container to covered on game start and reset
function coverAllCards() {
  $('.card').removeClass();
  $('.deck').children().addClass('card');
}

/*
*  On click display card and call compareCards function once openCards
* length is 2.
*/
function displayCard(card) {
  card.classList.add("open", "show", "disable"); // Displays clicked card clicked
  if (firstCardClick) {
    startTime();
    firstCardClick = false;
  }

  if (chosenCards.length === 0) {
    chosenCards.push(card);
  } else {
    chosenCards.push(card);
    compareCards();
  }
}

/*
*  Covers cards after compareCards function determines the chosen cards
*  don't match.
*/
function coverCards() {
  chosenCards[0].classList.remove("open", "show", "disable");
  chosenCards[1].classList.remove("open", "show", "disable");
  chosenCards.length = 0;
}

/*
*  Marks cards as matched by adding to the class match to .card and removing classes
*  open and show from .card after compareCards function determines the chosen cards
*  don't match.
*/
function matchedCards() {
  chosenCards[0].classList.add("match"); // Marks card as matched
  chosenCards[1].classList.add("match"); // Marks card as matched
  chosenCards[0].classList.remove("open", "show");
  chosenCards[1].classList.remove("open", "show");
  chosenCards.length = 0; // Reset the chosenCards list.
  matches++; // Increment matches variable to keep track of game progress.
}

/*
 *  This function is called once 2 cards have been chosen and
 *  and stored in the chosenCards list/array.
 */
function compareCards() {
  if (chosenCards[0].innerHTML === chosenCards[1].innerHTML) {
    matchedCards(chosenCards); // Cards matched.
  } else {
    setTimeout(function() {coverCards();}, 500); // Cards didn't match cover after 0.5sec.
  }
  movesCounter(); // Update moves counter.
  setRating(); // Update star rating.
  /*
   *  Check if game is over (8 matched card pairs - (cardDeck length)/2)
   *  if it is call endGame function.
   */
  if (matches === cardDeck.length/2) {
    endGame();
  }
}

/*
*  Shuffle cards in cardDeck list and assign returned array to shuffledDeck.
*  Itterate through shuffledDeck setting each .card class innerHTML to
*  new shuffled card.
*/
function setNewCards() {
  shuffledDeck = shuffle(cardDeck);
  // Place shuffled cards in covered card containers
  for (let i = 0; i < shuffledDeck.length; i++) {
    document.getElementsByClassName('card')[i].innerHTML = "<i class=\"" + shuffledDeck[i] + "\"></i>"
  }
}

 /*
 *  The reset function sets up the playboard/deck container and lays out the
 *  the shuffled cards in each covered cardContainer.
 */
 function resetGame() {
   chosenCards.length = 0;
   moves = 0;
   $('.timer').text('0'); // Reset second counter display
   $('.moves').text('0'); // Reset moves counter
   $('.stars i').removeClass('fa fa-star-o').addClass('fa fa-star'); //Reset star ratings.
   matches = 0; // Reset match counter for end of game determination.
   second = 0; // Reset second counter.
   firstCardClick = true; // Setup game start indicator to start time.
   coverAllCards();
   setNewCards();
   endTime();
}


// Setup listners
$('.card').on('click', function() {displayCard(this)});
$('.restart').on('click', function() {startGame()});
$('.close')[0].onclick = function() {$('.modal')[0].style.display = "none";};
