# -*- coding: utf-8 -*-
"""
L1 Attrition Model: Testing the hypothesis that L1 is protected from attrition in an L1-dominant environment.

Scenario A (L1 Environment): L1 baseline is protected by daily use and top-down support.
Scenario B (L2 Environment): L1 baseline declines due to disuse and sustained L2/L3 inhibition.

Compares L1 activation trajectories under both scenarios during 6 months of L3 learning.
"""

import numpy as np
import matplotlib.pyplot as plt

# =============================================
# 1. Shared Parameters
# =============================================
L1_baseline_initial = 0.8  # L1 Chinese initial baseline
L2_baseline = 0.5  # L2 English baseline (stable)
L3_baseline_start = 0.1  # L3 Japanese initial baseline

learning_rate = 0.008  # Daily L3 increase
days = 180  # 6 months
measurement_days = [0, 30, 90, 180]  # Month 0, 1, 3, 6
inhibition = 0.7  # Mutual inhibition strength
decay = 0.1  # Natural decay
input_strength = 0.1  # External input strength
steps = 100  # Time steps per trial

# L1 daily decline rates under two environments
L1_decay_L1_env = 0.001  # L1 environment: negligible decline
L1_decay_L2_env = 0.005  # L2 environment: significant decline


# =============================================
# 2. Core Simulation Function
# =============================================
def simulate_competition(L1_base, L2_base, L3_base):
    L1_act = np.zeros(steps)
    L2_act = np.zeros(steps)
    L3_act = np.zeros(steps)

    L1_act[0] = 0.0
    L2_act[0] = 0.0
    L3_act[0] = 0.0

    for t in range(1, steps):
        inp_L1 = input_strength * L1_base
        inp_L2 = input_strength * L2_base
        inp_L3 = input_strength * L3_base

        decay_L1 = decay * L1_act[t - 1]
        decay_L2 = decay * L2_act[t - 1]
        decay_L3 = decay * L3_act[t - 1]

        inhib_L1 = inhibition * (L2_act[t - 1] + L3_act[t - 1])
        inhib_L2 = inhibition * (L1_act[t - 1] + L3_act[t - 1])
        inhib_L3 = inhibition * (L1_act[t - 1] + L2_act[t - 1])

        L1_act[t] = L1_act[t - 1] + inp_L1 - decay_L1 - inhib_L1
        L2_act[t] = L2_act[t - 1] + inp_L2 - decay_L2 - inhib_L2
        L3_act[t] = L3_act[t - 1] + inp_L3 - decay_L3 - inhib_L3

        L1_act[t] = max(0, L1_act[t])
        L2_act[t] = max(0, L2_act[t])
        L3_act[t] = max(0, L3_act[t])

    return np.max(L1_act)


# =============================================
# 3. Simulation Loop for Both Scenarios
# =============================================
results_L1_env = {}
results_L2_env = {}
daily_L1_env = []
daily_L2_env = []

# Initialize L1 baselines for both scenarios
L1_env_baseline = L1_baseline_initial
L2_env_baseline = L1_baseline_initial
L3_current = L3_baseline_start

for day in range(days + 1):
    # Scenario A: L1 Environment
    peak_L1_env = simulate_competition(L1_env_baseline, L2_baseline, L3_current)
    daily_L1_env.append(peak_L1_env)

    # Scenario B: L2 Environment
    peak_L2_env = simulate_competition(L2_env_baseline, L2_baseline, L3_current)
    daily_L2_env.append(peak_L2_env)

    if day in measurement_days:
        month = {0: 0, 30: 1, 90: 3, 180: 6}[day]
        results_L1_env[month] = peak_L1_env
        results_L2_env[month] = peak_L2_env
        print(
            f"Day {day} (Month {month}): L1_env={peak_L1_env:.4f}, L2_env={peak_L2_env:.4f}, L3 base={L3_current:.4f}")

    # Daily updates
    L1_env_baseline -= L1_decay_L1_env
    L2_env_baseline -= L1_decay_L2_env
    L3_current += learning_rate

    # Ensure non-negative
    L1_env_baseline = max(0, L1_env_baseline)
    L2_env_baseline = max(0, L2_env_baseline)

# =============================================
# 4. Visualization (adjusted)
# =============================================
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Left panel: Daily L1 activation
ax = axes[0]
ax.plot(daily_L1_env, label='L1 Environment (Protected)', color='blue', alpha=0.8)
ax.plot(daily_L2_env, label='L2 Environment (Attrition)', color='red', alpha=0.8)
ax.set_title('L1 Activation: Attrition vs. Protection')
ax.set_xlabel('Day')
ax.set_ylabel('L1 Peak Activation')
ax.set_xlim(0, 180)  # 新增这一行
ax.legend()
ax.axhline(y=L1_baseline_initial, color='gray', linestyle='--', alpha=0.5)

# Right panel: Bar chart at measurement points
ax = axes[1]
months = [0, 1, 3, 6]
x = np.arange(len(months))
width = 0.35
bars_A = ax.bar(x - width/2, [results_L1_env[m] for m in months], width, label='L1 Environment', color='blue', alpha=0.7)
bars_B = ax.bar(x + width/2, [results_L2_env[m] for m in months], width, label='L2 Environment', color='red', alpha=0.7)
ax.set_title('L1 Peak at Measurement Points')
ax.set_ylabel('L1 Peak Activation')
ax.set_xticks(x)
ax.set_xticklabels([f'Month {m}' for m in months])
ax.set_xlim(-0.5, 3.5)  # 可选：让柱状图两边也留一点空间
ax.legend()
ax.set_ylim(0, 1.0)

plt.tight_layout()
plt.savefig('l1_attrition_model.png', dpi=150)
plt.show()