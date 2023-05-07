import eel
from main import eq_solving, fitting, plot
import numpy as np
import matplotlib.pyplot as plt

@eel.expose
def data(set):
    try:
        set = list(map(float, set))
        x_data1 = np.array([0, 0.5, 0.75, 1, 1.5, 2, 2.5, 3, 4, 6])
        x_data2 = np.array(set[::2])
        y_data1 = np.array([70, 150, 165, 145, 90, 75, 65, 75, 80, 75])
        y_data2 = np.array(set[1::2])
        x_subs = np.linspace(0, max(x_data1), 200)

        eq1 = eq_solving(x_data1, y_data1)
        fit1 = fitting(x_data1, y_data1)
        y_subs1 = eq1(x_subs, *fit1)

        eq2 = eq_solving(x_data2, y_data2)
        fit2 = fitting(x_data2, y_data2)
        y_subs2 = eq2(x_subs, *fit2)

        print(fit2)

        t0 = 2 * np.pi * np.sqrt(fit2[-2] ** 2 + fit2[1] ** 2) ** -1

        diabetic = 'Has Diabetes' if t0 > 4 else 'Has Not Diabetes'

        plot(x_data1, x_data2, x_subs, y_data1, y_data2, y_subs1, y_subs2, diabetic)

    except Exception as e:
        print(e)
        return False
    return True,t0

eel.init('static')
eel.start('index.html', size=(1440, 900))





