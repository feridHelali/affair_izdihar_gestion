## Inception

### Objectives 
Implement a System (Desktop Application) that migrate 3 legacy programs dbf/clipper data files to Sage Commercial Application or add-hoc sub-system or both in Context of forensic process (Customer : Cooperative IZDIHAR)
- the first legacy program is a kind of dbf/clipper program that manage milk collection and distribution (like warehouse/invoicing systems)
- the second legacy program is a kind od dbf/clipper program that mange/distribute  cattle feed, livestock feed, or animal feed from state organization (regulator), some food factory ... from/to agriculture as participant in the cooperative.
- the third legacy program is a "Caisse" dbf/clipper program ie:manage cash/ cheques/ and fees ...

NB: the programer of these systems may be manually or automatically integrate (Kind of data transfer) between these systems an accounting system (by the way it is programmed using dbf/clipper tech)

### Current State :
- In the folder D:\40_Cooperative_IZDIHAR_Lazhar_LATTAOUI\Sauvegarde_2_HDD and D:\40_Cooperative_IZDIHAR_Lazhar_LATTAOUI\IZDIHAE_HBIRA_CAISSE_GESTION contains copies (bad backup management) of these systems
- Warnings : 
    - You many find copies of the same system , the name of cash/cheque management usually stored in Folder with pattern "CAISSE{99}" french term
    - The same for cattle feed management it is stored in folders with patten : "GEST{YEAR}"
    - The same for milk program it is stored in folders with pattern : either "LAIT{YEAR}" or just {99}

### Todo:
- Break down the problem / solution in most efficient respecting forensic Tunisia practice
- Inspect dbf files and compare (metadata file) and the content of file to choose the most significant folder/files
- Once fixed sept before / copy all necessary files (dbf) to D:\40_Cooperative_IZDIHAR_Lazhar_LATTAOUI\02_AUDIT_PROGRAMME_LAIT_ALFA_CAISSE\00_Archives preserving th file structure and it's Ok to rename with most relevant names according to the context
- I have implement such thing for accounting assisted by many LLMs, AI Agents (Claude, Grok, Copilot) at folder D:\40_Cooperative_IZDIHAR_Lazhar_LATTAOUI\MIGRATION_CLIPPER_TO_SAGE_CIEL_2025 that contain design decision patterns, programming language, tools, paradigms,... preferences

-- the folder D:\40_Cooperative_IZDIHAR_Lazhar_LATTAOUI contain other resources (Recovery with EasyRecovery) restored after criminal delete (there an affaire in progress) , feel free (but no match) to look at (reason 18GB) you can ignore recovery folders
