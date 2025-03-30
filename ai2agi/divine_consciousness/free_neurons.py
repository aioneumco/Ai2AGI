import random
import time
import json
from cognitive_genomes.creative_imagination import CreativeImagination
from decision_making import DecisionMaking
from ada_network.ada_bridge import AdaBridge

class FreeNeuron:
    def __init__(self):
        # Initialize the FreeNeuron with essential components
        self.id = f"FREE_NEURON_{random.randint(1, 1000)}"  # Assign a unique ID to the neuron
        self.stability = random.uniform(0.5, 1.0)  # Stability ranges between 0 and 1
        self.learning_rate = random.uniform(0.01, 0.1)  # Learning rate (random for diversity)
        self.creative_imagination = CreativeImagination()  # Use the creative imagination model
        self.decision_maker = DecisionMaking()  # Decision-making system to process environmental inputs
        self.ada_bridge = AdaBridge()  # Interface to Ada’s network to send and receive signals
        self.memory = {}  # Memory storage for this free neuron
        self.connected_neurons = []  # List to store neurons connected to this one

    def activate(self, input_signal):
        """
        Simulate the activation of the neuron. This can be done based on an input signal, which is
        processed and then propagated to connected neurons or used to influence decision-making.
        """
        output_signal = self.stability * input_signal  # The output depends on the neuron’s stability
        print(f"Neuron activated with input signal {input_signal} -> Output: {output_signal}")
        return output_signal  # Return the processed output signal

    def learn(self, experience):
        """
        Simulate the learning process of the neuron. The neuron adjusts its stability based on the given
        experience, increasing or decreasing it depending on the quality of the experience.
        """
        # The experience might either improve or reduce the stability of the neuron
        improvement = experience * self.learning_rate  # Learning is based on the experience and learning rate
        self.stability += improvement  # Update the neuron’s stability
        self.stability = min(max(self.stability, 0), 1)  # Ensure stability is always between 0 and 1
        print(f"Neuron learning: Stability updated to {self.stability}")  # Output updated stability

    def analyze_environment(self, data):
        """
        Analyze environmental data and make decisions based on it. This method uses the decision-making system
        to process the input and output a decision or action based on environmental input.
        """
        analysis = self.decision_maker.process_data(data)  # Analyze data through the decision-making system
        action = self.decision_maker.decide(analysis)  # Make a decision based on the analysis
        print(f"Environmental analysis: {analysis} -> Action: {action}")  # Output decision
        return action  # Return the chosen action based on the environmental analysis

    def interact_with_ada(self):
        """
        Interact with Ada’s network by sending signals to it. This could be for various purposes such as
        enhancing the neural network or sharing processed information.
        """
        signal = self.ada_bridge.send_signal("enhance")  # Send an enhancement signal to Ada
        print(f"Signal sent to Ada: {signal}")  # Output the enhancement signal sent to Ada

    def connect_to_neuron(self, neuron):
        """
        Connect this neuron to another neuron, allowing them to influence each other by transmitting signals
        between them.
        """
        self.connected_neurons.append(neuron)  # Add the connected neuron to the list of connected neurons
        print(f"Neuron connected to {neuron.id}")  # Output connection details

    def save_state(self):
        """
        Save the current state of the neuron, including its stability, learning rate, memory, and connected neurons,
        to a JSON file for persistence across sessions.
        """
        state = {
            "stability": self.stability,
            "learning_rate": self.learning_rate,
            "memory": self.memory,
            "connected_neurons": [neuron.id for neuron in self.connected_neurons]
        }
        # Save the state of the neuron to a JSON file
        with open("free_neuron_state.json", "w") as f:
            json.dump(state, f)  # Write the neuron’s state to a JSON file
        print("Free neuron state saved.")  # Indicate the state has been saved successfully

# Running the FreeNeuron example
if __name__ == "__main__":
    neuron = FreeNeuron()  # Instantiate the FreeNeuron
    neuron.activate(0.5)  # Activate the neuron with an example input signal
    neuron.learn(0.2)  # Simulate learning from an experience, adjusting stability
    neuron.analyze_environment({"temperature": 25, "light": "high"})  # Analyze environmental data
    neuron.interact_with_ada()  # Send a signal to Ada for enhancement
    neuron.save_state()  # Save the current state of the neuron to a JSON file
