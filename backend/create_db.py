"""
Database creation script for Textile ERP
Creates all tables in the database
"""

from app.core.database import Base, engine
from app.models import (
    User, Role, AuditLog,  # Auth
    Supplier, PurchaseOrder, POItem, SupplierRating,  # Procurement
    Material, InventoryItem, StockMovement, ReorderAlert,  # Inventory
    Product, BillOfMaterials, Machine, WorkOrder, MachineAllocation, ProductionLog,  # Production
    QCInspection, DefectLog, DefectType, BatchApproval,  # Quality
    Customer, SalesOrder, SOItem, DispatchNote  # Sales
)

def create_tables():
    """Create all database tables"""
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("✅ Database tables created successfully!")

if __name__ == "__main__":
    create_tables()