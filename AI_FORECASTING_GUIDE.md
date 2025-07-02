# Flavi Dairy AI Forecasting System

## Overview

The Flavi Dairy AI Forecasting System is a comprehensive web application that uses advanced machine learning algorithms to predict future demand for dairy products. The system provides actionable insights, inventory recommendations, and interactive visualizations to help optimize operations.

## Features

### 🧠 AI-Powered Forecasting
- **Multiple Algorithms**: Prophet, Linear Regression, and Ensemble methods
- **Advanced Feature Engineering**: Seasonal patterns, trends, lag features
- **Confidence Intervals**: Statistical uncertainty bounds for predictions
- **Real-time Processing**: Instant forecast generation with live data

### 📊 Interactive Dashboard
- **Real-time Metrics**: Key performance indicators at a glance
- **Interactive Charts**: Chart.js powered visualizations
- **Export Capabilities**: CSV, Excel, and PDF export options
- **Responsive Design**: Works on desktop and mobile devices

### 🔍 Business Intelligence
- **Trend Analysis**: Identify upward/downward demand patterns
- **Seasonality Detection**: Peak and low demand periods
- **Inventory Insights**: Stockout risk assessment and recommendations
- **Production Planning**: Recommended production quantities

### 🚨 Smart Alerts
- **Low Stock Alerts**: Automatic notifications for inventory shortages
- **High Stock Alerts**: Warnings for excess inventory
- **Trend Alerts**: Notifications for significant demand changes
- **Production Recommendations**: AI-suggested production adjustments

## System Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Frontend      │    │   Backend       │    │   Database      │
│                 │    │                 │    │                 │
│ • Dashboard     │◄──►│ • Flask API     │◄──►│ • PostgreSQL    │
│ • Charts        │    │ • ML Models     │    │ • Sales Data    │
│ • Export        │    │ • Insights      │    │ • Inventory     │
│ • Alerts        │    │ • Analytics     │    │ • Forecasts     │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## Installation & Setup

### Prerequisites
- Python 3.8+
- PostgreSQL 12+
- Node.js (for development)

### 1. Clone the Repository
```bash
git clone <repository-url>
cd Flavi_Dairy_Forecasting_AI
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Database Setup
```bash
# Run database setup script
python setup_postgresql.py

# Initialize database
python init_db.py
```

### 5. Environment Configuration
Create a `.env` file:
```env
FLASK_APP=run.py
FLASK_ENV=development
DATABASE_URL=postgresql://username:password@localhost/flavi_dairy
SECRET_KEY=your-secret-key-here
```

### 6. Run the Application
```bash
python run.py
```

Access the application at: `http://localhost:5000`

## Usage Guide

### Accessing the AI Dashboard

1. **Login**: Use your admin credentials to access the system
2. **Navigate**: Go to `/forecast_dashboard` for the AI-powered dashboard
3. **Select SKU**: Choose the product you want to forecast
4. **Configure**: Set forecast period (7-90 days) and algorithm
5. **Generate**: Click "Generate Forecast" to run AI analysis

### Understanding the Dashboard

#### 📈 Key Metrics Cards
- **Total SKUs**: Number of products in the system
- **Low Stock Alerts**: Products with inventory shortages
- **Trending Up**: Products with increasing demand
- **Recent Forecasts**: Number of forecasts generated today

#### 🎯 Forecast Configuration
- **SKU Selection**: Choose from available products
- **Forecast Period**: 7-90 days prediction window
- **Algorithm**: Ensemble (recommended), Prophet, or Linear Regression

#### 📊 Results Section
- **Average Forecast**: Mean predicted demand
- **Current Inventory**: Available stock levels
- **Days of Stock**: Inventory coverage period
- **Recommended Production**: AI-suggested production quantity

#### 🧠 AI Insights Panel
- **Trend Analysis**: Direction and strength of demand trends
- **Seasonality**: Peak and low demand months
- **Inventory Status**: Stockout risk assessment

#### ⚠️ Alerts & Recommendations
- **Alerts**: Critical inventory and demand warnings
- **Recommendations**: Actionable business advice

### Exporting Data

The system supports multiple export formats:

1. **CSV Export**: Raw forecast data for spreadsheet analysis
2. **Excel Export**: Formatted tables with charts
3. **PDF Export**: Professional reports for presentations

## AI Algorithms

### 1. Prophet Algorithm
- **Best for**: Seasonal patterns and holiday effects
- **Strengths**: Handles missing data, trend changes, seasonality
- **Use case**: Products with strong seasonal demand

### 2. Linear Regression
- **Best for**: Trend-based forecasting
- **Strengths**: Fast computation, interpretable results
- **Use case**: Products with consistent growth patterns

### 3. Ensemble Method (Recommended)
- **Best for**: General purpose forecasting
- **Strengths**: Combines multiple algorithms for better accuracy
- **Use case**: Most products, especially when unsure of patterns

## Data Requirements

### Minimum Data Requirements
- **Historical Sales**: At least 10 data points for Prophet
- **Inventory Data**: Current stock levels for insights
- **SKU Information**: Product details and categories

### Data Quality
- **Consistent Dates**: Daily sales records
- **Accurate Quantities**: Reliable sales figures
- **Complete Records**: No missing critical data

## API Endpoints

### Forecast Generation
```
GET /api/forecast/{sku_id}?days={period}&method={algorithm}
```

### Dashboard Summary
```
GET /api/dashboard/summary
```

### Historical Data
```
GET /api/sales/{sku_id}
GET /api/inventory/{sku_id}
```

### Insights
```
GET /api/insights/{sku_id}
```

## Troubleshooting

### Common Issues

1. **Insufficient Data Error**
   - **Cause**: Less than 10 historical data points
   - **Solution**: Add more sales records or use shorter forecast periods

2. **Database Connection Issues**
   - **Cause**: PostgreSQL not running or incorrect credentials
   - **Solution**: Check database status and connection settings

3. **Forecast Generation Fails**
   - **Cause**: Data quality issues or algorithm limitations
   - **Solution**: Try different algorithms or clean data

4. **Slow Performance**
   - **Cause**: Large datasets or complex calculations
   - **Solution**: Reduce forecast period or optimize database queries

### Performance Optimization

1. **Database Indexing**: Ensure proper indexes on date columns
2. **Data Archiving**: Archive old data to improve query performance
3. **Caching**: Implement Redis for frequently accessed data
4. **Background Processing**: Use Celery for long-running forecasts

## Best Practices

### Data Management
- **Regular Updates**: Update sales data daily
- **Data Validation**: Verify data accuracy before forecasting
- **Backup Strategy**: Regular database backups

### Forecasting Strategy
- **Multiple Periods**: Generate forecasts for different time horizons
- **Algorithm Comparison**: Test different algorithms for each SKU
- **Regular Review**: Update forecasts based on actual performance

### Business Integration
- **Production Planning**: Use forecasts for production scheduling
- **Inventory Management**: Adjust stock levels based on predictions
- **Marketing**: Plan promotions around predicted demand peaks

## Support & Maintenance

### Regular Maintenance
- **Model Retraining**: Retrain models with new data monthly
- **Performance Monitoring**: Track forecast accuracy
- **System Updates**: Keep dependencies updated

### Support Channels
- **Documentation**: Check this guide for common issues
- **Logs**: Review application logs for error details
- **Development Team**: Contact for technical support

## Future Enhancements

### Planned Features
- **Real-time Streaming**: Live data integration
- **Advanced Analytics**: Customer segmentation and behavior analysis
- **Mobile App**: Native mobile application
- **Integration APIs**: Connect with ERP and CRM systems

### Machine Learning Improvements
- **Deep Learning**: Neural network-based forecasting
- **External Factors**: Weather, economic indicators integration
- **Automated Tuning**: Hyperparameter optimization
- **A/B Testing**: Algorithm performance comparison

---

## Quick Start Checklist

- [ ] Install Python 3.8+
- [ ] Set up PostgreSQL database
- [ ] Install dependencies (`pip install -r requirements.txt`)
- [ ] Configure environment variables
- [ ] Initialize database (`python init_db.py`)
- [ ] Add sample data for testing
- [ ] Start the application (`python run.py`)
- [ ] Access dashboard at `/forecast_dashboard`
- [ ] Generate your first forecast

For additional support or questions, please refer to the main README.md file or contact the development team. 