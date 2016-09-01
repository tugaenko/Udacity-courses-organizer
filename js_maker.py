import json
import re
from operator import itemgetter

filename = "udacity.json"
courses_filename = "js/course_data.js"

raw_data = open(filename).read()
jo = json.loads(raw_data)
# tracks_data = jo["tracks"]
list_of_courses = jo["courses"]

def prerequest_parser(text):
	list_of_courses = re.findall(r'[a-z][a-z][a-z]*\d\d\d\d*', text)	
	return list(set(list_of_courses))

def key_to_name(key, list_of_courses):
	for course in list_of_courses:
		if course["key"] == key:
			return course["title"]
	return "--"


def course_data_extractor(course, jo):  # jo = JSON object after json.loads
	if ( ( len(course["tracks"]) != 0 ) and 
		( (course["tracks"][0] == "iOS") or ( course["tracks"][0] == "Android") or ( course["tracks"][0] == "Non-Tech") ) ):
		return
	temp = {}
	temp["title"] = course["title"] + " -- " + course["key"] + " -- " + course["subtitle"]
	# temp["key"] = course["key"]
	temp["level"] = course["level"]
	
	if course["expected_duration_unit"] == "months" :
		temp["duration"] = str( course["expected_duration"] * 4 ) + " weeks"
	else:
		temp["duration"] = str(course["expected_duration"]) + " " + course["expected_duration_unit"]
	
	# temp["tracks"] = course["tracks"]
	temp_tracks = ""
	for track in course["tracks"]:
		temp_tracks	= temp_tracks + " // " + track
	temp["tracks"] = temp_tracks
	
	# temp["required"] = course["required_knowledge"]   # adds full requirements
	list_of_req_keys = prerequest_parser(course["required_knowledge"]) # list of required courses keys
	temp["required"] = []
	for key in list_of_req_keys:
		temp["required"].append(key_to_name(key, list_of_courses))
	
	return temp

result_course_list = []
for course in list_of_courses:
	temp = course_data_extractor(course, jo)
	if temp:
		result_course_list.append(temp)


# sort list by
result_course_list = sorted(result_course_list, key=itemgetter('tracks'))

# result_course_list = str(result_course_list)

# # print json to file
outfile = open(courses_filename, "w")
outfile.write(json.dumps(result_course_list, indent = 4, sort_keys=True))

print len(result_course_list)

# outfile = open(tracks_outfile_name, "w")
# outfile.write(json.dumps(courses_data, indent = 4))

# with open(raw_data, 'w') as fp:
# 	json.dump(data, fp)






# tracks_string = json.dumps(tracks_data)

# outfile = open(tracks_outfile_name, "w")
# outfile.write(tracks_data)

# print json.dumps(tracks_data)




# example from API docs

# import json,urllib
# response=urllib.urlopen('https://www.udacity.com/public-api/v0/courses') json_response=json.loads(response.read()) forcourseinjson_response['courses']:
# print course['title']+':'+course['homepage']