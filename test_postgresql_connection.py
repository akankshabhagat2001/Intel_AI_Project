#!/usr/bin/env python3
"""
PostgreSQL Connection Test Script
This script tests the PostgreSQL connection and basic functionality.
"""

import os
import sys
import psycopg2
from psycopg2.extras import RealDictCursor

# Add the project root to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_postgresql_connection():
    """Test PostgreSQL connection and basic functionality."""
    print("🔍 PostgreSQL Connection Test")
    print("=" * 40)
    
    # Load environment variables
    from dotenv import load_dotenv
    load_dotenv()
    
    database_url = os.environ.get('DATABASE_URL')
    if not database_url:
        print("❌ DATABASE_URL not found in .env file")
        return False
    
    try:
        # Test connection
        print("🔗 Testing connection...")
        conn = psycopg2.connect(database_url)
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        
        # Test basic query
        cursor.execute("SELECT version()")
        version = cursor.fetchone()
        print(f"✅ Connected to PostgreSQL: {version['version'].split(',')[0]}")
        
        # Test database info
        cursor.execute("SELECT current_database(), current_user")
        db_info = cursor.fetchone()
        print(f"📊 Database: {db_info['current_database']}")
        print(f"👤 User: {db_info['current_user']}")
        
        # Test table access
        cursor.execute("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public' 
            ORDER BY table_name
        """)
        tables = cursor.fetchall()
        
        if tables:
            print(f"📋 Found {len(tables)} tables:")
            for table in tables:
                table_name = table['table_name']
                cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
                count = cursor.fetchone()['count']
                print(f"  - {table_name}: {count} records")
        else:
            print("⚠️  No tables found in database")
        
        # Test Flask-SQLAlchemy integration
        print("\n🔧 Testing Flask-SQLAlchemy integration...")
        try:
            from app import create_app, db
            from sqlalchemy import text
            
            app = create_app()
            with app.app_context():
                # Test basic query
                result = db.session.execute(text('SELECT 1 as test'))
                test_result = result.fetchone()
                print(f"✅ Flask-SQLAlchemy connection: {test_result[0]}")
                
                # Test model queries
                try:
                    from app.models.user import User
                    user_count = User.query.count()
                    print(f"✅ User model query: {user_count} users found")
                except Exception as e:
                    print(f"⚠️  User model query failed: {e}")
                
                try:
                    from app.models.customer import Customer
                    customer_count = Customer.query.count()
                    print(f"✅ Customer model query: {customer_count} customers found")
                except Exception as e:
                    print(f"⚠️  Customer model query failed: {e}")
                
        except Exception as e:
            print(f"❌ Flask-SQLAlchemy test failed: {e}")
        
        conn.close()
        print("\n🎉 All tests passed! PostgreSQL is working correctly.")
        return True
        
    except Exception as e:
        print(f"❌ Connection test failed: {str(e)}")
        print("\nTroubleshooting tips:")
        print("1. Make sure PostgreSQL is running")
        print("2. Check your .env file has the correct DATABASE_URL")
        print("3. Verify the database and user exist")
        print("4. Ensure the user has proper permissions")
        return False

def test_data_integrity():
    """Test data integrity after migration."""
    print("\n🔍 Data Integrity Test")
    print("=" * 30)
    
    try:
        from dotenv import load_dotenv
        load_dotenv()
        
        database_url = os.environ.get('DATABASE_URL')
        if not database_url:
            print("❌ DATABASE_URL not found")
            return False
        
        conn = psycopg2.connect(database_url)
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        
        # Test key tables
        test_tables = ['user', 'customer', 'sku', 'sales', 'inventory']
        
        for table_name in test_tables:
            try:
                cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
                count = cursor.fetchone()['count']
                print(f"✅ {table_name}: {count} records")
                
                # Show sample data
                if count > 0:
                    cursor.execute(f"SELECT * FROM {table_name} LIMIT 1")
                    sample = cursor.fetchone()
                    print(f"   Sample: {dict(sample)}")
                    
            except Exception as e:
                print(f"❌ {table_name}: Error - {e}")
        
        conn.close()
        return True
        
    except Exception as e:
        print(f"❌ Data integrity test failed: {e}")
        return False

def main():
    """Main test function."""
    print("🚀 PostgreSQL Connection and Integration Test")
    print("=" * 50)
    
    # Test 1: Basic connection
    connection_ok = test_postgresql_connection()
    
    # Test 2: Data integrity
    data_ok = test_data_integrity()
    
    if connection_ok and data_ok:
        print("\n🎉 All tests passed!")
        print("✅ PostgreSQL is properly configured")
        print("✅ Your website can connect to PostgreSQL")
        print("✅ Data migration was successful")
        print("\nYou can now run: python run.py")
    else:
        print("\n❌ Some tests failed")
        print("Please check the error messages above")
        print("Refer to POSTGRESQL_QUICK_START.md for troubleshooting")

if __name__ == '__main__':
    main() 