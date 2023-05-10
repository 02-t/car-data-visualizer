import tkinter as tk
from threading import Thread

import chart_generator as cg


def run_chart(x, y, f, c):
    t1 = Thread(target=cg.run_chart, args=(x, y, f, c))
    t1.start()


if __name__ == '__main__':
    root = tk.Tk()

    fuel_button = tk.Button(root,
                            text="Run Fuel Chart",
                            command=lambda: run_chart('fuel', 'price', False, 'blue'))
    fuel_button.pack()

    production_year_button = tk.Button(root,
                                       text="Run Production Year Chart",
                                       command=lambda: run_chart('production year', 'price', False, 'red'))
    production_year_button.pack()

    km_driven_button = tk.Button(root,
                                 text="Run Km Driven Chart",
                                 command=lambda: run_chart('km driven', 'price', True, '#610076'))
    km_driven_button.pack()

    root.mainloop()