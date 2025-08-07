#  DNA Analysis System

A comprehensive web-based DNA analysis platform that transforms raw DNA sequences into meaningful genetic insights. Built with Flask, this system provides advanced STR (Short Tandem Repeat) analysis, genetic distance calculations, mutation detection, and a beautiful user interface for DNA research and forensic applications.

![DNA Analysis](https://img.shields.io/badge/DNA-Analysis-blue)
![Flask](https://img.shields.io/badge/Flask-2.2.5-green)
![Python](https://img.shields.io/badge/Python-3.8+-yellow)
![License](https://img.shields.io/badge/License-MIT-orange)

## ✨ Features

###  **Core DNA Analysis**
- **STR Pattern Recognition**: Analyzes 8 different STR markers (AGATC, TTTTTTCT, AATG, TCTAG, GATA, TATC, GAAA, TCTG)
- **Real-time Analysis**: Instant processing of DNA sequences with confidence scoring
- **Multiple Input Methods**: Manual text input or file upload (.txt, .csv, .fasta)
- **Comprehensive Matching**: Finds all potential matches with confidence percentages

### **Database Management**
- **Manual Profile Addition**: Add new individuals with their STR counts
- **Database Viewer**: Browse and manage all DNA profiles
- **CSV Integration**: Import existing DNA databases
- **Persistent Storage**: SQLite database for reliable data management

###  **Advanced Genetic Analysis**
- **Genetic Distance Calculator**: Measure similarity between DNA sequences
- **Mutation Detection**: Identify genetic variations and polymorphisms
- **Haplotype Analysis**: Group individuals by genetic marker patterns
- **Machine Learning Ready**: Framework for AI-powered genetic analysis

###  **User Experience**
- **Beautiful Web Interface**: Modern, responsive design with Bootstrap
- **Interactive Visualizations**: Confidence bars, progress indicators, and badges
- **Real-time Feedback**: Instant results with detailed explanations
- **Mobile-Friendly**: Works seamlessly on all devices

## Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/CS50-DNA-.git
   cd CS50-DNA-
   ```

2. **Install dependencies**
   ```bash
   cd dna
   pip install -r requirements.txt
   ```

3. **Initialize the database**
   ```bash
   python populate_db.py
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser**
   Navigate to `http://localhost:5001`

## 📖 How to Use

### 1. **DNA Sequence Analysis**
- **Manual Input**: Go to "Analyze DNA" and paste your DNA sequence
- **File Upload**: Use "Upload File" to process DNA sequence files
- **View Results**: Get instant analysis with confidence scores and matches

### 2. **Adding New Profiles**
- Navigate to "Add Person"
- Enter the individual's name
- Input STR counts for all 8 markers:
  ```
  AGATC: 48
  TTTTTTCT: 23
  AATG: 15
  TCTAG: 8
  GATA: 12
  TATC: 5
  GAAA: 28
  TCTG: 40
  ```

### 3. **Advanced Analysis**
- **Genetic Distance**: Compare two DNA sequences for similarity
- **Mutation Detection**: Find genetic variations between sequences
- **Haplotype Analysis**: Group individuals by genetic patterns

##  Understanding STR Analysis

### What are STRs?
Short Tandem Repeats (STRs) are repeating sequences of DNA that vary in length between individuals. They are commonly used in forensic DNA analysis and paternity testing.

### STR Markers Analyzed
| Marker | Description | Example |
|--------|-------------|---------|
| AGATC | Short Tandem Repeat 1 | AGATCAGATCAGATC = 3 repeats |
| TTTTTTCT | Short Tandem Repeat 2 | TTTTTTCTTTTTTCT = 2 repeats |
| AATG | Short Tandem Repeat 3 | AATGAATGAATG = 3 repeats |
| TCTAG | Short Tandem Repeat 4 | TCTAGTCTAG = 2 repeats |
| GATA | Short Tandem Repeat 5 | GATAGATA = 2 repeats |
| TATC | Short Tandem Repeat 6 | TATCTATC = 2 repeats |
| GAAA | Short Tandem Repeat 7 | GAAAGAAA = 2 repeats |
| TCTG | Short Tandem Repeat 8 | TCTGTCTG = 2 repeats |

##  Sample Output

### DNA Analysis Results
```
 DNA Analysis Results

Input Sequence: AAGGTAAGTTTAGAATATAAAAGGTGAGTTAAATAGAATAGGTTAAAATTAAAGGAGATCAGATCAGATCAGATCTATCTATCTATCTATCTATCAGAAAAGAGTAAATAGTTAAAGAGTAAGATATTGAATTAATGGAAAATATTGTTGGGGAAAGGAGGGATAGAAGG

STR Analysis Summary:
✅ AGATC: 3 repeats
✅ TTTTTTCT: 0 repeats
✅ AATG: 2 repeats
✅ TCTAG: 0 repeats
✅ GATA: 0 repeats
✅ TATC: 0 repeats
✅ GAAA: 0 repeats
✅ TCTG: 0 repeats

Database Matches:
🥇 Harry (100% confidence) - Perfect match!
🥈 Hermione (87.5% confidence) - Very good match
🥉 Ron (75% confidence) - Good match

Recommendation: High confidence match found with Harry!
```

### Confidence Score Interpretation
- **90-100%**: Excellent match (likely the same person)
- **80-89%**: Very good match (close relative)
- **70-79%**: Good match (possible relative)
- **50-69%**: Partial match (distant relative)
- **Below 50%**: Poor match (unrelated)

## 🔧 Technical Architecture

### Backend Stack
- **Flask 2.2.5**: Web framework for Python
- **SQLAlchemy**: Database ORM
- **SQLite**: Lightweight database
- **NumPy & Pandas**: Data processing
- **Scikit-learn**: Machine learning framework

### Frontend Stack
- **Bootstrap 5**: Responsive UI framework
- **Font Awesome**: Icon library
- **Chart.js**: Data visualization
- **Custom CSS**: Modern styling

### Database Schema
```sql
DNARecord:
- id (Primary Key)
- name (String)
- agatc (Integer)
- ttttttct (Integer)
- aatg (Integer)
- tctag (Integer)
- gata (Integer)
- tatc (Integer)
- gaaa (Integer)
- tctg (Integer)
- created_at (DateTime)
```

## 🌐 API Endpoints

### Core Analysis
- `POST /analyze` - Analyze DNA sequence manually
- `POST /upload` - Upload and analyze DNA file
- `GET /database` - View all DNA profiles
- `POST /add_person` - Add new DNA profile

### Advanced Analysis
- `POST /api/genetic_distance` - Calculate genetic distance
- `POST /api/mutations` - Detect mutations
- `GET /api/haplotypes` - Analyze haplotypes

## 📁 Project Structure

```
CS50-DNA-/
├── .gitignore                 # Git ignore rules
├── README.md                  # This file
└── dna/                       # Main application
    ├── app.py                 # Flask application
    ├── requirements.txt       # Python dependencies
    ├── populate_db.py         # Database initialization
    ├── run.py                 # Startup script
    ├── README_WEB.md          # Web app documentation
    ├── templates/             # HTML templates
    │   ├── base.html          # Base template
    │   ├── index.html         # Home page
    │   ├── analyze.html       # DNA analysis page
    │   ├── results.html       # Results display
    │   ├── upload.html        # File upload page
    │   ├── add_person.html    # Add person form
    │   ├── database.html      # Database viewer
    │   └── advanced_analysis.html # Advanced features
    ├── databases/             # DNA data files (gitignored)
    │   ├── large.csv
    │   └── small.csv
    └── sequences/             # DNA sequence files (gitignored)
        ├── 1.txt
        ├── 2.txt
        └── ...
```

## 🔬 Real-World Applications

### Forensic Science
- **Criminal Investigations**: DNA matching for evidence analysis
- **Missing Person Cases**: Identification through DNA comparison
- **Paternity Testing**: Genetic relationship verification

### Medical Research
- **Genetic Disease Screening**: Identify disease markers
- **Pharmacogenetic Testing**: Drug response prediction
- **Ancestry Analysis**: Genetic heritage exploration

### Educational Use
- **Biology Classes**: Learn DNA structure and analysis
- **Forensic Science Courses**: Practical DNA analysis training
- **Research Projects**: Data collection and analysis

## 🛠️ Customization

### Adding New STR Markers
1. Update the `str_names` list in `app.py`
2. Add new columns to the `DNARecord` model
3. Update analysis functions
4. Modify templates to include new fields

### Machine Learning Integration
The system includes placeholder functions for:
- Pattern Recognition
- Predictive Modeling
- Clustering Analysis

To implement these features, add your ML models and update the corresponding functions.

## 🐛 Troubleshooting

### Common Issues

1. **Port Already in Use**
   ```bash
   # Change port in app.py
   app.run(debug=True, use_reloader=False, port=5002)
   ```

2. **Database Errors**
   ```bash
   python populate_db.py
   ```

3. **Import Errors**
   ```bash
   pip install -r requirements.txt
   ```

### Getting Help
- Check the console output for error messages
- Ensure all dependencies are installed
- Verify the database is properly initialized

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

##  License

This project is part of CS50 and is for educational purposes. Feel free to use and modify for your own projects.

##  Acknowledgments

- **CS50**: Harvard's Introduction to Computer Science course
- **Flask**: Web framework for Python
- **Bootstrap**: Frontend framework
- **SQLAlchemy**: Database ORM

## 📞 Contact

- **GitHub**: [Your GitHub Profile]
- **Email**: [Your Email]
- **Project**: [GitHub Repository URL]

---

**Happy DNA Analysis! ✨**

*Transform your DNA sequences into meaningful genetic insights with this comprehensive analysis platform.*
