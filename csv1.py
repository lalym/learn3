import csv
answers = {
		"привет": "И тебе привет!",
		"как дела": "Лучше всех",
		"пока": "Увидимся"
		}
with open('answers.csv', 'w', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter=';')

    for key, value in answers.items():
        writer.writerow([key, value])
