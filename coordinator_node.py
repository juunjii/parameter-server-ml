import sys
import os
import threading
import random
from queue import Queue
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

from coordinator import coordinator
from coordinator.ttypes import WeightMatrices
from compute import compute
from compute.ttypes import WeightMatrices as ComputeWeightMatrices

from ML import mlp, scale_matricies, sum_matricies, calc_gradient

class CoordinatorHandler:
    def __init__(self, scheduling_policy):
        self.scheduling_policy = scheduling_policy
        self.compute_nodes = []
        self.get_compute_nodes()

    def get_compute_nodes(self):
        pass
        
    def connet_compute_node_server(self, host, port):
        pass

    def scheduling_policy(self):
        pass
   
    def train(self, dir, rounds, epochs, h, k, eta):
        pass