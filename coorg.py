import streamlit as st
import datetime

def main():
    st.title("🌟 Mysore & Coorg Trip Plan 🏔️")
    st.write("Let's track our travel schedule and check off places as you visit them!")
    trip_start = datetime.datetime(2025, 3, 3, 19, 5)
    now = datetime.datetime.now()
    time_left = trip_start - now
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
        ("Mysore Palace 11:50AM", 100),
        ("Jaganmohan Palace 12:50PM", 20),
        ("St. Philomena’s Church 3:00PM", 0),
        ("Karanji Lake 4:00PM", 50),
        ("Sand Museum 5:15PM", 60),
        ("Venugopalaswami Temple 6:40PM", 0),
        ("Brindavan Gardens 7:30PM", 50),
    ]
    for place, fee in mysore_places:
        st.checkbox(f"✅ {place} - Entry Fee: ₹{fee}")
    
    # Day 2 - Chamundi Hill and Travel to Coorg
    st.markdown("### 🌄 Day 2 - 5th March: Chamundi Hill & Travel to Coorg")
    st.checkbox("✅ Chamundi Hill (Sunrise at 6:30AM) - Entry Fee: ₹0")
    
    st.markdown("### 🚌 Travel: Mysore to Coorg")
    st.markdown("🚍 **KSRTC Bus (Trip Code: 0829MYSMNG)**  ")
    st.markdown("🕒 Departure: **05-Mar-2025, 08:29**  ")
    st.markdown("🕒 Arrival: **Mercara Madikeri, 11:29**  ")
    st.markdown("💰 Cost: **₹160**")
    
    # Hotel Check-in
    st.markdown("### 🏨 Hotel Check-in")
    st.markdown("🏠 **Treebo Elite Plaza**  ")
    st.markdown("📍 **700 Mtrs From Madikeri Fort, No 14# Race course road Near LIC Office, Coorg**")
    st.markdown("📅 **Check-in:** 5th March 2025, 12:00 PM  ")
    st.markdown("📅 **Check-out:** 8th March 2025, 11:00 AM  ")
    st.markdown("📞 **Contact:** 9731152789, 8277234040  ")
    st.markdown("💰 **Cost:** ₹11800")
    
    # Coorg Adventure
    st.markdown("### 🌳 Coorg Adventure - 5th March")
    coorg_day2_places = [
        ("Madikeri Fort 1:30PM", 0),
        ("Madikeri Palace 2:30PM", 0),
        ("Raja’s Tomb 3:30PM", 10),
        ("Museum 4:30PM", 10),
        ("Raja Seat (Sunset) 5:30PM", 20)
    ]
    for place, fee in coorg_day2_places:
        st.checkbox(f"✅ {place} - Entry Fee: ₹{fee}")
    
    # Day 3
    st.markdown("### ⛰️ Day 3 - 6th March: Peaks & Waterfalls")
    coorg_day3_places = [
        ("Mandalpatti Peak (Jeep Ride) 5:00AM", 3700),
        ("Abbey Falls 10:00AM", 10),
        ("Talakaveri Temple 11:50AM", 0),
        ("Bhagandeshwara Temple (Triveni Sangamam) 1:30PM", 0),
        ("Karike Waterfalls 3:30PM", 0),
        ("Omkareshwar Temple 5:30PM", 0)
    ]
    for place, fee in coorg_day3_places:
        st.checkbox(f"✅ {place} - Entry Fee: ₹{fee}")
    
    # Day 4
    st.markdown("### 🏛️ Day 4 - 7th March: Temples & Heritage")
    coorg_day4_places = [
        ("Dubare Elephant Camp 8:30AM", 50),
        ("River Rafting / Iruppu Falls 10:30AM", 0),
        ("Coffee plantation 12:30PM", 0),
        ("Nisargadhama 2:00PM", 20),
        ("Golden Temple (Namdroling Monastery) 5:00PM", 0),
        ("Chocolate Shop (Coorg Special) 7:30PM", 0),
        ("Harangi Dam", 0),
        ("Chiklihole Reservoir (closes at 4 PM)", 0)
    ]
    for place, fee in coorg_day4_places:
        st.checkbox(f"✅ {place} - Entry Fee: ₹{fee}")
    
    # Travel Back to Mysore
    st.markdown("### 🚌 Travel: Coorg to Mysore")
    st.markdown("🚍 **KSRTC Bus (Trip Code: 0730MRCOTY)**  ")
    st.markdown("🕒 Departure: **08-Mar-2025, 07:30**  ")
    st.markdown("🕒 Arrival: **Mysore** 11:00AM")
    st.markdown("💰 Cost: **₹160**")
    
    st.markdown("### 🏛️ Day 5 - 8th March: The Return")
    st.checkbox("✅ Sweet Shops - Entry Fee: ₹0")
    
    # Travel Back to Hyderabad
    st.markdown("### 🚆 Travel: Mysore to Hyderabad")
    st.markdown("🚄 **Train 12786 KACHEGUDA EXP**  ")
    st.markdown("🕒 Departure: **08-Mar-2025, 15:15**  ")
    st.markdown("🕒 Arrival: **09-Mar-2025, 05:40**  ")
    st.markdown("🎟️ Class: **SL**  | 💰 Cost: **₹438**")
    st.markdown("### 📊 [Total Trip Expense Tracker](https://www.kittysplit.com/k/7YGBJEqe4yYoBI36H6CqXeCiibjl1uiY-2)")

if __name__ == "__main__":
    main()
