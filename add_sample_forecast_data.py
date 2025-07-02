#!/usr/bin/env python3
"""
Sample Data Generator for Flavi Dairy Forecasting AI
This script adds sample sales and inventory data for testing the forecasting system.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import create_app, db
from app.models.sku import SKU
from app.models.sales import Sales
from app.models.inventory import Inventory
from datetime import datetime, timedelta
import random
import numpy as np

def create_sample_data():
    """Create sample SKUs, sales, and inventory data"""
    app = create_app()
    
    with app.app_context():
        print("🔄 Creating sample data for Flavi Dairy Forecasting AI...")
        
        # Clear existing data (optional - comment out if you want to keep existing data)
        # print("🗑️ Clearing existing data...")
        # Sales.query.delete()
        # Inventory.query.delete()
        # SKU.query.delete()
        # db.session.commit()
        
        # Create sample SKUs if they don't exist
        skus_data = [
            {'sku_id': 'MILK001', 'name': 'Fresh Whole Milk', 'category': 'Milk', 'price': 45.0, 'min_threshold': 100},
            {'sku_id': 'MILK002', 'name': 'Skimmed Milk', 'category': 'Milk', 'price': 42.0, 'min_threshold': 80},
            {'sku_id': 'YOG001', 'name': 'Plain Yogurt', 'category': 'Yogurt', 'price': 35.0, 'min_threshold': 60},
            {'sku_id': 'YOG002', 'name': 'Strawberry Yogurt', 'category': 'Yogurt', 'price': 40.0, 'min_threshold': 50},
            {'sku_id': 'CHE001', 'name': 'Cheddar Cheese', 'category': 'Cheese', 'price': 180.0, 'min_threshold': 30},
            {'sku_id': 'BUT001', 'name': 'Unsalted Butter', 'category': 'Butter', 'price': 120.0, 'min_threshold': 40},
            {'sku_id': 'CRE001', 'name': 'Fresh Cream', 'category': 'Cream', 'price': 85.0, 'min_threshold': 25},
            {'sku_id': 'CUR001', 'name': 'Paneer', 'category': 'Paneer', 'price': 200.0, 'min_threshold': 35}
        ]
        
        created_skus = []
        for sku_data in skus_data:
            existing_sku = SKU.query.filter_by(sku_id=sku_data['sku_id']).first()
            if not existing_sku:
                sku = SKU(**sku_data)
                db.session.add(sku)
                created_skus.append(sku)
                print(f"✅ Created SKU: {sku_data['sku_id']} - {sku_data['name']}")
            else:
                created_skus.append(existing_sku)
                print(f"ℹ️ SKU already exists: {sku_data['sku_id']}")
        
        db.session.commit()
        
        # Generate sample sales data for the last 90 days
        print("📊 Generating sample sales data...")
        end_date = datetime.now().date()
        start_date = end_date - timedelta(days=90)
        
        for sku in created_skus:
            # Generate realistic sales patterns with seasonality and trends
            base_demand = {
                'MILK001': 150, 'MILK002': 120, 'YOG001': 80, 'YOG002': 70,
                'CHE001': 25, 'BUT001': 35, 'CRE001': 20, 'CUR001': 30
            }.get(sku.sku_id, 50)
            
            # Add some trend (slight growth)
            trend_factor = 1.02  # 2% growth per month
            
            # Add seasonality (higher on weekends)
            weekend_boost = 1.3
            
            # Add some randomness
            noise_factor = 0.2
            
            current_date = start_date
            while current_date <= end_date:
                # Calculate base quantity
                days_from_start = (current_date - start_date).days
                trend = trend_factor ** (days_from_start / 30)  # Monthly trend
                
                # Weekend effect
                weekend_multiplier = weekend_boost if current_date.weekday() >= 5 else 1.0
                
                # Random noise
                noise = 1 + random.uniform(-noise_factor, noise_factor)
                
                # Calculate final quantity
                quantity = base_demand * trend * weekend_multiplier * noise
                quantity = max(0, int(quantity))  # Ensure non-negative
                
                # Create sales record
                sale = Sales(
                    sku_id=sku.sku_id,
                    date=current_date,
                    quantity_sold=quantity,
                    revenue=quantity * sku.price,
                    region_id='REGION001',
                    holiday_flag=current_date.weekday() >= 5,  # Weekend as holiday
                    festival_flag=False,
                    promotional_flag=False,
                    temperature_avg=random.uniform(20, 35),
                    humidity_avg=random.uniform(40, 80),
                    competitor_activity_index=random.uniform(0.1, 0.9),
                    fuel_price=random.uniform(80, 120)
                )
                db.session.add(sale)
                
                current_date += timedelta(days=1)
            
            print(f"✅ Generated sales data for {sku.sku_id} ({quantity} records)")
        
        db.session.commit()
        
        # Generate sample inventory data
        print("📦 Generating sample inventory data...")
        for sku in created_skus:
            # Get current inventory level based on recent sales
            recent_sales = Sales.query.filter_by(sku_id=sku.sku_id).order_by(Sales.date.desc()).limit(7).all()
            avg_daily_sales = sum(sale.quantity_sold for sale in recent_sales) / len(recent_sales) if recent_sales else 50
            
            # Set current inventory to 7 days of average sales
            current_inventory = int(avg_daily_sales * 7)
            
            # Create inventory record
            inventory = Inventory(
                sku_id=sku.sku_id,
                date=end_date,
                current_level=current_inventory,
                production_batch_size=int(avg_daily_sales * 3),  # 3 days of production
                shelf_life_days=random.randint(7, 21),
                storage_capacity_units=current_inventory * 2  # Double current inventory
            )
            db.session.add(inventory)
            print(f"✅ Generated inventory data for {sku.sku_id} (Level: {current_inventory})")
        
        db.session.commit()
        
        print("\n🎉 Sample data generation completed!")
        print(f"📊 Created {len(created_skus)} SKUs")
        print(f"📈 Generated sales data for the last 90 days")
        print(f"📦 Created current inventory records")
        print("\n🚀 You can now test the forecasting system:")
        print("   1. Start the application: python run.py")
        print("   2. Navigate to: http://localhost:5000/forecast_dashboard")
        print("   3. Select any SKU and generate forecasts")

if __name__ == '__main__':
    create_sample_data() 