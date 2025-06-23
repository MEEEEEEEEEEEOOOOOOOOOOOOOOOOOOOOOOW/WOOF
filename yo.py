import streamlit as st

def get_recommendations(soil_ph, soil_moisture, temperature, crop):
    recommendations = []

    # Soil pH advice
    if soil_ph < 6.0:
        recommendations.append("🌱 Soil is acidic. Consider adding lime to raise pH.")
    elif soil_ph > 7.5:
        recommendations.append("🌱 Soil is alkaline. Consider sulfur to lower pH.")
    else:
        recommendations.append("🌱 Soil pH is optimal for most crops.")

    # Soil moisture advice
    if soil_moisture < 30:
        recommendations.append("💧 Soil moisture is low. Increase irrigation.")
    elif soil_moisture > 70:
        recommendations.append("💧 Soil moisture is high. Improve drainage to avoid waterlogging.")
    else:
        recommendations.append("💧 Soil moisture is adequate.")

    # Temperature and crop specific advice
    crop = crop.lower()
    if crop == "tomato":
        if temperature < 15:
            recommendations.append("🌡️ Temperature is low for tomatoes. Use greenhouse or row covers.")
        elif temperature > 30:
            recommendations.append("🌡️ Temperature is high. Provide shade or irrigation to cool plants.")
        else:
            recommendations.append("🌡️ Temperature is suitable for tomatoes.")
    elif crop == "lettuce":
        if temperature > 24:
            recommendations.append("🌡️ Temperature is high for lettuce. Prefer cooler conditions.")
        elif temperature < 7:
            recommendations.append("🌡️ Temperature is low for lettuce. Protect from frost.")
        else:
            recommendations.append("🌡️ Temperature is suitable for lettuce.")
    elif crop == "corn":
        if temperature < 18:
            recommendations.append("🌡️ Temperature is low for corn. Growth may slow.")
        elif temperature > 35:
            recommendations.append("🌡️ Temperature is high for corn. Ensure adequate irrigation.")
        else:
            recommendations.append("🌡️ Temperature is suitable for corn.")
    elif crop == "wheat":
        if temperature < 10:
            recommendations.append("🌡️ Temperature is low for wheat. Growth may be delayed.")
        elif temperature > 25:
            recommendations.append("🌡️ Temperature is high for wheat. Monitor moisture carefully.")
        else:
            recommendations.append("🌡️ Temperature is suitable for wheat.")
    else:
        recommendations.append(f"🌡️ Crop '{crop}' is currently unsupported for detailed advice, but general tips still apply.")

    # Bonus tips based on combined factors
    if soil_ph < 5.5 and soil_moisture > 70:
        recommendations.append("⚠️ Warning: Acidic and overly moist soil can increase risk of root diseases.")

    if soil_moisture < 20 and temperature > 30:
        recommendations.append("⚠️ Warning: Dry and hot conditions may stress plants. Consider mulching and shading.")

    return recommendations

def main():
    st.set_page_config(page_title="Smart Crop Advisor", page_icon="🌾", layout="centered")
    st.title("🌱 Smart Crop Advisor")
    st.write("Get tailored recommendations to optimize your crop growth!")

    crops = ["Tomato", "Lettuce", "Corn", "Wheat", "Other"]

    with st.form("advisor_form"):
        soil_ph = st.slider("Soil pH", 3.0, 9.0, 6.5, 0.1)
        soil_moisture = st.slider("Soil Moisture (%)", 0, 100, 50)
        temperature = st.slider("Temperature (°C)", -10, 50, 22)
        crop = st.selectbox("Select Crop Type", crops)
        if crop == "Other":
            crop = st.text_input("Enter Crop Name", "")

        submitted = st.form_submit_button("Get Recommendations")

    if submitted:
        if not crop.strip():
            st.warning("Please enter a crop name.")
            return
        recommendations = get_recommendations(soil_ph, soil_moisture, temperature, crop)
        st.markdown("### Recommendations:")
        for rec in recommendations:
            st.info(rec)

if __name__ == "__main__":
    main()
