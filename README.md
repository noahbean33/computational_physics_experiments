# Computational Physics Experiments

A collection of computational physics experiments and simulations implemented in Python.

## Repository Structure

```
computational_physics_experiments/
├── data/                  # Data files (input/output)
├── docs/                  # Documentation
├── notebooks/             # Jupyter notebooks organized by topic
│   ├── cellular_automata/
│   ├── classical_mechanics/
│   ├── computational_methods/
│   ├── electromagnetism/
│   ├── general_relativity/
│   ├── quantum_mechanics/
│   └── misc/
├── examples/
│   ├── scripts/           # Standalone Python scripts
│   └── misc/              # Miscellaneous files
├── src/                   # Source code (Python modules)
│   ├── utils/             # Utility functions
│   └── visualization/     # Visualization helpers
├── tests/                 # Unit tests
├── .gitignore             # Git ignore file
├── requirements.txt       # Python dependencies
└── setup.py               # Package installation
```

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/computational_physics_experiments.git
   cd computational_physics_experiments
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   # source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Install the package in development mode:
   ```bash
   pip install -e .
   ```

5. Run tests to verify the installation:
   ```bash
   PYTHONPATH=. pytest tests/
   ```

6. Launch Jupyter Lab/Notebook:
   ```bash
   jupyter lab
   # or
   jupyter notebook
   ```

## Usage

- Each experiment is contained in its own Jupyter notebook in the `notebooks/` directory.
- Reusable code and utilities are in the `src/` directory.
- Data files should be stored in the `data/` directory.
- Standalone Python scripts have been moved to the `examples/scripts/` directory,
  with additional miscellaneous files in `examples/misc/`.

## Topics Covered

- [ ] Quantum Mechanics
- [ ] Statistical Mechanics
- [ ] Fluid Dynamics
- [ ] Electromagnetism
- [ ] Classical Mechanics
- [ ] Computational Methods

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
