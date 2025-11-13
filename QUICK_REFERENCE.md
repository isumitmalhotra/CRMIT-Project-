# Quick Reference - Development Setup

**Last Updated:** November 13, 2025

---

## Installation

```bash
# 1. Create virtual environment
python -m venv venv

# 2. Activate environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Verify installation
python -c "import fcsparser, pandas, boto3; print('All dependencies installed!')"
```

---

## Project Structure

```
EV (Exosome) Project/
├── scripts/              # Python implementation
│   ├── parse_fcs.py     # FCS parser
│   ├── parse_nta.py     # NTA parser
│   ├── s3_utils.py      # AWS S3 utilities
│   └── integrate_data.py # Data integration
├── config/              # Configuration files
│   ├── s3_config.json
│   ├── parser_rules.json
│   └── qc_thresholds.json
├── tests/               # Unit tests
├── test_data/           # Sample files (not in git)
│   ├── nanofacs/
│   └── nta/
├── docs/                # Documentation
└── requirements.txt     # Dependencies
```

---

## Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=scripts

# Run specific test file
pytest tests/test_parser.py

# Run specific test
pytest tests/test_parser.py::TestFCSParser::test_filename_parsing
```

---

## Key Files

| File | Purpose |
|------|---------|
| `UNIFIED_DATA_FORMAT_STRATEGY.md` | Complete schema definitions |
| `TASK_TRACKER.md` | All tasks and progress |
| `FILENAME_PARSING_RULES.md` | Parsing documentation |
| `PROJECT_SETUP_COMPLETE.md` | Setup summary |
| `README.md` | Project overview |

---

## Common Commands

```bash
# Parse single FCS file (once implemented)
python scripts/parse_fcs.py --file "path/to/file.fcs" --output "output.parquet"

# Parse all FCS files in folder
python scripts/parse_fcs.py --folder "nanoFACS/CD9 and exosome lots/"

# Parse NTA file
python scripts/parse_nta.py --file "path/to/nta.txt"

# Upload to S3
python scripts/s3_utils.py upload --file "data.parquet" --s3-path "processed_data/"
```

---

## Configuration

### AWS S3 Setup

```bash
# Set environment variables (Windows PowerShell)
$env:AWS_ACCESS_KEY_ID="your_key"
$env:AWS_SECRET_ACCESS_KEY="your_secret"

# Or create .env file
AWS_ACCESS_KEY_ID=your_key
AWS_SECRET_ACCESS_KEY=your_secret
AWS_DEFAULT_REGION=us-east-1
```

### Edit Config Files

- **S3 Settings:** `config/s3_config.json`
- **Parsing Rules:** `config/parser_rules.json`
- **QC Thresholds:** `config/qc_thresholds.json`

---

## Git Workflow

```bash
# Check status
git status

# Stage changes
git add .

# Commit
git commit -m "Description of changes"

# Push
git push

# Pull latest
git pull
```

---

## Debugging

### Check Python Environment
```bash
python --version
pip list
```

### Test FCS Parser
```bash
python -c "import fcsparser; print(fcsparser.__version__)"
```

### Test AWS Connection
```bash
python -c "import boto3; s3 = boto3.client('s3'); print('S3 connected!')"
```

---

## Important Notes

⚠️ **Never commit:**
- AWS credentials
- `.env` files
- `.fcs` or `.parquet` data files
- `__pycache__/` directories

✅ **Always commit:**
- Code changes in `scripts/`
- Configuration changes
- Documentation updates
- Test files

---

## Getting Help

1. Check `docs/FILENAME_PARSING_RULES.md` for parsing issues
2. Check `TASK_TRACKER.md` for task details
3. Check `UNIFIED_DATA_FORMAT_STRATEGY.md` for schema info
4. Review function docstrings in code files

---

## Next Steps (Week 1)

1. Install dependencies
2. Configure AWS credentials
3. Implement FCS parser (`parse_fcs.py`)
4. Test on sample files
5. Start NTA parser

**Deadline:** Week 1 checkpoint - November 19, 2025

