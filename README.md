# IZDIHAR Legacy Systems Audit & Migration

**Forensic audit and migration project for Cooperative IZDIHAR legacy systems**

## Overview

This project handles the forensic analysis, audit, and potential migration/re-implementation of three legacy Clipper/DBF systems:

1. **LAIT** (Milk Collection & Distribution System)
2. **GEST/ALFA** (Cattle Feed Management System)
3. **CAISSE** (Cash/Cheque/Fees Management System)

## Project Structure

```
02_AUDIT_PROGRAMME_LAIT_ALFA_CAISSE/
├── designDocs/                    # Documentation and design decisions
│   ├── 00_Inception/              # Sprint planning and analysis
│   │   ├── 00_sprint_01.md
│   │   ├── 01_MIGRATION_PATTERNS_FROM_ACCOUNTING.md
│   │   └── inventory_reports/     # DBF inventory reports
│   ├── 01_UserGuides/
│   └── 02_TechnicalGuides/
│
├── 00_Archives/                   # Validated source DBF files (to be created)
│   ├── LAIT_{year}/
│   ├── GEST_{year}/
│   └── CAISSE_{year}/
│
├── scripts/                       # Utility scripts
│   └── 01_inventory_dbf_files.py  # DBF inventory scanner
│
├── systems/                       # System implementations (to be created)
│   ├── milk_system/               # LAIT re-implementation
│   ├── feed_system/               # GEST/ALFA re-implementation
│   └── caisse_system/             # CAISSE re-implementation
│
├── mcp_adapters/                  # MCP servers for Sage ODBC (to be created)
│   └── sage_cbase_adapter/
│
├── CONSOLIDATED_MIGRATION/        # Working directory (to be created)
│   ├── 01_INPUT_DBF/
│   ├── 02_STAGE_INTERMEDIATE/
│   ├── 03_STAGE_SQLITE/
│   ├── 04_OUTPUT_FINAL/
│   ├── 05_FORENSICS_REPORTS/
│   ├── 06_BACKUPS/
│   └── 07_MAPPINGS/
│
├── tests/                         # Unit tests
├── pyproject.toml                 # UV project configuration
└── README.md                      # This file
```

## Strategic Options

This project supports multiple strategic approaches:

### Option 1: Migration to Sage Commercial
- Extract data from legacy DBF files
- Transform to Sage Commercial format
- Import via ODBC to Sage CBASE proprietary database
- Uses Sage ODBC driver

### Option 2: Re-implementation
- Build modern replacement systems
- Python-based with modern UI (CLI/TUI/GUI)
- SQLite or PostgreSQL backend
- Web-based interface option

### Option 3: Hybrid Approach
- Re-implement core systems
- MCP (Model Context Protocol) adapter for Sage integration
- Bidirectional data sync capabilities
- Maintain compatibility with existing Sage infrastructure

## Getting Started

### Installation

```bash
# Initialize UV environment
uv sync

# Install with GUI support
uv sync --extra gui

# Install development tools
uv sync --extra dev
```

### Running the DBF Inventory

```bash
# Scan all legacy DBF files and generate forensic inventory
uv run python scripts/01_inventory_dbf_files.py
```

This will:
- Scan all three legacy system folders
- Generate MD5/SHA256 checksums for each DBF file
- Identify duplicates across different backups
- Create JSON inventory and human-readable report
- Output to `designDocs/00_Inception/inventory_reports/`

## Source Data Locations

### LAIT (Milk) System
- `../Sauvegarde_2_HDD/IZDIHAR_HBIRA/LAIT{YEAR}/`
- `../Sauvegarde_2_HDD/Sauvegarde_Disque_Alfa/LAIT{YEAR}/`
- `../Sauvegarde_2_HDD/lait {YEAR}/`

### GEST/ALFA (Feed) System
- `../IZDIHAE_HBIRA_CAISSE_GESTION/IZDIHAR_ALFA_SAUVEGARDE/GEST{YEAR}/`

### CAISSE (Cash/Cheque) System
- `../IZDIHAE_HBIRA_CAISSE_GESTION/CAISSE/`
- `../Sauvegarde_2_HDD/Izdihar_Hbira_Caisse_A_Jour/CAISSE*/`

## Technology Stack

- **Python 3.9+**: Core implementation language
- **UV**: Fast package manager
- **dbfread**: Legacy DBF file reading (CP850, CP437, Latin-1 encodings)
- **SQLite**: Intermediate data storage and normalization
- **Rich**: Console UI with progress bars
- **Click**: CLI framework
- **PySide6**: Desktop GUI (optional)

## Forensic Approach

This project follows forensic best practices:

1. **Never Modify Source Files**: All operations work on copies
2. **Complete Audit Trail**: MD5/SHA256 checksums for all files
3. **Timestamped Operations**: ISO 8601 timestamps on all events
4. **Multi-Stage Pipeline**: Intermediate outputs at each stage
5. **Idempotent Operations**: Can re-run safely
6. **Structured Logging**: JSON + human-readable reports

## MCP Integration (Planned)

Model Context Protocol (MCP) adapter for Sage Commercial:

- **Server**: Python-based MCP server
- **Protocol**: MCP standard for AI-assisted operations
- **Access**: Sage CBASE via ODBC
- **Features**:
  - Query Sage data (customers, products, invoices)
  - Insert/Update operations
  - Transaction safety
  - Audit logging

## Next Steps

1. ✅ Review accounting migration patterns
2. ✅ Document proven architectural patterns
3. 🔄 Run DBF inventory scan (in progress)
4. ⏳ Compare and select best DBF versions
5. ⏳ Archive validated DBF files
6. ⏳ Analyze DBF schemas for each system
7. ⏳ Design migration/re-implementation strategy
8. ⏳ Implement MCP adapter for Sage (if needed)

## Context

This is part of a forensic audit for Cooperative IZDIHAR. There is an ongoing legal case involving data deletion. All operations must maintain complete audit trails and data integrity verification.

**Years Covered**: 2017-2024 (varies by system)

## Related Projects

- **MIGRATION_CLIPPER_TO_SAGE_CIEL_2025**: Accounting system migration (completed)
  - Proven patterns for DBF migration
  - 10 years of data successfully migrated
  - Complete forensic tracking

## License

MIT License - For Cooperative IZDIHAR internal use

## Contact

**Ferid HELALI** - helaliferid@gmail.com
**Client**: Cooperative IZDIHAR

---

**Bismillah! May this audit bring clarity and justice! 🌙**
