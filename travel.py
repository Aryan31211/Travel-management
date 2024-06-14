import streamlit as st

def create_trip():
    """Prompts user for trip details and stores them in a dictionary"""
    st.subheader("Create New Trip")
    
    destination = st.text_input("Enter your destination:")
    start_date = st.date_input("Enter your start date (YYYY-MM-DD):")
    end_date = st.date_input("Enter your end date (YYYY-MM-DD):")
    transport = st.selectbox("Enter your preferred mode of transport:", ["Flight", "Train", "Bus", "Car"])
    accommodation = st.text_input("Enter your preferred accommodation (e.g., hotel name, rental):")
    
    if st.button("Save Trip"):
        return {
            "destination": destination,
            "start_date": start_date,
            "end_date": end_date,
            "transport": transport,
            "accommodation": accommodation
        }
    return None

def display_itinerary(trip):
    """Prints the user's trip itinerary in a formatted way"""
    st.subheader("Trip Itinerary")
    if trip:
        st.write("-" * 30)
        for key, value in trip.items():
            st.write(f"**{key.capitalize()}:** {value}")
        st.write("-" * 30)
    else:
        st.write("No trip data to display.")

def main():
    """Main program loop for user interaction"""
    st.title("Travel Itinerary Management")
    
    menu = ["Create New Trip", "View Existing Trip"]
    choice = st.sidebar.selectbox("Menu", menu)
    
    if choice == "Create New Trip":
        new_trip = create_trip()
        if new_trip:
            st.session_state['trip'] = new_trip
            display_itinerary(new_trip)
    elif choice == "View Existing Trip":
        if 'trip' in st.session_state:
            display_itinerary(st.session_state['trip'])
        else:
            st.write("No trip saved yet. Please create a new trip.")
    else:
        st.write("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
