import tkinter as tk
from tkinter import ttk
from sklearn.linear_model import LinearRegression

# Sample house data (features)
house_data = [
    [3, 1500],
    [4, 2000],
    # Add more samples as needed
]

def predict_price():
    # Load the house data
    features = house_data

    # Create a linear regression model
    model = LinearRegression()

    # Sample target variable (house price)
    target = [250000, 320000]  # Example price values corresponding to the house_data

    # Fit the model to the data
    model.fit(features, target)

    # Get input values from the GUI
    bedrooms = int(entry_bedrooms.get())
    sqft = float(entry_sqft.get())

    # Predict the house price using manual data
    predicted_price = model.predict([[bedrooms, sqft]])

    # Display the predicted price
    result_label.config(text=f'Predicted Price: ${predicted_price[0]:.2f}')

root = tk.Tk()
root.title('House Price Prediction')

label_bedrooms = ttk.Label(root, text='Number of Bedrooms:')
label_bedrooms.grid(row=0, column=0, padx=10, pady=5)
entry_bedrooms = ttk.Entry(root)
entry_bedrooms.grid(row=0, column=1, padx=10, pady=5)

label_sqft = ttk.Label(root, text='Square Footage:')
label_sqft.grid(row=1, column=0, padx=10, pady=5)
entry_sqft = ttk.Entry(root)
entry_sqft.grid(row=1, column=1, padx=10, pady=5)

predict_button = ttk.Button(root, text='Predict Price', command=predict_price)
predict_button.grid(row=2, columnspan=2, padx=10, pady=10)

result_label = ttk.Label(root, text='', font=('Helvetica', 14))
result_label.grid(row=3, columnspan=2, padx=10, pady=10)

root.mainloop()
