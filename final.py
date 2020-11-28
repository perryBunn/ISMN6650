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
    customer_data = data.filter(items=["name", "category", "quantity", "unit price", "ext price"])
    dfclean = customer_data.groupby(['name'], dropna=False).sum('quantity')
    print(dfclean)

    labels = customer_data['name']
    sales = customer_data.groupby(['name']).sum('quantity')['quantity']
    width = .35
    print("sales:\n" + str(sales))
    # fig, ax = plt.subplots()
    # ax.bar(labels, sales['quantity'], width)
    # ax.set_ylabel('quantity sold')
    # ax.set_title('Sales by Name')
    # plt.show()
    plt.figure()
    dfclean.plot(kind='bar', stacked=True)



if __name__ == '__main__':
    main(sys.argv)
