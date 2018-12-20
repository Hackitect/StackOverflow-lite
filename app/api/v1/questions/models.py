#for the return specific question, we shall also need all the answers provided soo far
# hence we need to also have the answers model imported here
from app.api.v1.answers import models

questions_list = [
	{
		'id': 0,
		'user_id': 2,
		'question': 'How can you edit multiple lines using sublime text',
		'date_posted': '2018, 12, 17, 8, 24, 43, 312403'
		},
	{
		'id': 1,
		'user_id': 2,
		'question': 'Recovering evince session in Ubuntu 16.04',
		'date_posted': '2018, 12, 17, 8, 24, 43, 312403'
		},
	{
		'id': 2,
		'user_id': 0,
		'question': 'How to JSON serialize sets?',
		'date_posted': '2018, 12, 17, 8, 24, 43, 312403'
		}
]

ans = models.answers_list

class Questions:

	def get_all(self):
		if len(questions_list) == 0:
			return {"message": "Empty list"}
		else:
			return questions_list

	def post_question(self, user_id, question, timestamp):
		if len(question) < 5:
			return {"message": "Question too short, try typing a descriptive question"}
		
		id = len(questions_list) + 1
		new_question = {'id': id, 'user_id': user_id, 'question': question, 'date_posted': timestamp}
		questions_list.append(new_question)
		return {
			"message": "Your question has been posted successfully",
			"question": question,
			"time created": timestamp
			}
	def fetch_specific_question(self, questionId):
		for que in questions_list:
			if que['id'] == questionId:
				# for answers in ans:
				# 	if answers['Question_id'] == id:
				# 		return answers
					return {"question" : que['question']}	
			return{"message": "no question with that id found in the database"}