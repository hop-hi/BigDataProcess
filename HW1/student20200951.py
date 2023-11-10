#!/usr/bin/python3

import csv

# 파일 이름
input_file = 'student.xlsx'
output_file = 'student_updated.xlsx'

# 가중치
weights = {'midterm': 0.30, 'final': 0.35, 'homework': 0.34, 'attendance': 0.01}

# 학점 부여 함수
def calculate_grade(total_score, total_scores):
    total_students = len(total_scores)
    if total_score < 40:
        return 'F'
    elif total_score >= 90:
        return 'A+'
    elif total_score >= 80:
        if total_scores.count('A') / total_students < 0.3:
            return 'A'
        else:
            return 'B+'
    elif total_score >= 70:
        if total_scores.count('A') / total_students < 0.3:
            return 'A'
        elif total_scores.count('A+') / total_students < 0.5:
            return 'A+'
        else:
            return 'B'
    else:
        return 'C+'

# 총 점수 계산 및 학점 부여
total_scores = []
with open(input_file, 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    data = list(reader)
    for row in data:
        total_score = 0
        for key, value in row.items():
            if key in weights:
                total_score += float(value) * weights[key]
        total_scores.append(total_score)
        row['Grade'] = calculate_grade(total_score, total_scores)

# 학번을 기준으로 정렬
data.sort(key=lambda x: x['id'])

# 엑셀 파일에 쓰기
with open(output_file, 'w', newline='') as csv_file:
    fieldnames = data[0].keys()
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

import csv

# 파일 이름
input_file = 'student.xlsx'
output_file = 'student_updated.xlsx'

# 가중치
weights = {'midterm': 0.30, 'final': 0.35, 'homework': 0.34, 'attendance': 0.01}

# 학점 부여 함수
def calculate_grade(total_score, total_scores):
    total_students = len(total_scores)
    if total_score < 40:
        return 'F'
    elif total_score >= 90:
        return 'A+'
    elif total_score >= 80:
        if total_scores.count('A') / total_students < 0.3:
            return 'A'
        else:
            return 'B+'
    elif total_score >= 70:
        if total_scores.count('A') / total_students < 0.3:
            return 'A'
        elif total_scores.count('A+') / total_students < 0.5:
            return 'A+'
        else:
            return 'B'
    else:
        return 'C+'

# 총 점수 계산 및 학점 부여
total_scores = []
with open(input_file, 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    data = list(reader)
    for row in data:
        total_score = 0
        for key, value in row.items():
            if key in weights:
                total_score += float(value) * weights[key]
        total_scores.append(total_score)
        row['Grade'] = calculate_grade(total_score, total_scores)

# 학번을 기준으로 정렬
data.sort(key=lambda x: x['id'])

# 엑셀 파일에 쓰기
with open(output_file, 'w', newline='') as csv_file:
    fieldnames = data[0].keys()
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

import csv

# 파일 이름
input_file = 'student.xlsx'
output_file = 'student_updated.xlsx'

# 가중치
weights = {'midterm': 0.30, 'final': 0.35, 'homework': 0.34, 'attendance': 0.01}

# 학점 부여 함수
def calculate_grade(total_score, total_scores):
    total_students = len(total_scores)
    if total_score < 40:
        return 'F'
    elif total_score >= 90:
        return 'A+'
    elif total_score >= 80:
        if total_scores.count('A') / total_students < 0.3:
            return 'A'
        else:
            return 'B+'
    elif total_score >= 70:
        if total_scores.count('A') / total_students < 0.3:
            return 'A'
        elif total_scores.count('A+') / total_students < 0.5:
            return 'A+'
        else:
            return 'B'
    else:
        return 'C+'

# 총 점수 계산 및 학점 부여
total_scores = []
with open(input_file, 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    data = list(reader)
    for row in data:
        total_score = 0
        for key, value in row.items():
            if key in weights:
                total_score += float(value) * weights[key]
        total_scores.append(total_score)
        row['Grade'] = calculate_grade(total_score, total_scores)

# 학번을 기준으로 정렬
data.sort(key=lambda x: x['id'])

# 엑셀 파일에 쓰기
with open(output_file, 'w', newline='') as csv_file:
    fieldnames = data[0].keys()
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

import csv

# 파일 이름
input_file = 'student.xlsx'
output_file = 'student_updated.xlsx'

# 가중치
weights = {'midterm': 0.30, 'final': 0.35, 'homework': 0.34, 'attendance': 0.01}

# 학점 부여 함수
def calculate_grade(total_score, total_scores):
    total_students = len(total_scores)
    if total_score < 40:
        return 'F'
    elif total_score >= 90:
        return 'A+'
    elif total_score >= 80:
        if total_scores.count('A') / total_students < 0.3:
            return 'A'
        else:
            return 'B+'
    elif total_score >= 70:
        if total_scores.count('A') / total_students < 0.3:
            return 'A'
        elif total_scores.count('A+') / total_students < 0.5:
            return 'A+'
        else:
            return 'B'
    else:
        return 'C+'

# 총 점수 계산 및 학점 부여
total_scores = []
with open(input_file, 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    data = list(reader)
    for row in data:
        total_score = 0
        for key, value in row.items():
            if key in weights:
                total_score += float(value) * weights[key]
        total_scores.append(total_score)
        row['Grade'] = calculate_grade(total_score, total_scores)

# 학번을 기준으로 정렬
data.sort(key=lambda x: x['id'])

# 엑셀 파일에 쓰기
with open(output_file, 'w', newline='') as csv_file:
    fieldnames = data[0].keys()
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

import csv

# 파일 이름
input_file = 'student.xlsx'
output_file = 'student_updated.xlsx'

# 가중치
weights = {'midterm': 0.30, 'final': 0.35, 'homework': 0.34, 'attendance': 0.01}

# 학점 부여 함수
def calculate_grade(total_score, total_scores):
    total_students = len(total_scores)
    if total_score < 40:
        return 'F'
    elif total_score >= 90:
        return 'A+'
    elif total_score >= 80:
        if total_scores.count('A') / total_students < 0.3:
            return 'A'
        else:
            return 'B+'
    elif total_score >= 70:
        if total_scores.count('A') / total_students < 0.3:
            return 'A'
        elif total_scores.count('A+') / total_students < 0.5:
            return 'A+'
        else:
            return 'B'
    else:
        return 'C+'

# 총 점수 계산 및 학점 부여
total_scores = []
with open(input_file, 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    data = list(reader)
    for row in data:
        total_score = 0
        for key, value in row.items():
            if key in weights:
                total_score += float(value) * weights[key]
        total_scores.append(total_score)
        row['Grade'] = calculate_grade(total_score, total_scores)

# 학번을 기준으로 정렬
data.sort(key=lambda x: x['id'])

# 엑셀 파일에 쓰기
with open(output_file, 'w', newline='') as csv_file:
    fieldnames = data[0].keys()
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

import csv

# 파일 이름
input_file = 'student.xlsx'
output_file = 'student_updated.xlsx'

# 가중치
weights = {'midterm': 0.30, 'final': 0.35, 'homework': 0.34, 'attendance': 0.01}

# 학점 부여 함수
def calculate_grade(total_score, total_scores):
    total_students = len(total_scores)
    if total_score < 40:
        return 'F'
    elif total_score >= 90:
        return 'A+'
    elif total_score >= 80:
        if total_scores.count('A') / total_students < 0.3:
            return 'A'
        else:
            return 'B+'
    elif total_score >= 70:
        if total_scores.count('A') / total_students < 0.3:
            return 'A'
        elif total_scores.count('A+') / total_students < 0.5:
            return 'A+'
        else:
            return 'B'
    else:
        return 'C+'

# 총 점수 계산 및 학점 부여
total_scores = []
with open(input_file, 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    data = list(reader)
    for row in data:
        total_score = 0
        for key, value in row.items():
            if key in weights:
                total_score += float(value) * weights[key]
        total_scores.append(total_score)
        row['Grade'] = calculate_grade(total_score, total_scores)

# 학번을 기준으로 정렬
data.sort(key=lambda x: x['id'])

# 엑셀 파일에 쓰기
with open(output_file, 'w', newline='') as csv_file:
    fieldnames = data[0].keys()
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

import csv

# 파일 이름
input_file = 'student.xlsx'
output_file = 'student_updated.xlsx'

# 가중치
weights = {'midterm': 0.30, 'final': 0.35, 'homework': 0.34, 'attendance': 0.01}

# 학점 부여 함수
def calculate_grade(total_score, total_scores):
    total_students = len(total_scores)
    if total_score < 40:
        return 'F'
    elif total_score >= 90:
        return 'A+'
    elif total_score >= 80:
        if total_scores.count('A') / total_students < 0.3:
            return 'A'
        else:
            return 'B+'
    elif total_score >= 70:
        if total_scores.count('A') / total_students < 0.3:
            return 'A'
        elif total_scores.count('A+') / total_students < 0.5:
            return 'A+'
        else:
            return 'B'
    else:
        return 'C+'

# 총 점수 계산 및 학점 부여
total_scores = []
with open(input_file, 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    data = list(reader)
    for row in data:
        total_score = 0
        for key, value in row.items():
            if key in weights:
                total_score += float(value) * weights[key]
        total_scores.append(total_score)
        row['Grade'] = calculate_grade(total_score, total_scores)

# 학번을 기준으로 정렬
data.sort(key=lambda x: x['id'])

# 엑셀 파일에 쓰기
with open(output_file, 'w', newline='') as csv_file:
    fieldnames = data[0].keys()
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

import csv

# 파일 이름
input_file = 'student.xlsx'
output_file = 'student_updated.xlsx'

# 가중치
weights = {'midterm': 0.30, 'final': 0.35, 'homework': 0.34, 'attendance': 0.01}

# 학점 부여 함수
def calculate_grade(total_score, total_scores):
    total_students = len(total_scores)
    if total_score < 40:
        return 'F'
    elif total_score >= 90:
        return 'A+'
    elif total_score >= 80:
        if total_scores.count('A') / total_students < 0.3:
            return 'A'
        else:
            return 'B+'
    elif total_score >= 70:
        if total_scores.count('A') / total_students < 0.3:
            return 'A'
        elif total_scores.count('A+') / total_students < 0.5:
            return 'A+'
        else:
            return 'B'
    else:
        return 'C+'

# 총 점수 계산 및 학점 부여
total_scores = []
with open(input_file, 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    data = list(reader)
    for row in data:
        total_score = 0
        for key, value in row.items():
            if key in weights:
                total_score += float(value) * weights[key]
        total_scores.append(total_score)
        row['Grade'] = calculate_grade(total_score, total_scores)

# 학번을 기준으로 정렬
data.sort(key=lambda x: x['id'])

# 엑셀 파일에 쓰기
with open(output_file, 'w', newline='') as csv_file:
    fieldnames = data[0].keys()
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

import csv

# 파일 이름
input_file = 'student.xlsx'
output_file = 'student_updated.xlsx'

# 가중치
weights = {'midterm': 0.30, 'final': 0.35, 'homework': 0.34, 'attendance': 0.01}

# 학점 부여 함수
def calculate_grade(total_score, total_scores):
    total_students = len(total_scores)
    if total_score < 40:
        return 'F'
    elif total_score >= 90:
        return 'A+'
    elif total_score >= 80:
        if total_scores.count('A') / total_students < 0.3:
            return 'A'
        else:
            return 'B+'
    elif total_score >= 70:
        if total_scores.count('A') / total_students < 0.3:
            return 'A'
        elif total_scores.count('A+') / total_students < 0.5:
            return 'A+'
        else:
            return 'B'
    else:
        return 'C+'

# 총 점수 계산 및 학점 부여
total_scores = []
with open(input_file, 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    data = list(reader)
    for row in data:
        total_score = 0
        for key, value in row.items():
            if key in weights:
                total_score += float(value) * weights[key]
        total_scores.append(total_score)
        row['Grade'] = calculate_grade(total_score, total_scores)

# 학번을 기준으로 정렬
data.sort(key=lambda x: x['id'])

# 엑셀 파일에 쓰기
with open(output_file, 'w', newline='') as csv_file:
    fieldnames = data[0].keys()
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

