from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def predict(df):
    X = df[['Hour']]
    y = df['Vehicles']

    X_train,X_test,y_train,y_test = train_test_split(
        X,y,test_size=0.2,random_state=42
    )

    model = LinearRegression()
    model.fit(X_train,y_train)

    print("Accuracy:",model.score(X_test,y_test))
