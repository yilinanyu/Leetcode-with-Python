function checkCourse(input) {
  var arr = input.split(' ')
  var courseName;
  var courseNum = -1;
  var regex = /^[a-zA-Z]+$/;
  // cs 111
  if(arr[0].match(regex)) {
    courseName = arr[0]
  }
  else{
    var case1 = arr[0].split('-');
    var case2 = arr[0].split(':');
    // cs111
    if(case1.length == 1 && case2.length == 1){
      var begin = 0;
      while (arr[0].charAt(begin).match(regex)) {
        begin ++
      }
      courseName = arr[0].substr(0, begin);
      courseNum = arr[0].substr(begin, arr[0].length);
    }
    // cs-111
    else if(case2.length == 1){
      courseName = case1[0]
      courseNum = case1[1]
    }
    // cs:111
    else{
      courseName = case2[0]
      courseNum = case2[1]
    }
  }
  var semester;
  var year;
  var number = /^[0-9]+$/;
  var index;
  // cs 111 OR CS-111
  if (courseNum == -1) {
    courseNum = arr[1];
    index = 2
  } else {
    index = 1
  }
  //2014 FALL OR FALL 2014
  if(arr[index].match(number)) {
    year = arr[index];
    semester = arr[index + 1];
  }
  else {
    semester = arr[index];
    year = arr[index + 1];
  }
  // F2014
  if (!arr[index].match(regex) && !arr[index].match(number)) {
    var count = 0;
    while ( arr[index].charAt(count).match(regex)) {
      count++;
    }
    semester = arr[index].substr(0, count);
    year = arr[index].substr(count, arr[index].length);
       
  }
  // f, su etc
  if (semester.length <= 2) {
    if (semester.toLowerCase() == 'S') {
      semester = 'Spring';
    } else if (semester.toLowerCase() == 'su') {
      semester = 'Summer';
    } else if (semester.toLowerCase() == 'f') {
      semester = 'Fall';
    } else {
      semester = "Winter";
    }
  }
  return "Department: " + courseName + "\nCourse Number: " + courseNum + "\nYear: " + year + "\nSemester: " + semester;
  
}

console.log(checkCourse("CS 111 f2014"))
console.log(checkCourse("CS-111 Fall 2016"))
console.log(checkCourse("Math 111 F2014"))
console.log(checkCourse("CS 111 F2014"))



