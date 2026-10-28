import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error


data={
     "area": [5, 7, 8, 10, 12, 15, 18, 20],
     "bedrooms": [1, 2, 2, 3, 3, 4, 4, 5],
     "age": [10, 8, 6, 5, 4, 3, 2, 1],
     "price": [25, 35, 40, 50, 60, 75, 90, 100]

}

df=pd.DataFrame(data)

print(df.head())
print(df.isnull().sum())
print(df.shape)
print(df.dtypes)

X=df[["area", "bedrooms","age"]]
y=df["price"]

X_train,X_test,y_train,y_test=train_test_split(X, y, test_size=0.25, random_state=42)

model=LinearRegression()

model.fit(X_train,y_train)

predictions=model.predict(X_test)

mae=mean_absolute_error(y_test,predictions)

print("Training rows: ",len(X_train))
print("Testing rows: ",len(X_test))

print("Actual price: ",y_test.tolist())
print("Prediction price",predictions.round(2).tolist())

print("Mean Abosolute Error",round(mae,2))

new_house = pd.DataFrame({
     "area": [17],
     "bedrooms": [5],
     "age": [7]
 })

prediction_price = model.predict(new_house)

print("New house predicted price:", round(prediction_price[0], 2))