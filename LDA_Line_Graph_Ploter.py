import matplotlib.pyplot as plt

# Data
bit_lengths = ['last_1_bit', 'last_2_bit', 'last_4_bit', 'last_8_bit']
trace_counts = [100, 500, 1000, 5000, 10000, 50000, 100000]

data = {
    'last_1_bit': {
        'train_acc': [0.6875, 0.795, 0.88125, 0.99875, 1.0, 1.0, 1.0],
        'test_acc': [0.65, 0.72, 0.875, 1.0, 0.9995, 1.0, 1.0],
    },
    'last_2_bit': {
        'train_acc': [0.5375, 0.635, 0.7275, 0.92175, 0.9855, 0.9992, 0.9935875],
        'test_acc': [0.25, 0.41, 0.555, 0.756, 0.815, 0.8965, 0.95095],
    },
    'last_4_bit': {
        'train_acc': [0.4625, 0.6825, 0.74125, 0.94625, 0.997875, 1.0, 0.9959125],
        'test_acc': [0.05, 0.15, 0.14, 0.391, 0.451, 0.6841, 0.84815],
    },
    'last_8_bit': {
        'train_acc': [0.3, 0.9775, 0.9975, 1.0, 1.0, 1.0, 1.0],
        'test_acc': [0.05, 0.01, 0.01, 0.047, 0.102, 0.3431, 0.57455],
    },
}

# Training Accuracy Plot
plt.figure(figsize=(10, 6))

for key in bit_lengths:
    plt.plot(trace_counts, data[key]['train_acc'], marker='o', label=key)

plt.xscale('log')
plt.xlabel('Trace Count (log scale)')
plt.ylabel('Training Accuracy')
plt.title('Training Accuracy vs Trace Count')
plt.grid(True, which="both", ls="--")
plt.legend()
plt.tight_layout()
plt.savefig('training_accuracy_plot.png', dpi=300)
plt.show()

# Testing Accuracy Plot
plt.figure(figsize=(10, 6))

for key in bit_lengths:
    plt.plot(trace_counts, data[key]['test_acc'], marker='x', linestyle='--', label=key)

plt.xscale('log')
plt.xlabel('Trace Count (log scale)')
plt.ylabel('Testing Accuracy')
plt.title('Testing Accuracy vs Trace Count')
plt.grid(True, which="both", ls="--")
plt.legend()
plt.tight_layout()
plt.savefig('testing_accuracy_plot.png', dpi=300)
plt.show()
