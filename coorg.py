import streamlit as st

def main():
    st.title("Mysore & Coorg Trip Planner")
    st.write("Check off places as you visit them!")
    
    st.subheader("Travel Details (Chronological Order)")
    
    st.write("### Departure from Hyderabad")
    st.write("**Train: Hyderabad to Mysore**")
    st.write("Train 12785 KCG MYS SF EXP, Departure: 03-Mar-2025, 19:05, Arrival: 04-Mar-2025, 10:20, Class: 3A, Cost: ₹1155")
    
    st.write("### Day 1 - 4th March: Mysore Sightseeing")
    mysore_places = [
        ("Mysore Palace", 100),
        ("Jaganmohan Palace", 20),
        ("St. Philomena’s Church", 0),
        ("Chamundi Hill", 0),
        ("Sand Museum", 60),
        ("Brindavan Gardens", 50),
        ("Sweet Shops", 0),
        ("Karanji Lake", 50),
        ("Venugopalaswami Temple", 0)
    ]
    for place, fee in mysore_places:
        st.checkbox(f"{place} - Entry Fee: ₹{fee}")
    
    st.write("### Travel: Mysore to Coorg")
    st.write("**Bus: Mysore to Coorg**")
    st.write("KSRTC Bus (Trip Code: 2300CBTMRC), Departure: 05-Mar-2025, 04:15, Arrival: Mercara Madikeri, Cost: ₹160")
    
    st.write("### Day 2 - 5th March: Coorg Exploration")
    coorg_day2_places = [
        ("Dubare Elephant Camp", 50),
        ("River Rafting / Iruppu Falls", 0),
        ("Chiklihole Reservoir (closes at 4 PM)", 0),
        ("Nisargadhama", 20),
        ("Golden Temple (Namdroling Monastery)", 0),
        ("Harangi Dam", 0)
    ]
    for place, fee in coorg_day2_places:
        st.checkbox(f"{place} - Entry Fee: ₹{fee}")
    
    st.write("### Day 3 - 6th March: Coorg Peaks & Falls")
    coorg_day3_places = [
        ("Mandalpatti Peak (Jeep Ride)", 1500),
        ("Abbey Falls", 10),
        ("Omkareshwar Temple", 0),
        ("Raja Seat (Sunset)", 20)
    ]
    for place, fee in coorg_day3_places:
        st.checkbox(f"{place} - Entry Fee: ₹{fee}")
    
    st.write("### Day 4 - 7th March: Coorg Temples & Heritage")
    coorg_day4_places = [
        ("Talakaveri Temple", 0),
        ("Bhagandeshwara Temple (Triveni Sangamam)", 0),
        ("Karike Waterfalls", 0),
        ("Madikeri Fort", 0),
        ("Madikeri Palace", 0),
        ("Museum", 10),
        ("Raja’s Tomb", 10),
        ("Chocolate Shop (Coorg Special)", 0)
    ]
    for place, fee in coorg_day4_places:
        st.checkbox(f"{place} - Entry Fee: ₹{fee}")
    
    st.write("### Travel: Coorg to Mysore")
    st.write("**Bus: Coorg to Mysore**")
    st.write("KSRTC Bus (Trip Code: 0730MRCOTY), Departure: 08-Mar-2025, 07:30, Arrival: Mysore, Cost: ₹160")
    
    st.write("### Travel: Mysore to Hyderabad")
    st.write("**Train: Mysore to Hyderabad**")
    st.write("Train 12786 KACHEGUDA EXP, Departure: 08-Mar-2025, 15:15, Arrival: 09-Mar-2025, 05:40, Class: SL, Cost: ₹438")
    
if __name__ == "__main__":
    main()
