from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
import csv
import os
import json
from datetime import datetime
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dna_analysis.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database Models
class DNARecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    agatc = db.Column(db.Integer, nullable=False)
    ttttttct = db.Column(db.Integer, nullable=False)
    aatg = db.Column(db.Integer, nullable=False)
    tctag = db.Column(db.Integer, nullable=False)
    gata = db.Column(db.Integer, nullable=False)
    tatc = db.Column(db.Integer, nullable=False)
    gaaa = db.Column(db.Integer, nullable=False)
    tctg = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# DNA Analysis Functions
def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    for i in range(sequence_length):
        count = 0
        while True:
            start = i + count * subsequence_length
            end = start + subsequence_length
            if sequence[start:end] == subsequence:
                count += 1
            else:
                break
        longest_run = max(longest_run, count)
    return longest_run

def analyze_dna_sequence(dna_sequence):
    """Analyze DNA sequence and return STR counts and matches."""
    str_names = ['AGATC', 'TTTTTTCT', 'AATG', 'TCTAG', 'GATA', 'TATC', 'GAAA', 'TCTG']
    str_count = {}
    
    for subseq in str_names:
        str_count[subseq] = longest_match(dna_sequence, subseq)
    
    # Get all DNA records from database
    dna_records = DNARecord.query.all()
    matches = []
    
    for record in dna_records:
        match_score = 0
        total_strs = len(str_names)
        
        for str_name in str_names:
            if getattr(record, str_name.lower()) == str_count[str_name]:
                match_score += 1
        
        confidence = (match_score / total_strs) * 100
        
        if match_score > 0:
            matches.append({
                'name': record.name,
                'confidence': confidence,
                'match_score': match_score,
                'str_counts': {
                    'AGATC': record.agatc,
                    'TTTTTTCT': record.ttttttct,
                    'AATG': record.aatg,
                    'TCTAG': record.tctag,
                    'GATA': record.gata,
                    'TATC': record.tatc,
                    'GAAA': record.gaaa,
                    'TCTG': record.tctg
                }
            })
    
    # Sort by confidence score
    matches.sort(key=lambda x: x['confidence'], reverse=True)
    
    return str_count, matches

def calculate_genetic_distance(seq1, seq2):
    """Calculate genetic distance between two DNA sequences."""
    if len(seq1) != len(seq2):
        return None
    
    differences = sum(1 for a, b in zip(seq1, seq2) if a != b)
    return differences / len(seq1)

def detect_mutations(reference_sequence, test_sequence):
    """Detect mutations by comparing two sequences."""
    mutations = []
    min_length = min(len(reference_sequence), len(test_sequence))
    
    for i in range(min_length):
        if reference_sequence[i] != test_sequence[i]:
            mutations.append({
                'position': i,
                'reference': reference_sequence[i],
                'mutated': test_sequence[i],
                'type': 'substitution'
            })
    
    return mutations

def haplotype_analysis(dna_records):
    """Group people by genetic markers (haplotypes)."""
    haplotypes = {}
    
    for record in dna_records:
        # Create haplotype signature based on STR patterns
        haplotype = f"{record.agatc}_{record.ttttttct}_{record.aatg}_{record.tctag}_{record.gata}_{record.tatc}_{record.gaaa}_{record.tctg}"
        
        if haplotype not in haplotypes:
            haplotypes[haplotype] = []
        
        haplotypes[haplotype].append(record.name)
    
    return haplotypes

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['GET', 'POST'])
def analyze():
    if request.method == 'POST':
        dna_sequence = request.form['dna_sequence'].strip()
        
        if not dna_sequence:
            flash('Please enter a DNA sequence')
            return redirect(url_for('analyze'))
        
        str_count, matches = analyze_dna_sequence(dna_sequence)
        
        return render_template('results.html', 
                             str_count=str_count, 
                             matches=matches, 
                             dna_sequence=dna_sequence)
    
    return render_template('analyze.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file selected')
            return redirect(url_for('upload'))
        
        file = request.files['file']
        if file.filename == '':
            flash('No file selected')
            return redirect(url_for('upload'))
        
        if file:
            content = file.read().decode('utf-8').strip()
            str_count, matches = analyze_dna_sequence(content)
            
            return render_template('results.html', 
                                 str_count=str_count, 
                                 matches=matches, 
                                 dna_sequence=content)
    
    return render_template('upload.html')

@app.route('/add_person', methods=['GET', 'POST'])
def add_person():
    if request.method == 'POST':
        name = request.form['name']
        agatc = int(request.form['agatc'])
        ttttttct = int(request.form['ttttttct'])
        aatg = int(request.form['aatg'])
        tctag = int(request.form['tctag'])
        gata = int(request.form['gata'])
        tatc = int(request.form['tatc'])
        gaaa = int(request.form['gaaa'])
        tctg = int(request.form['tctg'])
        
        new_record = DNARecord(
            name=name,
            agatc=agatc,
            ttttttct=ttttttct,
            aatg=aatg,
            tctag=tctag,
            gata=gata,
            tatc=tatc,
            gaaa=gaaa,
            tctg=tctg
        )
        
        db.session.add(new_record)
        db.session.commit()
        
        flash(f'Successfully added {name} to the database!')
        return redirect(url_for('database'))
    
    return render_template('add_person.html')

@app.route('/database')
def database():
    records = DNARecord.query.all()
    return render_template('database.html', records=records)

@app.route('/advanced_analysis')
def advanced_analysis():
    return render_template('advanced_analysis.html')

@app.route('/api/genetic_distance', methods=['POST'])
def api_genetic_distance():
    data = request.get_json()
    seq1 = data['sequence1']
    seq2 = data['sequence2']
    
    distance = calculate_genetic_distance(seq1, seq2)
    return jsonify({'distance': distance})

@app.route('/api/mutations', methods=['POST'])
def api_mutations():
    data = request.get_json()
    reference = data['reference']
    test = data['test']
    
    mutations = detect_mutations(reference, test)
    return jsonify({'mutations': mutations})

@app.route('/api/haplotypes')
def api_haplotypes():
    records = DNARecord.query.all()
    haplotypes = haplotype_analysis(records)
    return jsonify(haplotypes)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, use_reloader=False, port=5001) 