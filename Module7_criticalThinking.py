#!/usr/bin/env python3


#dictionary definitions 
course_room = {
      "CSC101":"3004",
      "CSC102":"4501",
      "CSC103":"6755",
      "NET110":"1244",
      "COM241":"1411"	  
}

course_Instructor={
      "CSC101":"Haynes",
      "CSC102":"Alvarado",
      "CSC103":"Rich",
      "NET110":"Burke",
      "COM241":"Lee"	 
}

course_time = {
      "CSC101":"8:00 a.m.",
      "CSC102":"9:00 a.m",
      "CSC103":"10:00 a.m",
      "NET110":"11:00 a.m",
      "COM241":"1:00 p.m"  
}







#function definition for finding a room for a course
def find_room_number(course_num):  
    try:
	    room = course_room[course_num]
	    return room
    except:
        print('{} is not a valid course number cant find room'.format(course_num))

#function definition for finding the instructor for a course		  
def find_class_instructor(course_num):
    try:
	    instructor = course_Instructor[course_num]
	    return instructor
    except:
        print('{} is not a valid course number cant find instructor'.format(course_num))
		
#function definition for finding the course time
def find_class_time(course_num):
    try:
	    time = course_time[course_num]
	    return time
    except:
        print('{} is not a valid course number cant find time\n'.format(course_num))

def main():
    course_num = input('Please enter a course catalog number\n') #gets input from user 
	
    room = find_room_number(course_num)  #calls find_room_number function to get the class room number
    instructor = find_class_instructor(course_num)  #calls find_class_instructor function to get the instructor name
    time = find_class_time(course_num) #calls find_class_time function to get the time of the class
	
    print('\nCourse Number: {}'.format(course_num))
    print('Course Room: {}'.format(room))
    print('Course Instructor: {}'.format(instructor))
    print('Class Time: {}\n'.format(time))

if __name__ == "__main__":
   main()