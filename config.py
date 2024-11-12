### GENERAL ###
delete_bad_sessions = True # Удалять невалидные сессии. (True — да | False — нет)
main_session = 'data/main_session.session' # Путь до "главной" сессии, с которой будет происходить поиск новых задач (Эта сессия не будет участвовать в накрутке)


text_to_answer = 'data/text.txt'
sessions = 'data/sessions' # Путь до сессий
channels = {
	-1002046287809: {
		'link': 'https://t.me/babuinr',
		'sessions': (20, 25),
		'reactions': [
			'5217610834791903798',
			'5253589359218671331'
		],
		'strategy': [
			[3600, 10],
			[86400, 15]
		],
	},

	-1002082364358: {
		'link': 'https://t.me/samorazvitie_gorec',
		'sessions': (26, 33),
		'reactions': [
			'5231425197667532588'
		],
			'strategy': [
			[3600, 13],
			[86400, 20]
		],
	},

	-1002136518358: {
		'link': 'https://t.me/mantowern',
		'sessions': (23, 33),
		'reactions': [
			'5352658629646365029',
			'5411502954366643585'
		],
			'strategy': [
			[3600, 12],
			[86400, 21]
		],
	},

	-1001811956441: {
		'link': 'https://t.me/miketysonp',
		'sessions': (18, 26),
		'reactions': [
			'5377408279905323979',
			'5377490511349172813'
		],
			'strategy': [
			[3600, 9],
			[86400, 15]
		],
	},

	-1001926801608: {
		'link': 'https://t.me/hokageknow',
		'sessions': (40, 52),
		'reactions': [
			'5150280264580073010',
			'5150165481579086906'
		],
			'strategy': [
			[3600, 20],
			[86400, 32]
		],
	},

	-1002244091569: {
		'link': 'https://t.me/slilok',
		'sessions': (20, 30),
		'reactions': [
			'5287432911237167402'
		],
			'strategy': [
			[3600, 10],
			[86400, 20]
		],
	}
}		
time_to_answer = (10, 36000) # Промежуток времени в секундах через которое бот должен ответить


proxies = 'data/proxy.txt' # Путь до прокси
proxy_protocol = {'http': True, 'socks5': False} # Протокол прокси


# Шансы для выполнения действия
chances = {
	'skip_session': 20,
}


# Обработка
chances = {key: value/100 for (key, value) in chances.items()}
#all_range = 0
#for i, x in enumerate(reaction_set_strategy):
#	all_range += x[1]
#	reaction_set_strategy[i][1] = all_range