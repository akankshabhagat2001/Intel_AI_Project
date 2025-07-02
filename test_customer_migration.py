"""
Test script to check Customer table migration
"""
import sqlite3
from datetime import datetime

def test_migration():
    try:
        # Connect to the database
        conn = sqlite3.connect('instance/flavi_dairy_forecasting_ai.sqlite')
        cursor = conn.cursor()
        
        # Check table structure
        cursor.execute('PRAGMA table_info(customer)')
        columns = cursor.fetchall()
        print("Customer table columns:")
        for col in columns:
            print(f"  {col[1]} ({col[2]})")
        
        # Check if created_at column exists
        created_at_exists = any(col[1] == 'created_at' for col in columns)
        print(f"\ncreated_at column exists: {created_at_exists}")
        
        # Count customers
        cursor.execute('SELECT COUNT(*) FROM customer')
        count = cursor.fetchone()[0]
        print(f"Total customers: {count}")
        
        # Show sample customers
        if count > 0:
            cursor.execute('SELECT id, username, email, created_at FROM customer LIMIT 5')
            customers = cursor.fetchall()
            print("\nSample customers:")
            for customer in customers:
                print(f"  ID: {customer[0]}, Username: {customer[1]}, Email: {customer[2]}, Created: {customer[3]}")
        
        conn.close()
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_migration() 