import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

pconfig = Path(__file__).parents[1]


#aa = os.path.abspath(os.path.join(yourpath, os.pardir))


print(pconfig)

traindatapath = "%s/data/raw/Social_Network_Ads.csv"%pconfig


if __name__ == "__main__":
    print("訓練資料集在",traindatapath)