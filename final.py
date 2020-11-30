import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def main(arguments):
    file = ''
    # TODO: add error checking for files
    if len(arguments) > 1:
        file = arguments[1]
    else:
        file = "sample-salesv2.csv"

    data = pd.read_csv(file, ',', header=0)

    ###
    # I think this is what he wants for #2
    ###
    print('Quantity:')
    print("\tmean: " + str(data['quantity'].mean()))
    print("\tmedian: " + str(data['quantity'].median()))
    print("\trange : " + str(data['quantity'].max() - data['quantity'].min()))
    print("\tquartile : " + str(data['quantity'].quantile()))

    # I dont think that we need to filter this at all...
    customer_data = data.filter(items=["name", "category", "quantity", "unit price", "ext price", "date"])
    total_sales = customer_data.groupby(['name'])["ext price"].sum()
    total_sales.plot.bar()
    plt.show()

    customer_data.groupby(['name', 'category'])["ext price"].sum().unstack(1).plot.bar(stacked=True)
    plt.show()

    # I have no fucking idea what im suppose to do with this histogram
    customer_data["quantity"].plot.hist(density=True)
    plt.show()




if __name__ == '__main__':
    main(sys.argv)
