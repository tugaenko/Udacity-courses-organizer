import re

def prerequest_parser (text):
	list_of_courses = re.findall(r'[a-z][a-z][a-z]*\d\d\d\d*', text)	
	return set(list_of_courses)


a = """
    required": "Regardless of your programming background, you can learn about data visualization and design principles in Lesson 1a and Lesson 2a without the following recommended background.\n\nTo succeed in this course, you should to be familiar with basic programming principles, including data types (strings, arrays, booleans, etc.), `if else` statements, and `for` loops. You should also be able to describe concepts like functions and objects. Our <a href=\"https://www.udacity.com/course/cs101\" target=\"_blank\">Intro to Computer Science</a> and <a href=\"https://www.udacity.com/course/ud036\" target=\"_blank\">Programming Fundamentals with Python</a> courses are great places to get started.\n\nBasic knowledge of HTML and CSS (structuring and styling a web page) is not required but highly recommended. We suggest taking the <a href=\"https://www.udacity.com/course/ud304\" target=\"_blank\">Intro to HTML and CSS</a> course if you have no experience with HTML or CSS.\n\nThis course is unique in that the final project can be completed using either dimple.js or d3.js. The visualization library, dimple.js, is easier to use than d3.js and requires less background knowledge. Furthermore, a graphic can be created in considerably fewer lines of code using dimple.js as opposed to d3.js.\n\nSo why should you learn d3.js?\n\nData Driven Documents (d3.js) allows you to build highly customized graphics. If you would like to gain more technical skills and learn more about Javascript and open web standards, then you should complete Lesson 3 and Lesson 4 in order to prepare for the final project.\n\n\nIf you would like to complete the final project using d3.js, you should have some experience reading and using documentation. For example, you should be able to code a `for` loop in Javascript or be able to look up the syntax to work with strings and arrays in Javascript. We recommend taking the <a href=\"https://www.udacity.com/course/ud804\" target=\"_blank\">Javascript Basics</a> course if you have little to no experience with Javascript., 


"""
print prerequest_parser(a)