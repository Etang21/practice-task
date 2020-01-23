import yaml
import csv
import numpy as np

def main():
    CONFIG = yaml.load(open('config_global.yaml', 'rU'))
    num_draws = 10000
    mean = [0, 0]
    cov = [[1, 0.5], [0.5, 1]]
    samples = np.random.multivariate_normal(mean, cov, num_draws, check_valid = 'raise')
    with open('%s/data.csv' % CONFIG['build']['draw_data'], 'wb') as f:
    	writer = csv.writer(f)
    	writer.writerow(['x', 'y'])
    	writer.writerows(samples)

main()
