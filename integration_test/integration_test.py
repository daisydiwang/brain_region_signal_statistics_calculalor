# Integration test for brain_region_signal_statistics_calculalor using a synthetic data
import sys 
sys.path.append("../")
from volume_statistics_calculalor.brain_region_signal_statistics_calculalor import BrainRegionSignalStatisticsCalculator

def test_brain_region_signal_statistics_calculator():
    calculator = BrainRegionSignalStatisticsCalculator('synthetic_data/annotation.npz', 
                                                   'synthetic_data/signal.npz', 
                                                   'synthetic_data/structures.csv', 
                                                   'synthetic_data/statistics.csv')
    brain_statistics = calculator.calculate()

    # read in genereated statistics.csv and ground truth
    with open('synthetic_data/statistics.csv', 'r') as t1, open('synthetic_data/statistics_ground_truth.csv', 'r') as t2:
        file1 = t1.readlines()
        file2 = t2.readlines()

    # compare output with ground truth
    assert file1 == file2, "Output should be equal to ground truth!"

if __name__ == "__main__":
    test_brain_region_signal_statistics_calculator()
    print("Passed!")
