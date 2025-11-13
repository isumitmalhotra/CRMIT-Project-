# 🧬 CRMIT Exosome/EV Analysis Project

**Comprehensive Data Analysis Platform for Extracellular Vesicle Characterization**

[![Project Status](https://img.shields.io/badge/Status-Active-success)]()
[![Phase](https://img.shields.io/badge/Phase-1%3A%20Data%20Processing-blue)]()
[![Progress](https://img.shields.io/badge/Progress-8%25-yellow)]()
[![Deadline](https://img.shields.io/badge/Deadline-Mid%20January%202026-red)]()

---

## 📖 Project Overview

This project develops an **end-to-end automated pipeline** for analyzing Extracellular Vesicles (EVs/Exosomes) using:
- **nanoFACS** (nano Flow Cytometry Analysis) - 70 FCS files
- **NTA** (Nanoparticle Tracking Analysis) - 86 text files
- **AWS S3** cloud storage for all data
- **Baseline + Iterations Workflow** - Compare test runs vs controls

**Client:** Bio Varam via CRMIT  
**Application:** iPSC-derived exosome characterization for therapeutic development  
**Timeline:** 12-14 weeks (Nov 13, 2025 - Early February 2026)

---

## 📁 Repository Structure

```
├── � TASK_TRACKER.md              # Task tracking and progress monitoring (ACTIVE)
├── 📄 EXECUTIVE_SUMMARY.md         # 2-page quick reference for meetings
├── 🏗️ UNIFIED_DATA_FORMAT_STRATEGY.md  # Data schema definitions with baseline workflow
├── � DATA_FORMATS_FOR_ML_GUIDE.md # Parquet vs JSON/CSV analysis
├── 🔍 CRMIT_ARCHITECTURE_ANALYSIS.md   # Architecture validation (80% alignment)
├── 📝 MEETING_PRESENTATION_MASTER_DOC.md  # 93-page presentation guide
├── 🆕 MEETING_INSIGHTS_ANALYSIS_NOV13.md  # Latest meeting findings (Baseline workflow)
├── 📋 UPDATE_SUMMARY_NOV13.md      # Nov 13 changes log
├── 📚 Literature/                  # Scientific references and standards
│   ├── FCMPASS_Software-Aids-EVs-Light-Scatter-Stand.pdf
│   ├── Mie functions_scattering_Abs-V1.pdf
│   └── Mie functions_scattering_Abs-V2.pdf
├── 🔬 nanoFACS/                    # Flow cytometry data (FCS files)
│   ├── 10000 exo and cd81/         # CD81 antibody titration (21 files)
│   ├── CD9 and exosome lots/       # CD9 testing + lot variability (24 files)
│   └── EXP 6-10-2025/              # Dilution series experiment (25 files)
├── 📊 NTA/                         # Nanoparticle tracking data (TXT files)
│   ├── EV_IPSC_P1_19_2_25_NTA/     # Passage 1 (27 files)
│   ├── EV_IPSC_P2_27_2_25_NTA/     # Passage 2 (28 files)
│   ├── EV_IPSC_P2.1_28_2_25_NTA/   # Passage 2.1 (31 files)
│   └── Dataset 1.xlsx              # Consolidated NTA results
└── 💻 Project IT data/              # Analysis scripts and processed data
    ├── Take path and meta convert to csv.py  # FCS parser (existing)
    ├── metatest.csv                # Sample metadata output
    ├── test.csv                    # Sample event data
    └── Technical documentation/
```

---

## 🚀 Quick Start

### Prerequisites
```bash
Python 3.8+
Git
```

### Installation
```bash
# Clone the repository
git clone https://github.com/isumitmalhotra/CRMIT-Project-.git
cd CRMIT-Project-

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies (coming soon)
pip install -r requirements.txt
```

---

## 📚 Documentation

| Document | Description |
|----------|-------------|
| **[TASK_TRACKER.md](TASK_TRACKER.md)** | Real-time task status and progress tracking (PRIMARY) |
| **[EXECUTIVE_SUMMARY.md](EXECUTIVE_SUMMARY.md)** | 2-page quick reference for stakeholder meetings |
| **[UNIFIED_DATA_FORMAT_STRATEGY.md](UNIFIED_DATA_FORMAT_STRATEGY.md)** | Data schema definitions with baseline + iterations workflow |
| **[CRMIT_ARCHITECTURE_ANALYSIS.md](CRMIT_ARCHITECTURE_ANALYSIS.md)** | Architecture validation vs CRMIT design (80% alignment) |
| **[MEETING_INSIGHTS_ANALYSIS_NOV13.md](MEETING_INSIGHTS_ANALYSIS_NOV13.md)** | Nov 13 meeting findings (baseline workflow discovery) |
| **[DATA_FORMATS_FOR_ML_GUIDE.md](DATA_FORMATS_FOR_ML_GUIDE.md)** | Parquet format analysis (12-20x compression vs JSON) |
| `docs/` (Coming Soon) | Technical guides, API docs, user manuals |

---

## 🎯 Project Phases

### ✅ Phase 0: Setup & Planning (COMPLETE)
- [x] Repository setup
- [x] Data organization
- [x] Comprehensive documentation

### 🟡 Phase 1: Data Processing (IN PROGRESS - 8%)
- [ ] **Task 1.1:** Enhanced FCS Parser (Parquet + Baseline workflow + S3)
- [ ] **Task 1.2:** NTA Parser (ZetaView text files + S3)
- [ ] **Task 1.3:** Data Integration (Baseline comparison + ML-ready dataset)
- [ ] **Task 1.6:** AWS S3 Storage Integration ⭐ NEW (Client requirement)
- ⏸️ **Task 1.4/1.5:** TEM Module (DEFERRED - no sample data yet)

### ⏳ Phase 2: Analysis & Visualization (NOT STARTED)
- [ ] Exploratory data analysis
- [ ] Interactive dashboard
- [ ] Quality control module

### ⏳ Phase 3: Machine Learning (NOT STARTED)
- [ ] Predictive models
- [ ] Pattern recognition
- [ ] Anomaly detection

### ⏳ Phase 4: Deployment (PLANNING)
- [ ] Automated pipeline
- [ ] Web application & API
- [ ] Production deployment

---

## 📊 Current Data Assets

### Flow Cytometry Data (nanoFACS)
- **70 FCS files** across 3 experimental batches
- **26 parameters** per sample (FSC, SSC, 6 fluorescence channels)
- **~339K events per file** (23.7M total events)
- **Workflow:** 1 biological sample = 5-6 FCS files (baseline + iterations)
- **Experiments:** CD81/CD9 antibody optimization, SEC vs Centrifugation

### Nanoparticle Tracking (NTA)
- **86 TXT files** across 3 passages (P1, P2, P2.1)
- **Size distribution** (D10, D50, D90) and **concentration** measurements
- **11-position scanning** for spatial uniformity validation
- **Typical:** 1 NTA measurement per biological sample

### Storage
- **AWS S3** for all raw and processed data (client approved)
- **Parquet format** for processed data (78% compression vs CSV)

---

## 🔬 Key Scientific Questions

1. ❓ What is the optimal antibody concentration for CD81 and CD9?
2. ❓ Which preparation method is better (SEC vs Centrifugation)?
3. ❓ How consistent are EVs across different cell passages and lots?
4. ❓ What are the ideal dilution factors for each assay?
5. ❓ **How much does marker expression increase vs baseline (isotype)?** ⭐ NEW
6. ❓ Can we predict EV quality from early measurements?

**NEW Workflow Understanding (Nov 13, 2025):**
- Scientists run baseline (isotype control) FIRST
- Then run SAME biological sample 5-6 times with different antibodies
- System must compare each test to its baseline
- Calculate % increase, fold change, statistical significance

---

## 🛠️ Technology Stack

**Languages:** Python 3.8+, SQL  
**Data Processing:** pandas, numpy, fcsparser, scipy, pyarrow, dask  
**Storage:** AWS S3 (boto3), Parquet format (Snappy compression)  
**Visualization:** matplotlib, seaborn, plotly  
**Dashboard:** Dash / Streamlit  
**ML/AI:** scikit-learn, XGBoost  
**Web:** FastAPI / Flask  
**Deployment:** Docker, AWS, Git

**Key Technologies:**
- **Apache Parquet:** 78% smaller than CSV, 10x faster loading
- **AWS S3:** Centralized cloud storage for all data
- **Dask:** Parallel processing for large datasets
- **Baseline Workflow:** Two-level ID system (biological_sample + measurement)

---

## 📈 Progress Tracking

**Overall Progress:** 8%  
**Deadline:** Mid-January 2026 (Phase 1: nanoFACS + NTA only)

| Phase | Progress | Status |
|-------|----------|--------|
| Phase 1: Data Processing | 🟡🟡⚪⚪⚪⚪⚪⚪⚪⚪ 15% | Planning complete, implementation starting |
| Phase 2: Analysis | ⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪ 0% | Waiting on Phase 1 |
| Phase 3: ML & Analytics | ⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪ 0% | Waiting on Phase 1 |
| Phase 4: Deployment | 🟡🟡⚪⚪⚪⚪⚪⚪⚪⚪ 10% | GitHub repo + documentation |

**Recent Updates (Nov 13, 2025):**
- ✅ Baseline + iterations workflow discovered and documented
- ✅ AWS S3 storage approved by client
- ✅ All schemas updated for baseline comparisons
- ✅ Task 1.6 added (S3 Integration)
- ✅ Timeline revised: 12-14 weeks

**Last Updated:** November 13, 2025

For detailed task status, see [TASK_TRACKER.md](TASK_TRACKER.md)

---

## 🤝 Contributing

This is a client project for CRMIT/Bio Varam. For questions or collaboration:
- Review [PROJECT_ANALYSIS.md](PROJECT_ANALYSIS.md) for technical details
- Check [TASK_TRACKER.md](TASK_TRACKER.md) for current priorities
- Submit issues or pull requests

---

## 📝 Changelog

### [0.4.0] - 2025-11-13
- 🆕 **Major Update:** Integrated Nov 13 meeting feedback
- Added baseline + iterations workflow support
- Added AWS S3 storage integration
- Created MEETING_INSIGHTS_ANALYSIS_NOV13.md (25 pages)
- Updated all schemas for biological_sample_id + measurement_id
- Added new Task 1.6 (S3 Integration)
- Timeline revised to 12-14 weeks
- Cleaned up 7 redundant documentation files

### [0.3.0] - 2025-11-13
- Added EXECUTIVE_SUMMARY.md (2-page quick reference)
- Added 12-week detailed sprint timeline
- Added CRMIT_ARCHITECTURE_ANALYSIS.md (118 pages)
- Added MEETING_PRESENTATION_MASTER_DOC.md (93 pages)
- Confirmed Phase 1 scope: nanoFACS + NTA only

### [0.2.0] - 2025-11-12
- Added UNIFIED_DATA_FORMAT_STRATEGY.md
- Added DATA_FORMATS_FOR_ML_GUIDE.md
- Added TASK_TRACKER.md for progress monitoring
- Added README.md

### [0.1.0] - 2025-11-12
- Initial repository setup
- Committed all project data (206 files)
- Organized folder structure

---

## 📞 Contact

**Project Repository:** https://github.com/isumitmalhotra/CRMIT-Project-  
**Client:** Bio Varam via CRMIT  
**Data Scientist:** AI Solution Architect

---

## ⚠️ Important Notes

- **Large Files:** Some data files exceed 50MB. Consider Git LFS for future additions.
- **Data Privacy:** Ensure compliance with data handling protocols.
- **Active Development:** This project is under active development.

---

## 📄 License

Proprietary - CRMIT/Bio Varam Client Project

---

**🔗 Quick Links:**
- [� Task Tracker](TASK_TRACKER.md) - **PRIMARY REFERENCE**
- [📄 Executive Summary](EXECUTIVE_SUMMARY.md) - Quick 2-page overview
- [🏗️ Data Schema](UNIFIED_DATA_FORMAT_STRATEGY.md) - Technical specifications
- [🔍 Architecture Analysis](CRMIT_ARCHITECTURE_ANALYSIS.md) - Client alignment
- [🆕 Latest Updates](MEETING_INSIGHTS_ANALYSIS_NOV13.md) - Nov 13 meeting findings
- [🔬 Literature](Literature/) - Scientific references
- [📊 nanoFACS Data](nanoFACS/) - 70 FCS files
- [📈 NTA Data](NTA/) - 86 text files

---

*For the most up-to-date information, always refer to TASK_TRACKER.md and MEETING_INSIGHTS_ANALYSIS_NOV13.md*
