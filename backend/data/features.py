import numpy as np
from qutip import sigmax, sigmay, sigmaz, tensor

def compute_chsh_features(rho):
    """Compute CHSH features: <a0b0>, <a0b0'>, <a0'b0>, <a0'b0'> for a two-qubit state."""
    # Define measurement operators
    a0 = sigmaz()
    a0p = sigmax()
    b0 = (sigmax() - sigmaz()) / np.sqrt(2)
    b0p = (sigmax() + sigmaz()) / np.sqrt(2)
    # Tensor products for two-qubit measurements
    ops = [tensor(a0, b0), tensor(a0, b0p), tensor(a0p, b0), tensor(a0p, b0p)]
    features = [np.real((rho * op).tr()) for op in ops]
    return np.array(features) 