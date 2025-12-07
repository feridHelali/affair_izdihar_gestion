# MCP Adapters for Sage Integration

## Overview

Model Context Protocol (MCP) servers for integrating with Sage Commercial application via ODBC.

## Purpose

MCP adapters allow AI assistants (like Claude) to:
- Query Sage CBASE database (customers, products, invoices, etc.)
- Insert/update records programmatically
- Perform data synchronization
- Generate reports
- Maintain audit trails

## Architecture

```
AI Assistant (Claude)
    ↓ MCP Protocol
MCP Server (Python)
    ↓ ODBC
Sage CBASE Database
```

## Planned Adapters

### 1. sage_cbase_adapter/
- **Purpose**: General-purpose Sage ODBC adapter
- **Features**:
  - Read customer/supplier data
  - Query invoices and transactions
  - Insert new records
  - Update existing records
  - Transaction safety
  - Audit logging

### 2. milk_to_sage_adapter/
- **Purpose**: Sync milk system data to Sage
- **Features**:
  - Export milk invoices to Sage
  - Sync customer accounts
  - Generate accounting entries

### 3. feed_to_sage_adapter/
- **Purpose**: Sync feed system data to Sage
- **Features**:
  - Export feed distribution invoices
  - Sync inventory movements
  - Generate accounting entries

### 4. caisse_to_sage_adapter/
- **Purpose**: Sync caisse transactions to Sage
- **Features**:
  - Export cash/cheque transactions
  - Bank reconciliation
  - Generate journal entries

## Technology Stack

- **Python 3.9+**
- **MCP SDK**: Official Model Context Protocol SDK
- **pyodbc**: ODBC database connectivity
- **Sage ODBC Driver**: Provided by Sage
- **SQLAlchemy**: ORM for database operations (optional)

## Status

🚧 **Planned** - Will be implemented after system analysis

## Resources

- [MCP Specification](https://modelcontextprotocol.io/)
- [Sage ODBC Documentation](https://sage.com/)
- [pyodbc Documentation](https://github.com/mkleehammer/pyodbc)

## Security Considerations

- ODBC credentials stored securely (environment variables or config)
- Read-only mode by default
- Write operations require explicit permission
- Complete audit logging for all operations
- Transaction rollback on errors
