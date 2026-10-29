from sklearn.linear_model import LinearRegression

X=[[1],[2],[3],[4],[5]]
Y=[35,45,55,65,75]

model= LinearRegression()
model.fit(X,Y)

prediction = model.predict([[6]])

print("study hours: 6")
print("Predicted marks: ",prediction[0])
print("model trained successfully")
