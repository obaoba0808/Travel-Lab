# -*- coding: utf-8 -*-
import os

report_path = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab\golightly_audit_20260528.md'

with open(report_path, 'w', encoding='utf-8') as f:
    f.write('# golightly.fun Audit Report\n')
    f.write('**Date**: 2026-05-28\n')
    f.write('**Scope**: SEO / UX / Monetization\n')
    f.write('**Files**: 36 HTML files\n\n')
    f.write('---\n\n')
    
    f.write('## 1. Content Duplicate Check\n\n')
    f.write('### Method\n')
    f.write('Scan all HTML files for duplicate content in sections.\n\n')
    
    f.write('### Issues Found\n\n')
    f.write('#### 1.1 Inconsistent Sections\n')
    f.write('Not all articles have essential sections.\n\n')
    
    f.write('| File | Xiao Bian | Shi Zhan | FAQ | Trip CTA | Klook CTA |\n')
    f.write('|------|---------|----------|-----|----------|----------|\n')
    f.write('| tokyo-5days.html | NO | NO | YES (6) | YES (5) | YES (2) |\n')
    f.write('| kansai-pass.html | YES | NO | YES (8) | YES (1) | YES (2) |\n')
    f.write('| osaka-food.html | YES | YES | YES (6) | YES (1) | YES (1) |\n')
    f.write('| seoul-food.html | YES | NO | YES (9) | YES (4) | YES (1) |\n')
    f.write('| bangkok-3days.html | YES | NO | YES (7) | YES (1) | NO |\n\n')
    
    f.write('**Problem**: Inconsistent user experience across articles.\n\n')
    f.write('---\n\n')

print('Part 1 written successfully')
