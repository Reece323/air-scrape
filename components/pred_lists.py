

model_columns = [
    'property_type',
    'room_type',
    'bed_type',
    'cancellation_policy',
    'city',
    'host_identity_verified',
    'instant_bookable',
    'neighbourhood',
    'amenities',
    'accommodates',
    'bathrooms',
    'bedrooms',
    'beds',
]

amenity = [
    {'label': 'TV', 'value': 'TV'},
    {'label': 'Cable TV', 'value': 'Cable TV'},
    {'label': 'Kitchen', 'value': 'Kitchen'},
    {'label': 'Free parking on premises ', 'value': 'Free parking on premises'},
    {'label': 'Breakfast ', 'value': 'Breakfast'},
    {'label': 'Elevator in building ', 'value': 'Elevator in building'},
    {'label': 'Heating ', 'value': 'Heating'},
    {'label': 'Washer ', 'value': 'Washer'},
    {'label': 'Dryer ', 'value': 'Dryer'},
    {'label': 'Smoke detector ', 'value': 'Smoke detector'},
    {'label': 'First aid kit ', 'value': 'First aid kit'},
    {'label': 'Safety card ', 'value': 'Safety card'},
    {'label': 'Fire extinguisher ', 'value': 'Fire extinguisher'},
    {'label': 'Hair dryer ', 'value': 'Hair dryer'},
    {'label': 'Laptop friendly workspace ', 'value': 'Laptop friendly workspace'},
    {'label': 'Wireless Internet ', 'value': 'Wireless Internet'},
    {'label': 'Air conditioning ', 'value': 'Air conditioning'},
    {'label': 'Gym ', 'value': 'Gym'},
    {'label': 'Carbon monoxide detector ', 'value': 'Carbon monoxide detector'},
    {'label': 'First aid kit ', 'value': 'First aid kit'},
    {'label': 'Wheelchair accessible ', 'value': 'Wheelchair accessible'},
    {'label': 'Family/kid friendly ', 'value': 'Family/kid friendly'},
    {'label': 'Lock on bedroom door ', 'value': 'Lock on bedroom door'},
    {'label': 'Hangers ', 'value': 'Hangers'},
    {'label': 'Iron ', 'value': 'Iron'},
    {'label': 'Pets allowed ', 'value': 'Pets allowed'},
    {'label': 'Breakfast ', 'value': 'Breakfast'},
    {'label': 'Suitable for events ', 'value': 'Suitable for events'},
    {'label': 'Shampoo ', 'value': 'Shampoo'},
    {'label': 'Private entrance ', 'value': 'Private entrance'},
    {'label': 'Smoking allowed ', 'value': 'Smoking allowed'},
    {'label': 'Hot tub ', 'value': 'Hot tub'},
    {'label': 'Pool ', 'value': 'Pool'},
    {'label': 'Babysitter recommendations ', 'value': 'Babysitter recommendations'},
    {'label': '24-hour check-in ', 'value': '24-hour check-in'},
    {'label': 'Buzzer/wireless intercom ', 'value': 'Buzzer/wireless intercom'},
    {'label': 'Self Check-In ', 'value': 'Self Check-In'},
    {'label': 'Lockbox ', 'value': 'Lockbox'},
    {'label': 'Cat(s) ', 'value': 'Cat(s)'},
]

''' 
Used for creating marks for the input bathroom slider
in prediction.py
'''
bathroom_marks = {
    0: '0',
    0.5: '0.5',
    1: '1',
    1.5: '1.5',
    2: '2',
    2.5: '2.5',
    3: '3',
    3.5: '3.5',
    4: '4',
    4.5: '4.5',
    5: '5',
    5.5: '5.5',
    6: '6',
    6.5: '6.5',
    7: '7',
    7.5: '7.5',
    8: '8'
}

''' 
Used for creating all dropdown values for the 
neighborhood dropdown in prediction.py
'''
neighborhoods = [
    {'label': 'Bentonville', 'value': 'Bentonville'},
    {'label': 'Rogers', 'value': 'Rogers'},
    {'label': 'Springdale', 'value': 'Springdale'},
    {'label': 'Bella Vista', 'value': 'Bella Vista'},
    {'label': 'Fayetteville', 'value': 'Fayetteville'},
]


''' 
Used for creating all dropdown values for the 
property_type dropdown in predictions.py
'''
property_type = [
    {'label': 'Apartment', 'value': 'Apartment'},
    {'label': 'House', 'value': 'House'},
    {'label': 'Condominium', 'value': 'Condominium'},
    {'label': 'Townhouse', 'value': 'Townhouse'},
    {'label': 'Loft', 'value': 'Loft'},
    {'label': 'Other', 'value': 'Other'},
    {'label': 'Guesthouse', 'value': 'Guesthouse'},
    {'label': 'Bed & Breakfast', 'value': 'Bed & Breakfast'},
    {'label': 'Bungalow', 'value': 'Bungalow'},
    {'label': 'Dorm', 'value': 'Dorm'},
    {'label': 'Guest suite', 'value': 'Guest suite'},
    {'label': 'Villa', 'value': 'Villa'},
    {'label': 'Timeshare', 'value': 'Timeshare'},
    {'label': 'In-law', 'value': 'In-law'},
    {'label': 'Boutique hotel', 'value': 'Boutique hotel'},
    {'label': 'Hostel', 'value': 'Hostel'},
    {'label': 'Camper/RV', 'value': 'Camper/RV'},
    {'label': 'Cabin', 'value': 'Cabin'},
    {'label': 'Boat', 'value': 'Boat'},
    {'label': 'Serviced apartment', 'value': 'Serviced apartment'},
    {'label': 'Castle', 'value': 'Castle'},
    {'label': 'Tent', 'value': 'Tent'},
    {'label': 'Vacation home', 'value': 'Vacation home'},
    {'label': 'Yurt', 'value': 'Yurt'},
    {'label': 'Treehouse', 'value': 'Treehouse'},
    {'label': 'Chalet', 'value': 'Chalet'},
    {'label': 'Hut', 'value': 'Hut'},
    {'label': 'Tipi', 'value': 'Tipi'},
    {'label': 'Earth House', 'value': 'Earth House'},
    {'label': 'Cave', 'value': 'Cave'},
    {'label': 'Casa particular', 'value': 'Casa particular'},
    {'label': 'Train', 'value': 'Train'}
]