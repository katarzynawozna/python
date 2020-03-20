import numpy as np
import matplotlib.pyplot as plt


# Źródło dancyh (https://www.tiobe.com/tiobe-index/).
DATA = [
	17.253,  # Java
	16.086,  # C
	10.308,  # Python
	6.196,  # C++
	4.801,  # C#
	4.743,  # Visual Basic .NET
	2.090,  # JavaScript
	2.048,  # PHP
	1.843,  # SQL
	1.490  # Swift
]

NAMES = [
	'Java',
	'C',
	'Python',
	'C++',
	'C#',
	'VB .NET',
	'JS',
	'PHP',
	'SQL',
	'Swift'
]

if __name__ == '__main__':
	plt.bar(np.arange(len(DATA)),  
			DATA, 
			color='gold', 
			edgecolor='black',
			tick_label=NAMES)
	plt.title('10 najpopularniejszych języków programowania, grudzień 2019')
	plt.xlabel('Język')
	plt.ylabel('Procent użytkowników')
	plt.show()
