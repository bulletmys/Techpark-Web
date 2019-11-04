function like_btn() {//TODO Правильный подсчет оценок
    second_node = document.getElementById("dislike-btn");
    second_node.setAttribute(/**/"style", "color: grey");
    second_node.nextElementSibling.setAttribute(/**/"style", "color: grey");
    //second_node.nextElementSibling.textContent--;
    let node = document.getElementById("like-btn");
    node.nextElementSibling.textContent++;
    node.nextElementSibling.setAttribute("style", "color: green");
    node.setAttribute(/**/"style", "color: green");
}

function dislike_btn() { //TODO Слить функции для лайков
    second_node = document.getElementById("like-btn");
    second_node.setAttribute(/**/"style", "color: grey");
    second_node.nextElementSibling.setAttribute(/**/"style", "color: grey");
    //second_node.nextElementSibling.textContent--;
    let node = document.getElementById("dislike-btn");
    node.nextElementSibling.textContent++;
    node.nextElementSibling.setAttribute("style", "color: red");
    node.setAttribute(/**/"style", "color: red");
    console.log();
}

function correct_answer(num) {
    console.log("nomer", "" + num);
    document.getElementById("" + num).style.border = "2px solid green"
}