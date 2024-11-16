#main script to count cards
import sys
script_dir = __file__.rsplit('/', 2)[0]
sys.path.append(script_dir)

import Data_Processing.countCards
import Data_Processing.Data_Visualization.plotData

input("Press enter to stop script")