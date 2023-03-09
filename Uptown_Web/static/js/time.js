
function getTime(){
    var clock = document.getElementById("realtimeclock");  
    var currentDate = new Date();                                     // 현재시간
    var amPm = 'AM'; // 초기값 AM
    var currentHours = addZeros(currentDate.getHours(),2); 
    var currentMinute = addZeros(currentDate.getMinutes() ,2);
    var currentSeconds =  addZeros(currentDate.getSeconds(),2);
            
    if(currentHours >= 12){ // 시간이 12보다 클 때 PM으로 세팅, 12를 빼줌
        amPm = 'PM';
        currentHours = addZeros(currentHours - 12,2);
        }

    clock.innerHTML = currentHours+":"+currentMinute+":"+currentSeconds + " "+amPm; //날짜를 출력해 줌
            
    setTimeout("getTime()",1000);         // 1초마다 printClock() 함수 호출
        }
        
    function addZeros(num, digit) { // 자릿수 맞춰주기
        var zero = '';
        num = num.toString();
        if (num.length < digit) {
        for (i = 0; i < digit - num.length; i++) {
            zero += '0';
            }
            }
        return zero + num;
    }
    