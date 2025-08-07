# 🧬 DNA Analysis System

A web-based DNA analysis platform for analyzing DNA sequences and finding matches in a database.

## ✨ Features

### 🧬 DNA Analysis
- **Manual DNA Input**: Enter DNA sequences directly
- **File Upload**: Support for .txt, .csv, .fasta files
- **STR Analysis**: Analyze 8 different STR markers
- **Confidence Scoring**: Multiple potential matches with confidence scores
- **Real-time Results**: Instant analysis and visualization

### 👥 Database Management
- **Manual Profile Addition**: Add new individuals with STR counts
- **Database Viewer**: Browse all profiles in the system
- **Profile Management**: View and manage DNA records

### 🔬 Advanced Analysis
- **Genetic Distance Calculator**: Measure similarity between sequences
- **Mutation Detection**: Identify genetic variations
- **Haplotype Analysis**: Group individuals by genetic markers
- **Machine Learning Integration**: AI-powered pattern recognition

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Step 1: Install Dependencies
```bash
cd dna
pip install -r requirements.txt
```

### Step 2: Initialize Database
```bash
python populate_db.py
```

### Step 3: Run the Application
```bash
python app.py
```

### Step 4: Access the Application
Open your browser and go to: `http://localhost:5001`

## 📖 How to Use

### 1. Getting Started
1. **Open the application**: Go to `http://localhost:5001`
2. **Start analyzing**: Use "Analyze DNA" or "Upload File"

### 2. DNA Analysis
#### Option A: Manual Input
1. Go to "Analyze DNA" from the navigation
2. Enter your DNA sequence in the text area
3. Click "Analyze Sequence"
4. View results with confidence scores

#### Option B: File Upload
1. Go to "Upload File" from the navigation
2. Select your DNA sequence file (.txt, .csv, .fasta)
3. Click "Upload & Analyze"
4. View results with confidence scores

### 3. Adding New Profiles
1. Go to "Add Person" from the navigation
2. Enter the person's name
3. Input STR counts for all 8 markers:
   - AGATC
   - TTTTTTCT
   - AATG
   - TCTAG
   - GATA
   - TATC
   - GAAA
   - TCTG
4. Click "Add Person"

### 4. Advanced Analysis
1. Go to "Advanced Analysis" from the navigation
2. Choose your analysis type:
   - **Genetic Distance**: Compare two sequences
   - **Mutation Detection**: Find genetic variations
   - **Haplotype Analysis**: Group by genetic markers
   - **Machine Learning**: AI-powered analysis

## 🧪 STR Markers Explained

The system analyzes 8 Short Tandem Repeat (STR) markers:

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

## 📊 Understanding Results

### Confidence Scores
- **90-100%**: Excellent match
- **80-89%**: Very good match
- **70-79%**: Good match
- **50-69%**: Partial match
- **Below 50%**: Poor match

### Match Types
- **Exact Match**: All STR markers match perfectly
- **Partial Match**: Some STR markers match
- **No Match**: No significant similarity found

## 🔧 Technical Details

### Database Schema
- **DNARecords**: Store DNA profiles with STR counts

### API Endpoints
- `/api/genetic_distance`: Calculate genetic distance
- `/api/mutations`: Detect mutations
- `/api/haplotypes`: Analyze haplotypes

### File Structure
```
dna/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── populate_db.py         # Database population script
├── templates/            # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── analyze.html
│   ├── results.html
│   ├── upload.html
│   ├── add_person.html
│   ├── database.html
│   └── advanced_analysis.html
├── databases/            # CSV data files
│   ├── large.csv
│   └── small.csv
└── sequences/            # DNA sequence files
    ├── 1.txt
    ├── 2.txt
    └── ...
```

## 🛠️ Customization

### Adding New STR Markers
1. Update the `str_names` list in `app.py`
2. Add new columns to the `DNARecord` model
3. Update the analysis functions
4. Modify the templates to include new fields

### Machine Learning Integration
The system includes placeholder functions for:
- Pattern Recognition
- Predictive Modeling
- Clustering Analysis

To implement these features, add your ML models and update the corresponding functions.

## 🐛 Troubleshooting

### Common Issues

1. **Database Errors**
   ```bash
   python populate_db.py
   ```

2. **Import Errors**
   ```bash
   pip install -r requirements.txt
   ```

3. **Port Already in Use**
   - Change the port in `app.py`
   - Or kill the existing process

### Support
For issues or questions, check the console output for error messages.

## 📈 Future Enhancements

- [ ] Real-time collaboration
- [ ] Advanced visualization
- [ ] API rate limiting
- [ ] Data export features
- [ ] Mobile app
- [ ] Cloud deployment
- [ ] Advanced ML models
- [ ] Genetic trait prediction

## 📄 License

This project is part of CS50 and is for educational purposes.

---

**Happy DNA Analysis! 🧬✨** 