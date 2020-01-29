var room;
room = [true,false,true,false,false];
var selected_room = 0;

var el_condition = document.getElementById('result');
var el_room = document.getElementById('room_number')


function input_number(num){
	selected_room = el_room.value-1;

	if (room[selected_room] == true){
		el_condition.textContent = 'empty';
	} else {
		el_condition.textContent = 'full';
	}

 }
