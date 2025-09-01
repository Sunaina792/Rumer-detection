import os
import requests
from dotenv import load_dotenv
import pytesseract
from PIL import Image

# ✅ Load the environment variables from .env file
load_dotenv(dotenv_path=".env")

# ✅ Get the API key
API_KEY = os.getenv("API_KEY")

if not API_KEY:
    print("❌ Error: API key not found. Make sure it's set in the .env file.")
    exit()


# ✅ Function to check rumor claims using Google Fact Check Tools API
def check_rumor_claim(claim):
    url = f"https://factchecktools.googleapis.com/v1alpha1/claims:search?query={claim}&key={API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        results = response.json().get('claims', [])
        return results  # Always return a list
    else:
        print(f"❌ Error: {response.status_code} {response.text}")
        return []
def extract_text_from_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text.strip()

# Example usage
if __name__ == "__main__":
    test_claim = "COVID-19 vaccines contain microchips"
    results = check_rumor_claim(test_claim)

    if not results:
        print("No claims found.")
    else:
        for claim in results:
            print("✅ Claim:", claim.get("text"))
            print("🔗 Claimant:", claim.get("claimant"))
            print("📅 Claim date:", claim.get("claimDate"))
            print("🔍 Review rating:", claim['claimReview'][0]['textualRating'])
            print("🌐 Source:", claim['claimReview'][0]['url'])
            print("-" * 50)