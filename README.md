Bioinformatics Scripts Collection
This repository contains a set of Python scripts implementing core bioinformatics algorithms and utilities. The files are organized thematically and cover a broad range of topics, from sequence alignment to phylogenetic analysis and numerical sequence representations.

## Basic Sequence Processing
Scripts for fundamental operations on nucleotide and protein sequences:

basic_skills.py: Basic string-based sequence manipulations.

mutable_seq.py: Working with mutable sequence structures.

gc_content.py: Calculation of GC content.

protein_extract.py, exon_extract.py: Protein and exon extraction from sequences.

## Transcription, Translation, Indexing
read_frames.py: Reading frames for translation.

seq_mutations.py: Introduce or detect sequence mutations.

r_complement.py: Reverse complement of nucleotide sequences.

## File Parsing (FASTA, FASTQ, SAM/BAM, GenBank)
fasta_utils.py: Utilities for reading/writing FASTA files.

fastq_utils.py: Processing FASTQ sequencing reads.

sam_utils.py, sam_coverage.py: SAM file parsing and read coverage calculation.

gb_utils.py: Parsing GenBank files.

## Pattern Matching and Alignment (DP & MSP)
edit_distance_dp.py: Edit distance using dynamic programming.

lcs_dp.py: Longest common subsequence (LCS) via DP.

smith_waterman.py: Local alignment using the Smith-Waterman algorithm.

needleman_wunsch.py: Global alignment using Needleman-Wunsch.

msp_dp.py: Maximal segment pairs using dynamic programming.

## Pattern Search and Distance Metrics
match_matrix.py: Matching matrix computation for sequences.

p_distance.py: Proportional (p) distance between sequences.

distance_matrix.py: Pairwise distance matrix for multiple sequences.

## Antibiotic Decision Support
antibiotic_selection.py: Sort and classify patients based on need for antibiotic treatment.

## Utilities
align_utils.py, align_utils_local.py: Common utilities for alignment-related tasks.

counter_utils.py: Sequence counting or histogram utilities.

nt_to_bin.py, nt_to_binary.py, nt_to_num.py: Numerical conversion of nucleotides.

## Multiple Sequence Alignment and Consensus
clustal.py: Multiple sequence alignment using Clustal-like method.

consensus.py: Consensus sequence generation from aligned sequences.

## BLOSUM Matrix
blosum_builder.py: Build and compute BLOSUM substitution matrices.

## Phylogenetic Analysis
phylo_tree.py: Construct phylogenetic trees.

tree_to_newick.py: Convert tree structures into Newick format.

## Cumulative Phase Analysis
cumulative_phase.py: Compute cumulative phase for coding regions.

cumulative_phase_comparison.py: Compare phase data between samples.

cumulative_phase_graph.py: Graphical representation of phase shifts.

phase_coordinates.py: Coordinate handling for phase data.

## Numerical Representations & Analysis
seq_dft_analysis.py: Numerical analysis using Discrete Fourier Transform (DFT).

nt_to_num.py, nt_to_bin.py: Represent sequences numerically.
