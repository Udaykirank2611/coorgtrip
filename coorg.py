import streamlit as st
import datetime

def main():
    st.title("🌟 Mysore & Coorg Trip Plan 🏔️")
    st.write("Lets track our travel schedule and check off places as you visit them!")
    trip_start = datetime.datetime(2025, 3, 3, 19, 5)
    now = datetime.datetime.now()
    time_left = trip_start - now
    #st.subheader("⏳ Trip Countdown")
    st.subheader(f"Time left: {time_left.days} days, {time_left.seconds//3600} hours, {(time_left.seconds//60)%60} minutes")
    
    st.subheader("🛤️ Travel Schedule")
    
    # Departure from Hyderabad
    st.markdown("### 🚆 Departure from Hyderabad")
    st.markdown("**Train: Hyderabad to Mysore**  ")
    st.markdown("🚄 **12785 KCG MYS SF EXP**  ")
    st.markdown("🕒 Departure: **03-Mar-2025, 19:05**  ")
    st.markdown("🕒 Arrival: **04-Mar-2025, 10:20**  ")
    st.markdown("🎟️ Class: **3A**  | 💰 Cost: **₹1155**")
    
    # Day 1
    st.markdown("### 🏰 Day 1 - 4th March: Mysore Sightseeing")
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
        st.checkbox(f"✅ {place} - Entry Fee: ₹{fee}")
    
    # Travel to Coorg
    st.markdown("### 🚌 Travel: Mysore to Coorg")
    st.markdown("🚍 **KSRTC Bus (Trip Code: 2300CBTMRC)**  ")
    st.markdown("🕒 Departure: **05-Mar-2025, 04:15**  ")
    st.markdown("🕒 Arrival: **Mercara Madikeri**  ")
    st.markdown("💰 Cost: **₹160**")
    
    # Day 2
    st.markdown("### 🌳 Day 2 - 5th March: Coorg Adventure")
    coorg_day2_places = [
        ("Madikeri Fort", 0),
        ("Madikeri Palace", 0),
        ("Museum", 10),
        ("Raja Seat (Sunset)", 20),
        ("Raja’s Tomb", 10)
    ]
    for place, fee in coorg_day2_places:
        st.checkbox(f"✅ {place} - Entry Fee: ₹{fee}")
    
    # Day 3
    st.markdown("### ⛰️ Day 3 - 6th March: Peaks & Waterfalls")
    coorg_day3_places = [
        ("Mandalpatti Peak (Jeep Ride)", 1500),
        ("Abbey Falls", 10),
        ("Talakaveri Temple", 0),
        ("Bhagandeshwara Temple (Triveni Sangamam)", 0),
        ("Karike Waterfalls", 0),
        ("Omkareshwar Temple", 0),
    ]
    for place, fee in coorg_day3_places:
        st.checkbox(f"✅ {place} - Entry Fee: ₹{fee}")
    
    # Day 4
    st.markdown("### 🏛️ Day 4 - 7th March: Temples & Heritage")
    coorg_day4_places = [
        ("Dubare Elephant Camp", 50),
        ("River Rafting / Iruppu Falls", 0),
        ("Chiklihole Reservoir (closes at 4 PM)", 0),
        ("Nisargadhama", 20),
        ("Golden Temple (Namdroling Monastery)", 0),
        ("Harangi Dam", 0),
        ("Chocolate Shop (Coorg Special)", 0)
    ]
    for place, fee in coorg_day4_places:
        st.checkbox(f"✅ {place} - Entry Fee: ₹{fee}")
    
    # Travel Back to Mysore
    st.markdown("### 🚌 Travel: Coorg to Mysore")
    st.markdown("🚍 **KSRTC Bus (Trip Code: 0730MRCOTY)**  ")
    st.markdown("🕒 Departure: **08-Mar-2025, 07:30**  ")
    st.markdown("🕒 Arrival: **Mysore**  ")
    st.markdown("💰 Cost: **₹160**")
    
    # Travel Back to Hyderabad
    st.markdown("### 🚆 Travel: Mysore to Hyderabad")
    st.markdown("🚄 **Train 12786 KACHEGUDA EXP**  ")
    st.markdown("🕒 Departure: **08-Mar-2025, 15:15**  ")
    st.markdown("🕒 Arrival: **09-Mar-2025, 05:40**  ")
    st.markdown("🎟️ Class: **SL**  | 💰 Cost: **₹438**")
    st.markdown("### 📊 [Total Trip Expense Tracker](https://www.kittysplit.com/k/7YGBJEqe4yYoBI36H6CqXeCiibjl1uiY-2)")
    
    # Total Estimated Cost
    total_cost = 1155 + 438 + 160 + 160
    #st.markdown(f"### 💰 **Total Estimated Travel Cost: ₹{total_cost}**")
    
if __name__ == "__main__":
    main()
