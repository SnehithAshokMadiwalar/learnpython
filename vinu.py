import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model
import linearRegression
x=np.array([500,700,1000,1200,1500]).reshape(-1,1)
y=np.array([100,150,200,250,300])
x_test=np.array([800,1100,1400]).reshape(-1,1)
y_pred=model.predict(X_test)
plt.scatter(X,y,color='blue',label="Training Data")
plt.plot(X_test,y_pred,color='red',linestyle="dashed",label="predictions")
plt.xlabel("size(sq ft)")
plt.ylabel("price($1000s)")
plt.legend()
plt.show()
