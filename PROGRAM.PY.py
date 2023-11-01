import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
import cartopy.crs as ccrs  # Import cartopy for map projections
import cartopy.feature as cfeature  # Import cartopy feature for drawing borders

# Load earthquake data (you'll need a dataset with earthquake records)
data = pd.read_csv('synthetic_earthquake_data.csv')

# Select relevant features (latitude and longitude)
X = data[['Latitude', 'Longitude']]
# Create a binary label, e.g., 1 for earthquake-prone and 0 for non-prone
y = data['EarthquakeProne']

# Initialize and train a random forest classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X, y)

# Get latitude and longitude from the user
user_latitude = float(input("Enter the latitude: "))
user_longitude = float(input("Enter the longitude: "))

# Use the trained model to predict earthquake-prone regions with user input
user_data = pd.DataFrame({'Latitude': [user_latitude], 'Longitude': [user_longitude]})
prediction = clf.predict(user_data)

# Create a Cartopy map
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())

# Plot the entire world by setting the extent to global
ax.set_extent([-180, 180, -90, 90], crs=ccrs.PlateCarree())

# Add coastlines and country borders
ax.coastlines()
ax.add_feature(cfeature.BORDERS)

# Plot the user location on the world map
ax.scatter(user_longitude, user_latitude, transform=ccrs.PlateCarree(), c='red' if prediction[0] == 1 else 'blue', s=50)

# Show the plot
plt.title("Earthquake-Prone Location")
plt.show()
