import numpy as np
import typing

class DROLinearRegressionSolver:
  def __init__(self, 
               design: typing.List[np.array], 
               response: typing.List[np.float],
               config: typing.Dict):
    self.design = design
    self.response = response
    self.config = config
    if "p" not in self.config:
      self.p = np.inf
    else:
      trial_p = self.config["p"]
      try:
        self.p = np.float(self.config["p"])
        assert self.p >= 2.0
      except Exception as e:
        print(f"Error in deciding p. Config p must be a floatable between 2 and np.inf. Received: {trial_p}")
    if "GeometryType" in self.config:
      self.geometry_type = self.config["GeometryType"]
      assert self.geometry_type in ["Trivial", "Lewis"], f"invalid geometry type passed {self.geometry_type}"

  def compute_geometry(self):


  def step(self, x: np.array) -> np.array:
    # perform a single iteration of the algorithm starting at x
    # TODO: implement
    return np.array([0.0])

  def 