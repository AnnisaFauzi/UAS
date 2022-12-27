import numpy as np
import matplotlib.pyplot as plt

alpha = np.radians(45)
g = 9.8
v0 = 2.4e-3
y0 = 0
x0 = 0
t0 = 0
tmax = 0.1

v0x = v0*np.cos(alpha)
v0y = v0*np.sin(alpha)

X = ((v0**2)*np.sin(2*alpha))/(2*g)
print("Jarak Horizontal Maksimum = ",X," m")
Y = ((v0**2)*np.sin(2*alpha))/(2*g)
print("Jarak  Maksimum = ",Y," m")
T = (2*v0*np.sin(alpha))/g
print("Waktu Mencapai Jarak Horizontal Maksimum = ",T," s")
print("\n")

t = np.arange(0.0, T, 10**(-6))
y = v0y*t - 0.5*g*t**2
x = v0x*t

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set(xlabel='x (m)', ylabel= 'y (m)', title='Grafik Gerak Parabola')
ax.grid()
plt.show()

from sklearn.neural_network import MLPClassifier

# Database: Gerbang Logika AND
# x = Data, y = Target
x = [[0 ,0], [0, 5], [1,0], [1,3], [2,5], [3,2]]
y = [5.0,8.0,18.0,25.0,30.0,34.0]
t = [0,4,8,12,20,24]

# training and classify
clf = MLPClassifier(solver='1bfgs', alpha=1e-2,
                    hidden_layer_sizes=(10, 5),
                    random_state=1, max_iter=1000,
                    warm_sart=True)
clf.fit(x, y)

# prediksi
print ("Logika AND Metode Artificial Neural Network (ANN)")
print ("Logika = Prediksi")
print ("0 0 = ", clf.predict([[5, 0]]))
print ("0 5 = ", clf.predict([[8, 0]]))
print ("1 0 = ", clf.predict([[18, 0]]))
print ("1 3 = ", clf.predict([[25, 0]]))
print ("2 5 = ", clf.predict([[30, 0]]))
print ("3 2 = ", clf.predict([[34, 0]]))
