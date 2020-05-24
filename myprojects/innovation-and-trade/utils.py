import collections
import matplotlib.pyplot as plt


class Logger:
    def __init__(self, empires, start_year):
        self.empires = empires
        self.start_year = start_year
        self.items = set()
        for empire in self.empires:
            for good in empire.goods.keys():
                self.items.add(good)

        self.quanities = {
            empire.name: collections.defaultdict(list) for empire in self.empires
        }
        self.num_updates = 0

    def update(self):
        for empire in self.empires:
            for item in self.items:
                quant = empire.goods.get(item, 0)
                self.quanities[empire.name][item].append(quant)

        self.num_updates += 1

    def plot_results(self, goods_to_show=None):
        years = range(self.start_year, self.start_year + self.num_updates)
        if goods_to_show is None:
            goods_to_show = self.items

        for i, empire in enumerate(self.empires):
            for item in goods_to_show:
                if item not in self.items:
                    continue

                plt.plot(years, self.quanities[empire.name][item], label=item)

            plt.title(empire.name)
            plt.xlabel("Time (years)")
            plt.ylabel("Quantity")
            plt.legend(loc="upper left")
            plt.show()
