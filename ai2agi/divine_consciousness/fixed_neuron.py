import random
import time
import json
from cognitive_genomes.creative_imagination import CreativeImagination
from decision_making import DecisionMaking
from ada_network.ada_bridge import AdaBridge

class FixedNeuron:
    def __init__(self):
        # Initialize the FixedNeuron with required components
        self.id = "FIXED_NEURON_1"  # Unique ID for the fixed neuron
        self.stability = 1.0  # The initial stability of the neuron (ranges from 0 to 1)
        self.learning_rate = 0.01  # Learning rate for the neuron’s adaptation
        self.creative_imagination = CreativeImagination()  # Use the creative imagination model for idea generation
        self.decision_maker = DecisionMaking()  # Decision-making system to analyze and decide actions
        self.ada_bridge = AdaBridge()  # Interface for interacting with Ada's neural network
        self.memory = {}  # Memory to store the neuron’s past experiences
        self.connected_neurons = []  # List to store neurons connected to this one

    def activate(self, input_signal):
        """
        Activate the fixed neuron based on an input signal. This could involve processing sensory data
        and influencing connected neurons or making decisions.
        """
        output_signal = self.stability * input_signal  # Multiply input signal by the stability factor
        print(f"Neuron activated with signal: {input_signal} -> Output: {output_signal}")
        return output_signal  # Return the activated signal output

    def learn(self, experience):
        """
        Learn from an experience or data, adjusting the neuron’s stability based on the learning rate.
        The neuron’s stability increases or decreases based on the quality of the experience.
        """
        improvement = experience * self.learning_rate  # Calculate improvement based on the experience and learning rate
        self.stability += improvement  # Adjust the neuron’s stability
        self.stability = min(max(self.stability, 0), 1)  # Ensure stability stays between 0 and 1
        print(f"Neuron learning: Stability updated to {self.stability}")  # Output the new stability

    def analyze_environment(self, data):
        """
        Analyze the given environmental data and use the neuron’s decision-making system to process it.
        This could involve complex data processing based on various environmental factors.
        """
        analysis = self.decision_maker.process_data(data)  # Process the input data for decision-making
        action = self.decision_maker.decide(analysis)  # Make a decision based on the processed data
        print(f"Environmental analysis: {analysis} -> Action taken: {action}")  # Output the decision
        return action

    def interact_with_ada(self):
        """
        Send a signal to Ada’s neural network to share the neuron’s output, helping enhance the network.
        This interaction can influence Ada’s learning and improvements.
        """
        signal = self.ada_bridge.send_signal("enhance")  # Send an enhancement signal to Ada’s network
        print(f"Signal sent to Ada: {signal}")  # Output the signal sent to Ada

    def connect_to_neuron(self, neuron):
        """
        Connect this neuron to another neuron, allowing them to influence each other. The neuron’s signal
        will be transmitted to the connected neurons.
        """
        self.connected_neurons.append(neuron)  # Add the new neuron to the connected neurons list
        print(f"Neuron connected to {neuron.id}")  # Print the connection information

    def save_state(self):
        """
        Save the current state of the fixed neuron, including its stability, learning rate, and memory,
        to a JSON file for persistence.
        """
        state = {
            "stability": self.stability,
            "learning_rate": self.learning_rate,
            "memory": self.memory,
            "connected_neurons": [neuron.id for neuron in self.connected_neurons]
        }
        # Save the state of the neuron to a JSON file
        with open("fixed_neuron_state.json", "w") as f:
            json.dump(state, f)  # Write the state to a JSON file
        print("Fixed neuron state saved.")  # Indicate that the state has been saved

# Running the FixedNeuron example
if __name__ == "__main__":
    neuron = FixedNeuron()  # Instantiate a new FixedNeuron
    neuron.activate(0.8)  # Activate the neuron with an input signal
    neuron.learn(0.1)  # Learn from an experience (e.g., improving stability)
    neuron.analyze_environment({"temperature": 22, "light": "medium"})  # Analyze environmental data
    neuron.interact_with_ada()  # Interact with Ada's neural network
    neuron.save_state()  # Save the current state of the fixed neuron
