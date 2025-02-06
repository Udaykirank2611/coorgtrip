import streamlit as st

def main():
    st.title("Mysore & Coorg Trip Planner")
    st.write("Check off places as you visit them!")
    
    st.subheader("Travel Details")
    st.write("### Train Details")
    st.write("**Hyderabad to Mysore**: Train 12785 KCG MYS SF EXP, Departure: 03-Mar-2025, 19:05, Arrival: 04-Mar-2025, 10:20, Class: 3A")
    st.write("**Mysore to Hyderabad**: Train 12786 KACHEGUDA EXP, Departure: 08-Mar-2025, 15:15, Arrival: 09-Mar-2025, 05:40, Class: SL")
    
    st.write("### Bus Details")
    st.write("**Mysore to Coorg**: KSRTC Bus (Trip Code: 2300CBTMRC), Departure: 05-Mar-2025, 04:15, Arrival: Mercara Madikeri")
    st.write("**Coorg to Mysore**: KSRTC Bus (Trip Code: 0730MRCOTY), Departure: 08-Mar-2025, 07:30, Arrival: Mysore")
    
    days = {
        "Day 1 & 5 - Mysore": [
            ("Mysore Palace", 100),
            ("Jaganmohan Palace", 20),
            ("St. Philomena’s Church", 0),
            ("Chamundi Hill", 0),
            ("Sand Museum", 60),
            ("Brindavan Gardens", 50),
            ("Sweet Shops", 0),
            ("Karanji Lake", 50),
            ("Venugopalaswami Temple", 0)
        ],
        "Day 2 - Coorg": [
            ("Dubare Elephant Camp", 50),
            ("River Rafting / Iruppu Falls", 0),
            ("Chiklihole Reservoir", 0),
            ("Nisargadhama", 20),
            ("Golden Temple (Namdroling Monastery)", 0),
            ("Harangi Dam", 0)
        ],
        "Day 3 - Coorg": [
            ("Mandalpatti Peak (Jeep Ride)", 1500),
            ("Abbey Falls", 10),
            ("Omkareshwar Temple", 0),
            ("Raja Seat (Sunset)", 20)
        ],
        "Day 4 - Coorg": [
            ("Talakaveri Temple", 0),
            ("Bhagandeshwara Temple (Triveni Sangamam)", 0),
            ("Karike Waterfalls", 0),
            ("Madikeri Fort", 0),
            ("Madikeri Palace", 0),
            ("Museum", 10),
            ("Raja’s Tomb", 10),
            ("Chocolate Shop (Coorg Special)", 0)
        ]
    }
    
    for day, places in days.items():
        st.subheader(day)
        for place, fee in places:
            st.checkbox(f"{place} - Entry Fee: ₹{fee}")

if __name__ == "__main__":
    main()
