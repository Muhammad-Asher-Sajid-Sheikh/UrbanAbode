data = {
    'Size': [1500, 1800, 2400, 3000, 3500, 4000, 4500, 5000],
    'Rooms': [2, 3, 3, 4, 4, 5, 5, 6],
    'Price': [300000, 400000, 450000, 600000, 650000, 800000, 850000, 950000]
}
df = pd.DataFrame(data)


# Create a model that predicts the price of a house based on its size and number of rooms.