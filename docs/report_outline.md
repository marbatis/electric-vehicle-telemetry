# Report Outline Template

Use this structure to assemble the final notebook or written report. Replace the prompts with your findings and include the referenced figures/tables.

1. **Title & Abstract**
   - One-sentence project goal.
   - 2–3 sentences summarizing dataset, approach, and key results.

2. **Problem Definition & Success Criteria**
   - Business/technical motivation for EV RUL prediction.
   - Define supervised learning objective (regression + optional binary decision).
   - List evaluation metrics (RMSE, MAE, R², thresholded precision/recall).

3. **Data Provenance & Description**
   - Source citation and download details.
   - Dataset size, schema, diagnostics captured (capacity, HPPC, EIS, conditions).
   - Licensing and ethical considerations.
   - *Figure 1:* Table summarizing variables/types.

4. **Data Cleaning**
   - Outline missingness handling, type corrections, unit consistency.
   - Describe outlier detection and mitigation.
   - Document label construction (RUL, EOL threshold).
   - *Figure 2:* Missingness visualization.
   - *Figure 3:* Capacity vs. cycle plot with EOL line.

5. **Exploratory Data Analysis**
   - Key insights about degradation patterns and signal relationships.
   - *Figure 4:* RUL distribution.
   - *Figure 5:* Correlation heatmap or pairplots.
   - *Figure 6:* HPPC resistance vs. RUL (scatter/box).
   - Bullet list of insights guiding feature engineering.

6. **Feature Engineering**
   - Describe engineered features (capacity fade stats, resistance deltas, EIS aggregates, stability metrics).
   - Mention leakage prevention steps.

7. **Modeling Approach**
   - Train/validation/test split strategy (grouped CV, hold-out cells).
   - Baseline models and tree-based ensembles used.
   - Hyperparameter search process and tools.

8. **Results**
   - *Table 1:* Model leaderboard (CV mean ± std for RMSE/MAE/R²).
   - *Figure 7:* Predicted vs. actual RUL (parity plot).
   - *Figure 8:* Thresholded confusion matrix or PR curve (if binary variant).
   - Discuss performance differences and practical implications.

9. **Interpretability & Error Analysis**
   - Permutation/feature importance findings.
   - Partial dependence or accumulated local effects for top features.
   - Residual analysis across cells/C-rates/RUL bands.
   - Highlight failure cases and next steps.

10. **Conclusion & Future Work**
    - Recap achievements, limitations, and recommended improvements.
    - Outline future experimentation (alternate datasets, early-cycle prognosis).

11. **Reproducibility Notes**
    - Environment details (Python version, package list, random seeds).
    - Data access steps and any preprocessing scripts/notebooks.

12. **Appendix (Optional)**
    - Extended tables, additional plots, feature definitions, math derivations.

Keep notebook cells ordered and rerunnable from top to bottom; restart kernel before final export.
