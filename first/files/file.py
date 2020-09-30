import sys

sys.path.append('C:\\Users\\Moin Khan\\Desktop')
import price_prediction as pp

import numpy as np

print("imported successfully")

print(pp.showhead())

lr = pp.LR()
print(lr.score)
