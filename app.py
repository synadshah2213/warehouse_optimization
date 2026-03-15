import streamlit as st
import matplotlib.pyplot as plt
from after_deletion import setup_grid, find_optimized_route, run_simulation, calculate_distance
# Page config
st.set_page_config(page_title="Smart Warehouse Assistant", page_icon="🏭", layout="wide")

# Custom CSS
st.markdown("""
    <style>
    .main { background-color: #f5f7fa; }
    .block-container { padding: 2rem 3rem; }
    h1 { color: #1a1a2e; }
    .stButton>button {
        background-color: #e94560;
        color: white;
        border-radius: 8px;
        padding: 0.5rem 2rem;
        font-size: 16px;
        border: none;
        width: 100%;
    }
    .metric-box {
        background-color: white;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.title("🏭 Smart Warehouse Assistant")
st.markdown("**Optimize your warehouse picking routes with AI-powered simulation**")
st.markdown("---")

# Sidebar
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2037/2037457.png", width=80)
    st.title("⚙️ Configuration")
    st.markdown("---")

    st.subheader("📦 Select Items to Pick")
    order = st.multiselect("", 
    options=["item_A", "item_B", "item_C", "item_D", "item_E", "item_F", "item_G", "item_H"],
    default=["item_A", "item_B", "item_C", "item_D", "item_E"]
    )

    st.markdown("---")
    st.subheader("👷 Worker Starting Position")
    col1, col2 = st.columns(2)
    with col1:
        worker_row = st.number_input("Row", min_value=0, max_value=9, value=2)
    with col2:
        worker_col = st.number_input("Column", min_value=0, max_value=9, value=3)
    worker = (worker_row, worker_col)

    st.markdown("---")
    st.subheader("🚚 Dispatch Point")
    col3, col4 = st.columns(2)
    with col3:
        dispatch_row = st.number_input("Row ", min_value=0, max_value=9, value=0)
    with col4:
        dispatch_col = st.number_input("Column ", min_value=0, max_value=9, value=0)
    dispatch = (dispatch_row, dispatch_col)

    st.markdown("---")
    num_runs = st.slider("🔁 Number of Simulation Runs", min_value=1, max_value=50, value=10)

    run_button = st.button("🚀 Run Simulation")

# Main content
if run_button:
    if len(order) < 2:
        st.error("⚠️ Please select at least 2 items to run the simulation!")
    else:
        with st.spinner("Running simulation..."):
            grid = setup_grid()
            optimized_distance = find_optimized_route(order)
            random_distances, optimized_distances, improvements = run_simulation(order, optimized_distance)

        st.success("✅ Simulation Complete!")
        st.markdown("---")

        # Metrics
        st.subheader("📊 Simulation Results")
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("🏆 Optimized Distance", f"{optimized_distance} steps")
        col2.metric("🎲 Avg Random Distance", f"{sum(random_distances)/len(random_distances):.1f} steps")
        col3.metric("📈 Avg Improvement", f"{sum(improvements)/len(improvements):.1f}%")
        col4.metric("⭐ Best Improvement", f"{max(improvements):.1f}%")

        st.markdown("---")

        # Bar chart
        st.subheader("📉 Random vs Optimized Distance Per Run")
        fig2, ax2 = plt.subplots(figsize=(6, 3))
        runs = list(range(len(random_distances)))
        ax2.bar(runs, random_distances, width=0.4, label="Random Route", color="#e94560")
        ax2.bar([r + 0.4 for r in runs], optimized_distances, width=0.4, label="Optimized Route", color="#1a1a2e")
        ax2.set_xlabel("Simulation Run")
        ax2.set_ylabel("Distance (steps)")
        ax2.set_title("Random vs Optimized Distance")
        ax2.legend()
        st.pyplot(fig2)

        st.markdown("---")

        # Warehouse map
        st.subheader("🗺️ Warehouse Layout")
        item_positions = {
            "item_A": (4,5),
            "item_B": (6,2),
            "item_C": (8,8),
            "item_D": (10,12),
            "item_E": (12,4),
            "item_F": (14,9),
            "item_G": (3,7),
            "item_H": (7,11)
        }
        fig, ax = plt.subplots(figsize=(4, 4))
        ax.set_xlim(0, 15)
        ax.set_ylim(0, 15)
        ax.grid(True, alpha=0.3)
        ax.set_facecolor("#f5f7fa")
        ax.plot(dispatch[1], dispatch[0], marker="s", color="#e94560", markersize=15, label="Dispatch")
        ax.plot(worker[1], worker[0], marker="o", color="#1a1a2e", markersize=15, label="Worker")
        for item in order:
            pos = item_positions[item]
            ax.plot(pos[1], pos[0], marker="*", color="#f5a623", markersize=20, label=item)
        ax.legend(loc="upper right")
        ax.set_title("Warehouse Floor Map")
        st.pyplot(fig)
else:
    st.info("👈 Configure your settings in the sidebar and click **Run Simulation** to get started!")

