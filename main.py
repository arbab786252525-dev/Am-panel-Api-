import json
import urllib.request

# === 1. CONFIGURATION ===
api_url = "https://worldpanel24.com/api/v2"
api_key = "3ed238f9f8402cf6915876587888f760622698ef"

# === 2. JSON PAYLOAD & HEADERS ===
post_data = {"key": api_key, "action": "services"}

# Data ko JSON string mein convert kar rahe hain kyunki API JSON allow karti hai
json_data = json.dumps(post_data).encode("utf-8")

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like"
        " Gecko) Chrome/120.0.0.0 Safari/537.36"
    ),
    "Content-Type": "application/json",
}

try:
  req = urllib.request.Request(
      api_url, data=json_data, headers=headers, method="POST"
  )
  with urllib.request.urlopen(req) as response:
    result = response.read().decode("utf-8")
    services = json.loads(result)

    # === 3. PROCESS & DISPLAY SERVICES WITH 50 PKR MARKUP ===
    if isinstance(services, list):
      print("=== AM PANEL AGENCY - Live Services & Rates ===\n")
      for service in services:
        service_id = service.get("service")
        name = service.get("name")
        provider_rate = float(service.get("rate", 0))  # Base rate

        # Automatic 50 PKR profit markup added
        my_final_rate = provider_rate + 50

        min_val = service.get("min")
        max_val = service.get("max")

        print(f"Service ID: {service_id} | {name}")
        print(
            f"Final Selling Price: {my_final_rate} PKR (Min: {min_val} / Max:"
            f" {max_val})\n"
        )
    else:
      print("API Response mein masla hai:", services)

except Exception as e:
  print("Connection error aa gaya:", e)
