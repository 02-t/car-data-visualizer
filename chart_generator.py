import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import mplcursors
import locale

from threading import Thread

locale.setlocale(locale.LC_ALL, '')

df = pd.read_csv('data.csv')
df = df.dropna()

df = df[df['production year'].apply(lambda x: str(x).isdigit())]
df = df[df['price'].apply(lambda x: str(x).isdigit())]
df = df[df['km driven'].apply(lambda x: str(x).isdigit())]
df = df[df['fuel'] != '-']

df['production year'] = df['production year'].astype(int)
df['price'] = df['price'].astype(float)
df['km driven'] = pd.to_numeric(df['km driven'], errors='coerce')


def format_tick(value, _):
    return '{:,.0f}'.format(value)


def get_title(string):
    string = string.capitalize()
    if string == "Km driven":
        string = "Kilometers driven"
    return string


def run_chart(x, y, format, color):
    global df

    title_x = get_title(x)
    title_y = get_title(y)

    df = df.sort_values('km driven')

    sns.set_style('whitegrid')
    sns.lineplot(data=df, x=x, y=y, color=color)


    plt.title(title_y + ' vs ' + title_x)
    plt.ylabel(title_y)
    plt.xlabel(title_x)

    gca = plt.gca()
    if format:
        gca.xaxis.set_major_formatter(ticker.FuncFormatter(format_tick))
    gca.yaxis.set_major_formatter(ticker.FuncFormatter(format_tick))

    cursor = mplcursors.cursor(hover=True)


    @cursor.connect("add")
    def on_add(sel):
        x0 = sel.target[0]
        try:
            nearest_index = df[x].sub(x0).abs().idxmin()
            nearest_row = df.loc[nearest_index]
            y_val = locale.format_string("%d", nearest_row[y], grouping=True)
            x_val = str(nearest_row[x])
            if format:
                x_val = locale.format_string("%d", nearest_row[x], grouping=True)

            sel.annotation.set_text(f'{title_y}: {y_val}\n{title_x}: {x_val}')
        except:
            pass

    plt.show()
