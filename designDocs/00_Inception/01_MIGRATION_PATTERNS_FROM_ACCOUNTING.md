# Migration Patterns & Preferences from Accounting Project

**Source Project**: MIGRATION_CLIPPER_TO_SAGE_CIEL_2025
**Date**: December 2024
**Purpose**: Document proven patterns for the new milk/feed/caisse migration project

---

## Executive Summary

The accounting migration project successfully migrated 10 years (2015-2024) of legacy Clipper/DBF data through multiple transformation stages with complete forensic tracking. This document captures the proven patterns, tools, and architectural decisions for reuse.

---

## Architecture Pattern: Multi-Stage Pipeline

### Proven Pipeline Structure

```
Stage 1: Source Archive (Read-Only Protection)
    ↓
Stage 2: Working Copy (DBF Files)
    ↓
Stage 3: Intermediate Format (TXT/CSV)
    ↓
Stage 4: Normalized Database (SQLite)
    ↓
Stage 5: Target Export (CSV/Import Format)
    ↓
Stage 6: Forensics & Reports (JSON + TXT)
```

### Key Benefits
- **Data Protection**: Never modify source files
- **Idempotency**: Re-run operations safely
- **Traceability**: Complete audit trail at each stage
- **Debugging**: Inspect intermediate outputs
- **Recovery**: Restart from any stage

### Directory Structure Pattern

```
PROJECT_ROOT/
├── {SOURCE_FOLDERS}/              # Legacy data (read-only)
│   ├── LAIT{YEAR}/
│   ├── GEST{YEAR}/
│   └── CAISSE{99}/
│
└── CONSOLIDATED_MIGRATION_2025/   # Working directory
    ├── 01_INPUT_DBF/              # Archived working copies
    ├── 02_STAGE_INTERMEDIATE/     # Converted formats
    ├── 03_STAGE_SQLITE/           # Normalized databases
    ├── 04_OUTPUT_FINAL/           # Export files
    ├── 05_FORENSICS_REPORTS/      # Audit trails
    ├── 06_BACKUPS/                # Safety backups
    └── 07_MAPPINGS/               # Custom configurations
```

---

## Technology Stack & Tools

### Programming Language: Python 3.9+
**Rationale**: Rich ecosystem, excellent DBF support, cross-platform

### Key Libraries

| Library | Purpose | Notes |
|---------|---------|-------|
| `dbfread` | Read legacy DBF files | Handles multiple encodings (CP850, CP437, Latin-1) |
| `sqlite3` | Intermediate data storage | Built-in, perfect for validation/normalization |
| `pandas` | Data manipulation | Optional but powerful for analysis |
| `pathlib` | File operations | Modern, cross-platform path handling |
| `hashlib` | Checksums (MD5/SHA256) | Forensic file integrity verification |
| `click` | CLI framework | Clean command-line interfaces |
| `rich` | Console output | Beautiful progress bars and tables |
| `PySide6` | Desktop GUI | Qt-based, professional desktop apps |

### Package Manager: `uv`
**Why**: Fast, reliable, modern Python package management

```bash
# Quick setup
uv sync                    # Install all dependencies
uv run python main.py      # Run application
```

### Version Control: Git
**Critical**: Track every code change for forensic purposes

---

## Core Design Patterns

### 1. Configuration-Driven Design

**Pattern**: Single `config.py` with all paths, encodings, and constants

```python
class Config:
    # Dynamic paths (user-configurable)
    PROJECT_ROOT = _get_project_root()
    WORK_DIR = _get_work_dir()

    # Stage directories
    INPUT_DBF_DIR = WORK_DIR / "01_INPUT_DBF"
    STAGE_SQLITE_DIR = WORK_DIR / "03_STAGE_SQLITE"
    OUTPUT_DIR = WORK_DIR / "04_OUTPUT_FINAL"

    # Encodings
    DBF_ENCODINGS = ['cp850', 'cp437', 'latin1', 'utf-8']
    OUTPUT_ENCODING = "utf-8"

    # File patterns
    SQLITE_PATTERN = "{system}_{year}.db"

    # Helper methods
    @classmethod
    def get_sqlite_db(cls, system: str, year: int) -> Path:
        return cls.STAGE_SQLITE_DIR / cls.SQLITE_PATTERN.format(
            system=system, year=year
        )
```

**Benefits**:
- One place to change paths
- Type hints and validation
- Helper methods for path construction
- Dynamic configuration (user preferences)

### 2. Layered Architecture (UI Separation)

**Pattern**: Service layer decouples UI from business logic

```
┌─────────────────────────────────────┐
│    UI Layer (GUI/TUI/CLI)           │
│    - Presentation only               │
│    - Event handlers                  │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│    Service Layer (app_service.py)   │
│    - Facade pattern                  │
│    - Event emission                  │
│    - Returns data structures         │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│    Business Logic Layer              │
│    - Pipeline orchestration          │
│    - Data transformations            │
│    - Validation rules                │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│    Data Layer                        │
│    - File I/O                        │
│    - Database operations             │
│    - DBF reading                     │
└──────────────────────────────────────┘
```

**Key Principle**: Business logic NEVER uses `print()` - returns data instead

```python
# ❌ BAD - Business logic with print statements
def migrate_year(year):
    print(f"Starting migration for {year}")
    # ... migration logic
    print("Done!")

# ✅ GOOD - Business logic returns data
def migrate_year(year):
    results = {
        'year': year,
        'status': 'success',
        'records_processed': 5432,
        'output_file': output_path
    }
    return results

# UI layer handles presentation
results = service.migrate_year(2019)
print(f"Migration completed: {results['records_processed']} records")
```

### 3. Event-Driven Progress Tracking

**Pattern**: Pub/Sub event system for real-time progress

```python
from enum import Enum

class EventType(Enum):
    PIPELINE_START = "pipeline_start"
    OPERATION_PROGRESS = "operation_progress"
    PIPELINE_STAGE_START = "pipeline_stage_start"
    PIPELINE_COMPLETE = "pipeline_complete"
    ERROR = "error"

class EventEmitter:
    def __init__(self):
        self._handlers = {}

    def on(self, event_type: EventType, handler):
        """Register event handler"""
        if event_type not in self._handlers:
            self._handlers[event_type] = []
        self._handlers[event_type].append(handler)

    def emit(self, event_type: EventType, message: str,
             data: dict = None, progress: float = None):
        """Emit event to all registered handlers"""
        event = Event(event_type, message, data, progress)
        for handler in self._handlers.get(event_type, []):
            handler(event)
```

**Usage in GUI**:
```python
# Register progress handler
def on_progress(event):
    progress_bar.setValue(int(event.progress * 100))
    status_label.setText(event.message)

emitter.on(EventType.OPERATION_PROGRESS, on_progress)

# Run operation - progress updates automatically
service.migrate_year(2019)
```

### 4. Context Managers for Resources

**Pattern**: Automatic resource cleanup with `with` statement

```python
class SQLiteManager:
    def __init__(self, system: str, year: int):
        self.db_path = Config.get_sqlite_db(system, year)
        self.conn = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_path)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.close()

    def get_statistics(self):
        cursor = self.conn.cursor()
        # ... query logic
        return results

# Usage - automatic connection cleanup
with SQLiteManager("lait", 2019) as db:
    stats = db.get_statistics()
# Connection automatically closed here
```

### 5. Forensic Logging Pattern

**Pattern**: Complete audit trail with checksums

```python
class ForensicLogger:
    def __init__(self, operation_name: str, year: int):
        self.operation = operation_name
        self.year = year
        self.events = []
        self.start_time = datetime.now()

    def log_event(self, event_type: str, details: dict):
        """Log structured event"""
        self.events.append({
            'timestamp': datetime.now().isoformat(),
            'event_type': event_type,
            'details': details
        })

    def log_file_checksum(self, file_path: Path, operation: str):
        """Log file with integrity checksums"""
        md5 = self._calculate_md5(file_path)
        sha256 = self._calculate_sha256(file_path)

        self.log_event('file_operation', {
            'operation': operation,
            'file': str(file_path),
            'size_bytes': file_path.stat().st_size,
            'md5': md5,
            'sha256': sha256
        })

    def finalize(self, status: str, summary: dict):
        """Save forensic report"""
        report = {
            'operation': self.operation,
            'year': self.year,
            'status': status,
            'start_time': self.start_time.isoformat(),
            'end_time': datetime.now().isoformat(),
            'duration_seconds': (datetime.now() - self.start_time).total_seconds(),
            'events': self.events,
            'summary': summary
        }

        report_path = Config.FORENSICS_DIR / f"{self.operation}_{self.year}.json"
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
```

### 6. Dynamic Year Discovery

**Pattern**: Auto-detect available data years

```python
@classmethod
def get_available_years(cls) -> List[int]:
    """
    Discover years from source folders

    Looks for folders matching patterns:
    - LAIT{YEAR}
    - GEST{YEAR}
    - CAISSE{99}
    """
    years = set()

    for pattern in ['LAIT*', 'GEST*', 'CAISSE*']:
        for folder in cls.PROJECT_ROOT.glob(pattern):
            if folder.is_dir():
                # Extract year from folder name
                year = cls._extract_year_from_name(folder.name)
                if year and 2000 <= year <= 2099:
                    years.add(year)

    return sorted(years)
```

---

## DBF File Handling

### Encoding Detection

**Challenge**: Legacy DBF files use various DOS encodings

**Solution**: Try multiple encodings sequentially

```python
DBF_ENCODINGS = ['cp850', 'cp437', 'latin1', 'utf-8']

def read_dbf_with_fallback(file_path: Path):
    """Try multiple encodings until one works"""
    for encoding in DBF_ENCODINGS:
        try:
            table = dbfread.DBF(file_path, encoding=encoding)
            records = list(table)
            return records, encoding
        except Exception as e:
            continue

    raise ValueError(f"Could not read DBF with any encoding: {file_path}")
```

### Common DBF Field Patterns

```python
# Typical field mappings
DBF_FIELD_MAPPINGS = {
    # Entries/Transactions
    'JOURN': 'code_journal',
    'PIECE': 'num_piece',
    'DATECR': 'date_ecriture',
    'COMPTE': 'num_compte',
    'AUXI': 'num_auxiliaire',
    'LIBEL': 'libelle',
    'DEBIT': 'montant_debit',
    'CREDIT': 'montant_credit',

    # Third parties
    'NAUXI': 'code_tiers',
    'NOM': 'nom',
    'ADRESSE': 'adresse',
    'VILLE': 'ville',
    'TEL': 'telephone',

    # Journals
    'CODE': 'code_journal',
    'INTITULE': 'intitule',
    'TYPE': 'type_journal'
}
```

---

## Data Validation Patterns

### Balance Validation

```python
def validate_balance(entries: List[dict], tolerance: float = 0.01) -> bool:
    """
    Validate double-entry bookkeeping balance

    Args:
        entries: List of accounting entries
        tolerance: Acceptable difference (default: 0.01 TND)

    Returns:
        True if balanced within tolerance
    """
    total_debit = sum(e['montant_debit'] for e in entries)
    total_credit = sum(e['montant_credit'] for e in entries)

    difference = abs(total_debit - total_credit)

    return difference <= tolerance
```

### Data Integrity Checks

```python
class DataValidator:
    @staticmethod
    def validate_entry(entry: dict) -> List[str]:
        """
        Validate single entry, return list of errors

        Returns empty list if valid
        """
        errors = []

        # Required fields
        required = ['date_ecriture', 'num_compte', 'libelle']
        for field in required:
            if not entry.get(field):
                errors.append(f"Missing required field: {field}")

        # Amount validation
        debit = entry.get('montant_debit', 0)
        credit = entry.get('montant_credit', 0)

        if debit < 0 or credit < 0:
            errors.append("Negative amounts not allowed")

        if debit > 0 and credit > 0:
            errors.append("Entry cannot have both debit and credit")

        if debit == 0 and credit == 0:
            errors.append("Entry must have debit or credit amount")

        return errors
```

---

## SQLite Normalization Pattern

### Schema Design

```python
def create_schema(self):
    """Create normalized tables"""
    cursor = self.conn.cursor()

    # Main transactions table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            system TEXT NOT NULL,
            year INTEGER NOT NULL,
            date_operation TEXT NOT NULL,
            date_parsed TEXT,
            code_journal TEXT,
            num_piece TEXT,
            num_compte TEXT NOT NULL,
            libelle TEXT,
            num_auxiliaire TEXT,
            montant_debit REAL DEFAULT 0,
            montant_credit REAL DEFAULT 0,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY (code_journal) REFERENCES journals(code_journal)
        )
    ''')

    # Journals/Categories table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS journals (
            code_journal TEXT PRIMARY KEY,
            intitule TEXT,
            type_journal TEXT,
            system TEXT
        )
    ''')

    # Create indexes for performance
    cursor.execute('''
        CREATE INDEX IF NOT EXISTS idx_entries_year
        ON entries(year)
    ''')

    cursor.execute('''
        CREATE INDEX IF NOT EXISTS idx_entries_date
        ON entries(date_parsed)
    ''')

    self.conn.commit()
```

### Batch Insert Pattern

```python
def insert_entries_batch(self, entries: List[dict], batch_size: int = 1000):
    """
    Insert entries in batches for performance

    Processing 10,000 records:
    - Single inserts: ~45 seconds
    - Batch inserts (1000): ~2 seconds
    """
    cursor = self.conn.cursor()

    for i in range(0, len(entries), batch_size):
        batch = entries[i:i + batch_size]

        cursor.executemany('''
            INSERT INTO entries (
                system, year, date_operation, num_compte,
                libelle, montant_debit, montant_credit
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', [
            (
                e['system'], e['year'], e['date'],
                e['compte'], e['libelle'],
                e['debit'], e['credit']
            )
            for e in batch
        ])

        self.conn.commit()
```

---

## Error Handling Strategy

### Batch Operations Pattern

```python
def migrate_all_years(years: List[int]):
    """
    Migrate multiple years with graceful error handling

    Strategy: Continue processing remaining years if one fails
    """
    results = {
        'successful': [],
        'failed': [],
        'errors': {}
    }

    for year in years:
        try:
            result = migrate_year(year)
            results['successful'].append(year)

        except Exception as e:
            results['failed'].append(year)
            results['errors'][year] = {
                'error': str(e),
                'type': type(e).__name__,
                'traceback': traceback.format_exc()
            }

            # Log but continue
            logger.error(f"Year {year} failed: {e}")
            continue

    # Generate summary report
    return results
```

### User-Friendly Error Messages

```python
class MigrationError(Exception):
    """Base exception with user-friendly messages"""

    def __init__(self, technical_message: str, user_message: str = None):
        self.technical_message = technical_message
        self.user_message = user_message or technical_message
        super().__init__(technical_message)

# Usage
try:
    migrate_year(2019)
except FileNotFoundError as e:
    raise MigrationError(
        technical_message=str(e),
        user_message=(
            f"Fichiers source introuvables pour l'année 2019.\n"
            f"Vérifiez que le dossier LAIT2019 existe.\n"
            f"📂 Emplacement attendu: {expected_path}"
        )
    )
```

---

## User Interface Patterns

### Multiple Interface Support

**Provide 3 interface modes**:

1. **GUI (PySide6)**: For end users
   - Progress bars, status updates
   - File selection dialogs
   - Error message boxes
   - Dashboard with statistics

2. **TUI (Rich)**: For advanced users
   - Interactive console menu
   - Beautiful tables and progress bars
   - Keyboard navigation

3. **CLI (Click)**: For automation/scripting
   - Command-line arguments
   - Scriptable operations
   - CI/CD integration

### Example: Service Layer Usage in Different UIs

```python
# GUI (PySide6)
class MigrationWindow(QMainWindow):
    def on_migrate_clicked(self):
        year = self.year_spinner.value()

        # Connect progress events
        self.service.emitter.on(
            EventType.OPERATION_PROGRESS,
            self.update_progress
        )

        # Run in worker thread
        self.worker = MigrationWorker(self.service, year)
        self.worker.start()

    def update_progress(self, event):
        self.progress_bar.setValue(int(event.progress * 100))
        self.status_label.setText(event.message)

# TUI (Rich)
def migrate_year_tui(year: int):
    service = AppService()

    with Progress() as progress:
        task = progress.add_task(f"Migrating {year}", total=100)

        def on_progress(event):
            progress.update(task, completed=event.progress * 100)

        service.emitter.on(EventType.OPERATION_PROGRESS, on_progress)
        result = service.migrate_year(year)

    console.print(f"[green]✓[/green] Migration complete: {result['records']} records")

# CLI (Click)
@click.command()
@click.option('--year', type=int, required=True)
def migrate(year: int):
    """Migrate single year"""
    service = AppService()

    try:
        result = service.migrate_year(year)
        click.echo(f"Success: {result['records']} records migrated")
        sys.exit(0)
    except Exception as e:
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)
```

---

## Build & Deployment

### Executable Creation (PyInstaller)

```python
# migration_app.spec
# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['main_gui.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('src', 'src'),  # Include source modules
    ],
    hiddenimports=[
        'PySide6.QtCore',
        'PySide6.QtWidgets',
        'dbfread',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='migration_izdihar',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # No console window for GUI
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='assets/icon.ico'
)
```

### Build Script

```bash
# build_exe.bat
@echo off
echo Building executable...

REM Clean previous builds
rmdir /s /q build dist

REM Build with PyInstaller
uv run pyinstaller migration_app.spec

echo.
echo Build complete! Executable: dist\migration_izdihar.exe
pause
```

---

## Key Lessons Learned

### 1. Never Modify Source Data
- Always work on copies
- Preserve original files for forensic purposes
- Use checksums to verify integrity

### 2. Validate at Every Stage
- DBF read: Check encoding, field names
- Conversion: Validate data types, ranges
- Database: Check balance, referential integrity
- Export: Verify format, encoding

### 3. Idempotency is Critical
- All operations must be re-runnable
- Use `CREATE TABLE IF NOT EXISTS`
- Check for existing outputs before overwriting
- Timestamp all outputs to preserve history

### 4. Forensic Logging is Non-Negotiable
- Log every file operation with checksums
- Timestamp all events (ISO 8601 format)
- Save both JSON (structured) and TXT (human-readable) reports
- Include system info (Python version, OS, etc.)

### 5. User Experience Matters
- Provide multiple UI options (GUI/TUI/CLI)
- Show progress for long operations
- Use clear, actionable error messages in French
- Include help text and documentation

### 6. Performance Optimization
- Use batch inserts (1000+ records at a time)
- Create database indexes
- Use generators for large datasets
- Profile before optimizing

### 7. Configuration Flexibility
- Allow user to configure paths
- Auto-detect years when possible
- Provide sensible defaults
- Save user preferences

---

## Recommended Project Structure for New Migration

```
02_AUDIT_PROGRAMME_LAIT_ALFA_CAISSE/
│
├── designDocs/                    # Documentation
│   ├── 00_Inception/
│   │   ├── 00_sprint_01.md
│   │   └── 01_MIGRATION_PATTERNS_FROM_ACCOUNTING.md  # This file
│   ├── 01_UserGuides/
│   └── 02_TechnicalGuides/
│
├── 00_Archives/                   # Validated source DBF files
│   ├── LAIT_2015/
│   ├── LAIT_2016/
│   ├── GEST_2015/
│   └── CAISSE_2015/
│
├── CONSOLIDATED_MIGRATION/        # Working directory
│   ├── 01_INPUT_DBF/
│   ├── 02_STAGE_INTERMEDIATE/
│   ├── 03_STAGE_SQLITE/
│   ├── 04_OUTPUT_FINAL/
│   ├── 05_FORENSICS_REPORTS/
│   ├── 06_BACKUPS/
│   └── 07_MAPPINGS/
│
├── src/                           # Source code
│   ├── __init__.py
│   ├── config.py                  # Central configuration
│   ├── app_service.py             # Service facade
│   ├── events.py                  # Event system
│   ├── forensics.py               # Audit logging
│   ├── dbf_reader.py              # DBF file handling
│   ├── sqlite_manager.py          # Database operations
│   ├── pipeline.py                # Migration orchestration
│   ├── validators.py              # Data validation
│   └── gui/                       # GUI modules (if needed)
│
├── tests/                         # Unit tests
├── scripts/                       # Utility scripts
│
├── main.py                        # TUI entry point
├── main_gui.py                    # GUI entry point (if needed)
├── pyproject.toml                 # UV project config
├── README.md                      # Project overview
└── .gitignore
```

---

## Next Steps for New Project

1. **Setup Project Structure**
   - Create directory hierarchy
   - Initialize git repository
   - Setup UV with `pyproject.toml`

2. **Inspect Source Data**
   - Identify all DBF files in LAIT/GEST/CAISSE folders
   - Compare duplicates using checksums
   - Select most recent/complete versions

3. **Copy to Archives**
   - Preserve folder structure
   - Document selection criteria
   - Generate checksums

4. **Implement Core Pipeline**
   - Start with `config.py` (paths, patterns)
   - Create `dbf_reader.py` (reuse from accounting)
   - Build `sqlite_manager.py` (adapted schema)
   - Develop `pipeline.py` (orchestration)

5. **Add Forensics**
   - Implement `forensics.py`
   - Log all operations
   - Generate reports

6. **Build UI** (choose based on needs)
   - CLI first (fastest to implement)
   - TUI if interactive needed
   - GUI if end-user facing

7. **Test & Validate**
   - Test with one year first
   - Validate data integrity
   - Batch process all years

---

## Summary

This accounting migration project provides a proven, production-ready architecture for migrating legacy Clipper/DBF systems. The key patterns to reuse:

- **Multi-stage pipeline** with intermediate outputs
- **Forensic logging** at every step
- **Layered architecture** with service facade
- **Event-driven progress** for responsive UIs
- **Configuration-driven** design for flexibility
- **SQLite normalization** for validation
- **Batch error handling** for resilience

Apply these patterns to the milk/feed/caisse migration for a reliable, maintainable, and professional solution.
