// Make the DIV element draggable:
// dragElement(document.getElementById("mydiv"));
cards = document.getElementsByClassName("card");
console.log(cards)
for (i=0;i<cards.length;i++){
  console.log(cards[i])
  dragElement(cards[i])
}

function runCards(){
  all_cards = document.getElementsByClassName("card");
  data = [];
  for (i=0;i<all_cards.length;i++){
    data.push(all_cards[i].getElementsByClassName('command')[0].innerHTML);
    console.log(all_cards[i].getElementsByClassName('command')[0].innerHTML);
  }
  console.log(data)
  return fetchPost(data, 'https://sgp5y79yog.execute-api.us-west-2.amazonaws.com/refinery/run')
}

function dragElement(elmnt) {
  var pos1 = 0, pos2 = 0, pos3 = 0, pos4 = 0;
  if (document.getElementById(elmnt.id + "header")) {
    // if present, the header is where you move the DIV from:
    document.getElementById(elmnt.id + "header").onmousedown = dragMouseDown;
  } else {
    // otherwise, move the DIV from anywhere inside the DIV:
    elmnt.onmousedown = dragMouseDown;
  }

  function dragMouseDown(e) {
    e = e || window.event;
    e.preventDefault();
    // get the mouse cursor position at startup:
    pos3 = e.clientX;
    pos4 = e.clientY;
    document.onmouseup = closeDragElement;
    // call a function whenever the cursor moves:
    document.onmousemove = elementDrag;
  }

  function elementDrag(e) {
    e = e || window.event;
    e.preventDefault();
    // calculate the new cursor position:
    pos1 = pos3 - e.clientX;
    pos2 = pos4 - e.clientY;
    pos3 = e.clientX;
    pos4 = e.clientY;
    // set the element's new position:
    elmnt.style.top = (elmnt.offsetTop - pos2) + "px";
    elmnt.style.left = (elmnt.offsetLeft - pos1) + "px";
  }

  function closeDragElement() {
    // stop moving when mouse button is released:
    document.onmouseup = null;
    document.onmousemove = null;
  }
}

function fetchPost(data, url) {
  return fetch(url, {  
    method: "POST",  
    cors: true,
    body: JSON.stringify(
      data
    )
  }).then(response => response.json());   
}