from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def model(df):

    X=df[['Area','Cost']]
    y=df['Production']

    X_train,X_test,y_train,y_test=train_test_split(
        X,y,test_size=0.2,random_state=42
    )

    reg=LinearRegression()
    reg.fit(X_train,y_train)

    print("Model Accuracy:",reg.score(X_test,y_test))
