---
tags:
  - course
  - statistics
---

# BSMA1002 Statistics for Data Science I

**Course Credits**: 4

**Course Type**: Foundational

**Instructor**: Usha Mohan

**Pre-requisites**: None

## Overview
Students explore large datasets and learn how to extract insights from data. Basic probability is introduced along with random variables and key distributions.

## Learning Objectives
- Create, download and analyse data sets
- Frame questions using variables and cases
- Describe data using numerical summaries and visualisations
- Estimate chance using probability laws
- Model real-world situations with probability
- Calculate expectation and variance of random variables
- Apply properties of the Binomial and Normal distributions

## Course Structure
12 weeks of coursework with weekly online assignments, two invigilated quizzes and one invigilated end term exam.

## Weekly Topics
1.  **Introduction & Data Types**
    *   **What is Statistics?**:
        *   Definition: Statistics is the science of collecting, organizing, analyzing, interpreting, and presenting data.
        *   Importance: It helps in making informed decisions in various fields like business, medicine, social sciences, engineering, and is a cornerstone of data science.
    *   **Scope of Statistics**:
        *   Descriptive Statistics: Involves methods of organizing, summarizing, and presenting data in an informative way. This includes measures like mean, median, mode, and graphical displays like histograms, bar charts, etc. Example: Calculating the average marks of students in a class.
        *   Inferential Statistics: Involves methods used to draw conclusions or make inferences about a larger group (population) based on information obtained from a smaller group (sample). Example: Predicting election results based on a sample survey.
    *   **Population vs. Sample**:
        *   Population (N): The complete set of all individuals, items, or data of interest. For example, all students in a university.
        *   Sample (n): A subset of the population selected for study. For example, 100 students selected from that university.
        *   Parameter: A numerical value summarizing a characteristic of a population. Usually denoted by Greek letters (e.g., population mean μ, population standard deviation σ).
        *   Statistic: A numerical value summarizing a characteristic of a sample. Usually denoted by Roman letters (e.g., sample mean x̄, sample standard deviation s).
        *   Reason for Sampling: Studying the entire population may be too costly, time-consuming, or impractical. Samples allow us to get manageable data.
        *   Random Sampling: Techniques where each member of the population has a known chance of being selected, aiming to get a representative sample (e.g., Simple Random Sampling).
    *   **Variables**:
        *   A characteristic or attribute that can assume different values for different individuals or items. Examples: age, gender, income, test score.
    *   **Types of Data (Scales of Measurement)**:
        *   **Qualitative (Categorical) Data**: Represents categories or labels.
            *   Nominal Scale: Data consist of names, labels, or categories that cannot be ordered. Arithmetic operations are meaningless. Examples: Gender (Male, Female), Eye Color (Blue, Brown, Green), Country of Origin.
            *   Ordinal Scale: Data can be arranged in some order, but differences between data values either cannot be determined or are meaningless. Examples: Education Level (High School, Bachelor's, Master's, PhD), Survey Ratings (Poor, Fair, Good, Excellent), Social Class (Lower, Middle, Upper).
        *   **Quantitative (Numerical) Data**: Represents numerical values.
            *   Discrete Data: Values are countable and often integers. There are gaps between possible values. Examples: Number of children in a family (0, 1, 2...), Number of cars sold, Number of defects in a product.
            *   Continuous Data: Values can take on any numerical value within a given range (measurable). Examples: Height (165.2 cm, 170.5 cm), Weight, Temperature, Time.
            *   Interval Scale: Data can be ordered, and differences between data values are meaningful. However, there is no true zero point (a point that indicates absence of the quantity). Ratios are not meaningful. Examples: Temperature in Celsius or Fahrenheit (0°C doesn't mean no temperature; 20°C is not twice as hot as 10°C), Calendar Years (Year 0 is arbitrary).
            *   Ratio Scale: Data can be ordered, differences are meaningful, and there is a true zero point. Ratios between values are meaningful. Examples: Height (0 cm means no height, 200 cm is twice as tall as 100 cm), Weight, Age, Income, Number of items.
    *   **How to Summarize Data (Overview)**:
        *   Frequency Distributions: Organizing data into tables showing how often each value or category occurs.
        *   Graphical Displays: Visualizing data using charts and graphs (e.g., bar charts, pie charts, histograms).
        *   Numerical Summaries: Calculating statistics that describe central tendency (e.g., mean, median) and dispersion (e.g., variance, standard deviation).
    *   **Data Collection Methods (Brief Overview)**:
        *   Surveys: Collecting data by asking questions (e.g., questionnaires, interviews).
        *   Experiments: Manipulating one or more variables to observe the effect on another variable (e.g., clinical trials).
        *   Observational Studies: Observing and measuring characteristics without attempting to modify the subjects being studied (e.g., watching animal behavior in the wild).
        *   Primary Data: Data collected directly by the researcher for a specific purpose.
        *   Secondary Data: Data collected by someone else that the researcher uses (e.g., government statistics, existing databases).
2.  **Describing Categorical Data**
    *   **Frequency Distribution for Categorical Data**:
        *   Frequency (f): The count of observations falling into each category.
        *   Relative Frequency (rf): The proportion of observations falling into each category. Calculated as: Relative Frequency = Frequency / Total number of observations (n). It can be expressed as a decimal or a percentage.
        *   Frequency Table / Contingency Table (for one variable): A table that lists each category and its corresponding frequency and/or relative frequency.
            Example: Survey of 50 people's favorite fruit.
            | Fruit   | Frequency (f) | Relative Frequency (rf) |
            |---------|---------------|-------------------------|
            | Apple   | 15            | 15/50 = 0.30 (30%)      |
            | Banana  | 20            | 20/50 = 0.40 (40%)      |
            | Orange  | 10            | 10/50 = 0.20 (20%)      |
            | Other   | 5             | 5/50  = 0.10 (10%)      |
            | Total   | 50            | 1.00 (100%)             |
    *   **Graphical Displays for Categorical Data**:
        *   Bar Charts (Bar Graphs):
            *   Construction: Categories are displayed on one axis (usually horizontal) and frequencies or relative frequencies are displayed on the other axis (usually vertical). Bars are drawn for each category with height proportional to its frequency. Bars should be of equal width and have gaps between them to emphasize the distinctness of categories.
            *   Interpretation: Allows for easy comparison of the frequency of different categories.
        *   Pie Charts:
            *   Construction: A circle divided into sectors, where each sector represents a category and its area (or angle) is proportional to the category's relative frequency. Angle = Relative Frequency * 360°.
            *   Interpretation: Best for showing how each category contributes to the whole (i.e., parts of 100%).
            *   Limitations: Can be difficult to compare sizes of sectors, especially if there are many categories or if frequencies are similar. Generally not recommended for more than 5-7 categories.
        *   Pareto Charts (Optional but good):
            *   A type of bar chart where the bars are arranged in descending order of frequency from left to right. A cumulative frequency line is often overlaid.
            *   Purpose: Helps to identify the "vital few" categories that contain the bulk of the observations (Pareto Principle - 80/20 rule).
    *   **Measures of Central Tendency for Categorical Data**:
        *   Mode: The category that occurs with the highest frequency.
            *   A dataset can be unimodal (one mode), bimodal (two modes), or multimodal (more than two modes). If all categories have the same frequency, there is no mode.
            *   Example: In the fruit survey above, the mode is "Banana".
        *   Median (for Ordinal Data): The middle category when the data are ordered.
            *   To find the median for ordinal data:
                1. Arrange the observed categories in ascending or descending order.
                2. If the total number of observations (n) is odd, the median is the category of the ((n+1)/2)-th observation.
                3. If n is even, the median falls between two categories; often, it's reported by identifying both or through specific conventions if applicable. For purely ordinal data, a single "middle" category might not be precise if it falls between two different categories after ordering.
            *   Example: Ratings: Poor, Poor, Good, Good, Good, Excellent, Excellent. Ordered: Poor, Poor, Good, Good, Good, Excellent, Excellent (n=7). Median is the (7+1)/2 = 4th observation, which is "Good".
            *   Mean is not suitable for nominal data as categories don't have numerical values. For ordinal data, assigning numerical scores to categories to calculate a mean can be done but is often debated and depends on the assumption of equal spacing between categories.
    *   **Best Practices for Graphing Categorical Data**:
        *   Always provide a clear title for the chart.
        *   Label axes and categories clearly.
        *   Ensure the scale for frequencies (on bar charts) starts at zero to avoid misrepresentation.
        *   Avoid using 3D effects on bar charts or pie charts as they can distort perception of sizes/proportions.
        *   Choose the chart type that best conveys the information (e.g., pie chart for parts of a whole, bar chart for comparing frequencies).
3.  **Describing Numerical Data**
    *   **Frequency Distribution for Numerical Data**:
        *   Classes/Bins: For continuous or discrete data with many values, data is grouped into intervals called classes or bins.
            *   Choosing Class Width: Should be manageable and appropriate for the data. Too wide may hide details; too narrow may result in too few observations per class. (Number of classes often between 5 and 20).
            *   Class Boundaries: Must be clearly defined to avoid ambiguity (e.g., 10-19, 20-29 or [10, 20), [20, 30)).
        *   Frequency Table: Lists the classes and their corresponding frequencies (number of data points falling into each class).
        *   Relative Frequency: Frequency of a class / Total number of observations.
        *   Cumulative Frequency: The sum of frequencies for that class and all preceding classes.
        *   Cumulative Relative Frequency: The sum of relative frequencies for that class and all preceding classes.
    *   **Graphical Displays for Numerical Data**:
        *   Histograms:
            *   Construction: Similar to bar charts, but for numerical data. The horizontal axis represents the classes/bins of the numerical variable, and the vertical axis represents the frequency or relative frequency. Bars are drawn adjacent to each other (no gaps) to indicate the continuous nature of the data (or that bins are consecutive).
            *   Interpretation: Shows the shape of the data's distribution (e.g., symmetric/bell-shaped, skewed left, skewed right, unimodal, bimodal). Also gives an idea of central tendency and spread.
        *   Frequency Polygons:
            *   Construction: Line graph formed by connecting the midpoints of the tops of the histogram bars. The polygon is usually anchored to the x-axis at the midpoints of the classes before the first class and after the last class.
            *   Interpretation: Similar to histogram, useful for comparing distributions of two or more datasets on the same graph.
        *   Ogives (Cumulative Frequency Graphs):
            *   Construction: A line graph that plots the cumulative frequency or cumulative relative frequency (on the y-axis) against the upper class boundaries (on the x-axis).
            *   Interpretation: Useful for estimating the number or percentage of observations below a certain value, and for finding percentiles (e.g., median).
        *   Stem-and-Leaf Plots:
            *   Construction: Each data value is split into a "stem" (usually the leading digit(s)) and a "leaf" (usually the last digit). Stems are listed vertically, and leaves are listed horizontally next to their corresponding stems.
            *   Interpretation: Retains actual data values while showing the shape of the distribution. Useful for smaller datasets.
        *   Dot Plots:
            *   Construction: Each data value is represented as a dot plotted above its corresponding value on a number line. Dots are stacked if values repeat.
            *   Interpretation: Useful for small datasets to see individual values and distribution shape.
    *   **Measures of Central Tendency for Numerical Data**:
        *   Mean (Arithmetic Average):
            *   Sample Mean (x̄) = (Σx<sub>i</sub>) / n
            *   Population Mean (μ) = (ΣX<sub>i</sub>) / N
            *   Interpretation: The "balance point" of the data. Sensitive to extreme values (outliers).
        *   Median: The middle value when the data is sorted in ascending order.
            *   If n is odd, median is the ((n+1)/2)-th value.
            *   If n is even, median is the average of the (n/2)-th and ((n/2)+1)-th values.
            *   Interpretation: Divides the data into two equal halves. Robust to outliers.
        *   Mode: The value(s) that occur most frequently.
            *   Can be unimodal, bimodal, multimodal, or no mode if all values are unique.
        *   Relationship between Mean, Median, and Mode:
            *   Symmetric Distribution: Mean ≈ Median ≈ Mode.
            *   Right-Skewed (Positively Skewed) Distribution: Mean > Median > Mode. (Tail to the right)
            *   Left-Skewed (Negatively Skewed) Distribution: Mean < Median < Mode. (Tail to the left)
    *   **Measures of Position/Location**:
        *   Quartiles: Values that divide the sorted data into four equal parts.
            *   Q1 (First Quartile): 25th percentile. 25% of data lies below Q1.
            *   Q2 (Second Quartile): 50th percentile. This is the Median.
            *   Q3 (Third Quartile): 75th percentile. 75% of data lies below Q3.
            *   Calculation: Various methods exist, often involving finding medians of lower/upper halves of data.
        *   Percentiles: P<sub>k</sub> is the value below which k percent of the observations lie. Q1 = P<sub>25</sub>, Median = P<sub>50</sub>, Q3 = P<sub>75</sub>.
    *   **Measures of Dispersion/Spread/Variability**: Describe how spread out the data values are.
        *   Range: Maximum value - Minimum value. Simple to calculate but very sensitive to outliers.
        *   Interquartile Range (IQR): IQR = Q3 - Q1. The range of the middle 50% of the data. Robust to outliers.
        *   Variance: The average of the squared deviations of each data value from the mean.
            *   Sample Variance (s²): Σ(x<sub>i</sub> - x̄)² / (n-1). Division by (n-1) provides an unbiased estimator of population variance. (n-1) is degrees offreedom.
            *   Population Variance (σ²): Σ(X<sub>i</sub> - μ)² / N.
            *   Units are squared (e.g., if data is in cm, variance is in cm²).
        *   Standard Deviation: The square root of the variance.
            *   Sample Standard Deviation (s) = √s²
            *   Population Standard Deviation (σ) = √σ²
            *   Interpretation: A typical or average distance of data values from the mean. Measured in the same units as the original data.
            *   Chebyshev's Rule: For any dataset, at least (1 - 1/k²) of the data lies within k standard deviations of the mean (for k > 1).
            *   Empirical Rule (for bell-shaped/normal distributions): Approx. 68% of data within ±1σ, 95% within ±2σ, 99.7% within ±3σ of the mean.
        *   Coefficient of Variation (CV): (s / x̄) * 100% (for sample) or (σ / μ) * 100% (for population).
            *   A relative measure of dispersion, unitless. Useful for comparing variability between datasets with different means or different units of measurement.
    *   **Five-Number Summary and Box Plots (Box-and-Whisker Plots)**:
        *   Five-Number Summary: Minimum, Q1, Median (Q2), Q3, Maximum. Provides a concise summary of distribution.
        *   Box Plot:
            *   Construction: A box is drawn from Q1 to Q3, with a line inside at the median. "Whiskers" extend from the box to the minimum and maximum values (or to 1.5 * IQR beyond Q1 and Q3, with outliers plotted individually).
            *   Interpretation: Visually displays center (median), spread (IQR, range), and shape (skewness by comparing median position within box and whisker lengths). Effective for identifying potential outliers.
4.  **Association Between Variables**
    *   **Association Between Two Categorical Variables**:
        *   Contingency Tables (Two-Way Tables / Cross-Tabulation Tables):
            *   Construction: Rows represent categories of one variable, columns represent categories of the other. Cells contain joint frequencies (count of observations with that specific pair of categories). Marginal frequencies are row totals and column totals.
            Example:
            | Smokes | Lung Disease | No Lung Disease | Total |
            |--------|--------------|-----------------|-------|
            | Yes    | 70           | 30              | 100   |
            | No     | 10           | 90              | 100   |
            | Total  | 80           | 120             | 200   |
        *   Analyzing Contingency Tables:
            *   Row Percentages: (Cell Frequency / Row Total) * 100%. Shows distribution of column variable for each category of row variable.
            *   Column Percentages: (Cell Frequency / Column Total) * 100%. Shows distribution of row variable for each category of column variable.
            *   Total Percentages: (Cell Frequency / Grand Total) * 100%.
            *   Comparing Conditional Distributions: E.g., comparing the percentage of lung disease among smokers vs. non-smokers.
            *   Concept of Independence: Two categorical variables are independent if the conditional distribution of one variable is the same across all categories of the other. If dependent, there is an association. (Expected frequencies under independence = (Row Total * Column Total) / Grand Total. Comparing observed to expected can indicate association - leads to Chi-Squared test).
        *   Graphical Displays:
            *   Stacked Bar Charts: Each bar represents a category of one variable, segmented by categories of the other variable.
            *   Grouped (or Clustered) Bar Charts: Bars for categories of one variable are grouped side-by-side based on categories of the other variable.
    *   **Association Between Two Numerical Variables**:
        *   Scatterplots (Scatter Diagrams):
            *   Construction: A graph where each point (x, y) represents a pair of values for two numerical variables. One variable on the x-axis, the other on the y-axis.
            *   Interpreting Scatterplots:
                *   Form: Linear (points tend to cluster around a straight line), Curvilinear (points follow a curve), No Pattern (points are scattered randomly).
                *   Direction:
                    *   Positive Association: As x increases, y tends to increase (upward trend).
                    *   Negative Association: As x increases, y tends to decrease (downward trend).
                *   Strength: How closely the points follow the identified form. Strong (points very close to a line/curve), Moderate, Weak (points more scattered).
                *   Outliers: Points that deviate significantly from the overall pattern.
    *   **Measures of Linear Association Between Two Numerical Variables**:
        *   Covariance: Measures the direction of the linear relationship between two numerical variables.
            *   Sample Covariance (s<sub>xy</sub>): Σ[(x<sub>i</sub> - x̄)(y<sub>i</sub> - ȳ)] / (n-1)
            *   Population Covariance (σ<sub>xy</sub>): Σ[(X<sub>i</sub> - μ<sub>X</sub>)(Y<sub>i</sub> - μ<sub>Y</sub>)] / N
            *   Interpretation:
                *   Positive s<sub>xy</sub>: Indicates a positive linear relationship.
                *   Negative s<sub>xy</sub>: Indicates a negative linear relationship.
                *   s<sub>xy</sub> close to 0: Indicates a weak or no linear relationship.
            *   Limitation: The magnitude of covariance depends on the units of measurement of x and y, making it difficult to judge the strength of the relationship or compare across different pairs of variables.
        *   Pearson Correlation Coefficient (r for sample, ρ for population): Measures the strength and direction of the *linear* relationship between two numerical variables.
            *   Formula (Sample): r = s<sub>xy</sub> / (s<sub>x</sub> * s<sub>y</sub>) = [Σ(x<sub>i</sub> - x̄)(y<sub>i</sub> - ȳ)] / [√Σ(x<sub>i</sub> - x̄)² * √Σ(y<sub>i</sub> - ȳ)²]
            *   Properties:
                *   Unitless.
                *   Ranges from -1 to +1.
                *   r = +1: Perfect positive linear relationship. All points lie on a straight line with positive slope.
                *   r = -1: Perfect negative linear relationship. All points lie on a straight line with negative slope.
                *   r = 0: No linear relationship. This does NOT mean no relationship at all; there could be a strong non-linear relationship.
            *   Interpretation of Strength (general guidelines):
                *   |r| ≥ 0.7 to 1.0: Strong linear relationship.
                *   |r| ≥ 0.4 to < 0.7: Moderate linear relationship.
                *   |r| ≥ 0.2 to < 0.4: Weak linear relationship.
                *   |r| < 0.2: Very weak or no linear relationship.
            *   Important Caveats:
                *   Correlation does not imply causation. A strong correlation between x and y does not mean x causes y (or vice-versa). There might be a lurking variable influencing both.
                *   Sensitive to outliers.
                *   Only measures linear relationships.
    *   **Association Between a Numerical and a Categorical Variable**:
        *   Comparing Summary Statistics: Calculate and compare statistics like mean, median, standard deviation, IQR of the numerical variable for each category of the categorical variable.
            Example: Comparing average income (numerical) across different education levels (categorical).
        *   Graphical Displays:
            *   Side-by-side Box Plots: A box plot of the numerical variable is drawn for each category of the categorical variable, all on the same scale. This allows for visual comparison of distributions (center, spread, shape, outliers).
            *   Multiple Histograms or Dot Plots (on the same scale).
        *   Point Biserial Correlation Coefficient (r<sub>pb</sub>):
            *   Measures the association between a continuous numerical variable and a dichotomous (binary - only two categories) categorical variable.
            *   Calculation: One category is coded as 0, the other as 1. Then Pearson's r formula is applied.
            *   Interpretation: Similar to Pearson's r. Its square (r<sub>pb</sub>²) indicates the proportion of variance in the numerical variable explained by the categorical variable.
            *   Example: Correlation between test score (numerical) and pass/fail status (dichotomous categorical).
5.  **Counting Principles**
    *   **Introduction to Combinatorics**:
        *   Combinatorics is the branch of mathematics dealing with counting, arrangement, and combination of objects.
        *   It's fundamental for calculating probabilities (e.g., determining the size of sample spaces and events), understanding algorithm complexity, and in fields like cryptography and network design.
    *   **The Sum Rule (Addition Principle)**:
        *   Statement: If a first task can be performed in n<sub>1</sub> ways and a second task can be performed in n<sub>2</sub> ways, and the two tasks cannot be performed simultaneously, then performing either task can be accomplished in n<sub>1</sub> + n<sub>2</sub> ways.
        *   Generalization: If there are k disjoint sets of choices, and the i-th set has n<sub>i</sub> choices, then the total number of ways to choose one item from any of these sets is n<sub>1</sub> + n<sub>2</sub> + ... + n<sub>k</sub>.
        *   Examples:
            *   Choosing a dessert: If a restaurant offers 3 types of cake and 4 types of pie, you can choose 3 + 4 = 7 different desserts.
            *   Travel: If you can travel from city A to city B by 2 bus routes or 3 train routes, you have 2 + 3 = 5 ways to travel.
    *   **The Product Rule (Multiplication Principle)**:
        *   Statement: If a procedure can be broken down into a sequence of k independent tasks, and there are n<sub>1</sub> ways to perform the first task, n<sub>2</sub> ways to perform the second task, ..., and n<sub>k</sub> ways to perform the k-th task, then the total number of ways to perform the entire procedure is n<sub>1</sub> * n<sub>2</sub> * ... * n<sub>k</sub>.
        *   Examples:
            *   Outfits: If you have 3 shirts and 2 pairs of pants, you can create 3 * 2 = 6 different outfits.
            *   License Plates: A license plate consists of 3 letters followed by 3 digits. If any letter and any digit can be used, there are 26 * 26 * 26 * 10 * 10 * 10 = 26³ * 10³ = 17,576,000 possible license plates.
            *   Coin Flips: Flipping a coin 3 times results in 2 * 2 * 2 = 2³ = 8 possible outcomes (HHH, HHT, etc.).
    *   **Factorial Notation**:
        *   Definition: For a non-negative integer n, n-factorial, denoted by n!, is the product of all positive integers less than or equal to n.
        *   Formula: n! = n * (n-1) * (n-2) * ... * 3 * 2 * 1.
        *   Special Case: By definition, 0! = 1. This is important for consistency in formulas for permutations and combinations.
        *   Examples:
            *   3! = 3 * 2 * 1 = 6
            *   5! = 5 * 4 * 3 * 2 * 1 = 120
        *   Relevance: Factorials are used extensively in calculating the number of ways to arrange objects (permutations).
    *   **Permutations with Repetition (Arrangements with Replacement)**:
        *   Definition: The number of ordered arrangements of r items chosen from n distinct types of items, where repetition is allowed (or items are replaced after being chosen).
        *   Formula: n<sup>r</sup>.
        *   Explanation: For each of the r positions in the arrangement, there are n choices available because repetition is allowed. So, by the product rule, it's n * n * ... * n (r times).
        *   Examples:
            *   PIN Codes: A 4-digit PIN using digits 0-9 allows for 10 * 10 * 10 * 10 = 10⁴ = 10,000 possible PINs.
            *   Dice Rolls: Rolling a 6-sided die 3 times gives 6 * 6 * 6 = 6³ = 216 possible sequences of outcomes.
            *   Binary Strings: A binary string of length 8 has 2⁸ = 256 possibilities.
    *   **Permutations of n distinct objects**:
        *   The number of ways to arrange n distinct objects in a specific order is n!. This is a special case of permutations without repetition (covered in Week 6) where all n objects are chosen (r=n), so P(n,n) = n! / (n-n)! = n! / 0! = n!.
        *   Example: Arranging 3 distinct books on a shelf can be done in 3! = 6 ways.
    *   **Tree Diagrams**:
        *   A graphical way to represent all possible outcomes of a sequence of events or choices.
        *   Each branch represents a choice or outcome. The total number of outcomes is the number of "leaf" nodes at the end of the branches.
        *   Useful for visualizing problems involving the product rule and for understanding sample spaces in probability.
        *   Example: Outcomes of flipping a coin twice:
            Start -> H (1st flip) -> H (2nd flip)  (Outcome HH)
                  -> T (2nd flip)  (Outcome HT)
                  -> T (1st flip) -> H (2nd flip)  (Outcome TH)
                  -> T (2nd flip)  (Outcome TT)
6.  **Permutations & Combinations**
    *   **Permutations (Order Matters, Without Repetition)**:
        *   Definition: An arrangement of r items selected from a set of n distinct items, where the order of selection/arrangement is important, and items are not replaced once selected.
        *   Notation: P(n,r), <sub>n</sub>P<sub>r</sub>, or P<sup>n</sup><sub>r</sub>.
        *   Formula: P(n,r) = n! / (n-r)!
        *   Derivation/Intuition: For the first position, there are n choices. For the second, n-1 choices (since one is already used), ..., for the r-th position, there are n-(r-1) = n-r+1 choices. So, P(n,r) = n * (n-1) * ... * (n-r+1). Multiplying numerator and denominator by (n-r)! gives the formula.
        *   Examples:
            *   Arranging 3 books from a set of 5 distinct books on a shelf: P(5,3) = 5! / (5-3)! = 5! / 2! = (5*4*3*2*1) / (2*1) = 60 ways.
            *   Electing a President, Vice-President, and Treasurer from a group of 10 people: P(10,3) = 10! / (10-3)! = 10! / 7! = 10 * 9 * 8 = 720 ways.
    *   **Combinations (Order Does Not Matter, Without Repetition)**:
        *   Definition: A selection of r items from a set of n distinct items, where the order of selection is *not* important. This refers to forming subsets.
        *   Notation: C(n,r), <sub>n</sub>C<sub>r</sub>, or often as a binomial coefficient (<sup>n</sup><sub>r</sub>) read as "n choose r".
        *   Formula: C(n,r) = n! / [r! * (n-r)!]
        *   Derivation/Intuition: Each combination of r items can be arranged in r! ways (permutations of those r items). So, P(n,r) = C(n,r) * r!. Therefore, C(n,r) = P(n,r) / r!.
        *   Examples:
            *   Choosing a committee of 3 people from a group of 10: C(10,3) = 10! / [3! * (10-3)!] = 10! / (3! * 7!) = (10*9*8) / (3*2*1) = 120 ways.
            *   Selecting 2 fruits from a basket of 5 different fruits: C(5,2) = 5! / (2! * 3!) = (5*4) / (2*1) = 10 ways.
    *   **Key Difference: Order Matters vs. Order Doesn't Matter**:
        *   Permutations: Think "arrangements", "sequences", "line-ups", specific roles/positions. (Example: ABC is different from BAC).
        *   Combinations: Think "groups", "subsets", "committees", "samples" where internal order is irrelevant. (Example: {A,B,C} is the same group as {B,A,C}).
        *   Comparative Example: From 3 people (A,B,C),
            *   Choosing 2 to be President and VP (order matters): P(3,2) = 3!/1! = 6 (AB, BA, AC, CA, BC, CB).
            *   Choosing a committee of 2 (order doesn't matter): C(3,2) = 3!/(2!1!) = 3 ({A,B}, {A,C}, {B,C}).
    *   **Combinatorial Identities (Basic ones)**:
        *   C(n,0) = 1 (There's one way to choose zero items: choose nothing).
        *   C(n,n) = 1 (There's one way to choose all n items).
        *   C(n,1) = n (There are n ways to choose one item from n).
        *   C(n,r) = C(n, n-r) (Symmetry: Choosing r items to include is the same as choosing n-r items to exclude). Example: C(5,2) = C(5,3) = 10.
        *   Pascal's Identity: C(n,r) = C(n-1, r-1) + C(n-1, r). This identity forms the basis for Pascal's Triangle, where each entry is the sum of the two entries directly above it.
    *   **Permutations with Some Identical Items (Arrangements of Multisets)**:
        *   Formula: The number of distinct permutations of n objects where there are n<sub>1</sub> identical objects of type 1, n<sub>2</sub> identical objects of type 2, ..., n<sub>k</sub> identical objects of type k (and n<sub>1</sub> + n<sub>2</sub> + ... + n<sub>k</sub> = n) is:
            n! / (n<sub>1</sub>! * n<sub>2</sub>! * ... * n<sub>k</sub>!)
        *   Examples:
            *   Number of distinct arrangements of the letters in "MISSISSIPPI" (11 letters: 1 M, 4 I, 4 S, 2 P): 11! / (1! * 4! * 4! * 2!) = 34,650.
            *   Number of distinct arrangements of "APPLE" (5 letters: 1 A, 2 P, 1 L, 1 E): 5! / (1! * 2! * 1! * 1!) = 120 / 2 = 60.
    *   **Real-World Examples**:
        *   Probability calculations: Determining the number of favorable outcomes and total outcomes.
        *   Password creation: Number of possible passwords given certain character constraints (often involves product rule and permutations with repetition).
        *   Team selection for sports or projects.
        *   Lottery designs: Calculating odds of winning.
        *   Drug trials: Assigning patients to treatment groups.
7.  **Probability Basics**
    *   **Introduction to Probability**:
        *   Definition: Probability is a numerical measure of the likelihood or chance that a particular event will occur.
        *   Scale: Probabilities range from 0 to 1, inclusive.
            *   P(E) = 0 means event E is impossible.
            *   P(E) = 1 means event E is certain.
            *   0 < P(E) < 1 means event E is possible but not certain.
        *   Importance: Used for decision-making under uncertainty, risk assessment, modeling random phenomena.
    *   **Terminology**:
        *   Experiment: Any process that generates a set of data or observations, which can be repeated under similar conditions. Example: Tossing a coin, rolling a die, drawing a card.
        *   Outcome: A single possible result of an experiment. Example: Getting 'Heads' when tossing a coin.
        *   Sample Space (S): The set of all possible distinct outcomes of an experiment. Example: For a coin toss, S = {Heads, Tails}. For a die roll, S = {1, 2, 3, 4, 5, 6}.
        *   Event (E): Any subset of the sample space S. It is a collection of one or more outcomes. Example: Event "getting an even number" when rolling a die is E = {2, 4, 6}.
    *   **Definitions/Approaches to Probability**:
        *   Classical (Theoretical or Priori) Probability: Used when all outcomes in the sample space are equally likely.
            *   Formula: P(E) = (Number of outcomes favorable to E) / (Total number of outcomes in S)
            *   Examples: P(Heads) for a fair coin = 1/2. P(rolling a 3) with a fair die = 1/6.
        *   Empirical (Relative Frequency or Posteriori) Probability: Based on observations obtained from probability experiments.
            *   Formula: P(E) = (Frequency of event E occurring) / (Total number of trials or observations)
            *   Example: If a coin is tossed 100 times and lands heads 55 times, the empirical probability of heads is 55/100 = 0.55.
            *   Law of Large Numbers (brief idea): As the number of trials increases, the empirical probability tends to get closer to the theoretical probability.
        *   Subjective Probability: Based on an individual's personal belief, intuition, experience, or judgment about the likelihood of an event.
            *   Example: A sports analyst's prediction of a team winning a game, an investor's belief about a stock's future performance.
    *   **Basic Properties/Axioms of Probability (Kolmogorov Axioms)**:
        *   Axiom 1: For any event E, 0 ≤ P(E) ≤ 1. (Probability is non-negative and not greater than 1).
        *   Axiom 2: P(S) = 1. (The probability of the entire sample space, or a certain event, is 1).
        *   Axiom 3: If E<sub>1</sub>, E<sub>2</sub>, ..., E<sub>k</sub> are mutually exclusive events, then P(E<sub>1</sub> ∪ E<sub>2</sub> ∪ ... ∪ E<sub>k</sub>) = P(E<sub>1</sub>) + P(E<sub>2</sub>) + ... + P(E<sub>k</sub>).
        *   From these, P(∅) = 0 (probability of an impossible event is 0).
    *   **Operations on Events and Corresponding Probability Laws**:
        *   Complement of an Event (E'): The event that E does not occur. Consists of all outcomes in S that are not in E.
            *   Probability Law: P(E') = 1 - P(E).
            *   Venn Diagram: Area outside circle E within the rectangle S.
        *   Union of Events (E ∪ F or "E or F"): The event that either E occurs, or F occurs, or both occur. Consists of all outcomes in E or F or both.
            *   Addition Rule: P(E ∪ F) = P(E) + P(F) - P(E ∩ F). The P(E ∩ F) term is subtracted because it's counted twice (once in P(E) and once in P(F)).
            *   Venn Diagram: Total area covered by circles E and F.
        *   Intersection of Events (E ∩ F or "E and F"): The event that both E and F occur simultaneously. Consists of all outcomes common to both E and F.
            *   Venn Diagram: The overlapping area of circles E and F.
        *   Mutually Exclusive (Disjoint) Events: Events that have no outcomes in common, so they cannot occur at the same time. E ∩ F = ∅.
            *   If E and F are mutually exclusive, P(E ∩ F) = 0.
            *   The Addition Rule simplifies to: P(E ∪ F) = P(E) + P(F).
    *   **Examples**:
        *   Rolling a fair die: S = {1,2,3,4,5,6}. Let E = {2,4,6} (even), F = {1,2,3} (≤3).
            P(E) = 3/6 = 1/2. P(F) = 3/6 = 1/2.
            E' = {1,3,5}, P(E') = 1 - 1/2 = 1/2.
            E ∩ F = {2}, P(E ∩ F) = 1/6.
            E ∪ F = {1,2,3,4,6}, P(E ∪ F) = P(E) + P(F) - P(E ∩ F) = 1/2 + 1/2 - 1/6 = 1 - 1/6 = 5/6.
    *   **Odds (Briefly)**:
        *   Odds in favor of E = P(E) / P(E') = P(E) / [1 - P(E)].
        *   Odds against E = P(E') / P(E) = [1 - P(E)] / P(E).
        *   If odds in favor are a:b, then P(E) = a / (a+b).
8.  **Conditional Probability**
    *   **Conditional Probability**:
        *   Definition: The probability of an event A occurring, given that another event B has already occurred (or is known to have occurred).
        *   Notation: P(A|B), read as "the probability of A given B."
        *   Formula: P(A|B) = P(A ∩ B) / P(B), provided P(B) > 0.
        *   Intuition: The occurrence of event B reduces the effective sample space to only the outcomes in B. We are then interested in the proportion of those outcomes that are also in A.
        *   Examples:
            *   Drawing two cards from a deck without replacement. P(2nd card is King | 1st card was a King) = P(1st King AND 2nd King) / P(1st King) = (4/52 * 3/51) / (4/52) = 3/51.
            *   In a group of students, P(student plays soccer | student is male).
    *   **Multiplication Rule for Probability**: Derived from the conditional probability formula.
        *   P(A ∩ B) = P(B) * P(A|B)
        *   P(A ∩ B) = P(A) * P(B|A)
        *   This rule is used to find the probability of two events occurring in sequence.
        *   Generalization for k events: P(E<sub>1</sub> ∩ E<sub>2</sub> ∩ ... ∩ E<sub>k</sub>) = P(E<sub>1</sub>) * P(E<sub>2</sub>|E<sub>1</sub>) * P(E<sub>3</sub>|E<sub>1</sub>∩E<sub>2</sub>) * ... * P(E<sub>k</sub>|E<sub>1</sub>∩...∩E<sub>k-1</sub>).
    *   **Independent Events**:
        *   Definition: Two events A and B are independent if the occurrence (or non-occurrence) of one event does not affect the probability of the occurrence of the other event.
        *   Formal Conditions for Independence:
            *   P(A|B) = P(A) (if P(B) > 0)
            *   P(B|A) = P(B) (if P(A) > 0)
            *   P(A ∩ B) = P(A) * P(B) (This is the most general and practical definition to test for independence).
        *   Distinction from Mutually Exclusive Events: Independent events *can* occur together (unless one has zero probability), while mutually exclusive events *cannot* occur together. If A and B are non-empty mutually exclusive events, they are dependent.
        *   Examples:
            *   Flipping a fair coin twice: Outcome of 1st flip and outcome of 2nd flip are independent. P(H<sub>1</sub> ∩ H<sub>2</sub>) = P(H<sub>1</sub>) * P(H<sub>2</sub>) = 1/2 * 1/2 = 1/4.
            *   Drawing two cards *with replacement*: Events are independent.
    *   **Tree Diagrams for Sequential Events**:
        *   A visual tool to represent sequences of events and their probabilities, especially useful for conditional probabilities.
        *   Each branch represents an event, labeled with its probability. Probabilities on subsequent branches are conditional on the preceding events.
        *   To find the probability of a sequence of events (a path through the tree), multiply the probabilities along that path.
    *   **Law of Total Probability**:
        *   Statement: If B<sub>1</sub>, B<sub>2</sub>, ..., B<sub>n</sub> form a partition of the sample space S (i.e., they are mutually exclusive and their union is S, so ΣP(B<sub>i</sub>)=1), then for any event A in S:
            P(A) = Σ P(A ∩ B<sub>i</sub>) = Σ P(A|B<sub>i</sub>) * P(B<sub>i</sub>)
            P(A) = P(A|B<sub>1</sub>)P(B<sub>1</sub>) + P(A|B<sub>2</sub>)P(B<sub>2</sub>) + ... + P(A|B<sub>n</sub>)P(B<sub>n</sub>).
        *   Intuition: The overall probability of event A can be found by summing its probabilities across different, mutually exclusive scenarios (the B<sub>i</sub>'s).
        *   Example: A factory has two machines. Machine 1 produces 60% of items with a 2% defect rate. Machine 2 produces 40% of items with a 3% defect rate. P(Defective) = P(Defective|Machine1)P(Machine1) + P(Defective|Machine2)P(Machine2) = (0.02)(0.60) + (0.03)(0.40) = 0.012 + 0.012 = 0.024.
    *   **Bayes' Theorem**:
        *   Formula: Allows us to "reverse" conditional probabilities. Given P(A|B<sub>i</sub>) and prior probabilities P(B<sub>i</sub>), we can find the posterior probability P(B<sub>i</sub>|A).
            P(B<sub>i</sub>|A) = [P(A|B<sub>i</sub>) * P(B<sub>i</sub>)] / P(A)
            where P(A) in the denominator is calculated using the Law of Total Probability: P(A) = Σ P(A|B<sub>j</sub>) * P(B<sub>j</sub>).
        *   Terminology:
            *   P(B<sub>i</sub>): Prior probability of B<sub>i</sub> (before observing event A).
            *   P(A|B<sub>i</sub>): Likelihood of observing A if B<sub>i</sub> is true.
            *   P(B<sub>i</sub>|A): Posterior probability of B<sub>i</sub> (after observing event A).
        *   Interpretation: Bayes' Theorem provides a way to update our beliefs (probabilities of B<sub>i</sub>) in light of new evidence (occurrence of A).
        *   **Medical Test Examples**:
            *   Let D be the event that a person has a disease, D' be no disease. Let + be a positive test result, - be a negative test.
            *   Given: P(D) (prevalence/prior probability of disease), P(+|D) (sensitivity: prob. of positive test if person has disease), P(-|D') (specificity: prob. of negative test if person doesn't have disease). Note: P(+|D') = 1 - P(-|D') is the false positive rate.
            *   Often want to find P(D|+): Probability person has disease given a positive test.
                P(D|+) = [P(+|D) * P(D)] / [P(+|D)P(D) + P(+|D')P(D')]
            *   Discuss false positives (testing positive but not having the disease) and false negatives (testing negative but having the disease, P(-|D)).
    *   **Further Examples**:
        *   Spam Filtering: P(Spam | certain words occur) can be estimated using Bayes' Theorem. Prior probability of an email being spam, likelihood of certain words appearing in spam vs. non-spam emails.
        *   Fault Diagnosis: Probability of a particular component being faulty given certain system symptoms.
9.  **Random Variables**
    *   **Definition of a Random Variable (RV)**:
        *   A variable whose value is a numerical outcome of a random phenomenon.
        *   It maps outcomes from the sample space S to the set of real numbers ℝ.
        *   Notation: Typically denoted by uppercase letters like X, Y, Z. Specific values are denoted by lowercase letters like x, y, z.
    *   **Types of Random Variables**:
        *   **Discrete Random Variable**:
            *   A random variable that can take on a finite or countably infinite number of distinct values.
            *   Examples: Number of heads in 3 coin flips (can be 0, 1, 2, 3), number of defective items in a sample of 10, number of children in a family, number of cars passing an intersection in an hour.
        *   **Continuous Random Variable**:
            *   A random variable that can take on any value within a given range or interval (or multiple intervals).
            *   Examples: Height of a student (e.g., 165.234... cm), temperature of a room, time to complete a task, weight of a product.
    *   **Probability Distributions for Discrete Random Variables**:
        *   **Probability Mass Function (PMF)**:
            *   A function or table, denoted p(x), that gives the probability that a discrete random variable X is exactly equal to some value x. That is, p(x) = P(X=x).
            *   Properties:
                1.  0 ≤ p(x) ≤ 1 for all possible values of x.
                2.  Σ p(x) = 1, where the sum is taken over all possible values of x.
            *   Representations: Can be given as a table listing values of x and their probabilities, a formula, or a bar graph (where bar heights represent probabilities).
            *   Example: PMF for the number of heads (X) in 2 fair coin flips: S = {HH, HT, TH, TT}
                | x (Number of Heads) | P(X=x) = p(x) |
                |---------------------|---------------|
                | 0 (TT)              | 1/4           |
                | 1 (HT, TH)          | 2/4 = 1/2     |
                | 2 (HH)              | 1/4           |
        *   **Cumulative Distribution Function (CDF)** for Discrete RVs:
            *   A function F(x) that gives the probability that a random variable X takes on a value less than or equal to x. F(x) = P(X ≤ x) = Σ<sub>t≤x</sub> p(t).
            *   Properties:
                1.  0 ≤ F(x) ≤ 1 for all x.
                2.  F(x) is a non-decreasing function (i.e., if a < b, then F(a) ≤ F(b)).
                3.  F(x) is a step function for discrete RVs, increasing only at the possible values of X.
                4.  lim (x→-∞) F(x) = 0 and lim (x→∞) F(x) = 1.
            *   Using CDF to find probabilities:
                *   P(a < X ≤ b) = F(b) - F(a)
                *   P(X > a) = 1 - P(X ≤ a) = 1 - F(a)
                *   P(X = x) = F(x) - F(x<sup>-</sup>) (where x<sup>-</sup> is the largest possible value strictly less than x), which is simply p(x).
            *   Example: CDF for number of heads in 2 coin flips:
                | x   | F(x)=P(X≤x)         |
                |-----|----------------------|
                | x<0 | 0                    |
                | 0≤x<1| P(X=0) = 1/4         |
                | 1≤x<2| P(X=0)+P(X=1) = 3/4  |
                | x≥2 | P(X=0)+P(X=1)+P(X=2)=1|
    *   **Support (or Range) of a Random Variable**:
        *   The set of all possible values that the random variable X can take. For a discrete RV, this is the set of values x for which p(x) > 0.
    *   **Introduction to Probability Distributions for Continuous Random Variables (Briefly)**:
        *   For continuous RVs, P(X=x) = 0 for any specific value x. This is because there are infinitely many possible values in any interval.
        *   Instead of a PMF, we use a **Probability Density Function (PDF)**, denoted f(x).
        *   Probability is represented by the area under the curve of f(x) over an interval: P(a ≤ X ≤ b) = ∫<sub>a</sub><sup>b</sup> f(x)dx.
        *   The **Cumulative Distribution Function (CDF)** for a continuous RV is F(x) = P(X ≤ x) = ∫<sub>-∞</sub><sup>x</sup> f(t)dt.
10. **Expectation & Variance**
    *   **Expected Value (Mean) of a Discrete Random Variable**:
        *   Definition: The theoretical average of a discrete random variable. It's a weighted average of its possible values, where the weights are the probabilities of each value.
        *   Notation: E(X), μ<sub>X</sub>, or simply μ.
        *   Formula: E(X) = Σ x * P(X=x) = Σ x * p(x), where the sum is over all possible values of x.
        *   Interpretation: The long-run average value of X if the random experiment is repeated many times. It represents the center of mass of the probability distribution.
        *   Examples:
            *   Expected number of heads in 2 fair coin flips: E(X) = 0*(1/4) + 1*(2/4) + 2*(1/4) = 0 + 2/4 + 2/4 = 4/4 = 1.
            *   Lottery game: If a ticket costs $1, with a 1/100 chance to win $50 and 99/100 chance to win $0. RV Y = winnings. E(Y) = $50*(1/100) + $0*(99/100) = $0.50. Expected net gain = $0.50 - $1 = -$0.50.
    *   **Expected Value of a Function of a Discrete Random Variable**:
        *   If Y = g(X) is a function of a discrete random variable X, then the expected value of Y is:
            E(Y) = E(g(X)) = Σ g(x) * P(X=x) = Σ g(x) * p(x).
        *   Example: E(X²): If X is number of heads in 2 flips, E(X²) = 0²*(1/4) + 1²*(2/4) + 2²*(1/4) = 0 + 2/4 + 4/4 = 6/4 = 1.5.
    *   **Linearity of Expectation**: A very powerful property.
        *   For constants a and b: E(aX + b) = aE(X) + b.
        *   For two random variables X and Y (defined on the same sample space): E(X + Y) = E(X) + E(Y). This holds true even if X and Y are *not* independent.
        *   Generalization: E(a<sub>1</sub>X<sub>1</sub> + ... + a<sub>n</sub>X<sub>n</sub>) = a<sub>1</sub>E(X<sub>1</sub>) + ... + a<sub>n</sub>E(X<sub>n</sub>).
        *   Significance: Simplifies calculation of expected values for sums of random variables.
    *   **Variance of a Discrete Random Variable**:
        *   Definition: Measures the expected squared deviation of a random variable from its mean (E(X) = μ). It quantifies the spread or dispersion of the probability distribution.
        *   Notation: Var(X), σ²<sub>X</sub>, or σ².
        *   Formula: Var(X) = E[(X - μ)²] = Σ (x - μ)² * P(X=x) = Σ (x - μ)² * p(x).
        *   Computational Formula (often easier): Var(X) = E(X²) - [E(X)]² = E(X²) - μ².
        *   Example: Variance for heads in 2 flips (μ=1, E(X²)=1.5): Var(X) = 1.5 - 1² = 0.5.
            Alternatively: Var(X) = (0-1)²(1/4) + (1-1)²(2/4) + (2-1)²(1/4) = 1(1/4) + 0 + 1(1/4) = 2/4 = 0.5.
    *   **Standard Deviation of a Discrete Random Variable**:
        *   Definition: The positive square root of the variance.
        *   Notation: SD(X), σ<sub>X</sub>, or σ.
        *   Formula: SD(X) = √Var(X).
        *   Interpretation: Provides a measure of spread in the same units as the random variable X. A "typical" or "average" distance of an outcome from the mean.
    *   **Properties of Variance**:
        *   Var(aX + b) = a² * Var(X). (Adding a constant 'b' shifts the distribution but doesn't change its spread. Multiplying by 'a' scales the deviations by 'a', so squared deviations by a²).
        *   If X and Y are *independent* random variables:
            Var(X + Y) = Var(X) + Var(Y).
            Var(X - Y) = Var(X) + Var(Y) (Note: still addition, as (-1)² = 1).
    *   **Indicator Variables (Bernoulli Random Variables as a special case)**:
        *   Definition: An indicator variable I<sub>A</sub> for an event A is a random variable such that:
            I<sub>A</sub> = 1 if event A occurs
            I<sub>A</sub> = 0 if event A does not occur
        *   The PMF is P(I<sub>A</sub> = 1) = P(A) and P(I<sub>A</sub> = 0) = 1 - P(A). This is a Bernoulli(P(A)) distribution.
        *   Expected Value: E(I<sub>A</sub>) = 1 * P(A) + 0 * (1 - P(A)) = P(A).
        *   Variance: Var(I<sub>A</sub>) = E(I<sub>A</sub>²) - [E(I<sub>A</sub>)]². Since I<sub>A</sub>² = I<sub>A</sub> (as 1²=1, 0²=0), E(I<sub>A</sub>²) = E(I<sub>A</sub>) = P(A).
            So, Var(I<sub>A</sub>) = P(A) - [P(A)]² = P(A) * (1 - P(A)).
        *   Usefulness: Complex random variables can sometimes be expressed as sums of simpler indicator variables. Linearity of expectation can then be used to easily find the expected value of the complex RV. Example: Expected number of successes in a set of trials.
11. **Binomial & Poisson Distributions**
    *   **Bernoulli Trials and Bernoulli Distribution**:
        *   Definition of a Bernoulli Trial: A single random experiment with exactly two mutually exclusive outcomes, often labeled "success" (S) and "failure" (F). The probability of success is denoted by p, and the probability of failure is q = 1-p. Trials must be independent.
        *   Bernoulli Random Variable: A random variable X that takes the value 1 (for success) with probability p, and the value 0 (for failure) with probability 1-p.
        *   Notation: X ~ Bernoulli(p).
        *   PMF: P(X=1) = p, P(X=0) = 1-p.
        *   Mean: E(X) = 1*p + 0*(1-p) = p.
        *   Variance: Var(X) = E(X²) - [E(X)]² = (1²*p + 0²*(1-p)) - p² = p - p² = p(1-p).
    *   **Binomial Distribution**:
        *   Definition: Describes the probability of observing k successes in a fixed number (n) of independent Bernoulli trials, where the probability of success (p) is the same for each trial.
        *   Conditions for a Binomial Experiment (BINS acronym):
            1.  **B**inary: Each trial has only two outcomes (success/failure).
            2.  **I**ndependent: The outcome of one trial does not affect the outcome of other trials.
            3.  **N**umber: There is a fixed number of trials, n.
            4.  **S**uccess: The probability of success, p, is constant for every trial.
        *   Notation: If X is the number of successes, then X ~ Bin(n, p).
        *   PMF: P(X=k) = C(n,k) * p<sup>k</sup> * (1-p)<sup>(n-k)</sup>, for k = 0, 1, 2, ..., n.
            *   C(n,k) = n! / [k!(n-k)!] is the binomial coefficient, representing the number of ways to choose k successes from n trials.
            *   p<sup>k</sup> is the probability of k successes.
            *   (1-p)<sup>(n-k)</sup> is the probability of (n-k) failures.
        *   Mean: E(X) = np. (Intuitive: if you flip a coin 10 times, expect 10*0.5 = 5 heads).
        *   Variance: Var(X) = np(1-p).
        *   Standard Deviation: SD(X) = √[np(1-p)].
        *   Shape: Symmetric if p = 0.5. Skewed right if p < 0.5. Skewed left if p > 0.5. Becomes more bell-shaped as n increases.
        *   Examples: Number of heads in 10 coin flips (n=10, p=0.5). Number of defective items in a sample of 20, if probability of defect is 0.05 (n=20, p=0.05). Number of patients recovering from a disease after a treatment.
    *   **Poisson Distribution**:
        *   Definition: Describes the probability of a given number of events occurring in a fixed interval of time or space, provided these events occur with a known constant mean rate (λ) and independently of the time since the last event.
        *   Conditions for a Poisson Process:
            1.  Events occur independently of each other.
            2.  The probability of an event occurring in a very short interval is proportional to the length of the interval.
            3.  The probability of more than one event occurring in such a short interval is negligible.
            (Alternatively: the average rate λ is constant).
        *   Notation: If X is the number of events, then X ~ Poi(λ) or X ~ Poisson(λ). λ (lambda) is the average number of events in the given interval.
        *   PMF: P(X=k) = (λ<sup>k</sup> * e<sup>-λ</sup>) / k!, for k = 0, 1, 2, ...
            *   e is Euler's number (approx 2.71828).
            *   k! is k factorial.
        *   Mean: E(X) = λ.
        *   Variance: Var(X) = λ. (A unique property: mean equals variance).
        *   Examples: Number of phone calls received by a call center per hour (λ = average calls/hour). Number of typos on a page of a book (λ = average typos/page). Number of radioactive decays in a minute.
    *   **Poisson Approximation to the Binomial Distribution**:
        *   When n is large and p is small in a binomial distribution (Bin(n,p)), the calculations can become cumbersome.
        *   Approximation: If n is large (e.g., n ≥ 20 or n ≥ 100 by some stricter rules) and p is small (e.g., p ≤ 0.05 or np < 10), then Bin(n,p) ≈ Poi(λ) where λ = np.
        *   Usefulness: Simplifies probability calculations for rare events in many trials.
        *   Example: Number of defective screws in a large batch of 1000, where probability of a screw being defective is 0.002. Here n=1000, p=0.002. λ = np = 2. So, P(X=k) can be approximated using Poisson PMF with λ=2.
12. **Continuous Random Variables**
    *   **Recap of Continuous Random Variables**:
        *   A variable that can take any value within a given range or interval.
        *   P(X=x) = 0 for any specific value x due to infinitely many possibilities.
        *   Probabilities are defined for intervals, P(a ≤ X ≤ b).
    *   **Probability Density Function (PDF)**:
        *   A function f(x) used to describe the probability distribution of a continuous random variable X.
        *   Properties:
            1.  f(x) ≥ 0 for all x (the density must be non-negative).
            2.  The total area under the curve of f(x) over its entire range must be equal to 1: ∫<sub>-∞</sub><sup>∞</sup> f(x)dx = 1.
        *   Probability as Area: P(a ≤ X ≤ b) = ∫<sub>a</sub><sup>b</sup> f(x)dx. This is the area under the PDF curve between x=a and x=b.
    *   **Cumulative Distribution Function (CDF) for Continuous RVs**:
        *   Definition: F(x) = P(X ≤ x) = ∫<sub>-∞</sub><sup>x</sup> f(t)dt. It gives the cumulative probability up to a value x.
        *   Relationship to PDF: f(x) = d/dx F(x) (The PDF is the derivative of the CDF).
        *   Properties:
            1.  0 ≤ F(x) ≤ 1 for all x.
            2.  F(x) is a non-decreasing function (if a < b, then F(a) ≤ F(b)).
            3.  F(x) is continuous for continuous RVs.
            4.  lim (x→-∞) F(x) = 0.
            5.  lim (x→∞) F(x) = 1.
        *   Using CDF to find probabilities: P(a ≤ X ≤ b) = F(b) - F(a). Also, P(X > a) = 1 - F(a).
    *   **Expected Value (Mean) and Variance for Continuous RVs**:
        *   Expected Value (Mean): E(X) = μ = ∫<sub>-∞</sub><sup>∞</sup> x * f(x)dx.
        *   Variance: Var(X) = σ² = ∫<sub>-∞</sub><sup>∞</sup> (x - μ)² * f(x)dx = E(X²) - [E(X)]², where E(X²) = ∫<sub>-∞</sub><sup>∞</sup> x² * f(x)dx.
    *   **Uniform Distribution (Continuous)**:
        *   Definition: A distribution where all values within a specific interval [a, b] are equally likely.
        *   Notation: X ~ U(a, b).
        *   PDF: f(x) = 1/(b-a) for a ≤ x ≤ b, and f(x) = 0 otherwise. The graph is a rectangle.
        *   CDF: F(x) = 0 for x < a; F(x) = (x-a)/(b-a) for a ≤ x ≤ b; F(x) = 1 for x > b.
        *   Mean: E(X) = (a+b)/2 (the midpoint of the interval).
        *   Variance: Var(X) = (b-a)² / 12.
        *   Applications: Random number generators (often produce numbers from U(0,1)), modeling situations where any value in an interval is equally probable (e.g., waiting time for a bus that arrives regularly every 'T' minutes, where your arrival is random).
    *   **Exponential Distribution**:
        *   Definition: Describes the time between events in a Poisson process (events occurring independently at a constant average rate λ). Often models waiting times or lifetimes.
        *   Notation: X ~ Exp(λ), where λ > 0 is the rate parameter. (λ = average number of events per unit of time/space).
        *   PDF: f(x) = λ * e<sup>-λx</sup> for x ≥ 0, and f(x) = 0 for x < 0.
        *   CDF: F(x) = P(X ≤ x) = 1 - e<sup>-λx</sup> for x ≥ 0, and F(x) = 0 for x < 0.
        *   Mean: E(X) = 1/λ (average waiting time or lifetime).
        *   Variance: Var(X) = 1/λ². Standard Deviation: SD(X) = 1/λ.
        *   Memoryless Property: P(X > s+t | X > s) = P(X > t) for s, t ≥ 0. This means the probability of the item lasting for an additional time 't' is the same, regardless of how long it has already lasted 's'. This is unique to the exponential (and geometric) distribution.
        *   Applications: Time until an earthquake, lifetime of a radioactive particle, waiting time for a customer in a queue (under certain conditions), reliability of electronic components.
    *   **Normal Distribution (Gaussian Distribution)**:
        *   The most widely used continuous probability distribution. It's bell-shaped and symmetric.
        *   Notation: X ~ N(μ, σ²), where μ is the mean and σ² is the variance (σ is the standard deviation).
        *   PDF: f(x) = [1 / (σ√(2π))] * e<sup>-[(x-μ)² / (2σ²)]</sup>. (The formula is complex; understanding its properties is more crucial for an introductory course).
        *   Properties:
            1.  Symmetric about its mean μ.
            2.  Mean = Median = Mode = μ.
            3.  The shape is determined by μ (center of the bell) and σ (spread or width of the bell). Larger σ means wider, flatter curve.
            4.  The curve extends from -∞ to +∞ and never touches the x-axis (though it gets very close).
        *   **Standard Normal Distribution**: A special case of the normal distribution where μ = 0 and σ² = 1 (so σ = 1). Usually denoted by Z. Z ~ N(0, 1).
            *   Standardization (Z-score): Any normal random variable X ~ N(μ, σ²) can be transformed into a standard normal random variable Z using the formula: Z = (X - μ) / σ.
            *   The Z-score tells how many standard deviations an X value is from its mean μ.
            *   Using Z-tables (Standard Normal Tables) or software: These tables provide P(Z ≤ z) for various values of z. Probabilities like P(a ≤ Z ≤ b) or P(Z > c) can be found using these table values and properties of symmetry.
        *   **Empirical Rule (68-95-99.7 Rule)**: For any normal distribution:
            *   Approximately 68.27% of the data falls within μ ± σ.
            *   Approximately 95.45% of the data falls within μ ± 2σ.
            *   Approximately 99.73% of the data falls within μ ± 3σ.
        *   Applications: Many natural phenomena approximate a normal distribution (e.g., heights, weights, blood pressure, measurement errors). It's also crucial for statistical inference due to the Central Limit Theorem (which states that the distribution of sample means tends to be normal for large samples, regardless of the population distribution).
12. **Continuous Random Variables** – probability density functions, uniform, exponential and normal distributions with applications

## Glossary
- **Probability Mass Function (PMF)**: function that gives the probability for each possible value of a discrete random variable.
- **Cumulative Distribution Function (CDF)**: probability that a random variable is less than or equal to a given value.
- **Bayes’ Theorem**: method for updating probabilities based on new evidence.

## Reference Texts
- *Introductory Statistics* (10th Edition) by Neil A. Weiss
- *Introductory Statistics* (4th Edition) by Sheldon M. Ross
- *Descriptive Statistics (VOL 1)* and *Probability and Probability Distributions (VOL 2)*

## Additional Topics
- **Sampling Methods** – simple random, stratified and cluster sampling with pros and cons
- **Transformations** – logarithmic and square-root transformations to stabilise variance
- **Hypothesis Testing** – null vs. alternative hypotheses, p-values and significance levels

## Further Reading
- *Statistics* by Freedman, Pisani and Purves
