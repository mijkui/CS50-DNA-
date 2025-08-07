#!/usr/bin/env python3
"""
DNA Analysis System - Startup Script
Run this script to start the web application.
"""

import os
import sys
import subprocess

def check_dependencies():
    """Check if required packages are installed."""
    try:
        import flask
        import flask_sqlalchemy
        import flask_login
        import werkzeug
        import numpy
        import pandas
        import sklearn
        print("✅ All dependencies are installed!")
        return True
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        print("Please run: pip install -r requirements.txt")
        return False

def setup_database():
    """Set up the database with initial data."""
    try:
        print("📊 Setting up database...")
        subprocess.run([sys.executable, "populate_db.py"], check=True)
        print("✅ Database setup complete!")
        return True
    except subprocess.CalledProcessError:
        print("❌ Database setup failed!")
        return False

def start_application():
    """Start the Flask application."""
    print("🚀 Starting DNA Analysis System...")
    print("🌐 Open your browser and go to: http://localhost:5001")
    print("⏹️  Press Ctrl+C to stop the server")
    print("-" * 50)
    
    try:
        subprocess.run([sys.executable, "app.py"])
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")

def main():
    """Main startup function."""
    print("🧬 DNA Analysis System")
    print("=" * 30)
    
    # Check if we're in the right directory
    if not os.path.exists("app.py"):
        print("❌ Please run this script from the 'dna' directory")
        sys.exit(1)
    
    # Check dependencies
    if not check_dependencies():
        sys.exit(1)
    
    # Setup database
    if not setup_database():
        sys.exit(1)
    
    # Start application
    start_application()

if __name__ == "__main__":
    main() 