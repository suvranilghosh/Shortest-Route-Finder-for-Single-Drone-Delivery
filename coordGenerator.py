import random

NBLat = 40.486216
NBLong = -74.451819

if __name__ == '__main__':
    for i in range(2, 20):
        file = open('./data/deliveryLocs' + str(i) + '.txt', 'w')
        for _ in range(i):
            file.write(str(random.uniform(NBLat-.15, NBLat+.15))+' ')
            file.write(str(random.uniform(NBLong-.15, NBLong+.15))+'\n')
        file.close()

