const element = document.getElementById("myBtn");
element.addEventListener("click", myFunction);

function myFunction() {
    document.getElementById("demo").innerHTML = "Hello World";
    var x = document.getElementById("myAudio");
    x.play();
}