import os
import json

base_path = r"d:\carehub\arrow_health_website\assets\Directory of Endrocrinologists in Bangladesh"
doctors = []

# Add Dr. Nahid Hasan manually as he is in assets directly
doctors.append({
    "name": "Dr. Nahid Hasan",
    "title": "MD, Board Certified Endocrinologist",
    "specialty": "Diabetes Care",
    "tagClass": "specialty-diabetes",
    "image": "./assets/nahid.jpeg",
    "description": "Specialist in metabolic health, glucose trend analysis, and custom care plans to balance blood sugars."
})

if os.path.exists(base_path):
    folders = [f for f in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, f))]
    for folder in sorted(folders):
        folder_path = os.path.join(base_path, folder)
        # Find the first image file
        img_file = None
        for file in os.listdir(folder_path):
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.webp', '.avif')):
                img_file = file
                break
        
        if img_file:
            img_path = f"./assets/Directory of Endrocrinologists in Bangladesh/{folder}/{img_file}"
        else:
            img_path = "./assets/nahid.jpeg" # Fallback
            
        # Clean doctor name and title
        name = folder
        title = "Endocrinologist"
        specialty = "Endocrinology"
        tagClass = "specialty-diabetes"
        
        # Adjust tags/specialties slightly to vary the cards
        if "Prof" in folder or "Professor" in folder:
            title = "Professor of Endocrinology"
            specialty = "Metabolic Health"
            tagClass = "specialty-nutrition"
        elif "Assoc" in folder:
            title = "Associate Professor, Endocrinology"
            specialty = "Hormone Therapy"
            tagClass = "specialty-physician"
            
        doctors.append({
            "name": name,
            "title": title,
            "specialty": specialty,
            "tagClass": tagClass,
            "image": img_path,
            "description": f"Specialist in endocrinology, diabetes care, and metabolic health management."
        })

with open("doctors_data.json", "w", encoding="utf-8") as f:
    json.dump(doctors, f, indent=2, ensure_ascii=False)
