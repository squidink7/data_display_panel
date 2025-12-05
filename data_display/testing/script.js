window.onload = function() {
    //Define global constants.
    const card_container = document.getElementById("card_container");
    

    //Not working? Something is wrong.
    focus(document.getElementById("1"));
    console.log(document.activeElement.id);
    updateCards();

    //Start the input handling.
    window.addEventListener("keydown", handleInput);   
}

//Define a list of possible inputs. Handle each input individually.
function handleInput(e) {
    switch(e.key) {
        case "ArrowLeft":
            previousCard();
            break;
        case "ArrowRight":
            nextCard();
            break;
        case "r":
            const data = getData();
            console.log(data);
            break;
        default:
            console.log(e.key);
            break;
    }
}

//Select the previous card in the list. Update the list of cards.
function previousCard() {
    const card = document.activeElement;

    if (card.previousElementSibling != null) {
        console.log(card.previousElementSibling.id);
        updateCards(document.getElementById(card.previousElementSibling.id));
    }
}

//Select the next card in the list. Update the list of cards.
function nextCard() {
    const card = document.activeElement;

    if (card.nextElementSibling != null) {
        console.log(card.nextElementSibling.id);
        updateCards(document.getElementById(card.nextElementSibling.id));
    }
}

//Loop through all of the cards in the list, reset them all, and then flip the card that was selected. 
function updateCards(selected_card) {
    var cards = card_container.getElementsByTagName('div');

    for (i = 0; i < cards.length; i ++) {
        var card = cards[i];

        if (selected_card != null && card == selected_card) {
            card.tabIndex = 0;
            card.children[0].innerHTML = "focused";
            card.style.backgroundColor = "blue";
            card.focus()
        }

        else {
            card.tabIndex = -1;
            card.children[0].innerHTML = "unfocused";
            card.style.backgroundColor = "grey";
        }
    }
}

//Read from the data file.
async function getData(path) {
    //File path to data. This assumes that the server is hosting on port 8080, that could be a problem later.
    const data_path = "http://localhost:8080/data/data.json";

    try {
        const response = await fetch(data_path);
        if (!response.ok) {
            throw new Error("${response.status}");
        }

        return (await response.json());
    }
    //Catch should only be called when an error is caught, and isn't called. It needs a variable to represent the error.
    catch (error) {
        console.error(error.message);
    }
}



