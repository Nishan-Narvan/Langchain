import langchain_helper as lch
import streamlit as st

st.title("👶Glorious Baby Name Generator")

user_trait_type = st.sidebar.selectbox("🌟Choose the Top personality Trait ?", ("Leader","Charming","Kind", "Religious","Cool","Intellectual", "Disciplined", "Nerd", "Cunning"))
user_gender_type = st.sidebar.selectbox("🚻Choose the Gender?", ( "Boy", "Girl", "Prefer to mention"))
user_religion_type = st.sidebar.selectbox("🚻Choose your religion:",("Hinduism","Islam","Sikhism","Christianity" ,"Buddhism","Judaism","Jainism"))

user_country_type=st.sidebar.text_area(label="Mention your country here",max_chars=15)

st.image("https://images.squarespace-cdn.com/content/v1/5c86a0e48dfc8cba05a27d38/1594402386254-JW6XD4VSHMJBH82T8VM0/Minneapolis+Newborn+Baby+Photography+Hands+by+Face+Lauren+B.+Photography+3.jpg")

# Generate Button
if st.button("✨ Generate Baby Name ✨"):
    if user_trait_type and user_gender_type and user_religion_type and user_country_type:
        with st.spinner("Generating a perfect name..."):
            response = lch.generate_baby_name(user_trait_type, user_gender_type, user_religion_type, user_country_type)
        st.subheader("🎉 Suggested Baby Names:")
        st.write(response)
    else:
        st.warning("⚠️ Please fill in all fields before generating a name!")
