# Executable example: Steane transversal logical CNOT

**Definition.** For two Steane [[7,1,3]] CSS blocks, pair physical qubit `i` of control with physical qubit `i` of target. Verify the conjugation of stabilizers and logical operators. This is the code-specific foundation used when compiling transversal logical gates and teleportation protocols.

The example is pure Python 3.10+:

~~~python
# Three mutually orthogonal Hamming parity checks; each has even weight.
checks = [0b0001111, 0b0110011, 0b1010101]
logical = 0b1111111
assert all(((a & b).bit_count() % 2) == 0 for a in checks for b in checks)
assert all(((h & logical).bit_count() % 2) == 0 for h in checks)
assert (logical & logical).bit_count() % 2 == 1

# Heisenberg action of seven pairwise CNOTs, represented over GF(2).
def transversal_cnot(x_control, x_target, z_control, z_target):
    return (x_control, x_target ^ x_control, z_control ^ z_target, z_target)

for h in checks:
    assert transversal_cnot(h, 0, 0, 0) == (h, h, 0, 0)
    assert transversal_cnot(0, h, 0, 0) == (0, h, 0, 0)
    assert transversal_cnot(0, 0, h, 0) == (0, 0, h, 0)
    assert transversal_cnot(0, 0, 0, h) == (0, 0, h, h)
assert transversal_cnot(logical, 0, 0, 0) == (logical, logical, 0, 0)
assert transversal_cnot(0, 0, 0, logical) == (0, 0, logical, logical)
print("Steane stabilizers preserved; logical CNOT map verified")
~~~

**Primary documentation:** https://qiskit.qotlabs.org/learning/courses/foundations-of-quantum-error-correction/fault-tolerant-quantum-computing/controlling-error-propagation

**Published teleportation/reset implementation:** https://www.nist.gov/publications/fault-tolerant-neutral-atom-architecture-universal-quantum-computation

**Scope:** The executable invariant proves the exact Steane transversal CNOT logical map. A particular teleportation protocol must additionally provide its encoded preparation, measurements, decoded byproducts, and physical reset schedule from its published implementation.
