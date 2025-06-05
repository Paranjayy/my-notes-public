---
tags:
  - course
  - math
---

# BSMA1001 Mathematics for Data Science I

**Course Credits**: 4

**Course Type**: Foundational

**Instructors**: Neelesh Upadhye, Madhavan Mukund

**Pre-requisites**: None

## Overview
This course introduces straight lines, polynomials, exponentials, logarithms and the basics of discrete mathematics. Students learn to model real-life problems using abstract mathematical structures.

## Learning Objectives
- Recall the basics of sets and number systems
- Plot and analyse straight lines
- Understand and differentiate between linear, quadratic, polynomial, exponential and logarithmic functions
- Apply algorithmic methods to find roots, maxima and minima of polynomials
- Represent sets and relations as discrete graphs
- Formulate and solve common graph-based problems

## Course Structure
12 weeks of coursework with weekly online assignments, two invigilated quizzes and one invigilated end term exam.

## Weekly Topics
1.  **Set Theory**
    *   **Number Systems**:
        *   Natural Numbers (ℕ): Counting numbers starting from 1 (e.g., 1, 2, 3, ...). Some definitions include 0.
        *   Whole Numbers: Natural numbers including 0 (e.g., 0, 1, 2, 3, ...).
        *   Integers (ℤ): Whole numbers and their negatives (e.g., ..., -2, -1, 0, 1, 2, ...).
        *   Rational Numbers (ℚ): Numbers that can be expressed as a fraction p/q, where p and q are integers and q ≠ 0 (e.g., 1/2, -3/4, 5, 0.25). Rational numbers have terminating or repeating decimal expansions.
        *   Irrational Numbers: Numbers that cannot be expressed as a simple fraction of two integers (e.g., √2, π, e). Their decimal expansions are non-terminating and non-repeating.
        *   Real Numbers (ℝ): All rational and irrational numbers. They can be represented on a number line.
    *   **Sets**:
        *   Definition: A well-defined collection of distinct objects, called elements or members.
        *   Notation:
            *   Roster Form: Listing all elements, e.g., A = {1, 2, 3}.
            *   Set-Builder Form: Describing elements by a property, e.g., B = {x | x is an even number and x > 0}.
        *   Types of Sets:
            *   Empty Set (∅ or {}): A set with no elements.
            *   Finite Set: A set with a countable number of elements.
            *   Infinite Set: A set with an uncountable number of elements.
            *   Subset (⊆): Set A is a subset of set B if all elements of A are also elements of B. E.g., if A = {1, 2} and B = {1, 2, 3}, then A ⊆ B.
            *   Proper Subset (⊂): Set A is a proper subset of set B if A ⊆ B and A ≠ B.
            *   Superset (⊇): If A is a subset of B, then B is a superset of A.
            *   Power Set (P(A)): The set of all subsets of set A, including the empty set and the set itself. If |A| = n, then |P(A)| = 2^n. Example: If A = {1, 2}, P(A) = {∅, {1}, {2}, {1, 2}}.
            *   Universal Set (U): The set containing all possible elements relevant to a particular discussion.
    *   **Set Operations**:
        *   Union (A ∪ B): The set of elements that are in A, or in B, or in both. E.g., {1, 2} ∪ {2, 3} = {1, 2, 3}.
        *   Intersection (A ∩ B): The set of elements that are in both A and B. E.g., {1, 2} ∩ {2, 3} = {2}.
        *   Difference (A - B): The set of elements that are in A but not in B. E.g., {1, 2} - {2, 3} = {1}.
        *   Complement (A'): The set of elements in the universal set U that are not in A. A' = U - A.
        *   Cartesian Product (A × B): The set of all ordered pairs (a, b) such that a ∈ A and b ∈ B. E.g., {1, 2} × {a} = {(1, a), (2, a)}.
        *   Venn Diagrams: Visual representations of sets and their relationships using overlapping circles.
            *Example:*
            ```mermaid
            graph TD
                A --- B
            ```
            (Illustrative: A real Venn diagram would show circles for A and B, with overlaps representing intersections.)
    *   **Relations**:
        *   Definition: A set of ordered pairs (a, b) where 'a' is from a set A (domain) and 'b' is from a set B (codomain). The set of all second elements in the ordered pairs is called the range.
        *   Domain: The set of all first elements in the ordered pairs of a relation.
        *   Codomain: The set from which the second elements of the ordered pairs are chosen.
        *   Range: The set of all actual second elements in the ordered pairs. The range is a subset of the codomain.
        *   Types of Relations (on a set A, i.e., from A to A):
            *   Reflexive: A relation R on set A is reflexive if (a, a) ∈ R for every a ∈ A. Example: "is equal to" on ℤ. (5 = 5)
            *   Symmetric: A relation R on set A is symmetric if whenever (a, b) ∈ R, then (b, a) ∈ R. Example: "is a sibling of" (if A is a sibling of B, then B is a sibling of A).
            *   Transitive: A relation R on set A is transitive if whenever (a, b) ∈ R and (b, c) ∈ R, then (a, c) ∈ R. Example: "is less than" on ℕ (if a < b and b < c, then a < c).
            *   Equivalence Relation: A relation that is reflexive, symmetric, and transitive. It partitions the set into disjoint equivalence classes. Example: "has the same remainder when divided by 3" on ℤ.
    *   **Functions**:
        *   Definition: A function f from a set A (domain) to a set B (codomain), denoted f: A → B, is a special type of relation where every element in A is associated with exactly one element in B.
        *   Domain: The set A.
        *   Codomain: The set B.
        *   Range: The set of all actual output values f(a) for a ∈ A. The range is a subset of the codomain.
        *   Types of Functions:
            *   One-to-one (Injective): A function where distinct elements in the domain map to distinct elements in the codomain. If f(x1) = f(x2), then x1 = x2.
            *   Many-to-one: A function where at least two distinct elements in the domain map to the same element in the codomain.
            *   Onto (Surjective): A function where every element in the codomain B is an image of at least one element in the domain A. The range equals the codomain.
            *   One-to-one Correspondence (Bijective): A function that is both one-to-one (injective) and onto (surjective).
        *   Vertical Line Test: A graph represents a function if and only if no vertical line intersects the graph at more than one point.
        *   Composition of Functions: Given f: A → B and g: B → C, the composition (g ∘ f)(x) = g(f(x)).
        *   Inverse Functions: If f: A → B is a bijective function, then its inverse function f⁻¹: B → A exists, such that if f(a) = b, then f⁻¹(b) = a.
2.  **Coordinate Geometry**
    *   **Rectangular Coordinate System (Cartesian Plane)**:
        *   A plane formed by two perpendicular number lines: the horizontal x-axis and the vertical y-axis.
        *   Origin (0,0): The point where the x-axis and y-axis intersect.
        *   Quadrants: The four regions into which the axes divide the plane (I, II, III, IV, numbered counter-clockwise starting from the top right).
        *   Coordinates of a Point (x, y): An ordered pair that specifies the location of a point, where x is the horizontal distance from the origin and y is the vertical distance.
    *   **Plotting Points**:
        *   To plot a point (x, y), start at the origin, move x units horizontally (right if positive, left if negative), and then y units vertically (up if positive, down if negative).
        *   Distance Formula: The distance 'd' between two points (x1, y1) and (x2, y2) is given by d = √[(x2 - x1)² + (y2 - y1)²].
        *   Midpoint Formula: The midpoint M of a line segment connecting (x1, y1) and (x2, y2) is M = ((x1 + x2)/2, (y1 + y2)/2).
    *   **Slope of a Line (m)**:
        *   Definition: A measure of the steepness and direction of a line. It is the ratio of the vertical change (rise) to the horizontal change (run) between any two distinct points on the line.
        *   Formula: Given two points (x1, y1) and (x2, y2), the slope m = (y2 - y1) / (x2 - x1).
        *   Interpretation of Slope:
            *   Positive Slope (m > 0): Line rises from left to right.
            *   Negative Slope (m < 0): Line falls from left to right.
            *   Zero Slope (m = 0): Horizontal line.
            *   Undefined Slope: Vertical line (denominator x2 - x1 = 0).
    *   **Parallel and Perpendicular Lines**:
        *   Parallel Lines: Two non-vertical lines are parallel if and only if their slopes are equal (m1 = m2).
        *   Perpendicular Lines: Two non-vertical lines are perpendicular if and only if the product of their slopes is -1 (m1 * m2 = -1). This also means one slope is the negative reciprocal of the other (m2 = -1/m1).
    *   **Representations of a Line**:
        *   Slope-Intercept Form: y = mx + c, where m is the slope and c is the y-intercept (the y-coordinate where the line crosses the y-axis).
        *   Point-Slope Form: y - y1 = m(x - x1), where m is the slope and (x1, y1) is a point on the line.
        *   Two-Point Form: (y - y1) / (x - x1) = (y2 - y1) / (x2 - x1), derived from the slope formula using two points (x1, y1) and (x2, y2).
        *   Intercept Form: x/a + y/b = 1, where 'a' is the x-intercept and 'b' is the y-intercept.
        *   General Equation of a Line: Ax + By + C = 0, where A, B, and C are constants, and A and B are not both zero.
    *   **Straight-line Fit (Introduction)**:
        *   In data science, we often have a collection of data points that appear to follow a linear trend.
        *   Straight-line fitting, or linear regression, is the process of finding a single straight line that best represents the relationship in the data.
        *   Visually, this line tries to pass as close as possible to all data points. This line can then be used to make predictions or understand the underlying relationship between variables.
3.  **Quadratic Functions**
    *   **Quadratic Functions**:
        *   Definition: A function of the form f(x) = ax² + bx + c, where a, b, and c are real numbers and a ≠ 0.
    *   **Parabolas**:
        *   The graph of a quadratic function is a U-shaped curve called a parabola.
        *   Concavity:
            *   If a > 0, the parabola opens upwards (concave up), and the vertex is the minimum point.
            *   If a < 0, the parabola opens downwards (concave down), and the vertex is the maximum point.
        *   Axis of Symmetry: A vertical line that divides the parabola into two mirror images. Its equation is x = -b / (2a).
    *   **Vertex**:
        *   The highest point (maximum) or lowest point (minimum) of the parabola.
        *   Coordinates of the Vertex (h, k): h = -b / (2a), and k = f(h) = f(-b / (2a)).
    *   **Vertex Form**:
        *   The vertex form of a quadratic function is f(x) = a(x - h)² + k, where (h, k) is the vertex of the parabola.
        *   Conversion from Standard Form (ax² + bx + c) to Vertex Form:
            1.  Identify a, b, c.
            2.  Calculate h = -b / (2a).
            3.  Calculate k = f(h) = a(h)² + b(h) + c.
            4.  Substitute a, h, k into f(x) = a(x - h)² + k.
    *   **Roots/Zeros/X-intercepts**:
        *   These are the points where the parabola intersects the x-axis, i.e., where f(x) = 0.
        *   Methods to find roots:
            *   Factorisation: If the quadratic expression ax² + bx + c can be factored into a(x - r1)(x - r2), then r1 and r2 are the roots. Example: x² - 5x + 6 = (x - 2)(x - 3) = 0, so roots are x = 2 and x = 3.
            *   Quadratic Formula: For ax² + bx + c = 0, the roots are given by x = [-b ± √(b² - 4ac)] / (2a).
        *   Discriminant (Δ): Δ = b² - 4ac. The discriminant determines the nature of the roots:
            *   If Δ > 0: Two distinct real roots (parabola intersects x-axis at two points).
            *   If Δ = 0: One real root (or two equal real roots; parabola touches x-axis at one point - the vertex).
            *   If Δ < 0: No real roots (two complex conjugate roots; parabola does not intersect x-axis).
    *   **Completing the Square**:
        *   A method used to solve quadratic equations and to convert the standard form of a quadratic function to the vertex form.
        *   Steps for ax² + bx + c = 0:
            1. If a ≠ 1, divide the entire equation by a: x² + (b/a)x + (c/a) = 0.
            2. Move the constant term to the right side: x² + (b/a)x = -(c/a).
            3. Take half of the coefficient of x, square it, and add it to both sides. Half of (b/a) is (b/2a), squaring it gives (b/2a)².
               x² + (b/a)x + (b/2a)² = -(c/a) + (b/2a)².
            4. The left side is now a perfect square: (x + b/2a)² = (b² - 4ac) / 4a².
            5. Solve for x by taking the square root of both sides.
    *   **Maxima and Minima**:
        *   The vertex (h, k) of the parabola provides the maximum or minimum value of the quadratic function.
        *   If a > 0 (parabola opens upwards), the function has a minimum value of k at x = h.
        *   If a < 0 (parabola opens downwards), the function has a maximum value of k at x = h.
        *   Applications: Used in optimization problems, e.g., finding the maximum height of a projectile or minimizing costs.
4.  **Polynomials**
    *   **Polynomials**:
        *   Definition: An expression consisting of variables (also called indeterminates) and coefficients, that involves only the operations of addition, subtraction, multiplication, and non-negative integer exponents of variables. Example: P(x) = 3x⁴ - 2x² + x - 5.
        *   Degree of a Polynomial: The highest power of the variable in the polynomial. In the example, the degree is 4.
        *   Leading Term: The term with the highest power of the variable (3x⁴).
        *   Leading Coefficient: The coefficient of the leading term (3).
        *   Constant Term: The term without a variable (-5).
        *   Standard Form: Polynomials are usually written in descending order of powers of the variable.
        *   Types:
            *   Monomial: A polynomial with one term (e.g., 5x²).
            *   Binomial: A polynomial with two terms (e.g., 3x + 1).
            *   Trinomial: A polynomial with three terms (e.g., x² + 2x - 1).
    *   **Polynomial Arithmetic**:
        *   Addition and Subtraction: Combine like terms (terms with the same power of the variable).
            Example: (2x² + 3x - 1) + (x² - x + 4) = (2+1)x² + (3-1)x + (-1+4) = 3x² + 2x + 3.
        *   Multiplication: Use the distributive property. For binomials, the FOIL (First, Outer, Inner, Last) method can be used.
            Example: (x + 2)(x - 3) = x(x) + x(-3) + 2(x) + 2(-3) = x² - 3x + 2x - 6 = x² - x - 6.
    *   **Division of Polynomials**:
        *   Long Division: Similar to long division for numbers. Used to divide a polynomial by another polynomial of a lower or equal degree.
            Example: Divide x³ - 2x² + x - 5 by x - 2.
            ```
                  x²   + 1
              ________________
            x-2 | x³ - 2x² +  x - 5
                -(x³ - 2x²)
                _________
                       0 +  x - 5
                         -(x - 2)
                         _______
                               -3  (Remainder)
            ```
            So, (x³ - 2x² + x - 5) / (x - 2) = x² + 1 with a remainder of -3.
        *   Remainder Theorem: If a polynomial P(x) is divided by a linear binomial (x - c), the remainder is P(c).
            For the example above, P(x) = x³ - 2x² + x - 5, c = 2. P(2) = 2³ - 2(2)² + 2 - 5 = 8 - 8 + 2 - 5 = -3, which is the remainder.
        *   Factor Theorem: A linear binomial (x - c) is a factor of the polynomial P(x) if and only if P(c) = 0 (i.e., the remainder is 0).
        *   Synthetic Division: A shortcut method for dividing a polynomial by a linear binomial of the form (x - c).
            Example: Divide x³ - 2x² + x - 5 by x - 2 (c=2).
            ```
            2 | 1  -2   1  -5
              |    2   0   2
              ----------------
                1   0   1  -3
            ```
            The coefficients of the quotient are 1, 0, 1 (so x² + 0x + 1 = x² + 1) and the remainder is -3.
    *   **Graphs of Polynomials**:
        *   X-intercepts (Roots/Zeros): The points where the graph intersects or touches the x-axis. These are the real solutions to P(x) = 0.
        *   Multiplicity of Roots: The number of times a particular root appears as a factor of the polynomial.
            *   Odd Multiplicity: The graph crosses the x-axis at the root. Example: P(x) = (x-1)¹.
            *   Even Multiplicity: The graph touches the x-axis at the root (bounces off). Example: P(x) = (x-1)².
        *   End Behavior: The direction of the graph as x approaches positive infinity (x → ∞) and as x approaches negative infinity (x → -∞). It is determined by the leading term (axⁿ):
            *   n is even, a > 0: Up on left, Up on right (e.g., x²)
            *   n is even, a < 0: Down on left, Down on right (e.g., -x²)
            *   n is odd, a > 0: Down on left, Up on right (e.g., x³)
            *   n is odd, a < 0: Up on left, Down on right (e.g., -x³)
        *   Turning Points: Points where the graph changes from increasing to decreasing or vice-versa. A polynomial of degree n has at most (n - 1) turning points.
    *   **Graphing & Polynomial Creation**:
        *   To sketch a polynomial graph: Find x-intercepts (roots) and their multiplicities, determine end behavior, find y-intercept (P(0)), and use turning points to guide the shape.
        *   Creating a polynomial equation: If the roots (r1, r2, ..., rn) are known, the polynomial can be written in factored form: P(x) = a(x - r1)(x - r2)...(x - rn). The value of 'a' can be found if another point on the graph is known.
5.  **Functions (Advanced Topics)**
    *   **Review of Function Basics**:
        *   Definition: A rule that assigns each input element from a set (domain) to exactly one output element in another set (codomain).
        *   Domain: Set of all possible inputs.
        *   Codomain: Set of all possible outputs.
        *   Range: Set of all actual outputs.
    *   **Graphical Tests for Functions**:
        *   Vertical Line Test: A curve in the xy-plane represents the graph of a function if and only if no vertical line intersects the curve more than once. This ensures that each x-value maps to only one y-value.
        *   Horizontal Line Test: A function is one-to-one if and only if no horizontal line intersects its graph more than once. This ensures that each y-value is mapped from only one x-value.
    *   **One-to-one and Many-to-one Functions (Deeper Dive)**:
        *   One-to-one (Injective): Every distinct input produces a distinct output. Example: f(x) = 2x. If f(x1) = f(x2), then 2x1 = 2x2, which implies x1 = x2. These functions pass the Horizontal Line Test. They are crucial for having well-defined inverse functions.
        *   Many-to-one: At least two different inputs produce the same output. Example: f(x) = x². Here, f(2) = 4 and f(-2) = 4. These functions do not pass the Horizontal Line Test and do not have simple inverse functions unless their domain is restricted.
    *   **Inverse Functions**:
        *   Conditions for Existence: A function f must be bijective (both one-to-one and onto) to have an inverse function f⁻¹. If a function is not one-to-one, its inverse would not be a function (one input would map to multiple outputs). If it's not onto, the domain of the inverse would not cover all of the original function's codomain.
        *   Finding the Inverse:
            1.  Replace f(x) with y.
            2.  Swap x and y in the equation.
            3.  Solve the new equation for y. The resulting expression is f⁻¹(x).
            Example: Find the inverse of f(x) = 2x + 3.
            y = 2x + 3
            x = 2y + 3 (swap)
            x - 3 = 2y
            y = (x - 3) / 2
            So, f⁻¹(x) = (x - 3) / 2.
        *   Graphical Property: The graph of f⁻¹(x) is the reflection of the graph of f(x) across the line y = x.
        *   Composition Property: (f⁻¹ ∘ f)(x) = x and (f ∘ f⁻¹)(x) = x.
    *   **Exponential Functions**:
        *   Definition: A function of the form f(x) = aˣ, where 'a' is a positive constant called the base (a > 0, a ≠ 1), and 'x' is the exponent.
        *   Natural Exponential Function: f(x) = eˣ, where 'e' is Euler's number (approximately 2.71828). This base is frequently used in calculus and many natural phenomena.
        *   Properties:
            *   Domain: (-∞, ∞) (all real numbers).
            *   Range: (0, ∞) (all positive real numbers).
            *   Y-intercept: (0, 1) because a⁰ = 1 for any a ≠ 0.
            *   Horizontal Asymptote: The x-axis (y=0) is a horizontal asymptote. The graph approaches but never touches the x-axis.
        *   Graphs:
            *   If a > 1, the function is increasing (exponential growth). Example: f(x) = 2ˣ.
            *   If 0 < a < 1, the function is decreasing (exponential decay). Example: f(x) = (1/2)ˣ.
        *   Applications:
            *   Compound Interest: A = P(1 + r/n)^(nt).
            *   Population Growth: P(t) = P₀e^(kt).
            *   Radioactive Decay: N(t) = N₀e^(-λt).
    *   **Composition of Functions (Further Examples)**:
        *   Let f(x) = x² + 1 and g(x) = √(x - 1).
        *   (f ∘ g)(x) = f(g(x)) = f(√(x - 1)) = (√(x - 1))² + 1 = (x - 1) + 1 = x.
            Domain of g(x) is x ≥ 1. Range of g(x) is y ≥ 0. Domain of f(x) is all real numbers.
            Domain of (f ∘ g)(x) is x ≥ 1.
        *   (g ∘ f)(x) = g(f(x)) = g(x² + 1) = √((x² + 1) - 1) = √(x²) = |x|.
            Domain of f(x) is all real numbers. Range of f(x) is y ≥ 1. Domain of g(x) requires input ≥ 1.
            Since x² + 1 is always ≥ 1, the domain of (g ∘ f)(x) is all real numbers.
6.  **Logarithmic Functions**
    *   **Definition of Logarithms**:
        *   A logarithm is the power to which a base must be raised to produce a given number.
        *   If y = aˣ (exponential form), then x = logₐ(y) (logarithmic form).
        *   'a' is the base (a > 0, a ≠ 1), 'y' is the argument (y > 0).
        *   Example: Since 2³ = 8, then log₂(8) = 3.
    *   **Common Logarithm**: Base 10, written as log(x) or log₁₀(x). Used in various scientific scales.
    *   **Natural Logarithm**: Base 'e' (Euler's number), written as ln(x) or logₑ(x). Arises naturally in calculus and models continuous growth/decay.
    *   **Relationship between Logarithmic and Exponential Forms**:
        *   logₐ(y) = x  <=>  aˣ = y
        *   Example: Convert log₃(9) = 2 to exponential form: 3² = 9.
        *   Example: Convert 5⁴ = 625 to logarithmic form: log₅(625) = 4.
    *   **Graphs of Logarithmic Functions**: f(x) = logₐ(x)
        *   Domain: (0, ∞) (only positive real numbers). You cannot take the logarithm of a negative number or zero.
        *   Range: (-∞, ∞) (all real numbers).
        *   X-intercept: (1, 0) because logₐ(1) = 0 (since a⁰ = 1).
        *   Vertical Asymptote: The y-axis (x=0) is a vertical asymptote.
        *   Shape:
            *   If a > 1, the graph is increasing. Example: f(x) = log₂(x).
            *   If 0 < a < 1, the graph is decreasing. Example: f(x) = log₁/₂(x).
        *   The graph of logₐ(x) is a reflection of the graph of aˣ across the line y = x.
    *   **Laws of Logarithms**:
        *   Product Rule: logₐ(xy) = logₐ(x) + logₐ(y)  (The log of a product is the sum of the logs)
        *   Quotient Rule: logₐ(x/y) = logₐ(x) - logₐ(y) (The log of a quotient is the difference of the logs)
        *   Power Rule: logₐ(xᵖ) = p * logₐ(x) (The log of a number raised to a power is the power times the log of the number)
        *   Change of Base Formula: logₐ(x) = log<sub>b</sub>(x) / log<sub>b</sub>(a). This allows conversion between logarithms of different bases. Commonly used to convert to ln(x) or log(x) for calculator use: logₐ(x) = ln(x) / ln(a).
        *   Other properties: logₐ(a) = 1, logₐ(1) = 0, logₐ(aˣ) = x, a^(logₐ(x)) = x.
    *   **Solving Exponential Equations**:
        *   If possible, make the bases the same: If aᵁ = aⱽ, then U = V.
        *   Otherwise, take the logarithm (common or natural) of both sides and use the power rule to bring down the exponent.
            Example: Solve 3ˣ = 10.
            ln(3ˣ) = ln(10)
            x * ln(3) = ln(10)
            x = ln(10) / ln(3) ≈ 2.096.
    *   **Solving Logarithmic Equations**:
        *   Use laws of logarithms to combine terms into a single logarithm if possible.
        *   Convert the logarithmic equation to its exponential form.
        *   Solve for the variable.
        *   **Crucial**: Always check for extraneous solutions by substituting the solution back into the original equation. Logarithms are only defined for positive arguments.
            Example: Solve log₂(x) + log₂(x - 2) = 3.
            log₂(x(x - 2)) = 3
            x(x - 2) = 2³
            x² - 2x = 8
            x² - 2x - 8 = 0
            (x - 4)(x + 2) = 0
            x = 4 or x = -2.
            Check x = 4: log₂(4) + log₂(4 - 2) = 2 + log₂(2) = 2 + 1 = 3. (Valid)
            Check x = -2: log₂(-2) is undefined. (Extraneous solution)
            So, the only solution is x = 4.
    *   **Applications**:
        *   pH Scale: pH = -log[H⁺] (concentration of hydrogen ions).
        *   Richter Scale: Magnitude M = log(I/S) (measures earthquake intensity).
        *   Decibel Levels (Sound Intensity): dB = 10 * log(P₁/P₀).
        *   Information Theory: Entropy calculations.
7.  **Sequences and Limits**
    *   **Sequences**:
        *   Definition: An ordered list of numbers, called terms. A sequence can be thought of as a function whose domain is the set of natural numbers.
        *   Notation: Often denoted by {a<sub>n</sub>} or a<sub>n</sub>, where a<sub>n</sub> is the nth term.
        *   Example: {1, 3, 5, 7, ...}, where a<sub>n</sub> = 2n - 1.
    *   **Arithmetic Sequences**:
        *   Definition: A sequence where the difference between consecutive terms is constant. This constant difference is called the common difference (d).
        *   Formula for nth term: a<sub>n</sub> = a₁ + (n-1)d, where a₁ is the first term.
        *   Sum of first n terms: S<sub>n</sub> = n/2 * [2a₁ + (n-1)d] or S<sub>n</sub> = n/2 * (a₁ + a<sub>n</sub>).
        *   Example: Sequence 2, 5, 8, 11, ... (a₁ = 2, d = 3). a₄ = 2 + (4-1)3 = 11.
    *   **Geometric Sequences**:
        *   Definition: A sequence where the ratio between consecutive terms is constant. This constant ratio is called the common ratio (r).
        *   Formula for nth term: a<sub>n</sub> = a₁ * r<sup>(n-1)</sup>, where a₁ is the first term.
        *   Sum of first n terms: S<sub>n</sub> = a₁(1 - r<sup>n</sup>) / (1 - r), for r ≠ 1.
        *   Sum of an infinite geometric series: If |r| < 1, the series converges and its sum is S = a₁ / (1 - r). If |r| ≥ 1, the series diverges.
        *   Example: Sequence 3, 6, 12, 24, ... (a₁ = 3, r = 2). a₄ = 3 * 2<sup>(4-1)</sup> = 24.
    *   **Introduction to Limits (Intuitive)**:
        *   The concept of a limit describes the value that a function or sequence "approaches" as the input or index approaches some value.
        *   It's about the behavior of the function *near* a point, not necessarily *at* the point itself.
    *   **Limits of Sequences**:
        *   lim (n→∞) a<sub>n</sub> = L means that the terms of the sequence a<sub>n</sub> get arbitrarily close to L as n becomes very large.
        *   Convergent Sequence: A sequence that has a finite limit. Example: a<sub>n</sub> = 1/n, lim (n→∞) 1/n = 0.
        *   Divergent Sequence: A sequence that does not have a finite limit (it may go to ∞, -∞, or oscillate). Example: a<sub>n</sub> = n, lim (n→∞) n = ∞.
    *   **Limits of Functions**:
        *   lim (x→c) f(x) = L means that the values of f(x) get arbitrarily close to L as x gets arbitrarily close to c (but not equal to c).
        *   One-Sided Limits:
            *   Right-hand limit: lim (x→c⁺) f(x) (x approaches c from values greater than c).
            *   Left-hand limit: lim (x→c⁻) f(x) (x approaches c from values less than c).
            *   The limit lim (x→c) f(x) exists if and only if lim (x→c⁺) f(x) = lim (x→c⁻) f(x) = L.
    *   **Limit Laws/Properties**: If lim (x→c) f(x) = L and lim (x→c) g(x) = M:
        *   Sum Rule: lim [f(x) + g(x)] = L + M.
        *   Difference Rule: lim [f(x) - g(x)] = L - M.
        *   Product Rule: lim [f(x) * g(x)] = L * M.
        *   Quotient Rule: lim [f(x) / g(x)] = L / M (if M ≠ 0).
        *   Constant Multiple Rule: lim [k * f(x)] = k * L.
        *   Power Rule: lim [f(x)]<sup>n</sup> = L<sup>n</sup>.
    *   **Evaluating Limits**:
        *   Direct Substitution: If f(x) is a polynomial or rational function and c is in its domain, then lim (x→c) f(x) = f(c).
        *   Factorization and Cancellation: For indeterminate forms like 0/0. Example: lim (x→1) (x²-1)/(x-1) = lim (x→1) (x-1)(x+1)/(x-1) = lim (x→1) (x+1) = 2.
        *   Rationalization: Multiplying by the conjugate, often for limits involving square roots.
        *   L'Hôpital's Rule (brief mention): If a limit is of the form 0/0 or ∞/∞, it can sometimes be evaluated by taking the derivatives of the numerator and denominator. (More detail in Week 8).
    *   **Tangent Lines (Conceptual Link to Limits)**:
        *   A secant line passes through two points on a curve. Its slope is (f(x) - f(c)) / (x - c).
        *   A tangent line touches the curve at a single point c. Its slope is found by taking the limit of the slopes of secant lines as x approaches c: m_tangent = lim (x→c) [f(x) - f(c)] / (x - c). This is the definition of the derivative.
    *   **Continuity**:
        *   Definition of Continuity at a Point: A function f is continuous at a point x=c if all three conditions are met:
            1.  f(c) is defined (c is in the domain of f).
            2.  lim (x→c) f(x) exists (left-hand limit = right-hand limit).
            3.  lim (x→c) f(x) = f(c) (the limit equals the function value).
        *   Continuity on an Interval: A function is continuous on an interval if it is continuous at every point in that interval. Most common functions (polynomials, rational functions where defined, exponential, logarithmic, trigonometric) are continuous on their domains.
    *   **Discontinuities**: Points where a function is not continuous.
        *   Types:
            *   Removable Discontinuity (Hole): Occurs when lim (x→c) f(x) exists but is not equal to f(c), or f(c) is undefined. Graphically, there's a hole in the graph. Example: f(x) = (x²-1)/(x-1) at x=1.
            *   Jump Discontinuity: Occurs when the left-hand limit and right-hand limit both exist but are not equal. Graphically, there's a jump in the graph. Example: A step function like f(x) = 1 for x ≥ 0, and f(x) = -1 for x < 0, at x=0.
            *   Infinite Discontinuity (Asymptotic): Occurs when one or both of the one-sided limits go to ∞ or -∞. Graphically, there's a vertical asymptote. Example: f(x) = 1/x at x=0.
        *   Intermediate Value Theorem: If f is continuous on a closed interval [a, b], and N is any number between f(a) and f(b) (where f(a) ≠ f(b)), then there exists at least one number c in (a, b) such that f(c) = N. Intuitively, a continuous function doesn't skip values.
8.  **Derivatives & Critical Points**
    *   **Definition of the Derivative**:
        *   As the slope of the tangent line to the graph of f(x) at point x:
            f'(x) = lim (h→0) [f(x+h) - f(x)] / h
            This limit represents the slope of the line that just touches the curve at x.
        *   As the instantaneous rate of change of the function f(x) with respect to x.
            Example: If f(t) is position at time t, f'(t) is instantaneous velocity.
        *   Notations:
            *   Lagrange's notation: f'(x) (read "f prime of x")
            *   Leibniz's notation: dy/dx (read "d y d x" or "derivative of y with respect to x")
            *   y' (read "y prime")
            *   d/dx [f(x)] (operator notation)
    *   **Differentiability**:
        *   A function is differentiable at a point x=c if f'(c) exists.
        *   Conditions for Non-differentiability:
            *   Corners: e.g., f(x) = |x| at x=0. The left and right limits of the difference quotient are different.
            *   Cusps: e.g., f(x) = x^(2/3) at x=0. Slopes of secant lines approach ∞ from one side and -∞ from the other.
            *   Vertical Tangents: e.g., f(x) = x^(1/3) at x=0. The tangent line is vertical, so its slope is undefined.
            *   Discontinuities: If a function is not continuous at a point, it cannot be differentiable at that point.
        *   Relationship between Differentiability and Continuity: If a function is differentiable at a point, it MUST be continuous at that point. However, a function can be continuous at a point but not differentiable there (e.g., f(x) = |x| at x=0).
    *   **Basic Differentiation Rules**:
        *   Constant Rule: d/dx (c) = 0 (The derivative of a constant is zero).
        *   Power Rule: d/dx (xⁿ) = nxⁿ⁻¹ (For any real number n). Example: d/dx (x³) = 3x².
        *   Constant Multiple Rule: d/dx [c * f(x)] = c * f'(x). Example: d/dx (5x³) = 5 * (3x²) = 15x².
        *   Sum/Difference Rule: d/dx [f(x) ± g(x)] = f'(x) ± g'(x). Example: d/dx (x² + 3x) = 2x + 3.
        *   Derivative of eˣ: d/dx (eˣ) = eˣ.
        *   Derivative of ln(x): d/dx (ln(x)) = 1/x (for x > 0).
    *   **Product Rule**: For differentiating the product of two functions:
        *   d/dx [f(x)g(x)] = f'(x)g(x) + f(x)g'(x)
        *   Example: d/dx (x² * eˣ) = (2x)(eˣ) + (x²)(eˣ) = xeˣ(2 + x).
    *   **Quotient Rule**: For differentiating the quotient of two functions:
        *   d/dx [f(x)/g(x)] = [f'(x)g(x) - f(x)g'(x)] / [g(x)]² (where g(x) ≠ 0)
        *   Example: d/dx (x² / (x+1)) = [2x(x+1) - x²(1)] / (x+1)² = (2x² + 2x - x²) / (x+1)² = (x² + 2x) / (x+1)².
    *   **Chain Rule (Introduction)**: For differentiating composite functions f(g(x)):
        *   d/dx [f(g(x))] = f'(g(x)) * g'(x) (Derivative of the outer function evaluated at the inner function, times the derivative of the inner function).
        *   Example: d/dx [(x² + 1)³]. Let u = x² + 1 (inner), f(u) = u³ (outer).
            f'(u) = 3u², u'(x) = 2x.
            So, d/dx [(x² + 1)³] = 3(x² + 1)² * (2x) = 6x(x² + 1)².
    *   **L'Hôpital's Rule**:
        *   Used to evaluate limits of indeterminate forms like 0/0 or ∞/∞.
        *   If lim (x→c) f(x)/g(x) is of the form 0/0 or ∞/∞, AND if lim (x→c) f'(x)/g'(x) exists (or is ±∞),
            then lim (x→c) f(x)/g(x) = lim (x→c) f'(x)/g'(x).
        *   Example: lim (x→0) sin(x)/x (form 0/0).
            lim (x→0) cos(x)/1 = cos(0)/1 = 1/1 = 1.
    *   **Critical Points**:
        *   A point 'c' in the domain of f is a critical point if either f'(c) = 0 or f'(c) is undefined.
        *   These are candidates for where local maxima or minima can occur.
    *   **Finding Extrema (Local/Relative Maxima and Minima)**:
        *   Local Maximum: A point where the function's value is greater than or equal to the values at nearby points.
        *   Local Minimum: A point where the function's value is less than or equal to the values at nearby points.
        *   First Derivative Test:
            1. Find critical points of f.
            2. Determine the sign of f'(x) in intervals to the left and right of each critical point.
            *   If f'(x) changes from positive to negative at c, then f has a local maximum at c.
            *   If f'(x) changes from negative to positive at c, then f has a local minimum at c.
            *   If f'(x) does not change sign at c, then f has neither a local maximum nor minimum at c (e.g., a saddle point or horizontal inflection).
        *   Intervals of Increase and Decrease:
            *   If f'(x) > 0 on an interval, f is increasing on that interval.
            *   If f'(x) < 0 on an interval, f is decreasing on that interval.
    *   **Linear Approximation**:
        *   The tangent line to the graph of f(x) at x=a can be used to approximate values of f(x) for x near a.
        *   The equation of the tangent line is L(x) = f(a) + f'(a)(x-a).
        *   So, for x near a, f(x) ≈ f(a) + f'(a)(x-a).
        *   Example: Approximate √4.1. Let f(x) = √x, a = 4.
            f(a) = √4 = 2.
            f'(x) = 1/(2√x), so f'(a) = f'(4) = 1/(2√4) = 1/4.
            √4.1 ≈ f(4) + f'(4)(4.1 - 4) = 2 + (1/4)(0.1) = 2 + 0.025 = 2.025.
9.  **Integrals**
    *   **Antiderivatives**:
        *   Concept: If the derivative of F(x) is f(x) (i.e., F'(x) = f(x)), then F(x) is an antiderivative of f(x).
        *   Reversing Differentiation: Integration is often thought of as the reverse process of differentiation.
        *   Family of Antiderivatives: If F(x) is an antiderivative of f(x), then any function of the form F(x) + C, where C is an arbitrary constant (the constant of integration), is also an antiderivative. This is because the derivative of a constant is zero.
        *   Example: If f(x) = 2x, then F(x) = x² is an antiderivative, because d/dx(x²) = 2x. So are x² + 5, x² - 3, etc. We write the general antiderivative as x² + C.
    *   **Indefinite Integrals**:
        *   Notation: ∫f(x)dx represents the family of all antiderivatives of f(x). It is called the indefinite integral of f(x) with respect to x.
        *   ∫f(x)dx = F(x) + C, where F'(x) = f(x).
        *   Basic Integration Rules (reverse of differentiation rules):
            *   Power Rule: ∫xⁿdx = (xⁿ⁺¹)/(n+1) + C (for n ≠ -1). Example: ∫x³dx = x⁴/4 + C.
            *   Constant Rule: ∫kdx = kx + C.
            *   Constant Multiple Rule: ∫k*f(x)dx = k * ∫f(x)dx.
            *   Sum/Difference Rule: ∫[f(x) ± g(x)]dx = ∫f(x)dx ± ∫g(x)dx.
            *   Integral of eˣ: ∫eˣdx = eˣ + C.
            *   Integral of 1/x: ∫(1/x)dx = ln|x| + C (absolute value is important as x can be negative, but ln is defined for positive values).
    *   **Area Under a Curve**:
        *   The problem: Finding the exact area of a region in the xy-plane bounded by the graph of a non-negative continuous function y = f(x), the x-axis, and the vertical lines x = a and x = b.
    *   **Riemann Sums**:
        *   Approximating Area: The area under the curve is approximated by dividing the interval [a, b] into n subintervals of equal width Δx = (b-a)/n, and then summing the areas of rectangles constructed on these subintervals.
        *   Types of Sums:
            *   Left Riemann Sum: Uses the left endpoint of each subinterval to determine the height of the rectangle: Σ f(x<sub>i-1</sub>)Δx.
            *   Right Riemann Sum: Uses the right endpoint: Σ f(x<sub>i</sub>)Δx.
            *   Midpoint Riemann Sum: Uses the midpoint: Σ f((x<sub>i-1</sub>+x<sub>i</sub>)/2)Δx.
        *   Definition of the Definite Integral: The definite integral of f(x) from a to b is the limit of these Riemann sums as the number of subintervals n approaches infinity (and Δx approaches 0):
            ∫<sub>a</sub><sup>b</sup> f(x)dx = lim (n→∞) Σ<sub>i=1</sub><sup>n</sup> f(x<sub>i</sub>*)Δx, where x<sub>i</sub>* is any sample point in the i-th subinterval.
            If the limit exists, f(x) is said to be integrable on [a, b].
    *   **Definite Integrals**:
        *   Notation: ∫<sub>a</sub><sup>b</sup> f(x)dx, where 'a' is the lower limit of integration and 'b' is the upper limit.
        *   Interpretation: Represents the net signed area between the curve f(x) and the x-axis from x=a to x=b. Areas above the x-axis are positive; areas below are negative.
        *   Properties:
            *   ∫<sub>a</sub><sup>a</sup> f(x)dx = 0.
            *   ∫<sub>a</sub><sup>b</sup> f(x)dx = -∫<sub>b</sub><sup>a</sup> f(x)dx.
            *   ∫<sub>a</sub><sup>b</sup> k*f(x)dx = k * ∫<sub>a</sub><sup>b</sup> f(x)dx.
            *   ∫<sub>a</sub><sup>b</sup> [f(x) ± g(x)]dx = ∫<sub>a</sub><sup>b</sup> f(x)dx ± ∫<sub>a</sub><sup>b</sup> g(x)dx.
            *   ∫<sub>a</sub><sup>c</sup> f(x)dx + ∫<sub>c</sub><sup>b</sup> f(x)dx = ∫<sub>a</sub><sup>b</sup> f(x)dx.
    *   **The Fundamental Theorem of Calculus (FTC)**:
        *   Part 1 (FTC1): If f is continuous on [a, b] and F(x) is defined as F(x) = ∫<sub>a</sub><sup>x</sup> f(t)dt, then F'(x) = f(x) for every x in [a, b].
            This part shows that differentiation and integration are inverse processes: the derivative of an integral (defined as an area function) is the original function.
        *   Part 2 (FTC2 - Evaluation Theorem): If f is continuous on [a, b] and F is any antiderivative of f (i.e., F'(x) = f(x)), then:
            ∫<sub>a</sub><sup>b</sup> f(x)dx = F(b) - F(a).
            This provides a powerful method for evaluating definite integrals without directly using the limit of Riemann sums.
            Example: Evaluate ∫<sub>1</sub><sup>3</sup> x²dx.
            An antiderivative of x² is F(x) = x³/3.
            So, ∫<sub>1</sub><sup>3</sup> x²dx = F(3) - F(1) = (3³/3) - (1³/3) = 27/3 - 1/3 = 9 - 1/3 = 26/3.
    *   **Applications of Integration**:
        *   Area Calculation: Primary application discussed. Area between two curves: ∫<sub>a</sub><sup>b</sup> [f(x) - g(x)]dx.
        *   Net Change: If f'(x) is the rate of change of a quantity f(x), then ∫<sub>a</sub><sup>b</sup> f'(x)dx = f(b) - f(a) gives the net change in f(x) from x=a to x=b.
        *   Average Value of a Function: The average value of f(x) on [a,b] is (1/(b-a)) * ∫<sub>a</sub><sup>b</sup> f(x)dx.
    *   **Basic Techniques of Integration**:
        *   Substitution Rule (u-substitution): Used to integrate composite functions. It's the reverse of the chain rule for differentiation.
            If u = g(x), then du = g'(x)dx. So, ∫f(g(x))g'(x)dx = ∫f(u)du.
            Example: ∫2x * (x² + 1)⁵ dx.
            Let u = x² + 1. Then du = 2x dx.
            The integral becomes ∫u⁵du = u⁶/6 + C = (x² + 1)⁶/6 + C.
10. **Graph Theory Basics**
    *   **Introduction to Graphs**:
        *   Definition: A graph G = (V, E) consists of a set V of vertices (or nodes) and a set E of edges (or links/arcs), where each edge connects two vertices.
        *   Examples: Social networks (people are vertices, friendships are edges), road networks (intersections are vertices, roads are edges), the World Wide Web (web pages are vertices, hyperlinks are edges).
    *   **Types of Graphs**:
        *   Undirected Graph: Edges have no orientation; (u, v) is the same as (v, u).
        *   Directed Graph (Digraph): Edges have a direction; (u, v) goes from u to v.
        *   Weighted Graph: Each edge has an associated numerical value (weight or cost). Unweighted graphs assume all edges have weight 1 or are simply unconcerned with weight.
        *   Simple Graph: An unweighted, undirected graph with no loops (edges from a vertex to itself) and no multiple edges between the same two vertices.
        *   Multigraph: Allows multiple edges between the same pair of vertices.
        *   Pseudograph: Allows loops and multiple edges.
        *   Complete Graph (K<sub>n</sub>): A simple undirected graph where every pair of distinct vertices is connected by a unique edge. K<sub>n</sub> has n(n-1)/2 edges.
        *   Cycle (C<sub>n</sub>): A graph with n vertices where vertices are connected in a circular fashion (v<sub>1</sub>-v<sub>2</sub>-...-v<sub>n</sub>-v<sub>1</sub>).
        *   Path (P<sub>n</sub>): A graph with n vertices connected in a line.
        *   Bipartite Graph: A graph whose vertices can be divided into two disjoint sets, U and V, such that every edge connects a vertex in U to one in V.
    *   **Graph Terminology**:
        *   Adjacent Vertices (Neighbors): Two vertices are adjacent if there is an edge connecting them.
        *   Degree of a Vertex (for undirected graphs): The number of edges incident to it. Sum of degrees = 2|E|.
        *   In-degree (for digraphs): Number of edges pointing to a vertex.
        *   Out-degree (for digraphs): Number of edges pointing from a vertex. Sum of in-degrees = Sum of out-degrees = |E|.
        *   Path: A sequence of vertices where each adjacent pair is connected by an edge.
        *   Cycle: A path that starts and ends at the same vertex and does not repeat other vertices.
        *   Connected Graph (undirected): There is a path between every pair of distinct vertices.
        *   Connected Components: The maximally connected subgraphs of an undirected graph.
        *   Strongly Connected Components (digraphs): A digraph is strongly connected if there is a directed path from u to v and from v to u for every pair of vertices u, v. SCCs are the maximal strongly connected subgraphs.
    *   **Representing Graphs**:
        *   Adjacency Matrix: A |V| x |V| matrix A where A[i][j] = 1 if there is an edge from vertex i to vertex j, and 0 otherwise. For weighted graphs, A[i][j] can store the weight.
            *   Pros: Fast to check if an edge (i,j) exists (O(1)).
            *   Cons: Space complexity O(|V|²), which is inefficient for sparse graphs (graphs with few edges). Adding/removing vertices is hard.
        *   Adjacency List: An array of lists. For each vertex u, Adj[u] stores a list of vertices adjacent to u. For weighted graphs, the list can store pairs (neighbor, weight).
            *   Pros: Space efficient for sparse graphs O(|V| + |E|). Easy to iterate over neighbors of a vertex.
            *   Cons: Checking for an edge (u,v) can take O(degree(u)) time.
    *   **Graph Traversals**: Algorithms for systematically visiting all vertices in a graph.
        *   Breadth-First Search (BFS):
            *   Algorithm: Starts at a source vertex, explores all its neighbors at the present depth prior to moving on to the vertices at the next depth level. Uses a queue.
            *   Properties: Finds the shortest path (in terms of number of edges) from the source to all other vertices in an unweighted graph.
            *   Example: Useful for finding connected components, shortest paths in unweighted graphs.
        *   Depth-First Search (DFS):
            *   Algorithm: Explores as far as possible along each branch before backtracking. Uses a stack (often implicitly via recursion).
            *   Properties: Useful for cycle detection, topological sorting, finding connected components, path finding.
            *   Example: Can produce a DFS tree/forest.
    *   **Directed Acyclic Graphs (DAGs)**:
        *   Definition: A directed graph that contains no directed cycles.
        *   Examples: Task scheduling (tasks and their dependencies), prerequisite charts for courses, version history in Git.
    *   **Topological Sorting**:
        *   Definition: A linear ordering of vertices in a DAG such that for every directed edge (u,v) from vertex u to vertex v, u comes before v in the ordering. A DAG can have multiple topological sorts.
        *   Algorithms:
            *   Kahn's Algorithm: Based on in-degrees. Repeatedly find vertices with in-degree 0, add them to the sort, and remove their outgoing edges. Uses a queue.
            *   DFS-based Algorithm: Perform DFS. The topological sort is the reverse of the finishing times of the vertices.
        *   Example: If A depends on B, and B depends on C, a topological sort could be C, B, A.
    *   **Applications**: Network analysis (social, biological, computer networks), recommendation systems (user-item interactions), logistics and operations research, bioinformatics (gene interactions), circuit design.
11. **Graph Algorithms**
    *   **Shortest Path Problems**: Finding a path between two vertices such that the sum of the weights of its constituent edges is minimized.
        *   **Single-Source Shortest Paths (SSSP)**: Find the shortest paths from a single source vertex 's' to all other vertices in the graph.
            *   Dijkstra's Algorithm:
                *   Applies to graphs with non-negative edge weights.
                *   Algorithm: Maintains a set of visited vertices and distances to all vertices (initially 0 for source, ∞ for others). Iteratively selects the unvisited vertex with the smallest known distance, marks it visited, and updates distances to its neighbors. Often implemented using a priority queue.
                *   Example: GPS navigation, network routing protocols.
                *   Limitations: Fails if there are negative edge weights because its greedy choice might not be optimal in such cases.
            *   Bellman-Ford Algorithm:
                *   Applies to graphs that may include negative edge weights.
                *   Algorithm: Relaxes all edges |V|-1 times. In each relaxation step, it updates distances if a shorter path is found. After |V|-1 iterations, if distances can still be improved, a negative-weight cycle reachable from the source is detected.
                *   Example: Detecting arbitrage opportunities in currency exchange.
                *   Handles negative weights correctly and can detect negative cycles (if after |V|-1 iterations, an edge can still be relaxed, a negative cycle exists).
    *   **All-Pairs Shortest Paths (APSP)**: Finding the shortest paths between all pairs of vertices in the graph.
        *   Floyd-Warshall Algorithm:
            *   Dynamic programming approach.
            *   Algorithm: Iteratively considers all possible intermediate vertices for each pair of start and end vertices. For each pair (i,j) and intermediate vertex k, it checks if path i-k-j is shorter than the current path i-j.
            *   Complexity: O(|V|³).
            *   Example: Precomputing distances in a network, transit route planning.
            *   Handles negative edge weights (but reports existence if negative cycles make shortest paths undefined).
    *   **Minimum Spanning Trees (MST)**:
        *   Definition: Given a connected, undirected, weighted graph, an MST is a subgraph that connects all vertices together, without any cycles and with the minimum possible total edge weight.
        *   Applications: Network design (e.g., laying cables to connect cities with minimum cost), clustering, image segmentation.
        *   Prim's Algorithm:
            *   Greedy algorithm that builds the MST one vertex at a time.
            *   Algorithm: Starts with an arbitrary vertex. In each step, adds the cheapest edge connecting a vertex in the growing MST to a vertex outside the MST. Often uses a priority queue to select the minimum weight edge.
            *   Example: Good for dense graphs.
        *   Kruskal's Algorithm:
            *   Greedy algorithm that builds the MST one edge at a time.
            *   Algorithm: Sorts all edges by weight in ascending order. Iteratively adds the next cheapest edge if it does not form a cycle with previously added edges. Uses a Disjoint Set Union (DSU) data structure to efficiently detect cycles.
            *   Example: Good for sparse graphs.
    *   **Applications**: Network routing (OSPF, RIP use SSSP), flight or traffic information systems, gene network analysis, image processing, efficient resource allocation.
12. **Revision**
    *   **Summary of Key Concepts**:
        *   Set Theory & Basic Logic: Number systems, set operations, relations, functions.
        *   Functions: Properties of linear, quadratic, polynomial, exponential, and logarithmic functions; their graphs and applications. Inverse functions, composition.
        *   Coordinate Geometry: Points, lines, slopes, distances, equations of lines.
        *   Sequences & Series: Arithmetic and geometric sequences and their sums.
        *   Limits & Continuity: Concept of limits for sequences and functions, limit laws, continuity and its types, Intermediate Value Theorem.
        *   Derivatives: Definition as slope/rate of change, rules of differentiation (power, product, quotient, chain), L'Hôpital's rule, applications like finding maxima/minima, intervals of increase/decrease, linear approximation.
        *   Integrals: Antiderivatives, indefinite and definite integrals, Riemann sums, Fundamental Theorem of Calculus, basic integration techniques (substitution), application in finding areas.
        *   Graph Theory Basics: Types of graphs, representation (adjacency matrix/list), traversals (BFS, DFS), Directed Acyclic Graphs (DAGs), topological sorting.
        *   Graph Algorithms: Shortest path algorithms (Dijkstra, Bellman-Ford, Floyd-Warshall), Minimum Spanning Tree algorithms (Prim, Kruskal).
    *   **Problem-Solving Strategies**:
        *   Revisit Definitions and Theorems: Ensure a solid understanding of the formal definitions and the statements of major theorems.
        *   Practice Diverse Problems: Work through examples from lectures, textbooks, and assignments. Start with basic problems to solidify understanding before tackling more complex ones.
        *   Identify Keywords and Patterns: Learn to recognize which concepts or methods are applicable based on the problem's wording and structure.
        *   Step-by-Step Tracing: For algorithms (especially graph algorithms), manually trace their execution on small, representative examples to understand their mechanics.
        *   Visualization: Sketch graphs of functions, draw diagrams for geometry problems, and visualize graph structures.
    *   **Interconnections between Topics**:
        *   Recognize how calculus concepts are linked: limits are the foundation for derivatives and definite integrals.
        *   Understand functions as a core concept that reappears in algebra, calculus, and even in graph theory (e.g., a sequence is a function).
        *   Appreciate how different areas of mathematics are used to model and solve problems.
    *   **Focus Areas for Data Science**:
        *   Calculus (Derivatives & Integrals): Essential for optimization algorithms in machine learning (e.g., gradient descent), understanding probability distributions.
        *   Linear Algebra (covered in "Additional Topics" but related): Fundamental for data representation (vectors, matrices), dimensionality reduction, and many machine learning models.
        *   Graph Theory: Useful for analyzing networks (social, information, biological), recommendation systems, and understanding complex relationships in data.
        *   Functions (Exponential, Logarithmic): Key for modeling growth, decay, and transformations in data.
    *   **Suggested Practice**:
        *   Review past assignments and quiz/exam questions.
        *   Work through solved examples in the reference texts, then attempt similar unsolved problems.
        *   Use online resources like Khan Academy, Paul's Online Math Notes, or university open courseware for additional explanations and practice problems.
        *   Collaborate with peers in study groups to discuss challenging concepts and solve problems together. Explaining a concept to someone else is a great way to solidify your own understanding.
        *   For conceptual topics, try to summarize them in your own words.

## Glossary
- **Polynomial**: an expression made up of variables and coefficients using only addition, subtraction, multiplication and non-negative integer exponents.
- **Composite Function**: a function created when one function is applied after another.
- **Derivative**: the rate at which a function changes with respect to its input value; geometrically the slope of the tangent.
- **BFS/DFS**: Breadth-first and depth-first search algorithms for exploring graphs.

## Reference Texts
- *Introductory Algebra: a real-world approach* (4th Edition) by Ignacio Bello
- *Sets & Functions (VOL 1)*, *Calculus (VOL 2)* and *Graph Theory (VOL 3)*

## Additional Topics
- **Complex Numbers** – arithmetic with imaginary units, polar representation and Euler's formula
- **Matrices** – matrix operations, determinants, inverses and applications in systems of equations
- **Probability Review** – counting principles and how they connect to polynomial expansions

## Further Reading
- *Linear Algebra and Its Applications* by Gilbert Strang
