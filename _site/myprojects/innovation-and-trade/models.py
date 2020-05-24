import math
import random
import numpy as np
import matplotlib.pyplot as plt


class Empire:
    def __init__(self, name, goods, innovation_index=0.1):
        self.name = name
        self.goods = goods
        self.innovation_index = innovation_index
        self.original_quantity = dict((good, quantity) for good, quantity in self.goods.items())
        
    def trade(self, other, innovation_idx=None):
        # Only trade with probability defined by innovation index
        if random.uniform(0, 1) < self.innovation_index:
            # Randomly choose a good to trade and receive
            our_goods = [key for key in self.goods.keys()]
            their_goods = [key for key in other.goods.keys()]
            good_to_trade = random.choice(our_goods)
            good_to_receive = random.choice(their_goods)
            
            if innovation_idx is not None:
                idx = innovation_idx
            else:
                idx = self.innovation_index

            
            # Quantity is a function of the innovation index
            quantity = int(min(self.goods[good_to_trade], other.goods[good_to_receive]) * idx)

            # Execute the trade
            if good_to_receive in self.goods:
                self.goods[good_to_receive] += quantity
            else:
                self.goods[good_to_receive] = quantity
            
            other.goods[good_to_receive] -= quantity
            
            if good_to_trade in other.goods:
                other.goods[good_to_trade] += quantity
            else:
                other.goods[good_to_trade] = quantity
                
            self.goods[good_to_trade] -= quantity

    def innovate(self):
        self.innovation_index = min(self.innovation_index * 1.1, 0.5)
    
    def produce_goods(self):
        for good, quantity in self.original_quantity.items():
            self.goods[good] += int(quantity * self.innovation_index)

    def reset(self):
        self.goods = {}
        for good, quantity in self.original_quantity.items():
            self.goods[good] = quantity
    
    def show_distribution_of_goods(self):
        labels = []
        percentages = [] # The ratio of each good to the total number of goods
        total_num_goods = sum(amount for amount in self.goods.values())
        for label, amount in self.goods.items():
            labels.append(label)
            percentage = amount / total_num_goods * 100
            percentages.append(percentage)
           
        fig1, ax1 = plt.subplots()
        ax1.pie(percentages, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.title(f"{self.name} distribution of goods")

        plt.show()
        