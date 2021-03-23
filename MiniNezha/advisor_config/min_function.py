#!/usr/bin/env python

import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("-a", type=float, default=0.0)
args = parser.parse_args()


def main():
  # Read parameters
  restart_torque = args.a
  param_dic = {"restart_torque":restart_torque}

  ## Compute or learning

  # write args to txt
  with open("../controllers/my_controller_python/args.txt",'w') as f1:
    f1.write(str(param_dic))

  # run webots
  os.system('webots --mode=fast --no-rendering')

  # read metrics from txt
  with open("../controllers/my_controller_python/metrics.txt",'r') as f2:
    metrics_dic = eval(f2.read())
    y = metrics_dic["restart_metrics"]

  # Output the metrics
  print(y)


if __name__ == "__main__":
  main()