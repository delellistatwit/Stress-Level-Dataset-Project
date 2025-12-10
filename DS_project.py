# -*- coding: utf-8 -*-
"""
Created on Sun Nov 30 20:31:54 2025

@author: tyler
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("StressLevelDataset.csv")  #loads dataset

numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns

mean_scores = df[numeric_cols].mean().sort_values(ascending=False)

print("Top 10 Stressors (Ranked by Average Score):")
print(mean_scores.head(10))

print("\n")
# Count how many times each stressor received the maximum stress rating (5)
max_votes = (df[numeric_cols] == 5).sum().sort_values(ascending=False)

print("Top Stressors by Max Stress Votes (Score = 5):")
print(max_votes.head(10))

print("\n")
categories = {
    "Psychological": [
        "anxiety_level", "self_esteem", "mental_health_history", "depression"
    ],
    "Physiological": [
        "headache", "blood_pressure", "sleep_quality", "breathing_problem"
    ],
    "Environmental": [
        "noise_level", "living_conditions", "safety", "basic_needs"
    ],
    "Academic": [
        "academic_performance", "study_load", "teacher_student_relationship", "future_career_concerns"
    ],
    "Social": [
        "social_support", "peer_pressure", "extracurricular_activities", "bullying"
    ]
}

category_means = {cat: df[cols].mean().mean() for cat, cols in categories.items()}

print("\nAverage Stress Score by Category:")
for cat, value in category_means.items():
    print(f"{cat}: {value:.2f}")
    
print("\nTop Stressor in Each Category:")
for cat, cols in categories.items():
    top = df[cols].mean().sort_values(ascending=False).head(1)
    print(f"{cat}: {top.index[0]} ({top.values[0]:.2f})")
    

print("\nGenerating scatterplots for each category...")

for cat, cols in categories.items():
    plt.figure(figsize=(9,6))

    for i, col in enumerate(cols):
        # Grab all votes (1–5) for this stressor
        votes = df[col]

        # Add jitter so points don't overlap
        x_positions = np.random.normal(loc=i, scale=0.05, size=len(votes))

        # Scatter the points
        plt.scatter(x_positions, votes, alpha=0.3, s=20, label=col)

    plt.title(f"{cat} Stressor Vote Distribution (1–5)", fontsize=14)
    plt.xlabel(f"{cat} Stressors", fontsize=12)
    plt.ylabel("Vote Value (1–5)", fontsize=12)
    plt.xticks(range(len(cols)), cols, rotation=45, ha='right')
    plt.yticks([1,2,3,4,5])
    plt.ylim(0.5, 5.5)
    plt.grid(True, linestyle='--', alpha=0.3)

    plt.tight_layout()
    plt.savefig(f"{cat}_VoteDistribution_Scatterplot.png", dpi=300)
    plt.show()

    print(f"{cat} scatterplot saved as {cat}_VoteDistribution_Scatterplot.png")
    
    