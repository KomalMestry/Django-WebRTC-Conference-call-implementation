'use strict';

const joinconference = document.querySelector('button#joinconference');
//joinconference.onclick(window.location.replace($('#join-room-name-entry').value));
joinconference.onclick = conference;


function conference() {
console.log("@@@@@@@@@@@@@@@)
   window.location.replace($('#join-room-name-entry').value));
}