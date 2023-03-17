import requests
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the API URL
url = "http://api.coincap.io/v2/assets/bitcoin/"

# Initialize the figure
fig, ax = plt.subplots()

# Define the x and y data lists as global variables
global x_data, y_data
x_data, y_data = [], []

# Initialize the line plot
line, = ax.plot(x_data, y_data)

# Define the update function
def update(frame):
    global x_data, y_data
    # Retrieve the data from the API
    response = requests.get(url)
    data = response.json()["data"]
    
    
    
    
    # Extract the price and timestamp
    price = float(data["priceUsd"])
    timestamp = response.json()["timestamp"]

    print(price)
    print(timestamp)
    
    
    # Append the data to the lists
    x_data.append(timestamp)
    y_data.append(price)
    
    # Limit the data to the last 100 values
    x_data = x_data[-100:]
    y_data = y_data[-100:]
    
    # Update the line plot
    line.set_data(x_data, y_data)
    
    # Set the axis limits
    ax.set_xlim(min(x_data), max(x_data))
    ax.set_ylim(min(y_data), max(y_data))
    
    # Set the title
    ax.set_title(f"Bitcoin Price: {price:.2f} USD")
    
    # Set the x and y labels
    ax.set_xlabel("Timestamp")
    ax.set_ylabel("Price (USD)")

# Create the animation
animation = FuncAnimation(fig, update, interval=5000)

# Show the plot
plt.show()