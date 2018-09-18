national_parks = {'Yellowstone': 
		{'state':'WY',
		'annual_visitors': 4116528,
		'size': 8991,
		'attractions':
			{'Old Faithful': 'geyser',
			'Grand Canyon of the Yellowstone': 'canyon',
			'Tower Fall': 'waterfall',
			'Yellowstone Lake': 'lake',
			'Mammoth Hot Springs': 'hot springs'},
		'trails':
			{'Uncle Tom\'s Trail':
				{'length': 0.1,
				'loop': False},
			'Trout Lake Trail': 
				{'length': 1.4,
				'loop': True},
			'Storm Point Trail':
				{'length': 3.3,
				'loop': True}
			}
		},
	'Yosemite':
		{'state':'CA',
		'annual_visitors': 4336890,
		'size': 3027,
		'attractions':
			{'El Capitan': 'monolith',
			'Half Dome': 'granite dome',
			'Vernal Fall': 'waterfall',
			'Yosemite Falls': 'waterfall',
			'Tuolomne Meadows': 'meadow',
			'Tunnel View': 'lookout point',
			'Cathedral Peak': 'mountain'},
		'trails':
			{'Mist Trail':
				{'length': 11,
				'loop': False},
			'Yosemite Falls Trail': 
				{'length': 11.6,
				'loop': False},
			'Panorama Trail':
				{'length': 13.5,
				'loop': False},
 			'Clouds Rest':
				{'length': 23.3,
				'loop': False}
			}
		},
	'Grand Teton':
		{'state': 'WY',
		'annual_visitors': 3270076,
		'size': 130,
		'attractions':
			{'Grand Teton': 'mountain',
			'Jenny Lake': 'lake',
			'Inspiration Point': 'lookout point',
			'Jackson Lake': 'lake',
			'Snake River': 'river'},
		'trails':
			{'String Lake Loop': 
				{'length': 6.1,
				'loop': True},
			'Cascade Canyon':
				{'length': 16.1,
				'loop': False},
			'Static Peak Divide':
				{'length': 26.2,
				'loop': False}
			}
		}
	}

key_array = []

def manipulate_dict(a_dictionary):
		print('Keys at this level:')
		print_keys(a_dictionary)
		user_input = input('Would you like to:\n1: add a key\n2: delete a key\n3: choose a key\n4: print current dictionary\n')
		if ('1' == user_input or 'add a key' == user_input):
			add_key(a_dictionary)
		elif ('2' == user_input or 'delete a key' == user_input):
			delete_key(a_dictionary)
		elif ('3' == user_input or 'choose another key' == user_input):
			user_input = input ('What key would you like to interact with?\n')
			working_object = a_dictionary[user_input]
			key_array.append(user_input)
			if (isinstance(working_object,dict)):
				working_dictionary = a_dictionary[user_input]
				manipulate_dict(working_dictionary)		
			else:
				print('Value: ',working_object)
		else:
			print(national_parks)
			manipulate_dict(a_dictionary)	
		
def delete_key(a_dictionary):
	user_input = input('What key would you like to delete?\n')
	a_dictionary.pop(user_input, None)
	rebuild_dictionary(national_parks, a_dictionary)
	manipulate_dict(a_dictionary)

def add_key(a_dictionary):
	user_key = input('What key would you like to add?\n')
	user_value = input('What is the value of this key?\n')
	a_dictionary[user_key] = user_value
	rebuild_dictionary(national_parks, a_dictionary)
	manipulate_dict(a_dictionary)

def rebuild_dict(full_dict, dict_fragment):
	length = len(key_array)
	if (length == 4):
		full_dict[key_array[0]][key_array[1][key_array[2][key_array[3]]]] = dict_fragment
	elif (length == 3):
		full_dict[key_array[0]][key_array[1]][key_array[2]] = dict_fragment
	elif (length == 2):
		full_dict[key_array[0]][key_array[1]] = dict_fragment
	elif (length == 1):
		full_dict = dict_fragment

def print_keys(dict_to_print):
	keys_to_print =  list(dict_to_print.keys())
	for key in keys_to_print:
		print(key %(keys_to_print))

print_keys(national_parks)
manipulate_dict(national_parks)

