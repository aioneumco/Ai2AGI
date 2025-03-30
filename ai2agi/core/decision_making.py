class DecisionMaking:
    def __init__(self):
        pass

    def process_data(self, data):
        """Process environmental data and prepare it for decision-making."""
        print(f"Processing data: {data}")
        return data

    def decide(self, analysis):
        """Make a decision based on the processed data."""
        actions = []
        
        # Decision based on temperature
        if "temperature" in analysis:
            if analysis["temperature"] > 30:
                actions.append("Activate cooling system.")
            elif analysis["temperature"] < 15:
                actions.append("Activate heating system.")
        
        # Decision based on light levels
        if "light" in analysis:
            if analysis["light"] == "high":
                actions.append("Optimize energy usage.")
            elif analysis["light"] == "low":
                actions.append("Increase lighting.")
        
        # Decision based on humidity
        if "humidity" in analysis:
            if analysis["humidity"] > 80:
                actions.append("Activate dehumidifier.")
            elif analysis["humidity"] < 20:
                actions.append("Activate humidifier.")
        
        # If no actions are decided, return a default message
        if not actions:
            actions.append("No action needed.")
        
        return actions

# Example of using decision making with expanded factors
if __name__ == "__main__":
    decision_maker = DecisionMaking()
    
    # Example data with more factors
    data = {"temperature": 35, "light": "medium", "humidity": 85}
    analysis = decision_maker.process_data(data)
    
    actions = decision_maker.decide(analysis)
    
    # Output the actions that should be taken
    for action in actions:
        print(f"Action taken: {action}")
