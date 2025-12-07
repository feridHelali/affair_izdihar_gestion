#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DBF Files Inventory Script
Scans source folders and catalogs all DBF files with metadata
for forensic analysis and version comparison
"""

import os
import hashlib
from pathlib import Path
from datetime import datetime
import json
from typing import Dict, List, Tuple
from collections import defaultdict


class DBFInventory:
    """Forensic inventory of DBF files across legacy systems"""

    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.inventory = {
            'scan_date': datetime.now().isoformat(),
            'project_root': str(project_root),
            'systems': {
                'milk': {},      # LAIT system
                'feed': {},      # GEST/ALFA system
                'caisse': {}     # CAISSE system
            },
            'summary': {
                'total_folders': 0,
                'total_files': 0,
                'by_system': {}
            }
        }

    def calculate_file_hash(self, file_path: Path) -> Tuple[str, str]:
        """Calculate MD5 and SHA256 hashes for file integrity"""
        md5_hash = hashlib.md5()
        sha256_hash = hashlib.sha256()

        try:
            with open(file_path, 'rb') as f:
                # Read file in chunks to handle large files
                for chunk in iter(lambda: f.read(4096), b''):
                    md5_hash.update(chunk)
                    sha256_hash.update(chunk)

            return md5_hash.hexdigest(), sha256_hash.hexdigest()
        except Exception as e:
            print(f"Error hashing {file_path}: {e}")
            return None, None

    def get_file_metadata(self, file_path: Path) -> Dict:
        """Extract comprehensive file metadata"""
        try:
            stat = file_path.stat()
            md5, sha256 = self.calculate_file_hash(file_path)

            return {
                'filename': file_path.name,
                'path': str(file_path),
                'size_bytes': stat.st_size,
                'size_kb': round(stat.st_size / 1024, 2),
                'modified_date': datetime.fromtimestamp(stat.st_mtime).isoformat(),
                'created_date': datetime.fromtimestamp(stat.st_ctime).isoformat(),
                'md5': md5,
                'sha256': sha256,
                'extension': file_path.suffix.upper()
            }
        except Exception as e:
            print(f"Error getting metadata for {file_path}: {e}")
            return None

    def scan_directory(self, directory: Path, system_name: str) -> Dict:
        """Scan directory for DBF files recursively"""
        if not directory.exists():
            print(f"⚠️  Directory not found: {directory}")
            return {}

        print(f"\n📂 Scanning: {directory}")
        print(f"   System: {system_name}")

        dbf_files = []
        folder_info = {
            'path': str(directory),
            'name': directory.name,
            'scan_date': datetime.now().isoformat(),
            'dbf_files': [],
            'total_files': 0,
            'total_size_mb': 0
        }

        # Find all DBF files (case-insensitive)
        for dbf_file in directory.rglob('*.[Dd][Bb][Ff]'):
            metadata = self.get_file_metadata(dbf_file)
            if metadata:
                folder_info['dbf_files'].append(metadata)
                folder_info['total_files'] += 1
                folder_info['total_size_mb'] += metadata['size_bytes']

        folder_info['total_size_mb'] = round(folder_info['total_size_mb'] / (1024 * 1024), 2)

        print(f"   Found: {folder_info['total_files']} DBF files ({folder_info['total_size_mb']} MB)")

        return folder_info

    def scan_milk_system(self):
        """Scan LAIT (milk) system folders"""
        print("\n" + "="*60)
        print("🥛 SCANNING MILK (LAIT) SYSTEM")
        print("="*60)

        # Pattern: LAIT{YEAR} folders
        base_paths = [
            self.project_root / "Sauvegarde_2_HDD" / "IZDIHAR_HBIRA",
            self.project_root / "Sauvegarde_2_HDD" / "Sauvegarde_Disque_Alfa",
            self.project_root / "Sauvegarde_2_HDD",
        ]

        for base_path in base_paths:
            if not base_path.exists():
                continue

            # Look for LAIT folders
            for item in base_path.iterdir():
                if item.is_dir() and 'LAIT' in item.name.upper():
                    folder_key = item.name
                    folder_info = self.scan_directory(item, 'milk')
                    if folder_info and folder_info.get('total_files', 0) > 0:
                        self.inventory['systems']['milk'][folder_key] = folder_info

    def scan_feed_system(self):
        """Scan GEST/ALFA (cattle feed) system folders"""
        print("\n" + "="*60)
        print("🌾 SCANNING FEED (GEST/ALFA) SYSTEM")
        print("="*60)

        # Pattern: GEST{YEAR} folders
        base_paths = [
            self.project_root / "IZDIHAE_HBIRA_CAISSE_GESTION" / "IZDIHAR_ALFA_SAUVEGARDE",
        ]

        for base_path in base_paths:
            if not base_path.exists():
                continue

            # Look for GEST folders
            for item in base_path.iterdir():
                if item.is_dir() and 'GEST' in item.name.upper():
                    folder_key = item.name
                    folder_info = self.scan_directory(item, 'feed')
                    if folder_info and folder_info.get('total_files', 0) > 0:
                        self.inventory['systems']['feed'][folder_key] = folder_info

    def scan_caisse_system(self):
        """Scan CAISSE (cash/cheque) system folders"""
        print("\n" + "="*60)
        print("💰 SCANNING CAISSE (CASH/CHEQUE) SYSTEM")
        print("="*60)

        # Pattern: CAISSE folders
        base_paths = [
            self.project_root / "IZDIHAE_HBIRA_CAISSE_GESTION" / "CAISSE",
            self.project_root / "Sauvegarde_2_HDD" / "Izdihar_Hbira_Caisse_A_Jour",
        ]

        for base_path in base_paths:
            if not base_path.exists():
                continue

            # Look for CAISSE folders
            if base_path.is_dir():
                folder_key = base_path.name
                folder_info = self.scan_directory(base_path, 'caisse')
                if folder_info and folder_info.get('total_files', 0) > 0:
                    self.inventory['systems']['caisse'][folder_key] = folder_info

            # Also check subdirectories
            for item in base_path.iterdir():
                if item.is_dir() and 'CAISSE' in item.name.upper():
                    folder_key = f"{base_path.name}/{item.name}"
                    folder_info = self.scan_directory(item, 'caisse')
                    if folder_info and folder_info.get('total_files', 0) > 0:
                        self.inventory['systems']['caisse'][folder_key] = folder_info

    def generate_summary(self):
        """Generate summary statistics"""
        print("\n" + "="*60)
        print("📊 GENERATING SUMMARY")
        print("="*60)

        for system_name, folders in self.inventory['systems'].items():
            total_files = sum(f['total_files'] for f in folders.values())
            total_size = sum(f['total_size_mb'] for f in folders.values())

            self.inventory['summary']['by_system'][system_name] = {
                'total_folders': len(folders),
                'total_files': total_files,
                'total_size_mb': round(total_size, 2)
            }

            self.inventory['summary']['total_folders'] += len(folders)
            self.inventory['summary']['total_files'] += total_files

            print(f"\n{system_name.upper()}:")
            print(f"  Folders: {len(folders)}")
            print(f"  Files: {total_files}")
            print(f"  Size: {round(total_size, 2)} MB")

    def find_duplicates(self) -> Dict:
        """Find duplicate files across folders based on hash"""
        print("\n" + "="*60)
        print("🔍 ANALYZING DUPLICATES (by MD5 hash)")
        print("="*60)

        hash_map = defaultdict(list)
        duplicates = {}

        # Collect all files with their hashes
        for system_name, folders in self.inventory['systems'].items():
            for folder_name, folder_data in folders.items():
                for file_info in folder_data['dbf_files']:
                    if file_info['md5']:
                        hash_map[file_info['md5']].append({
                            'system': system_name,
                            'folder': folder_name,
                            'file': file_info
                        })

        # Find duplicates
        for md5_hash, file_list in hash_map.items():
            if len(file_list) > 1:
                # Group by filename
                filename = file_list[0]['file']['filename']
                if filename not in duplicates:
                    duplicates[filename] = []

                duplicates[filename].append({
                    'md5': md5_hash,
                    'occurrences': len(file_list),
                    'locations': file_list
                })

        # Print duplicates
        if duplicates:
            print(f"\nFound {len(duplicates)} duplicate file names:\n")
            for filename, dup_list in sorted(duplicates.items()):
                print(f"📄 {filename}:")
                for dup_group in dup_list:
                    print(f"   MD5: {dup_group['md5']}")
                    print(f"   Found in {dup_group['occurrences']} locations:")
                    for loc in dup_group['locations']:
                        file_info = loc['file']
                        print(f"     • {loc['folder']} ({file_info['size_kb']} KB, {file_info['modified_date'][:10]})")
        else:
            print("\n✓ No duplicates found")

        return duplicates

    def save_inventory(self, output_dir: Path):
        """Save inventory to JSON file"""
        output_dir.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = output_dir / f"dbf_inventory_{timestamp}.json"

        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(self.inventory, f, indent=2, ensure_ascii=False)

        print(f"\n✓ Inventory saved: {output_file}")

        # Also save human-readable report
        report_file = output_dir / f"dbf_inventory_report_{timestamp}.txt"
        self.save_report(report_file)

        return output_file

    def save_report(self, report_file: Path):
        """Save human-readable report"""
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write("="*80 + "\n")
            f.write("DBF FILES INVENTORY REPORT - IZDIHAR COOPERATIVE\n")
            f.write("="*80 + "\n\n")
            f.write(f"Scan Date: {self.inventory['scan_date']}\n")
            f.write(f"Project Root: {self.inventory['project_root']}\n\n")

            f.write("SUMMARY\n")
            f.write("-"*80 + "\n")
            f.write(f"Total Folders: {self.inventory['summary']['total_folders']}\n")
            f.write(f"Total Files: {self.inventory['summary']['total_files']}\n\n")

            for system_name, stats in self.inventory['summary']['by_system'].items():
                f.write(f"\n{system_name.upper()} SYSTEM:\n")
                f.write(f"  Folders: {stats['total_folders']}\n")
                f.write(f"  Files: {stats['total_files']}\n")
                f.write(f"  Size: {stats['total_size_mb']} MB\n")

            # Detailed file listings
            f.write("\n\n" + "="*80 + "\n")
            f.write("DETAILED FILE LISTINGS\n")
            f.write("="*80 + "\n\n")

            for system_name, folders in self.inventory['systems'].items():
                f.write(f"\n{'='*80}\n")
                f.write(f"{system_name.upper()} SYSTEM\n")
                f.write(f"{'='*80}\n")

                for folder_name, folder_data in sorted(folders.items()):
                    f.write(f"\n{'-'*80}\n")
                    f.write(f"Folder: {folder_name}\n")
                    f.write(f"Path: {folder_data['path']}\n")
                    f.write(f"Files: {folder_data['total_files']} ({folder_data['total_size_mb']} MB)\n")
                    f.write(f"{'-'*80}\n\n")

                    for file_info in sorted(folder_data['dbf_files'], key=lambda x: x['filename']):
                        f.write(f"  {file_info['filename']:<30} {file_info['size_kb']:>8.2f} KB  {file_info['modified_date'][:10]}\n")
                        f.write(f"    MD5: {file_info['md5']}\n")

        print(f"✓ Report saved: {report_file}")

    def run_full_scan(self):
        """Execute complete inventory scan"""
        print("\n" + "="*60)
        print("🚀 STARTING DBF INVENTORY SCAN")
        print("="*60)
        print(f"Project Root: {self.project_root}")

        # Scan all systems
        self.scan_milk_system()
        self.scan_feed_system()
        self.scan_caisse_system()

        # Generate summary and analysis
        self.generate_summary()
        duplicates = self.find_duplicates()

        # Save results
        output_dir = self.project_root / "02_AUDIT_PROGRAMME_LAIT_ALFA_CAISSE" / "designDocs" / "00_Inception" / "inventory_reports"
        self.save_inventory(output_dir)

        print("\n" + "="*60)
        print("✓ SCAN COMPLETE")
        print("="*60)


def main():
    """Main execution"""
    # Project root is parent of current working directory
    project_root = Path(__file__).resolve().parent.parent.parent

    print(f"Project Root: {project_root}")

    inventory = DBFInventory(project_root)
    inventory.run_full_scan()


if __name__ == "__main__":
    main()
