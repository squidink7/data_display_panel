window.setInterval(updateCardContent, 2000);

//Constant document elements.
const card_container = document.getElementById("card_container");

function updateCardContent() {
    var data_cards = card_container.getElementsByClassName("data_card");

    //Change the colour of the individual elements of each card.
    for (var i = 0; i < data_cards.length; i++) {
        
        //Change background colour.
        const data_card = document.getElementById(i);
        
        for (var j = 0; j < data_card.children.length; j++) {
            const child_element = data_card.children[j];
            child_element.style.background_color = "red";
            

            switch (child_element.className) {
                case "background_svg":
                   child_element.style.backgroundColor = getNewColour();
                case "data_card_left":
                    for (var k = 0; k < child_element.children.length; k++) {
                        child_element.children[k].children[0].style.backgroundColor = getNewColour();
                    }
                case "data_card_right":
                    for (var k = 0; k < child_element.children.length; k++) {
                        child_element.children[k].children[0].style.backgroundColor = getNewColour();
                    }
                default:
                    break;
            }
        }

        
    }
}

function getNewColour() {
    var rand = Math.floor(Math.random() * 3);

    switch (rand) {
        case 0:
            return "1ac095";
        case 1:
            return "faac06";
        case 2:
            return "e8253f";
        default:
            return "ffffff";

    }
}