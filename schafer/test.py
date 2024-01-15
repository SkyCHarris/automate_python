from datetime import datetime

birthday = datetime(1990, 1, 1)

sentence = f'Jenn has a birthday on {birthday:%B %d, %Y}'
print(sentence)