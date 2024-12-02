#!/usr/bin/env python3

# Advent 2


with open("../rosalind_data/advent2.txt", 'r') as infile:
    lines = infile.readlines()
    stripped = []
    for line in lines:
        stripped.append(line.strip())

reports = stripped

def is_safe(report):
    increasing = all(report[i] < report[i+1] for i in range(len(report) - 1))
    decreasing = all(report[i] > report[i+1] for i in range(len(report) - 1))
    if not (increasing or decreasing):
        return False
    
    for i in range(len(report) - 1):
        if not (1 <= abs(report[i] - report[i+1]) <= 3):            
            return False
        
    return True

def number_of_safe(reports_total):
    safe_count = 0
    for report in reports_total:
        if is_safe(report):
            safe_count += 1
        return safe_count
    
safe_report_count = number_of_safe(reports)
print(safe_report_count)