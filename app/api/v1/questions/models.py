


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

class Questions():

	def get_all(self):
		if len(questions_list) == 0:
			return {"message": "Empty list"}
		else:
			return questions_list

	def post_question(self, user_id, question, timestamp):
		if len(question) < 5:
			return {"message": "Try typing a descriptive question"}
		
		id = len(questions_list) + 1
		new_question = {'id': id, 'user_id': user_id, 'question': question, 'date_posted': timestamp}
		questions_list.append(new_question)
		return {
			"message": "Your question has been posted successfully",
			"question": question,
			"time created": timestamp
			}