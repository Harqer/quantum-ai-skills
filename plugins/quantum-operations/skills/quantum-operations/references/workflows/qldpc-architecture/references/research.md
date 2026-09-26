# Quantum LDPC research map

Research reviewed September 2026. Use these sources as architecture evidence attached to their stated code family, noise model, connectivity, decoder, and workload assumptions.

## Foundations and asymptotic constructions

1. MacKay, Mitchison, McFadden, **Sparse Graph Codes for Quantum Error-Correction** (2004), arXiv:quant-ph/0304161. Introduces sparse quantum parity-check constructions and the bounded-interaction motivation.
   https://arxiv.org/abs/quant-ph/0304161
2. Tillich, Zémor, **Quantum LDPC codes with positive rate and minimum distance proportional to the square root of the blocklength** (2014), arXiv:0903.0566. Hypergraph-product construction with constant rate and sqrt(n)-scale distance.
   https://arxiv.org/abs/0903.0566
3. Kovalev, Pryadko, **Quantum Kronecker sum-product low-density parity-check codes with finite rate** (2013).
   https://doi.org/10.1103/PhysRevA.88.012311
4. Gottesman, **Fault-Tolerant Quantum Computation with Constant Overhead** (2014), arXiv:1310.2984. Establishes a constant-overhead FTQC route under suitable qLDPC assumptions.
   https://arxiv.org/abs/1310.2984
5. Leverrier, Tillich, Zémor, **Quantum Expander Codes** (2015), arXiv:1504.00822. Constant-rate HGP/expander codes with an efficient small-set-flip style decoder.
   https://arxiv.org/abs/1504.00822
6. Fawzi, Grospellier, Leverrier, **Constant overhead quantum fault-tolerance with quantum expander codes** (2018), arXiv:1808.03821. Noisy-syndrome fault-tolerance and constant-overhead architecture results for expander codes.
   https://arxiv.org/abs/1808.03821
7. Hastings, Haah, O'Donnell, **Fiber Bundle Codes: Breaking the N^(1/2) polylog(N) Barrier for Quantum LDPC Codes** (2021), arXiv:2009.03921.
   https://arxiv.org/abs/2009.03921
8. Breuckmann, Eberhardt, **Balanced Product Quantum Codes** (2021), arXiv:2012.09271.
   https://arxiv.org/abs/2012.09271
9. Panteleev, Kalachev, **Asymptotically Good Quantum and Locally Testable Classical LDPC Codes** (2021/2022), arXiv:2111.03654. Establishes asymptotically good qLDPC constructions.
   https://arxiv.org/abs/2111.03654
10. Leverrier, Zémor, **Quantum Tanner Codes** (2022), arXiv:2202.13641. Asymptotically good Tanner-code construction.
    https://arxiv.org/abs/2202.13641
11. Breuckmann, Eberhardt, **Quantum Low-Density Parity-Check Codes** (PRX Quantum 2021). Broad review of constructions, decoding, geometry, and logical-computation challenges.
    https://doi.org/10.1103/PRXQuantum.2.040101

## Finite-length codes and bivariate bicycles

12. Panteleev, Kalachev, **Degenerate Quantum LDPC Codes With Good Finite Length Performance** (Quantum 2021), arXiv:1904.02703. Generalized bicycle/finite-length evidence and BP+OSD.
    https://arxiv.org/abs/1904.02703
13. Bravyi, Cross, Gambetta, Maslov, Rall, Yoder, **High-threshold and low-overhead fault-tolerant quantum memory** (Nature 2024), arXiv:2308.07915. Bivariate-bicycle codes, circuit-level threshold, explicit [[144,12,12]] Gross-code example and syndrome architecture.
    https://arxiv.org/abs/2308.07915
14. Wang et al., **Demonstration of low-overhead quantum error correction codes** (Nature Physics 2026), arXiv:2505.09684. Hardware demonstration of BB/punctured-BB codes on long-range-coupled superconducting qubits.
    https://arxiv.org/abs/2505.09684
15. Liang, Chen, **Self-dual bivariate bicycle codes with transversal Clifford gates** (npj Quantum Information 2026), arXiv:2510.05211.
    https://arxiv.org/abs/2510.05211
16. Kim, Gicev, Sevior, Usman, **Time-Dynamic Circuits for Fault-Tolerant Shift Automorphisms in Quantum LDPC Codes** (2026), arXiv:2601.09911. Dynamic syndrome circuits for logical shift automorphisms including Gross-code-family benchmarks.
    https://arxiv.org/abs/2601.09911

## Decoding

17. Roffe, White, Burton, Campbell, **Decoding Across the Quantum LDPC Code Landscape** (2020/2026 revision), arXiv:2005.07016. BP+OSD across HGP/topological/semitopological/random qLDPC.
    https://arxiv.org/abs/2005.07016
18. Delfosse, Londe, Beverland, **Toward a Union-Find decoder for quantum LDPC codes** (2021), arXiv:2103.08049.
    https://arxiv.org/abs/2103.08049
19. Gu et al., **Decoding Quantum Tanner Codes** (IEEE Transactions on Information Theory 2023).
    https://doi.org/10.1109/TIT.2023.3267945
20. Higgott, Breuckmann, **Improved Single-Shot Decoding of Higher-Dimensional Hypergraph-Product Codes** (PRX Quantum 2023).
    https://doi.org/10.1103/PRXQuantum.4.020332
21. Wolanski, Barber, **Ambiguity Clustering: an accurate and efficient decoder for qLDPC codes** (2024), arXiv:2406.14527. Finite BB/qLDPC decoder targeting accuracy/latency tradeoffs.
    https://arxiv.org/abs/2406.14527
22. Hillmann et al., **Localized statistics decoding: A parallel decoding algorithm for quantum low-density parity-check codes** (Nature Communications 2025), arXiv:2406.18655. BP+LSD/local post-processing with parallelization advantages.
    https://arxiv.org/abs/2406.18655
23. **Decoding correlated errors in quantum LDPC codes** (Nature Communications 2026). Graph augmentation and iterative/min-sum decoding for correlated circuit-level errors, including FPGA-oriented latency evidence.
    https://doi.org/10.1038/s41467-026-70556-3
24. **An almost-linear time decoding algorithm for quantum LDPC codes under circuit-level noise** (npj Quantum Information 2026).
    https://doi.org/10.1038/s41534-026-01292-1
25. **Machine Learning Decoding of Circuit-Level Noise for Bivariate Bicycle Codes** (Quantum 2026).
    https://doi.org/10.22331/q-2026-06-30-2149

## Connectivity and hardware architecture

26. Tremblay, Delfosse, Beverland, **Constant-Overhead Quantum Error Correction with Thin Planar Connectivity** (PRL 2022). Decomposes qLDPC Tanner connectivity into a small number of planar layers and quantifies overhead under a stated noise regime.
    https://doi.org/10.1103/PhysRevLett.129.050504
27. Xu et al., **Constant-overhead fault-tolerant quantum computation with reconfigurable atom arrays** (Nature Physics 2024). Maps product qLDPC structure to atom movement and compares full overhead against surface code.
    https://doi.org/10.1038/s41567-024-02479-z
28. Poole et al., **Architecture for fast implementation of qLDPC codes with optimized Rydberg gates** (2024), arXiv:2404.18809. Hardware layout/communication study including BB codes.
    https://arxiv.org/abs/2404.18809
29. Pecorari et al., **High-rate quantum LDPC codes for long-range-connected neutral atom registers** (Nature Communications 2025).
    https://doi.org/10.1038/s41467-025-56255-5
30. Mathews et al., **Placing and routing quantum LDPC codes in multilayer superconducting hardware** (npj Quantum Information 2026). Explicit placement/routing studies for many qLDPC instances and multilayer hardware assumptions.
    https://doi.org/10.1038/s41534-026-01243-w
31. **Fusion-based implementation of qLDPC codes with quantum emitters** (npj Quantum Information 2026). Photonic/fusion-based route to nonlocal qLDPC checks.
    https://doi.org/10.1038/s41534-026-01233-y

## Logical computation, state preparation, and universal FTQC

32. **Fault-Tolerant Logical Clifford Gates from Code Automorphisms** (PRX Quantum 2025). Automorphism-based logical Clifford synthesis with qLDPC/BB examples.
    https://doi.org/10.1103/vf7v-cpq9
33. **Computing efficiently in QLDPC codes** (Nature Communications 2026). High-rate qLDPC computation with efficient logical Clifford operations and circuit-level analysis.
    https://doi.org/10.1038/s41467-026-73061-9
34. Menon et al., **Magic Tricycles: Efficient Magic-State Generation with Finite Block-Length Quantum LDPC Codes** (PRX 2026). qLDPC-like finite blocks supporting transversal non-Clifford structure for magic-state generation.
    https://doi.org/10.1103/ghhp-cytl
35. **HetEC: Architectures for Heterogeneous Quantum Error Correction Codes** (ASPLOS 2025). Motivates qLDPC storage combined with a complementary computation code when logical-operation mechanisms differ.
    https://research.ibm.com/publications/hetec-architectures-for-heterogeneous-quantum-error-correction-codes
36. **Fault-tolerant quantum computation with polylogarithmic time and constant space overheads** (Nature Physics 2025).
    https://doi.org/10.1038/s41567-025-03102-5
37. **Single-shot preparation of hypergraph product codes via dimension jump** (Quantum 2025). Constant-depth/single-shot-oriented HGP state-preparation result with stated extra spatial resources.
    https://doi.org/10.22331/q-2025-10-07-1879
38. **Bias-tailored single-shot quantum LDPC codes** (2025), arXiv:2507.02239.
    https://arxiv.org/abs/2507.02239
39. **Abelian Multi-Cycle Codes for Single-Shot Error Correction** (PRX Quantum 2026).
    https://doi.org/10.1103/mj28-925w

## Additional recent directions

40. **Quantum error correction near the coding theoretical bound** (npj Quantum Information 2025). High-rate qLDPC construction/decoding near coding bounds under its model.
    https://doi.org/10.1038/s41534-025-01090-1
41. **LDPC-cat codes for low-overhead quantum computing in 2D** (Nature Communications 2025). Hybrid bosonic/qLDPC route with different hardware assumptions than qubit-only qLDPC.
    https://doi.org/10.1038/s41467-025-56298-8
42. **Almost optimal geometrically local quantum LDPC codes in any dimension** (Nature Communications 2026). Clarifies locality/rate/distance tradeoffs for geometrically constrained qLDPC.
    https://doi.org/10.1038/s41467-026-69031-w

## Engineering conclusions carried into the workflow

- qLDPC names a broad family. Candidate selection records the exact finite code, not only the family.
- Positive/asymptotically constant encoding rate is a potential space advantage; total execution overhead also includes syndrome ancillas, routing/transport, logical-operation ancillas/factories, and the classical decoder.
- Low check weight means sparse Tanner incidence. It does not by itself provide 2D geometric locality.
- BB/generalized-bicycle codes currently provide unusually concrete finite-length engineering targets because published parity checks, syndrome circuits, decoders, layouts, and hardware demonstrations exist.
- BP+OSD is a useful generic baseline rather than a universal final decoder. BP+LSD/localized statistics, ambiguity clustering, correlated-error methods, Tanner/expander-specific decoders, and accelerated implementations occupy different accuracy/latency points.
- Code-capacity, phenomenological, and circuit-level results remain separate evidence classes.
- Memory success does not imply a universal logical ISA. Logical Clifford, non-Clifford, state-preparation, code-switching, and heterogeneous-code protocols are independently costed.
- Hardware connectivity determines whether the asymptotic/fixed-block qubit advantage survives execution. Long-range gates, movement, multilayer routing, photonic links, or another explicit mechanism must realize Tanner edges.
- Compare qLDPC and surface-code candidates under the same physical noise/timing model, logical workload, and failure target; preserve the Pareto frontier instead of applying a fixed overhead multiplier.
