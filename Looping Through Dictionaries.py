# Looping Through Dictionaries
Providers = {"Cardiologist" : "Heart", "pediatrics" : "childrens", "Ob-Gyn" : "gynecological", "chiropractic" : "Bone"}
for provider in Providers:
    print("providers specialities are : ", provider)
for treatment in Providers.values():
    print("Providers treats to : ", treatment)
for provider,treatment in Providers.items():
    print(f"provider specility is {provider} and they treats {treatment} issues")