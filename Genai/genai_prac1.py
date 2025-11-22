import google.generativeai as genai
import json
import os

os.environ["GOOGLE_API_KEY"] = "key_"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

model = genai.GenerativeModel('gemini-2.5-flash')

# MOCK DB
flight_database = {
    "AI123": {
        "flight_number": "AI123",
        "departure_time": "08:00 AM",
        "destination": "Delhi",
        "status": "Delayed"
    },
    "AI456": {
        "flight_number": "AI456",
        "departure_time": "10:30 AM",
        "destination": "Mumbai",
        "status": "On Time"
    }
}

# INFO AGENT
def get_flight_info(flight_number: str) -> dict:
    flight_number = flight_number.upper().replace(" ", "")
    result = flight_database.get(flight_number)
    
    if result:
        return result
    else:
        return {"error": "Flight not found", "flight_number": flight_number}

def info_agent_request(flight_number: str) -> str:
    data = get_flight_info(flight_number)
    # dictionary to JSON string
    return json.dumps(data)


# QA AGENT
def qa_agent_respond(user_query: str) -> str:    
    extraction_prompt = f"""
    Extract the flight number from this query: "{user_query}".
    Return a JSON object with exactly one key: "flight_number".
    Flight number format is two letters followed by 1 to 4 digits (e.g., AI123).
    If none found, return: {{"flight_number": "NONE"}}
    """

    extraction_response = model.generate_content(
        extraction_prompt,
        generation_config={"response_mime_type": "application/json"}
    )

    flight_number = json.loads(extraction_response.text).get("flight_number", "NONE")
    
    if flight_number == "NONE":
        return json.dumps({"answer": "Could not identify a flight number."})
        
    # call info agent
    flight_data_json = info_agent_request(flight_number)
    
    final_prompt = f"""
    You are a helpful airline assistant.
    User Query: "{user_query}"
    Flight Data (JSON): {flight_data_json}
    
    Task: Answer the user's question based strictly on the Flight Data.
    Format: Return a JSON object with a single key "answer".
    Example: {{"answer": "Flight AI123 departs at..."}}
    """
    
    final_response = model.generate_content(
        final_prompt,
        generation_config={"response_mime_type": "application/json"}
    )
    
    return final_response.text

if __name__ == "__main__":
    print(" Airline Call Center System \n")

    query1 = "When does Flight AI123 depart?"
    print(f"User: {query1}")
    print(f"Agent: {qa_agent_respond(query1)}\n")

    query2 = "What is the status of AI456?"
    print(f"User: {query2}")
    print(f"Agent: {qa_agent_respond(query2)}\n")

    query3 = "Tell me about Flight AI999"
    print(f"User: {query3}")
    print(f"Agent: {qa_agent_respond(query3)}\n")
