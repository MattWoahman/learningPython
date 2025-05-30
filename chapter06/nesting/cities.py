cities = { "Dallas":{
				"state":"texas",
				"fact":"i've lived here",
			},
			"New York City":{
				"state":"new york",
				"fact":"my favorite city",
			},
			"San Jose":{
				"state":"califonia",
				"fact":"bryant from here",
			}
		}
for city, info in cities.items():
	print(city)
	print(info['state'])	
	print(info['fact'])
