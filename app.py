import streamlit as st
from utils import check_rumor_claim, extract_text_from_image

st.set_page_config(page_title="Rumor Detector", page_icon="🕵️‍♀️")

st.title("🕵️‍♀️ Rumor Detection System")
st.markdown("🔎 Enter any claim or rumor below and we’ll check if it's fact-checked by trusted sources.")

# User input
user_input = st.text_input("💬 Enter a claim:")

# Submit button
if st.button("🔍 Check Now"):
    if not user_input.strip():
        st.warning("Please enter a valid claim.")
    else:
        with st.spinner("Checking claim with Google Fact Check..."):
            results = check_rumor_claim(user_input)

        if not results:
            st.error("❌ No fact-checked result found for this claim.")
        else:
            st.success(f"✅ Found {len(results)} result(s). Scroll down to view.")

            for idx, claim in enumerate(results):
                st.markdown(f"### 🔹 Result {idx + 1}")
                st.write(f"**🗣️ Claim:** {claim.get('text', 'N/A')}")
                st.write(f"**👤 Claimant:** {claim.get('claimant', 'Unknown')}")
                st.write(f"**📅 Date:** {claim.get('claimDate', 'N/A')}")

                if claim.get("claimReview"):
                    review = claim["claimReview"][0]
                    st.write(f"**✅ Rating:** `{review.get('textualRating', 'N/A')}`")
                    st.markdown(f"**🔗 Source:** [{review.get('publisher', {}).get('name', 'Publisher')}]({review.get('url', '#')})")

                st.markdown("---")

uploaded_image = st.file_uploader("Upload an image to extract and fact-check", type=["png", "jpg", "jpeg"])

if uploaded_image is not None:
    with open("temp_uploaded_image.png", "wb") as f:
        f.write(uploaded_image.getbuffer())

    extracted_text = extract_text_from_image("temp_uploaded_image.png")
    st.text_area("Extracted Text", extracted_text)

    if st.button("Check Extracted Text"):
        results = check_rumor_claim(extracted_text)
        results(results)

