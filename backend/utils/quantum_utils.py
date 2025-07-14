import numpy as np
from qutip import rand_dm, partial_transpose

def generate_random_two_qubit_state():
    """Generate a random two-qubit density matrix."""
    return rand_dm(4)

def is_entangled_ppt(rho):
    """Check if a two-qubit state is entangled using the PPT criterion."""
    # Partial transpose with respect to the second qubit
    rho_pt = partial_transpose(rho, [0, 1])
    # If any eigenvalue is negative, the state is entangled
    return np.any(rho_pt.eigenenergies() < -1e-10) 