import tensorflow as tf

"""
Usage:
    python variable_example.py
"""

sess = tf.InteractiveSession()


raw_data = [1., 2., 8., -1, 0, 5.5, 7, 13]

spike = tf.Variable(False)
spike.initializer.run()

for i in range(1, len(raw_data)):
    if raw_data[i] - raw_data[i - 1] > 5:
        updater = tf.assign(spike, True)
        updater.eval()
    else:
        tf.assign(spike, False).eval()
    print("Spike", spike.eval())


