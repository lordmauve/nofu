
from bs4 import BeautifulSoup
import csv
from random import sample
import json

# with open('answers.csv', 'wb') as csvfile:

data = open('/Users/tinazhang/Documents/MyPython/dojo_quiz/disney_characters.html').read()

doc = BeautifulSoup(data)
tables = doc.find_all('table', class_='sortable')

results = []

for table in tables:
	for row in table.find_all('tr')[1:]:
		cells = row.find_all('td')
		if len(cells) != 3:
			continue
		else:
			character_cell, actor_cell, film_cell = cells
			film_name = film_cell.text
			if "!" in film_name:
				_, film_name = film_name.split("!", 1)
			results.append((character_cell.text, film_name))

questions = []

for result in results:
	herrings = filter(lambda n: n != result, results)
	red_herrings = [film for character, film in sample(herrings, 5)]
	character, film = result
	questions.append({
		"question": u"In what film did {} appear?".format(character),
		"answer": film,
		"red_herrings": red_herrings
		})

print json.dumps(questions, indent=4)