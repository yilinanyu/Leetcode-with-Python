/**
Course selection

On our site, students can input the courses they are taking in any combination of a Department+Course Number and Semester+Year. A department is only alphabetic characters and a course number is only numeric characters.

"CS111 2016 Fall"
"CS-111 Fall 2016"
"MATH 123 2015 Spring"

Valid forms of Department+Course Number are:
CS111
CS 111
CS:111
CS-111 

And valid forms of Semester+Year are:
Fall 2014
fall 14
2014 Fall
F2014

Semesters are Fall (F), Winter (W), Spring (S), Summer (Su).

For example, all of the above combinations would give you:
Department: CS
Course Number: 111
Year: 2014
Semester: Fall

**/
function checkCourse(input) {
  var arr = input.split(' ');
  var courseName;
  var courseNum = -1;
  var regex = /^[a-zA-Z]+$/;
  var courseWork = {};
  // CS 111
  if(arr[0].match(regex)) {
    courseName = arr[0];
  }
  else {
    var case1 = arr[0].split('-');
    var case2 = arr[0].split(':');
    // cs111
    if(case1.length == 1 && case2.length == 1){
      var begin = 0;
      while (arr[0].charAt(begin).match(regex)){
        begin ++;
      }
      courseName = arr[0].substr(0, begin);
      courseNum = arr[0].substr(begin, arr[0].length);
      
    }
    // cs-111
    else if(case2.length == 1){
      courseName = case1[0];
      courseNum = case1[1];
    }
    // cs:111
    else {
      courseName = case2[0];
      courseNum = case2[1];
    }
  }
  var semester;
  var year;
  var index;
  var number = /^[0-9]+$/;
  // cs 111 
  if (courseNum == -1) {
    courseNum = arr[1];
    index = 2;
  }
  // cs-111 or cs:111
  else {
    index = 1;
  }
  // 2014 FALL OR FALL 2014
  if(arr[index].match(number)) {
    year = arr[index];
    semester = arr[index + 1]; 
  }
  else {
    semester = arr[index];
    year = arr[index + 1];
  }
  // f2014 
  if (!arr[index].match(regex) && !arr[index].match(number)) {
    var count = 0;
    while (arr[index].charAt(count).match(regex)) {
      count ++;
    }
    semester = arr[index].substr(0, count);
    year = arr[index].substr(count, arr[index].length);  
  }
  if (semester.charAt(0) >= 'a' && semester.charAt(0) <= 'z') {
    semester = semester[0].toUpperCase() + semester.substr(1,semester.length);
  }
  // f, su,w,s ..
  if (semester.length <= 2) {
    if (semester.toLowerCase() == "s") {
      semester = "Spring";
    } else if (semester.toLowerCase() == "su") {
      semester = "Summer";
    } else if (semester.toLowerCase() == "f") {
      semester = "Fall";
    } else {
      semester = "Winter"
    }
  }
  if (year.length <= 2) {
    year = "20" + year;
  }
  
  for (var k in courseWork) {
    if (!courseWork.hasOwnProperty(k)) {
      courseWork[courseName + courseNum] = 1;
    }
    else {
      
    }
  }
  
  
  return "Department: " + courseName + "\nCourse Number: " + courseNum + "\nYear: " + year + "\nSemester: " + semester;  
}

//console.log(checkCourse("CS111 2016 Fall"));
//console.log(checkCourse("CS:111 2016 Fall"));
//console.log(checkCourse("CS-111 Fall 2016"));
//console.log(checkCourse("MATH 123 2015 Spring"));
//console.log(checkCourse("MATH 123 Su2015"));
console.log(checkCourse("MATH 123 spring 15"));
// console.log(checkCourse("MATH123 Su2015"));
// "CS111 2016 Fall"
// "CS-111 Fall 2016"
// "MATH 123 2015 Spring"
