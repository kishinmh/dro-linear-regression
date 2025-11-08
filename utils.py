import numpy as np
import typing

class DROLinearRegressionSolver:
  def __init__(self, 
               design: typing.List[np.array], 
               response: typing.List[np.float] | np.array,
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

    # dimension validations
    self.dim = design[0].shape[1]
    for des in design:
      assert des.shape[1] == self.dim, f"Dimension mismatch in design. Expected {self.dim} but got the matrix {des}"
    assert len(design) == len(response), f"Received {len(design)} designs and {len(response)} responses"
    self.num_problems = len(design)
    
    if not isinstance(response, np.array):
      self.response = np.array(self.response)
    assert self.response.shape in [(self.num_problems, 1), (self.num_problems, ), (1, self.num_problems)], f"Responses have invalid shape {self.response.shape}"

    self.x = np.zeros(self.dim)

  def objective(self):


  def compute_geometry(self):
    # TODO: implement
    return None

  def initialize(self):
    # TODO: implement
    return None

  def step(self) -> np.array:
    # perform a single iteration of the algorithm and update the internal state variables
    # TODO: implement
    return np.array([0.0])