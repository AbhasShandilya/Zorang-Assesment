import numpy as np

def calculate_distance(coords1, coords2):
    return np.sqrt((coords1[0] - coords2[0])**2 + (coords1[1] - coords2[1])**2)

def nearest_neighbor(current_location, remaining_locations):
    min_distance = float('inf')
    nearest_location = None

    for location in remaining_locations:
        distance = calculate_distance(current_location, location)
        if distance < min_distance:
            min_distance = distance
            nearest_location = location

    return nearest_location

def generate_routes(store_location, delivery_addresses, num_agents):
    routes = [[] for _ in range(num_agents)]

    remaining_locations = delivery_addresses.copy()

    for agent in range(num_agents):
        current_location = store_location
        while remaining_locations:
            nearest_location = nearest_neighbor(current_location, remaining_locations)
            routes[agent].append(nearest_location['_id'])
            remaining_locations.remove(nearest_location)
            current_location = (nearest_location['latitude'], nearest_location['longitude'])

    return routes

# Input data
store_location = (28.9428, 77.2276)
delivery_addresses = [{
  "_id": 1,
  "latitude": 77.26398177444935,
  "longitude": 29.08908139212639
},{
  "_id": 2,
  "latitude": 77.2652468523133,
  "longitude": 29.092540182173252
},{
  "_id": 3,
  "latitude": 77.26404986407397,
  "longitude": 29.09916289150715
},{
  "_id": 4,
  "latitude": 77.26563535630703,
  "longitude": 29.095355203949506
},{
  "_id": 5,
  "latitude": 77.26583819836377,
  "longitude": 29.095966333768118
},{
  "_id": 6,
  "latitude": 77.26591865459652,
  "longitude": 29.096030741930008
},{
  "_id": 7,
  "latitude": 77.26655669510365,
  "longitude": 29.096778433551563
},{
  "_id": 8,
  "latitude": 77.26625794215028,
  "longitude": 29.10057406872511
},{
  "_id": 9,
  "latitude": 77.26653425798689,
  "longitude": 29.09987032413483
},{
  "_id": 10,
  "latitude": 77.26763392032183,
  "longitude": 29.09902442246675
},{
  "_id": 11,
  "latitude": 77.26816771909714,
  "longitude": 29.100369215011597
},{
  "_id": 12,
  "latitude": 77.26838428527117,
  "longitude": 29.106186546794223
},{
  "_id": 13,
  "latitude": 77.26839568465948,
  "longitude": 29.10613791918116
},{
  "_id": 14,
  "latitude": 77.26839568465948,
  "longitude": 29.10613791918116
},{
  "_id": 15,
  "latitude": 77.2683805969933,
  "longitude": 29.10623084753752
},{
  "_id": 16,
  "latitude": 77.26900588721037,
  "longitude": 29.104451171249522
},{
  "_id": 17,
  "latitude": 77.27113638840338,
  "longitude": 29.109589643776417
},{
  "_id": 18,
  "latitude": 77.05522680276044,
  "longitude": 28.42167042195797
},{
  "_id": 19,
  "latitude": 78.0288378149,
  "longitude": 27.1434745807
},{
  "_id": 20,
  "latitude": 78.0554456636,
  "longitude": 27.1581814282
},{
  "_id": 21,
  "latitude": 80.93117639422417,
  "longitude": 26.838514896886736
},{
  "_id": 22,
  "latitude": 73.86530748177277,
  "longitude": 18.50923240184784
},{
  "_id": 23,
  "latitude": 72.83506723783144,
  "longitude": 21.194217503070828
},{
  "_id": 24,
  "latitude": 72.8313768915411,
  "longitude": 21.173333823680878
},{
  "_id": 25,
  "latitude": 84.09939866513014,
  "longitude": 24.04220160698313
},{
  "_id": 26,
  "latitude": 84.54404924064875,
  "longitude": 25.515784804698182
},{
  "_id": 27,
  "latitude": 85.05047530433829,
  "longitude": 23.352146856486797
},{
  "_id": 28,
  "latitude": 85.05042222303217,
  "longitude": 22.47985292226076
},{
  "_id": 29,
  "latitude": 86.97660762816668,
  "longitude": 23.51162401401524
},{
  "_id": 30,
  "latitude": 47.86461110553439,
  "longitude": 17.760396860539913
},{
  "_id": 31,
  "latitude": 45.83053924115291,
  "longitude": 21.818511039018635
},{
  "_id": 32,
  "latitude": 39.230719330494054,
  "longitude": 36.83638673275709
},{
  "_id": 33,
  "latitude": 39.230719330494054,
  "longitude": 36.83638673275709
},{
  "_id": 34,
  "latitude": 35.7229859499076,
  "longitude": 51.3818771392107
},{
  "_id": 35,
  "latitude": 31.765385760128474,
  "longitude": 35.13460122048855
},{
  "_id": 36,
  "latitude": 34.144458671130096,
  "longitude": 72.09338553249836
},{
  "_id": 37,
  "latitude": 34.139665017636545,
  "longitude": 72.09170512855053
},{
  "_id": 38,
  "latitude": 30.048276616619038,
  "longitude": 31.257372200489044
},{
  "_id": 39,
  "latitude": 33.66878794612444,
  "longitude": 73.00006840378046
},{
  "_id": 40,
  "latitude": 33.64388599157803,
  "longitude": 73.09087257832289
},{
  "_id": 41,
  "latitude": 33.64383379679333,
  "longitude": 73.0908202752471
},{
  "_id": 42,
  "latitude": 33.64378188109373,
  "longitude": 73.09081591665745
},{
  "_id": 43,
  "latitude": 33.634549320550285,
  "longitude": 73.09619408100843
},{
  "_id": 44,
  "latitude": 33.517871148888894,
  "longitude": 72.87231914699078
},{
  "_id": 45,
  "latitude": 33.01481109437303,
  "longitude": 73.73526658862829
},{
  "_id": 46,
  "latitude": 32.64872430665188,
  "longitude": 73.33715736865997
},{
  "_id": 47,
  "latitude": 32.48295697624009,
  "longitude": 72.91242320090532
},{
  "_id": 48,
  "latitude": 32.48093109522745,
  "longitude": 72.91209161281586
},{
  "_id": 49,
  "latitude": 32.7638266997,
  "longitude": 74.8428532854
},{
  "_id": 50,
  "latitude": 32.7628017939,
  "longitude": 74.8444502493
},{
  "_id": 51,
  "latitude": 32.760082,
  "longitude": 74.837532
},{
  "_id": 52,
  "latitude": 32.758788,
  "longitude": 74.847437
},{
  "_id": 53,
  "latitude": 32.7555441471,
  "longitude": 74.8496761546
},{
  "_id": 54,
  "latitude": 32.7506722614,
  "longitude": 74.8493418843
},{
  "_id": 55,
  "latitude": 32.7420613597,
  "longitude": 74.81924247
},{
  "_id": 56,
  "latitude": 32.7462234,
  "longitude": 74.8454447
},{
  "_id": 57,
  "latitude": 32.7485445,
  "longitude": 74.8585121
},{
  "_id": 58,
  "latitude": 32.7415018592,
  "longitude": 74.8203016073
},{
  "_id": 59,
  "latitude": 32.7437509,
  "longitude": 74.8426261
},{
  "_id": 60,
  "latitude": 32.7432816854,
  "longitude": 74.8578136756
},{
  "_id": 61,
  "latitude": 32.7432816854,
  "longitude": 74.8578136756
},{
  "_id": 62,
  "latitude": 32.7428125667,
  "longitude": 74.8578551112
},{
  "_id": 63,
  "latitude": 32.7428125667,
  "longitude": 74.8578551112
},{
  "_id": 64,
  "latitude": 32.7428125667,
  "longitude": 74.8578551112
},{
  "_id": 65,
  "latitude": 32.7428125667,
  "longitude": 74.8578551112
},{
  "_id": 66,
  "latitude": 32.74307,
  "longitude": 74.86004
},{
  "_id": 67,
  "latitude": 32.7354934932,
  "longitude": 74.829938449
},{
  "_id": 68,
  "latitude": 32.7338418818,
  "longitude": 74.8278872938
},{
  "_id": 69,
  "latitude": 32.7415949215,
  "longitude": 74.870993346
},{
  "_id": 70,
  "latitude": 32.7396496167,
  "longitude": 74.864856787
},{
  "_id": 71,
  "latitude": 32.7406888287,
  "longitude": 74.8717064783
},{
  "_id": 72,
  "latitude": 32.738674,
  "longitude": 74.8653551
},{
  "_id": 73,
  "latitude": 32.7379826218,
  "longitude": 74.8635763675
},{
  "_id": 74,
  "latitude": 32.733540722316874,
  "longitude": 74.84355971217155
},{
  "_id": 75,
  "latitude": 32.7376498396,
  "longitude": 74.8677170277
},{
  "_id": 76,
  "latitude": 32.7377053974,
  "longitude": 74.8712541908
},{
  "_id": 77,
  "latitude": 32.7355137991,
  "longitude": 74.8709685355
},{
  "_id": 78,
  "latitude": 32.7317385171,
  "longitude": 74.8665485904
},{
  "_id": 79,
  "latitude": 32.7293183153,
  "longitude": 74.8691439629
},{
  "_id": 80,
  "latitude": 32.7264631204,
  "longitude": 74.8598400503
},{
  "_id": 81,
  "latitude": 32.7233903626,
  "longitude": 74.8576342687
},{
  "_id": 82,
  "latitude": 32.7087539626,
  "longitude": 74.8641419783
},{
  "_id": 83,
  "latitude": 32.7058673,
  "longitude": 74.8622451
},{
  "_id": 84,
  "latitude": 31.961006249510373,
  "longitude": 70.6146340817213
},{
  "_id": 85,
  "latitude": 32.7057310942,
  "longitude": 74.8729382828
},{
  "_id": 86,
  "latitude": 32.7049338185,
  "longitude": 74.8720541596
},{
  "_id": 87,
  "latitude": 32.7049425643,
  "longitude": 74.8721138388
},{
  "_id": 88,
  "latitude": 32.7017937356,
  "longitude": 74.8603342474
},{
  "_id": 89,
  "latitude": 32.7017911964,
  "longitude": 74.8604636639
},{
  "_id": 90,
  "latitude": 32.7017889394,
  "longitude": 74.8605726287
},{
  "_id": 91,
  "latitude": 32.7005277968,
  "longitude": 74.8538288847
},{
  "_id": 92,
  "latitude": 32.7025092216,
  "longitude": 74.8671165481
},{
  "_id": 93,
  "latitude": 32.7013457076,
  "longitude": 74.8617779464
},{
  "_id": 94,
  "latitude": 32.7008401217,
  "longitude": 74.8591239005
},{
  "_id": 95,
  "latitude": 32.6997485079,
  "longitude": 74.8626565265
},{
  "_id": 96,
  "latitude": 32.700267102,
  "longitude": 74.8679507151
},{
  "_id": 97,
  "latitude": 32.6981801055,
  "longitude": 74.8611114174
},{
  "_id": 98,
  "latitude": 32.6978824429,
  "longitude": 74.861696139
},{
  "_id": 99,
  "latitude": 32.6974942103,
  "longitude": 74.8615952209
},{
  "_id": 100,
  "latitude": 32.7029324164,
  "longitude": 74.8970647529
}]
num_agents = 10

# Generate routes
output_routes = generate_routes(store_location, delivery_addresses, num_agents)
print(output_routes)
