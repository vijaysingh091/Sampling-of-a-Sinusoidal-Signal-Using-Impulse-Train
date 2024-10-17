# Sampling-of-a-Sinusoidal-Signal-Using-Impulse-Train
 Signal Sampling with Impulse Train
This repository demonstrates the process of sampling a continuous-time signal using an impulse train. The code visualizes the original signal, the impulse train, and the sampled signal using matplotlib.

📁 Project Structure
bash
Copy code
├── sampling.py         # Main script to generate and plot sampled signals  
├── requirements.txt    # List of dependencies  
└── README.md           # Documentation of the project  
🚀 How It Works
Original Signal (m(t)):
A sine wave with frequency 
𝑓𝑚=5𝐻𝑧
fm=5Hz.

Impulse Train:
An impulse train (delta_n) is generated to sample the continuous signal at discrete points.

Sampled Signal (ms):
The product of the original signal and the impulse train, representing the sampled signal.

Plotting:
The code plots:

The original sine wave 
𝑚(𝑡)
The impulse train used for sampling
The sampled signal resulting from the multiplication of the sine wave and impulse train
📦 Dependencies
Install the required dependencies using the following command:

bash
Copy code
pip install -r requirements.txt
requirements.txt:

Copy code
numpy
matplotlib
📝 Usage
Clone the Repository:

bash
Copy code
git clone https://github.com/your-username/signal-sampling.git
cd signal-sampling
Run the Script:

bash
Copy code
python sampling.py
Expected Output:

A three-panel plot showing:
Original Signal 
𝑚(𝑡)

Impulse Train
Sampled Signal
📊 Code Overview
python
Copy code
# Parameters
fs = 1000       # Sampling frequency
T = 1 / fs      # Sampling period
t = np.arange(0, 1 + 0.001, 0.001)  # Time vector for original signal
fm = 5          # Frequency of the original sine wave
mt = np.sin(2 * np.pi * fm * t)  # Original signal

# Impulse Train Generation
n = np.arange(0, 1 + T, T)  # Time vector for impulse train
delta_n = np.zeros_like(t)  # Initialize impulse train
for i in range(len(n)):
    delta_n[np.abs(t - n[i]) < T/2] = 1  # Set impulses

# Sampled Signal
ms = mt * delta_n  # Element-wise product of signal and impulse train
🎯 Features
Demonstrates the basics of signal sampling using an impulse train.
Visualizes the original, sampled, and impulse signals using stem plots.
Modular code that can be easily adapted for different signals and sampling rates.
🛠 Troubleshooting
Matplotlib Warnings: If you encounter any warnings with stem plots, ensure you are using an up-to-date version of matplotlib.
Python Compatibility: Tested on Python 3.8+.
📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

💡 Contributing
Feel free to submit issues or pull requests if you have any suggestions for improvements.

👨‍💻 Author
Vijay Bhushan Singh
