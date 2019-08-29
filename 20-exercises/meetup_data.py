attendees_locations = [
    { 'blocks_east_of_city_center': -48 , 'blocks_north_of_city_center': 16 },
    { 'blocks_east_of_city_center': -49 , 'blocks_north_of_city_center': 0 },
    { 'blocks_east_of_city_center': -46 , 'blocks_north_of_city_center': 6 },
    { 'blocks_east_of_city_center': -39 , 'blocks_north_of_city_center': 8 },
    { 'blocks_east_of_city_center': -34 , 'blocks_north_of_city_center': -1 },

    { 'blocks_east_of_city_center': -26 , 'blocks_north_of_city_center': -9 },
    { 'blocks_east_of_city_center': -22 , 'blocks_north_of_city_center': -18 },
    { 'blocks_east_of_city_center': -19 , 'blocks_north_of_city_center': -12 },
    { 'blocks_east_of_city_center': -18 , 'blocks_north_of_city_center': -2 },
    { 'blocks_east_of_city_center': -14 , 'blocks_north_of_city_center': -4 },
    { 'blocks_east_of_city_center': -10 , 'blocks_north_of_city_center': -7 },
    { 'blocks_east_of_city_center': -11 , 'blocks_north_of_city_center': -9 },
    { 'blocks_east_of_city_center': -13 , 'blocks_north_of_city_center': -19 },
    { 'blocks_east_of_city_center': -9 , 'blocks_north_of_city_center': -16 },

    { 'blocks_east_of_city_center': 11 , 'blocks_north_of_city_center': 15 },
    { 'blocks_east_of_city_center': 13 , 'blocks_north_of_city_center': 13 },
    { 'blocks_east_of_city_center': 24 , 'blocks_north_of_city_center': 12 },
    { 'blocks_east_of_city_center': 21 , 'blocks_north_of_city_center': 22 },
    { 'blocks_east_of_city_center': 22 , 'blocks_north_of_city_center': 26 },
    { 'blocks_east_of_city_center': 19 , 'blocks_north_of_city_center': 28 },
]

attendees_locations_tuples = [
    [ 
        attendee['blocks_east_of_city_center'], 
        attendee['blocks_north_of_city_center'] 
    ]

    for attendee
    in attendees_locations
]