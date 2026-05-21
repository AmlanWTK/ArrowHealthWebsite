const fs = require('fs');
const path = require('path');

const basePath = 'd:\\carehub\\arrow_health_website\\assets\\Directory of Endrocrinologists in Bangladesh';
const doctors = [];

// Add Dr. Nahid Hasan manually
doctors.push({
  name: "Dr. Nahid Hasan",
  title: "MD, Board Certified Endocrinologist",
  specialty: "Diabetes Care",
  tagClass: "specialty-diabetes",
  image: "./assets/nahid.jpeg",
  description: "Specialist in metabolic health, glucose trend analysis, and custom care plans to balance blood sugars."
});

if (fs.existsSync(basePath)) {
  const folders = fs.readdirSync(basePath).filter(f => fs.statSync(path.join(basePath, f)).isDirectory());
  
  folders.forEach(folder => {
    const folderPath = path.join(basePath, folder);
    const files = fs.readdirSync(folderPath);
    const imgFile = files.find(file => /\.(png|jpe?g|webp|avif)$/i.test(file));
    
    const imgPath = imgFile 
      ? `./assets/Directory of Endrocrinologists in Bangladesh/${folder}/${imgFile}`
      : './assets/nahid.jpeg';
      
    let title = "Endocrinologist";
    let specialty = "Endocrinology";
    let tagClass = "specialty-diabetes";
    
    if (folder.includes("Prof") || folder.includes("Professor")) {
      title = "Professor of Endocrinology";
      specialty = "Metabolic Health";
      tagClass = "specialty-nutrition";
    } else if (folder.includes("Assoc")) {
      title = "Associate Professor, Endocrinology";
      specialty = "Hormone Therapy";
      tagClass = "specialty-physician";
    }
    
    doctors.push({
      name: folder,
      title: title,
      specialty: specialty,
      tagClass: tagClass,
      image: imgPath,
      description: `Specialist in endocrinology, diabetes care, and metabolic health management.`
    });
  });
}

fs.writeFileSync('doctors_data.json', JSON.stringify(doctors, null, 2), 'utf-8');
console.log(`Successfully generated data for ${doctors.length} doctors.`);
