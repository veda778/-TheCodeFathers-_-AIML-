from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Sample chatbot logic
def chatbot_response(user_message):
    # Replace this function with your chatbot's logic
    if user_message.lower() == "hello":
        return "Hi there! How can I help you?"
    else:
        return f"I'm not sure how to respond to: {user_message}"

# API endpoint to handle chatbot messages
@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()  # Get JSON data from POST request
    user_message = data.get('message', '')  # Extract the user message
    response = chatbot_response(user_message)  # Get the chatbot's response
    return jsonify({'reply': response})  # Return response as JSON

# Route to serve the frontend
@app.route('/')
def index():
    return render_template('index.html')  # Serve HTML file from /templates

if __name__ == '__main__':
    app.run(debug=True)  # Start the Flask server



@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()  # JSON payload from frontend
    user_message = data.get('message', '')  # Extract user input
    response = chatbot_response(user_message)  # Generate chatbot response
    return jsonify({'reply': response})  # Send response back to frontend


@app.route('/')
def index():
    return render_template('templates.html')


def chatbot_response(user_message):
    # Replace this with your chatbot's actual logic
    if "hello" in user_message.lower():
        return "Hi there! How can I assist you today?"
    return "I'm still learning. Could you rephrase that?"


from chatbot_logic import chatbot_response  # Import chatbot logic





