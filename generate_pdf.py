"""
PDF Generator for Developer Onboarding Guide
Converts DEVELOPER_ONBOARDING_GUIDE.md to a formatted PDF

Requirements:
pip install markdown2 reportlab
"""

import os
from datetime import datetime
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.lib import colors
from reportlab.pdfgen import canvas

def generate_pdf():
    """Generate PDF from the markdown content"""
    
    # File paths
    project_root = os.path.dirname(os.path.abspath(__file__))
    output_pdf = os.path.join(project_root, "DEVELOPER_ONBOARDING_GUIDE.pdf")
    
    # Create PDF
    doc = SimpleDocTemplate(
        output_pdf,
        pagesize=letter,
        rightMargin=0.75*inch,
        leftMargin=0.75*inch,
        topMargin=1*inch,
        bottomMargin=0.75*inch
    )
    
    # Container for the 'Flowable' objects
    story = []
    
    # Define styles
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#1a237e'),
        spaceAfter=30,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Normal'],
        fontSize=12,
        textColor=colors.grey,
        spaceAfter=12,
        alignment=TA_CENTER,
        fontName='Helvetica'
    )
    
    heading1_style = ParagraphStyle(
        'CustomHeading1',
        parent=styles['Heading1'],
        fontSize=18,
        textColor=colors.HexColor('#1976d2'),
        spaceAfter=12,
        spaceBefore=12,
        fontName='Helvetica-Bold'
    )
    
    heading2_style = ParagraphStyle(
        'CustomHeading2',
        parent=styles['Heading2'],
        fontSize=14,
        textColor=colors.HexColor('#0288d1'),
        spaceAfter=10,
        spaceBefore=10,
        fontName='Helvetica-Bold'
    )
    
    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['BodyText'],
        fontSize=10,
        leading=14,
        alignment=TA_JUSTIFY,
        spaceAfter=8
    )
    
    code_style = ParagraphStyle(
        'CustomCode',
        parent=styles['Code'],
        fontSize=9,
        fontName='Courier',
        textColor=colors.HexColor('#d32f2f'),
        leftIndent=20,
        spaceAfter=8
    )
    
    # Title Page
    story.append(Spacer(1, 1*inch))
    story.append(Paragraph("🎓 Complete Developer Onboarding Guide", title_style))
    story.append(Paragraph("CRMIT Exosome/EV Analysis Project", subtitle_style))
    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph("For: Python Full-Stack Developers", subtitle_style))
    story.append(Paragraph("Client: Bio Varam via CRMIT", subtitle_style))
    story.append(Paragraph(f"Date: {datetime.now().strftime('%B %d, %Y')}", subtitle_style))
    story.append(Spacer(1, 0.5*inch))
    
    # Info box
    info_data = [
        ['Project Type:', 'Biomedical Data Science & AI'],
        ['Technologies:', 'Python, Flow Cytometry, NTA, ML'],
        ['Scope:', 'End-to-end automated analysis pipeline'],
        ['Impact:', 'Medical-grade therapeutic development']
    ]
    info_table = Table(info_data, colWidths=[2*inch, 4*inch])
    info_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#e3f2fd')),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#90caf9'))
    ]))
    story.append(info_table)
    story.append(PageBreak())
    
    # Table of Contents
    story.append(Paragraph("📋 Table of Contents", heading1_style))
    story.append(Spacer(1, 0.2*inch))
    
    toc_items = [
        "1. The Science - What Are We Analyzing?",
        "2. The Machines - How Do We Measure?",
        "3. The Experiments - What Were They Testing?",
        "4. What CRMIT Needs to Build",
        "5. Technical Deep Dive - Data Flow",
        "6. Key Parameters & Calculations",
        "7. Questions for Tech Lead",
        "8. Learning Path",
        "9. Project Impact"
    ]
    
    for item in toc_items:
        story.append(Paragraph(item, body_style))
    
    story.append(PageBreak())
    
    # Main Content Sections
    sections = [
        {
            'title': 'Part 1: The Science - What Are We Actually Analyzing?',
            'content': [
                '<b>What are Exosomes/Extracellular Vesicles (EVs)?</b>',
                'Think of EVs as <b>tiny biological packages</b> that cells naturally release:',
                '• <b>Size:</b> 30-200 nanometers (nm)',
                '• <b>Comparison:</b> A human hair is ~80,000 nm wide. These are 400-2500 times smaller!',
                '• <b>Function:</b> Cells use them to communicate, like biological text messages',
                '• <b>Contents:</b> Proteins, RNA, lipids - basically cellular cargo',
                '',
                '<b>Why Does This Matter?</b>',
                '1. <b>Medical Diagnostics:</b> EVs carry disease markers',
                '2. <b>Therapeutics:</b> Can be loaded with drugs for targeted delivery',
                '3. <b>Regenerative Medicine:</b> iPSC-derived EVs can help tissue repair',
                '4. <b>Research:</b> Understanding cell communication',
                '',
                '<b>This Project Specifically:</b>',
                '• Client (Bio Varam) is producing EVs from iPSCs',
                '• They want to ensure quality, consistency, and characterization',
                '• These EVs might be used for therapeutic purposes'
            ]
        },
        {
            'title': 'Part 2: The Machines - How Do We Measure?',
            'content': [
                '<b>Machine 1: CytoFLEX nano (nanoFACS)</b>',
                '',
                'A specialized flow cytometer designed for nanoparticles.',
                '',
                '<b>How It Works:</b>',
                '1. Sample flows through a tiny tube',
                '2. Laser beams hit each particle one-by-one',
                '3. Particles scatter light in different directions',
                '4. Fluorescent antibodies (if bound) emit light',
                '5. Detectors measure: Forward Scatter (FSC) → size, Side Scatter (SSC) → complexity',
                '6. Computer records data for ~300,000-500,000 individual particles',
                '',
                '<b>The Data You\'ll Work With:</b>',
                '• FCS Files: Binary files, 35-55 MB per sample',
                '• 26 parameters per particle',
                '• Format: FCS 3.1 standard (requires special parser)',
                '',
                '<b>Machine 2: ZetaView (NTA - Nanoparticle Tracking Analysis)</b>',
                '',
                'A microscope-based system that tracks particle movement.',
                '',
                '<b>Key Physics:</b>',
                '• Particles undergo Brownian motion (random jiggling)',
                '• Smaller particles move faster (less mass)',
                '• Larger particles move slower (more mass)',
                '• Software calculates size from movement speed',
                '',
                '<b>The Data You\'ll Work With:</b>',
                '• TXT Files: Plain text, 10-50 KB',
                '• Size distribution and concentration data',
                '• 11-position scans for quality assurance'
            ]
        },
        {
            'title': 'Part 3: What CRMIT Needs to Build',
            'content': [
                '<b>Client\'s Pain Points:</b>',
                '1. Manual data processing (days/weeks per experiment)',
                '2. No standardized analysis',
                '3. No automated quality control',
                '4. No integrated view (FCS and NTA separate)',
                '5. No predictive capability',
                '',
                '<b>Your Complete System:</b>',
                '',
                '1. DATA INGESTION LAYER',
                '   • FCS File Parser (binary → structured data)',
                '   • NTA File Parser (text → structured data)',
                '   • Metadata Extraction',
                '   • Data Validation',
                '',
                '2. PROCESSING LAYER',
                '   • Data Cleaning',
                '   • Data Transformation',
                '   • Data Integration',
                '   • Database Storage (SQLite/PostgreSQL)',
                '',
                '3. ANALYSIS LAYER',
                '   • Statistical Analysis',
                '   • Quality Control Module',
                '   • Comparative Analysis',
                '   • Exploratory Data Analysis',
                '',
                '4. VISUALIZATION LAYER',
                '   • Interactive Dashboard (Dash/Streamlit)',
                '   • Static Reports (PDF)',
                '   • Real-time Monitoring',
                '   • Export Capabilities',
                '',
                '5. MACHINE LEARNING LAYER (Advanced)',
                '   • Quality Prediction',
                '   • Antibody Optimization',
                '   • Anomaly Detection',
                '',
                '6. DEPLOYMENT LAYER',
                '   • Web Application',
                '   • REST API',
                '   • Automated Pipeline',
                '   • Docker Containers'
            ]
        },
        {
            'title': 'Part 4: Your Learning Path',
            'content': [
                '<b>Week 1: Domain Knowledge (5-7 hours)</b>',
                '• Flow Cytometry Basics (YouTube tutorials)',
                '• Extracellular Vesicles (MISEV2018 guidelines)',
                '• NTA Technology (ZetaView docs)',
                '• Read Literature PDFs in project folder',
                '',
                '<b>Week 2: Data Formats (5-7 hours)</b>',
                '• FCS File Format (FCS 3.1 standard)',
                '• Practice with fcsparser library',
                '• Statistical Analysis for Biology',
                '',
                '<b>Week 3: Technical Implementation</b>',
                '• Start coding parsers',
                '• Database design',
                '• Basic visualizations',
                '',
                '<b>Key Skills to Develop:</b>',
                '✓ Binary file parsing (FCS format)',
                '✓ Statistical analysis (scipy, statsmodels)',
                '✓ Scientific visualization (matplotlib, plotly)',
                '✓ Dashboard development (Streamlit/Dash)',
                '✓ Database design for scientific data',
                '✓ Bioinformatics best practices'
            ]
        },
        {
            'title': 'Part 5: Project Impact',
            'content': [
                '<b>Before Your System:</b>',
                '• Lab technician: 2 days to analyze one experiment',
                '• No standardization',
                '• Only 1-2 experiments analyzed per week',
                '• Wasting expensive reagents',
                '',
                '<b>After Your System:</b>',
                '• Automated analysis in 10 minutes',
                '• Standardized, reproducible results',
                '• Analyze entire experimental series instantly',
                '• Data-driven optimization (save $10K+ on antibodies)',
                '• Real-time QC catches problems immediately',
                '• Scale from 150 to 10,000+ samples',
                '',
                '<b>Business Impact:</b>',
                '✓ Regulatory compliance (FDA requirements)',
                '✓ Speed to market (faster development)',
                '✓ Cost reduction (optimize protocols)',
                '✓ Quality assurance (prevent bad batches)',
                '✓ Competitive advantage',
                '',
                '<b>Your Career Growth:</b>',
                'This project gives you experience in:',
                '• Bioinformatics (specialized domain)',
                '• Data Engineering (complex ETL pipelines)',
                '• Scientific Computing (statistical analysis, ML)',
                '• Full-Stack Development (backend + frontend)',
                '• Domain Expertise (coding + biology)',
                '',
                '<b>Career paths this opens:</b>',
                '• Bioinformatics Developer',
                '• Scientific Software Engineer',
                '• Computational Biologist',
                '• Data Engineer (Healthcare/Pharma)',
                '• ML Engineer (Biotech)',
                '',
                '<b>Salary premium:</b> Biotech + Python + Domain Knowledge = High value'
            ]
        }
    ]
    
    # Add sections to story
    for section in sections:
        story.append(Paragraph(section['title'], heading1_style))
        story.append(Spacer(1, 0.2*inch))
        
        for line in section['content']:
            if line == '':
                story.append(Spacer(1, 0.1*inch))
            else:
                story.append(Paragraph(line, body_style))
        
        story.append(PageBreak())
    
    # Summary page
    story.append(Paragraph("🎬 Your Action Plan", heading1_style))
    story.append(Spacer(1, 0.2*inch))
    
    action_items = [
        '<b>This Week:</b>',
        '1. ✓ Read this entire document',
        '2. Read the Literature PDFs (2-3 hours)',
        '3. Watch flow cytometry tutorial videos (1-2 hours)',
        '4. Install fcsparser, open one FCS file',
        '5. Plot FSC vs SSC scatter plot',
        '6. List questions for tech lead meeting',
        '',
        '<b>Next Week:</b>',
        '1. Meet with tech lead',
        '2. Set up development environment',
        '3. Start Task 1.1 - Enhance FCS parser',
        '4. Process first batch of files (5-10 files)',
        '5. Generate sample visualizations',
        '',
        '<b>Month 1 Goal:</b>',
        '✓ All FCS and NTA files parsed',
        '✓ Basic statistical analysis working',
        '✓ Simple dashboard prototype',
        '✓ Initial results to show client'
    ]
    
    for item in action_items:
        story.append(Paragraph(item, body_style))
    
    story.append(Spacer(1, 0.3*inch))
    
    # Final message
    final_message = ParagraphStyle(
        'FinalMessage',
        parent=styles['Normal'],
        fontSize=12,
        textColor=colors.HexColor('#1976d2'),
        alignment=TA_CENTER,
        fontName='Helvetica-Bold',
        spaceAfter=12
    )
    
    story.append(Paragraph("Remember: You're not just coding - you're enabling scientific discovery!", final_message))
    story.append(Paragraph("Your code might help develop life-saving therapeutics.", final_message))
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("You've got this! 🚀", final_message))
    
    # Build PDF
    doc.build(story)
    
    print(f"✅ PDF generated successfully: {output_pdf}")
    return output_pdf

if __name__ == "__main__":
    try:
        pdf_path = generate_pdf()
        print(f"\n📄 PDF saved to: {pdf_path}")
        print("\n📚 Documents created:")
        print("   1. DEVELOPER_ONBOARDING_GUIDE.pdf (This PDF)")
        print("   2. DEVELOPER_ONBOARDING_GUIDE.md (Markdown version)")
        print("   3. MEETING_PREPARATION_CHECKLIST.md (Meeting prep)")
        print("\n✨ You're all set for the project!")
    except Exception as e:
        print(f"❌ Error generating PDF: {e}")
        print("\nNote: This script requires:")
        print("   pip install reportlab")
        print("\nAlternatively, you can use an online markdown to PDF converter")
        print("with the DEVELOPER_ONBOARDING_GUIDE.md file.")
