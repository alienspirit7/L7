# Linear Regression Trend Finding Tool

A Python demonstration script that implements linear regression using a brute-force parameter search approach to find the best-fit line for randomly generated 2D data points.

## Overview

This educational tool generates synthetic data following a known linear relationship and then uses a brute-force optimization method to rediscover that relationship. It provides visual insights into how linear regression works by showing the search process and comparing multiple candidate solutions.

## Features

- **Synthetic Data Generation**: Creates 1000 data points following `y = 0.2x + 0.3 + noise`
- **Brute-Force Optimization**: Tests 10,000 random parameter combinations to find optimal fit
- **Multiple Visualizations**: 
  - Initial scatter plot of generated data
  - Best-fit line overlay
  - Comparison of top 10 performing lines
- **Performance Metrics**: Displays mean squared error for all candidate solutions

## Requirements

```
numpy>=1.20.0
matplotlib>=3.3.0
```

## Installation

1. Clone or download the script file `findTrend.py`
2. Install required dependencies:
   ```bash
   pip install numpy matplotlib
   ```

## Usage

### Basic Execution
```bash
python findTrend.py
```

### Jupyter Notebook
The script includes `@title` comments and is optimized for Jupyter notebook execution. Simply run each cell sequentially.

## Output

The script generates three main outputs:

### 1. Console Output
```
Pair (a, b) with minimum average error: a = 0.1987, b = 0.3012
Minimum average error: 0.0132
```

### 2. Visualizations
- **Plot 1**: Scatter plot of the 1000 generated data points
- **Plot 2**: Data points with the best-fit line overlaid in red
- **Plot 3**: Comparison showing the top 10 best-fit lines (best line highlighted in red)

## Technical Details

### Data Generation
- **Sample Size**: 1000 points
- **X-coordinates**: Uniform random distribution [0, 1]
- **Y-coordinates**: `y = 0.2x + 0.3 + noise` where noise ∈ [-0.2, 0.2]
- **Ground Truth**: Slope = 0.2, Intercept = 0.3

### Optimization Algorithm
- **Method**: Brute-force parameter search
- **Search Space**: 10,000 random (a, b) parameter pairs
- **Error Metric**: Mean Squared Error (MSE)
- **Formula**: `MSE = mean((y_actual - a*x - b)²)`

### Performance
- **Time Complexity**: O(n × m) where n = data points, m = parameter combinations
- **Space Complexity**: O(m) for storing all error values
- **Typical Runtime**: 2-5 seconds on modern hardware

## Educational Value

This script demonstrates several key concepts:

1. **Linear Regression Fundamentals**: Shows how optimal parameters minimize prediction error
2. **Optimization Visualization**: Makes the parameter search process tangible
3. **Error Landscape**: Illustrates how different parameters affect model performance
4. **Noise Impact**: Shows how random noise affects the fitting process

## Customization

### Modify Sample Size
```python
sample_size_n = 2000  # Change from default 1000
```

### Adjust Search Parameters
```python
n_pairs = 50000  # Increase from default 10,000 for better accuracy
```

### Change Noise Level
```python
random_noise = -0.1 + (0.1+0.1) * np.random.rand(sample_size_n)  # Reduce noise
```

## Limitations

- **Computational Inefficiency**: Brute-force approach is much slower than analytical solutions
- **Limited Scalability**: Not suitable for large datasets or high-dimensional problems
- **No Validation**: Lacks train/test split or cross-validation procedures
- **Fixed Search Space**: Parameter pairs are randomly sampled, not systematically explored

## Comparison with Standard Methods

This brute-force approach is primarily educational. In practice, linear regression uses:
- **Normal Equation**: Direct analytical solution
- **Gradient Descent**: Iterative optimization
- **Built-in Libraries**: sklearn.linear_model.LinearRegression

## Future Enhancements

- [ ] Add analytical solution comparison
- [ ] Implement gradient descent alternative
- [ ] Include R² coefficient calculation
- [ ] Add interactive parameter controls
- [ ] Support for real dataset import

## License

This code is provided for educational purposes. Feel free to modify and distribute.

## Contributing

Suggestions for improvements or educational enhancements are welcome. Please focus on maintaining the script's educational clarity while adding functionality.