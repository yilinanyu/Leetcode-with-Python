function checkCourse(input) {
    var arr = input.split(' ');
    var courseName;
    var courseNum = -1;


    var regex = /^[a-zA-Z]+$/;
    if (arr[0].match(regex)) {
        courseName = arr[0];
    } else {
        var list = arr[0].split('-');
        var list2 = arr[0].split(':');
        // cs111
        if (list.length == 1 && list2.length == 1) {
            var begin = 0;
            while (arr[0].charAt(begin).match(regex)) {
                begin++;
            }
            courseName = arr[0].substr(0, begin);
            courseNum = arr[0].substr(begin, arr[0].length);
        } else if (list2.length == 1){
            //cs-111
            courseName = list[0];
            courseNum = list[1];
        } else {
            //cs:111
            courseName = list2[0];
            courseNum = list2[1];
        }
    }
    
    var semester;
    var year;
    
    var number = /^[0-9]+$/;
    
    // CS 111 F2014
    
    // MATH 123 2015 Spring
    
    var index;
    if (courseNum == -1) {
        courseNum = arr[1]; 
        index = 2;
    } else {
        index = 1;
        
        // if (arr[1].match(number)) {
        //     year = arr[1];
        //     semester = arr[2];
        // //F2014
        // }
    }
    //"CS 111 2014 Fall"
    // CS-111 Fall 2016
    
    if (arr[index].match(number)) {
        year = arr[index];
        semester = arr[index + 1];
    } else {
        semester = arr[index];
        year = arr[index + 1];
    }
    
    // handle f2014
    if (!arr[index].match(regex) && !arr[index].match(number)) {
        var count = 0;
        while (arr[index].charAt(count).match(regex)) {
            count++;
        }
        semester = arr[index].substr(0, count);
        year = arr[index].substr(count, arr[index].length);
    } 
    
    
    if (semester.length <= 2) {
        if (semester.toLowerCase() === 'f') {
            semester = 'Fall';
        } else if (semester.toLowerCase() === 'su') {
            semester = 'Summer';
        } else if (semester.toLowerCase() === 'w') {
            semester = 'Winter';
        } else {
            semester = 'Spring';
        }
    }