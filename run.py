import pandas as pd
import numpy as np
import argparse

from volume_statistics_calculalor.brain_region_signal_statistics_calculalor import BrainRegionSignalStatisticsCalculator

# parse commandline args
parser = argparse.ArgumentParser()
parser.add_argument('--annotation_volume_path', required=True, help='annotation_volume filename')
parser.add_argument('--signal_volume_path', required=True, help='signal_volume filename')
parser.add_argument('--structures_df_path', required=True, help='structures_df filename')
parser.add_argument('--statistics_df_path', required=True, help='out statistics_df filename')
args = parser.parse_args()

calculator = BrainRegionSignalStatisticsCalculator(
    args.annotation_volume_path, args.signal_volume_path, args.structures_df_path, args.statistics_df_path)

calculator.calculate()
