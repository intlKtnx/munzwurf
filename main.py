import h5py
import numpy
import os
import re
from pathlib import Path


def convert_to_h5():
    f = h5py.File("coinData", mode='w', )
    one_cent = f.create_group("oneCent")
    two_cent  = f.create_group("twoCent")
    five_cent = f.create_group("fiveCent")
    twenty_cent = f.create_group("twentyCent")
    fifty_cent = f.create_group("fiftyCent")
    one_euro  = f.create_group("oneEuro")
    two_euro  = f.create_group("twoEuro")

    directory = os.path.join("/home", "marcus", "Dokumente", "munzwurf", "data_csv")
    pattern = re.compile('\d\d*')
    for filename in os.listdir(directory):
        label = pattern.match(filename)
        data = numpy.genfromtxt(os.path.join(directory, filename), delimiter=',', dtype=int)
        if label.group() == '1':
            dset = one_cent.create_dataset(filename, data=data)
        elif label.group() == '2':
            dset = two_cent.create_dataset(filename, data=data)
        elif label.group() == '5':
            dset = five_cent.create_dataset(filename, data=data)
        elif label.group() == '20':
            dset = twenty_cent.create_dataset(filename, data=data)
        elif label.group() == '50':
            dset = fifty_cent.create_dataset(filename, data=data)
        elif label.group() == '100':
            dset = one_euro.create_dataset(filename, data=data)
        elif label.group() == '200':
            dset = two_euro.create_dataset(filename, data=data)


def check_dataset():
    p = Path("/home/marcus/PycharmProjects/pythonProject/")
    files = p.glob('*.h5')
    for h5dataset_fp in files:
        with h5py.File(h5dataset_fp.resolve()) as h5_file:
            # Walk through all groups, extracting datasets
            for gname, group in h5_file.items():
                i = 1
                for dname, ds in group.items():
                    if i == 1:
                        print(gname, dname, ds.shape)
                        i += 1


if __name__ == '__main__':
    mode = input()
    if mode == "1":
        print("mode = 1")
        convert_to_h5()
    elif mode == "2":
        print("mode = 2")
        check_dataset()
