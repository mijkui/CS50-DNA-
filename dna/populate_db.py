import csv
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import app, db, DNARecord

def populate_database():
    """Populate the database with data from CSV files."""
    with app.app_context():
        # Create tables
        db.create_all()
        
        # Check if database is already populated
        if DNARecord.query.count() > 0:
            print("Database already contains data. Skipping population.")
            return
        
        # Read from large.csv
        csv_file = 'databases/large.csv'
        if os.path.exists(csv_file):
            print(f"Populating database from {csv_file}...")
            
            with open(csv_file, 'r') as file:
                reader = csv.DictReader(file)
                
                for row in reader:
                    # Create new DNA record
                    record = DNARecord(
                        name=row['name'],
                        agatc=int(row['AGATC']),
                        ttttttct=int(row['TTTTTTCT']),
                        aatg=int(row['AATG']),
                        tctag=int(row['TCTAG']),
                        gata=int(row['GATA']),
                        tatc=int(row['TATC']),
                        gaaa=int(row['GAAA']),
                        tctg=int(row['TCTG'])
                    )
                    
                    db.session.add(record)
                
                db.session.commit()
                print(f"Successfully added {DNARecord.query.count()} records to database.")
        else:
            print(f"CSV file {csv_file} not found.")

if __name__ == '__main__':
    populate_database() 