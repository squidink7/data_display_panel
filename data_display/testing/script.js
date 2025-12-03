window.onload = function() {
    focus(document.getElementById("1"));
    console.log(document.activeElement.id);

    updateCards();
}



const card_container = document.getElementById("card_container");

window.addEventListener("keydown", function(e) {
    switch(e.key) {
        case "ArrowLeft":
            previousCard();
            break;
        case "ArrowRight":
            nextCard();
            break;
        default:
            console.log("Unhandled Input");
            break;
    }
})

function previousCard() {
    const card = document.activeElement;

    if (card.previousElementSibling != null) {
        console.log(card.previousElementSibling.id);
        updateCards(document.getElementById(card.previousElementSibling.id));
    }
}

function nextCard() {
    const card = document.activeElement;

    if (card.nextElementSibling != null) {
        console.log(card.nextElementSibling.id);
        updateCards(document.getElementById(card.nextElementSibling.id));
    }
}

//Doing stuff with each card

function updateCards(selected_card) {
    var cards = card_container.getElementsByTagName('div');

    for (i = 0; i < cards.length; i ++) {
            var card = cards[i];

            if (selected_card != null && card == selected_card) {
                //card.tabIndex = -1;
                card.children[0].innerHTML = "focused";
                card.style.backgroundColor = "black";
                card.focus()
            }
            else {
                //card.tabIndex = -1;
                card.children[0].innerHTML = "unfocused";
                card.style.backgroundColor = "grey";
            }
        }
}




