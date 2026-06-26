import sqlite3

conn = sqlite3.connect("study.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS topics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject TEXT,
    title TEXT,
    content TEXT,
    questions TEXT
)
""")
  
def insert_topics(topics):
    for subject, title, content, questions in topics:
        cur.execute("SELECT id FROM topics WHERE subject = ? AND title = ?", (subject, title))
        if not cur.fetchone():
            cur.execute("INSERT INTO topics (subject, title, content, questions) VALUES (?, ?, ?, ?)",
                (subject, title, content, questions)
            )

math_topics = [
    ("Math", "Financial Mathematics",
"""Loans and Investments

• Rearranging the Future Value Formula

• Appreciation

• Shares and Dividends

• Depreciation

• Reducing Balance Loans

• Credit Cards

Annuities

• Introduction to Annuities

Applications of Financial Mathematics

• Investments
• Savings Plans
• Loans
• Mortgages
• Credit Cards
• Superannuation

Financial Formulas

• Future Value
• Present Value
• Compound Interest
• Depreciation Models
• Loan Repayments
• Annuities

Financial Decision Making

• Comparing Investment Options
• Evaluating Loan Costs
• Analysing Interest Rates
• Understanding Risk and Return
""",

"""1. What is the Future Value formula?
2. How can the Future Value formula be rearranged?
3. What is appreciation?
4. How is appreciation calculated?
5. What are shares?
6. What are dividends?
7. What is depreciation?
8. What is the difference between straight-line and reducing balance depreciation?
9. What is a reducing balance loan?
10. How is interest calculated on a reducing balance loan?
11. How do credit cards charge interest?
12. What is an annuity?
13. How are annuities used in financial planning?
14. What factors should be considered when comparing investments?
15. How can Financial Mathematics be applied in everyday life?
"""), 
("Math", "Rates and Ratio",
"""Rates

• Rates and Fuel Consumption

• Energy Cost and Consumption

Applications of Rates

• Speed
• Fuel Consumption
• Energy Consumption
• Unit Pricing
• Population Growth
• Water Usage

Ratio

• Ratio

• Scale Drawings

• Trapezoidal Rule (Using Ratio)

Applications of Ratio

• Simplifying Ratios
• Sharing in a Given Ratio
• Comparing Quantities
• Scale Models
• Scale Maps
• Financial Applications

Problem Solving

• Converting Between Units
• Interpreting Real-World Data
• Using Ratios to Estimate Values
• Applying Rates to Everyday Situations

Mathematical Modelling

• Using Rates and Ratios to Solve Real-World Problems
• Interpreting Results
• Checking Reasonableness of Solutions
""",

"""1. What Is A Rate?
2. What Is A Ratio?
3. What Is The Difference Between A Rate And A Ratio?
4. How Is Fuel Consumption Calculated?
5. How Can Rates Be Used To Compare Energy Consumption?
6. What Is A Unit Rate?
7. How Are Ratios Simplified?
8. How Is A Quantity Shared In A Given Ratio?
9. What Is A Scale Drawing?
10. How Are Scale Drawings Used In Real Life?
11. What Is The Trapezoidal Rule?
12. How Can Rates And Ratios Be Applied To Financial Situations?
13. Why Is Unit Conversion Important When Solving Rate Problems?
14. How Can Rates And Ratios Be Used To Model Real-World Situations?
15. How Can You Check Whether A Solution Is Reasonable?
"""),
("Math", "Networks and Critical Path Analysis",
"""Networks

• Introduction to Networks

• Drawing Network Diagrams

• Minimum Spanning Tree

• Shortest Path

Network Applications

• Connecting Locations Efficiently
• Minimising Costs
• Route Planning
• Transport Networks
• Communication Networks

Critical Path Analysis

• Drawing a Network from an Activity Log

• Forward and Backward Scanning

• Critical Path and Float Times

• Maximum Flow

• Minimum Cut Theorem

Applications of Critical Path Analysis

• Project Planning
• Scheduling Tasks
• Identifying Critical Activities
• Determining Project Completion Time
• Managing Resources

Problem Solving

• Interpreting Network Diagrams
• Finding the Shortest Path
• Finding the Minimum Spanning Tree
• Calculating Float Times
• Determining Maximum Flow
• Applying the Minimum Cut Theorem

Mathematical Modelling

• Using Networks to Solve Real-World Problems
• Analysing Project Schedules
• Optimising Routes and Resources
""",

"""1. What Is A Network?
2. What Is A Network Diagram?
3. What Is A Minimum Spanning Tree?
4. How Is A Minimum Spanning Tree Used In Real-World Situations?
5. What Is The Shortest Path Problem?
6. How Can Network Diagrams Be Used For Route Planning?
7. What Is Critical Path Analysis?
8. How Is A Network Drawn From An Activity Log?
9. What Is Forward Scanning?
10. What Is Backward Scanning?
11. What Is The Critical Path In A Project?
12. What Is Float Time?
13. What Is Maximum Flow?
14. What Is The Minimum Cut Theorem?
15. How Can Networks And Critical Path Analysis Be Used In Project Management?
"""),
("Math", "Linear Modelling and Equations",
"""Algebra and Equations

• Solving Equations

• Rearranging Formulae

• Substitution

• Expanding and Simplifying Algebraic Expressions

• Factorising Algebraic Expressions

• Solving Linear Equations

Applications of Algebra

• Modelling Real-World Situations
• Financial Applications
• Formula Manipulation
• Problem Solving

Simultaneous Equations

• Solving Simultaneous Equations Graphically

• Applications of Simultaneous Equations

• Solving Simultaneous Equations Algebraically

Methods of Solving Simultaneous Equations

• Graphical Method

• Substitution Method

• Elimination Method

Linear Modelling

• Constructing Linear Models

• Interpreting Graphs

• Gradient and Intercept

• Using Equations to Represent Relationships

Applications of Linear Modelling

• Cost and Revenue Models
• Distance and Time Relationships
• Financial Modelling
• Population and Growth Models

Problem Solving

• Selecting Appropriate Equations
• Interpreting Solutions
• Checking Reasonableness of Answers
• Applying Mathematics to Real-World Contexts
""",

"""1. What Is Algebra?
2. How Do You Solve A Linear Equation?
3. How Can A Formula Be Rearranged?
4. What Is The Difference Between Expanding And Factorising?
5. What Is Substitution In Algebra?
6. What Is A Simultaneous Equation?
7. How Are Simultaneous Equations Solved Graphically?
8. How Are Simultaneous Equations Solved Using Substitution?
9. How Are Simultaneous Equations Solved Using Elimination?
10. What Is A Linear Model?
11. What Do The Gradient And Intercept Represent?
12. How Can Equations Be Used To Model Real-World Situations?
13. What Are Some Applications Of Simultaneous Equations?
14. How Can Linear Models Be Used In Financial Mathematics?
15. How Can You Check Whether An Algebraic Solution Is Correct?
"""),
("Math", "Trigonometry",
"""Right-Angled Trigonometry

• Trigonometric Ratios in Right-Angled Triangles

• Practical Problems Involving Right-Angled Triangles

Trigonometric Ratios

• Sine (sin)

• Cosine (cos)

• Tangent (tan)

Applications of Right-Angled Trigonometry

• Finding Unknown Side Lengths

• Finding Unknown Angles

• Solving Real-World Problems

• Navigation and Surveying

Non-Right-Angled Trigonometry

• Area of a Triangle

• The Sine Rule

• The Cosine Rule

• Applications of the Sine and Cosine Rule

Bearings

• Introduction to Bearings

• Using Bearings to Solve Problems

Applications of Trigonometry

• Angles of Elevation and Depression

• Compass Radial Survey

• Navigation

• Construction and Engineering

• Mapping and Surveying

Problem Solving

• Interpreting Diagrams

• Selecting Appropriate Trigonometric Methods

• Applying Trigonometry to Real-World Situations

• Checking Reasonableness of Solutions
""",

"""1. What Are The Trigonometric Ratios Sine, Cosine And Tangent?
2. How Are Trigonometric Ratios Used In Right-Angled Triangles?
3. How Can An Unknown Side Length Be Calculated Using Trigonometry?
4. How Can An Unknown Angle Be Calculated Using Trigonometry?
5. What Types Of Real-World Problems Use Right-Angled Trigonometry?
6. What Is The Area Formula For A Triangle Using Trigonometry?
7. What Is The Sine Rule?
8. When Should The Sine Rule Be Used?
9. What Is The Cosine Rule?
10. When Should The Cosine Rule Be Used?
11. What Are Bearings?
12. How Are Bearings Used To Solve Navigation Problems?
13. What Are Angles Of Elevation And Depression?
14. What Is A Compass Radial Survey?
15. How Can Trigonometry Be Applied In Real-World Situations Such As Navigation And Surveying?
"""),
("Math", "Statistics",
"""Bivariate Data Analysis

• Scatterplots

• Data Trends

• Line of Best Fit

• Making Predictions Using Data

Bivariate Relationships

• Positive Correlation

• Negative Correlation

• No Correlation

• Strength of Correlation

Data Analysis

• Interpreting Scatterplots

• Identifying Trends

• Drawing and Using a Line of Best Fit

• Making Predictions and Interpolations

• Understanding Extrapolation

Normal Distribution

• The Bell Curve

• Z-Scores – It's All Relative!

• Z-Scores and the Normal Curve

• Z-Scores and Probability

Properties of the Normal Distribution

• Mean

• Standard Deviation

• Symmetry of the Bell Curve

Applications of Statistics

• Comparing Data Sets

• Analysing Trends

• Making Predictions

• Assessing Probability

• Interpreting Real-World Data

Problem Solving

• Selecting Appropriate Statistical Methods

• Interpreting Results

• Evaluating Reliability of Predictions

• Using Statistics to Support Decision Making
""",

"""1. What Is A Scatterplot?
2. What Is Bivariate Data?
3. What Is The Difference Between Positive And Negative Correlation?
4. What Does It Mean If There Is No Correlation?
5. What Is A Line Of Best Fit?
6. How Is A Line Of Best Fit Used To Make Predictions?
7. What Is The Difference Between Interpolation And Extrapolation?
8. What Is A Normal Distribution?
9. What Is The Bell Curve?
10. What Is A Z-Score?
11. How Are Z-Scores Used To Compare Data Values?
12. How Are Z-Scores Related To The Normal Distribution?
13. How Is Probability Connected To The Normal Curve?
14. How Can Statistics Be Used To Analyse Real-World Data?
15. Why Is It Important To Evaluate The Reliability Of Statistical Predictions?
"""),
("Math", "Non-Linear Relationships",
"""Non-Linear Relationships

• Application of Straight Line Functions

• The Graph of an Exponential Function

• The Graph of a Quadratic Function

• Practical Applications of the Quadratic Function

• Reciprocal Functions and Inverse Variation

Straight Line Functions

• Gradient

• Intercept

• Linear Models

• Applications in Real-World Contexts

Exponential Functions

• Exponential Growth

• Exponential Decay

• Interpreting Exponential Graphs

• Applications in Finance and Population Growth

Quadratic Functions

• Features of a Parabola

• Axis of Symmetry

• Turning Point (Vertex)

• Maximum and Minimum Values

• Solving Quadratic Equations

• Practical Applications of Quadratic Models

Reciprocal Functions

• Graphing Reciprocal Functions

• Asymptotes

• Inverse Variation

• Applications of Reciprocal Relationships

Problem Solving

• Interpreting Graphs

• Comparing Linear and Non-Linear Relationships

• Selecting Appropriate Models

• Applying Mathematical Models to Real-World Situations
""",

"""1. What Is A Non-Linear Relationship?
2. What Is The Difference Between A Linear And A Non-Linear Relationship?
3. What Are The Key Features Of A Straight Line Function?
4. What Is An Exponential Function?
5. What Is The Difference Between Exponential Growth And Exponential Decay?
6. How Are Exponential Functions Used In Real-World Situations?
7. What Is A Quadratic Function?
8. What Are The Main Features Of A Parabola?
9. What Is The Axis Of Symmetry?
10. What Is The Turning Point (Vertex) Of A Quadratic Function?
11. How Can Quadratic Functions Be Applied To Real-World Problems?
12. What Is A Reciprocal Function?
13. What Is Inverse Variation?
14. What Are Asymptotes In Reciprocal Functions?
15. How Can Different Mathematical Models Be Used To Represent Real-World Relationships?
""")
]

english_topics = [
    ("English", "Advanced Common Module: Texts and Human Experiences",
"""Purpose of the Module
• Analyse and Explore Individual and Collective Human Experiences
• Interpret Human Qualities and Emotions
• Examine Anomalies, Paradoxes and Inconsistencies in Human Behaviour
• Explore Motivations, Aspirations and Actions
• Consider the Complexity and Diversity of Human Experiences
• Investigate the Relationship Between Individuals and Society

Representation of Human Experiences
• Language Forms and Features
• Literary Techniques
• Narrative Voice
• Characterisation
• Imagery
• Symbolism
• Motifs
• Structure

Understanding Meaning
• Context
• Perspective
• Values and Attitudes
• Audience
• Purpose
• Interpretation

Human Experiences in Texts
• Identity
• Belonging
• Resilience
• Isolation
• Conflict
• Hope
• Loss
• Growth
• Discovery
• Relationships

Responding to Texts
• Critical Analysis
• Close Textual Reading
• Evaluating Authorial Choices
• Analysing Evidence
• Developing Personal Responses

Composition
• Analytical Writing
• Creative Writing
• Reflective Writing
• Discursive Writing

Skills Development
• Forming Thesis Statements
• Integrating Textual Evidence
• Analysing Language Techniques
• Linking Ideas to Human Experiences
• Constructing Sustained Arguments
""",

"""1. What Is Meant By 'Texts And Human Experiences'?
2. How Do Texts Represent Individual And Collective Human Experiences?
3. Why Is Context Important In Understanding A Text?
4. How Do Values And Attitudes Influence Meaning?
5. What Is The Purpose Of Characterisation?
6. How Can Symbolism Convey Human Experiences?
7. What Is The Difference Between Personal And Collective Experiences?
8. How Do Authors Use Language Techniques To Shape Meaning?
9. What Human Qualities Are Commonly Explored In Literature?
10. How Can Conflict Influence Human Experiences?
11. Why Is Resilience A Significant Theme In Texts?
12. What Is The Importance Of Perspective In A Text?
13. How Can Evidence Be Effectively Integrated Into Analytical Writing?
14. What Makes A Strong Thesis Statement?
15. Why Is The Study Of Human Experiences Relevant To Readers?
"""),
("English", "Module A: Textual Conversations",
"""Purpose of the Module
• Explore Relationships Between Texts
• Examine How Texts Influence and Reimagine One Another
• Analyse Similarities and Differences Between Texts
• Investigate How Context Shapes Meaning
• Consider How Values Are Reflected, Challenged and Reinterpreted

Textual Conversations
• Resonances Between Texts
• Dissonances Between Texts
• Reimagining Ideas
• Reinterpreting Perspectives
• Transformation of Meaning

Context
• Historical Context
• Social Context
• Cultural Context
• Political Context
• Personal Context

Comparative Analysis
• Similarities Between Texts
• Differences Between Texts
• Perspectives
• Values
• Attitudes
• Beliefs
• Contextual Influences

Language, Form and Structure
• Literary Techniques
• Imagery
• Symbolism
• Motifs
• Characterisation
• Narrative Voice
• Form
• Structure

Responding to Texts
• Comparative Essays
• Comparative Thesis Statements
• Comparative Analysis
• Integrating Textual Evidence
• Evaluating Authorial Choices

Key Concepts
• Intertextuality
• Context
• Perspective
• Values
• Representation
• Reinterpretation
• Transformation
• Resonance
• Dissonance
• Continuity and Change

Writing Skills
• Developing a Thesis
• Comparative Paragraphs
• Integrating Quotations
• Analysing Techniques
• Linking Ideas Across Texts
• Constructing Sustained Arguments
""",

"""1. What Is A Textual Conversation?
2. How Can One Text Influence Another?
3. What Is Intertextuality?
4. What Is Meant By Resonance Between Texts?
5. What Is Meant By Dissonance Between Texts?
6. How Does Context Shape Meaning?
7. Why Is Comparative Analysis Important In Module A?
8. How Do Values Influence The Interpretation Of Texts?
9. What Role Does Perspective Play In Textual Conversations?
10. How Can Authors Reinterpret Ideas From Earlier Texts?
11. How Do Language Techniques Contribute To Meaning?
12. What Makes An Effective Comparative Thesis Statement?
13. How Can Quotations Be Integrated Into A Comparative Essay?
14. What Is The Difference Between Continuity And Change In Textual Conversations?
15. How Do Texts Transform Meaning Across Different Contexts?
"""), 
("English", "Module B: Critical Study of Literature",
"""Purpose of the Module
• Develop An Informed Personal Understanding Of Literature
• Engage In Close Study Of A Prescribed Text
• Analyse Literary Form, Language And Style
• Evaluate The Text's Ideas And Values
• Consider The Text's Enduring Significance

Critical Study
• Close Reading
• Detailed Analysis
• Personal Interpretation
• Critical Evaluation
• Independent Judgement

Context
• Historical Context
• Social Context
• Cultural Context
• Authorial Context

Language, Form And Structure
• Literary Techniques
• Imagery
• Symbolism
• Motifs
• Characterisation
• Narrative Voice
• Form
• Structure

Themes And Ideas
• Human Nature
• Identity
• Power
• Conflict
• Belonging
• Morality
• Justice
• Relationships
• Change
• Society

Values And Perspectives
• Authorial Values
• Cultural Values
• Personal Values
• Alternative Perspectives

Responding To Literature
• Analytical Essays
• Critical Responses
• Personal Responses
• Evaluation Of Meaning
• Analysis Of Literary Craft

Writing Skills
• Developing A Thesis
• Integrating Quotations
• Analysing Techniques
• Evaluating Ideas
• Constructing Sustained Arguments
• Supporting Interpretations With Evidence

Textual Integrity
• Unity Of Form And Meaning
• Enduring Value
• Complexity Of Ideas
• Universal Relevance
• Artistic Quality
""",

"""1. What Is A Critical Study Of Literature?
2. Why Is Close Reading Important In Module B?
3. What Is Textual Integrity?
4. How Does Context Influence Meaning?
5. What Is The Importance Of Personal Interpretation?
6. How Do Literary Techniques Shape Meaning?
7. What Role Does Characterisation Play In Literature?
8. How Can Symbolism Convey Complex Ideas?
9. Why Is It Important To Evaluate Authorial Values?
10. What Makes A Text Enduring And Significant?
11. How Can Quotations Be Effectively Integrated Into Essays?
12. What Is The Difference Between Analysis And Evaluation?
13. How Can A Strong Thesis Be Developed?
14. Why Is Evidence Important In Literary Analysis?
15. How Does Textual Integrity Contribute To A Text's Value?
"""),
("English", "Module C: The Craft of Writing",
"""Purpose of the Module
• Develop Writing Skills For A Variety Of Purposes
• Experiment With Language Forms And Features
• Explore How Writers Create Meaning
• Reflect On The Writing Process
• Compose Effective And Engaging Texts

The Craft Of Writing
• Creative Writing
• Discursive + Reflective Writing
• Persuasive Writing

Writing Processes
• Planning
• Drafting
• Editing
• Revising
• Proofreading

Language Forms And Features
• Imagery
• Symbolism
• Motifs
• Characterisation
• Dialogue
• Tone
• Voice
• Figurative Language

Narrative Elements
• Setting
• Character
• Plot
• Conflict
• Resolution
• Point Of View

Discursive Writing
• Exploration Of Ideas
• Personal Reflection
• Consideration Of Multiple Perspectives
• Use Of Anecdotes And Examples

Reflective Writing
• Reflection On Experiences
• Reflection On The Writing Process
• Personal Insights
• Evaluation Of Choices

Writing For Purpose And Audience
• Inform
• Persuade
• Entertain
• Explain
• Reflect

Developing Ideas
• Observation
• Imagination
• Personal Experience
• Research
• Critical Thinking

Writing Skills
• Thesis Development
• Paragraph Structure
• Cohesion
• Clarity
• Style
• Expression

Evaluation And Reflection
• Evaluating Writing Choices
• Analysing Effectiveness
• Identifying Areas For Improvement
• Responding To Feedback
""",

"""1. What Is The Purpose Of Module C: The Craft Of Writing?
2. What Is The Difference Between Creative, Discursive And Reflective Writing?
3. Why Is Planning Important In The Writing Process?
4. What Is The Purpose Of Editing And Revising?
5. How Can Imagery Enhance Writing?
6. What Role Does Characterisation Play In Writing?
7. How Does Dialogue Help Develop Characters And Ideas?
8. What Is The Importance Of Tone And Voice?
9. How Can Setting Influence Meaning?
10. What Are The Key Features Of Discursive Writing?
11. What Are The Key Features Of Reflective Writing?
12. How Should Writers Consider Audience And Purpose?
13. How Can Personal Experiences Be Used To Develop Ideas?
14. Why Is Feedback Important During The Writing Process?
15. How Can Writers Evaluate The Effectiveness Of Their Work?
"""),
("English", "Essential English Techniques and Verbs",
"""COMMON MODULE              MODULE A                    MODULE B                    MODULE C

• Characterisation           • Allusion                  • Symbolism                 • Imagery
• Symbolism                  • Intertextuality           • Motif                     • Simile
• Imagery                    • Symbolism                 • Irony                     • Metaphor
• Motif                      • Motif                     • Dramatic Irony            • Extended Metaphor
• Tone                       • Irony                     • Foreshadowing             • Symbolism
• Contrast                   • Juxtaposition             • Imagery                   • Motif
• Juxtaposition              • Contrast                  • Metaphor                  • Personification
• Anecdote                   • Characterisation          • Extended Metaphor         • Dialogue
• Dialogue                   • Narrative Voice           • Characterisation          • Characterisation
• Narrative Voice            • Imagery                   • Narrative Structure       • Sensory Language
• First-Person Narration     • Structural Parallels      • Juxtaposition             • Contrast
• Setting                    • Adaptation                • Allusion                  • Juxtaposition
• Flashback                  • Reimagining               • Repetition                • Tone
• Repetition                 • Satire                    • Ambiguity                 • Repetition
• Emotive Language           • Parody                    • Syntax                    • Anecdote

STRONG VERBS

COMMON MODULE              MODULE A                    MODULE B                    MODULE C

• Represents               • Reinterprets              • Critiques                 • Crafts
• Illustrates              • Reimagines                • Examines                  • Evokes
• Reveals                  • Challenges                • Evaluates                 • Captures
• Explores                 • Mirrors                   • Constructs                • Conveys
• Demonstrates             • Extends                   • Deconstructs              • Illustrates
• Conveys                  • Resonates With            • Reinforces                • Shapes
• Highlights               • Contrasts                 • Undermines                • Establishes
• Emphasises               • Reframes                  • Questions                 • Develops
• Reflects                 • Repositions               • Investigates              • Enhances
• Suggests                 • Transforms                • Interrogates              • Engages

UNIVERSAL TECHNIQUES

• Symbolism
• Imagery
• Characterisation
• Motif
• Contrast
• Juxtaposition
• Repetition
• Tone
• Narrative Voice
• Irony

UNIVERSAL VERBS

• Explores
• Reveals
• Demonstrates
• Highlights
• Represents
• Illustrates
• Conveys
• Emphasises
• Reflects
• Challenges
""",

"""1. Which techniques are most useful for the Common Module?
2. Which techniques are most useful for Module A?
3. Which techniques are most useful for Module B?
4. Which techniques are most useful for Module C?
5. What is the purpose of symbolism?
6. What is the difference between contrast and juxtaposition?
7. What is intertextuality?
8. Why is characterisation important?
9. What are strong analytical verbs?
10. Why should strong verbs be used in essays?
11. Which verbs are best suited to Module A?
12. Which verbs are best suited to Module B?
13. Which verbs are best suited to Module C?
14. What techniques work well across all English modules?
15. What verbs work well across all English modules?
""")
]

software_topics = [
    ("Software", "Programming fundamentals",
"""Software development

Explore fundamental software development steps used by programmers when designing software
• Requirements definition
• Determining specifications
• Design
• Development
• Integration
• Testing and debugging
• Installation
• Maintenance

Research and evaluate the prevalence and use of online code collaboration tools

Designing algorithms

Apply computational thinking and algorithmic design by defining the key features of standard algorithms
• Sequence
• Selection
• Iteration
• Identifying data that should be stored

Apply divide and conquer and backtracking as algorithmic design strategies

Develop structured algorithms using pseudocode and flowcharts
• Use of subprograms

Use modelling tools to support top-down and bottom-up design
• Structure charts
• Abstraction diagrams
• Refinement diagrams

Analyse the logic and structure of written algorithms
• Determining inputs and outputs
• Determining the purpose of the algorithm
• Desk checking and peer checking
• Determining connections to other subroutines or functions

Identify procedures and functions in an algorithm

Experiment with programming paradigms
• Object-oriented programming
• Imperative programming
• Logic programming
• Functional programming

Data for software engineering

Investigate the use of number systems for computing purposes
• Binary
• Decimal
• Hexadecimal

Represent integers using two's complement

Investigate standard data types
• Character (char) and string
• Boolean
• Real
• Single precision floating point
• Integer
• Date and time

Create data dictionaries to describe data and data types, structure data and record relationships

Use data structures
• Arrays
• Records
• Trees
• Sequential files

Developing solutions with code

Apply skills in computational thinking and programming to develop a software solution
• Converting an algorithm into code
• Using control structures
• Using data structures
• Using standard modules
• Creating relevant subprograms with parameter passing

Implement data structures that support data storage
• Single-dimensional arrays
• Multidimensional arrays
• Lists
• Trees
• Stacks
• Hash tables

Compare the execution of the Waterfall and Agile project management models as applied to software development

Test and evaluate solutions
• Functionality
• Performance
• Readability of code
• Quality of documentation

Use debugging tools
• Breakpoints
• Single line stepping
• Watches
• Interfaces between functions
• Debugging output statements
• Debugging software available in an IDE

Determine sets of suitable test data
• Boundary values
• Path coverage
• Faulty and abnormal data

Determine typical errors experienced when developing code
• Syntax errors
• Logic errors
• Runtime errors

Explain their likely causes
""",

"""1. What are the main stages of the software development lifecycle?
2. What are online code collaboration tools and why are they useful?
3. What is the difference between sequence, selection and iteration?
4. What is the divide and conquer strategy?
5. What is backtracking in algorithm design?
6. Why are pseudocode and flowcharts used when designing algorithms?
7. What is the difference between top-down and bottom-up design?
8. What is the purpose of desk checking and peer checking?
9. What is the difference between a procedure and a function?
10. What are the advantages of object-oriented programming?
11. What is the difference between binary, decimal and hexadecimal number systems?
12. What is two's complement used for?
13. What is the purpose of a data dictionary?
14. What is the difference between Agile and Waterfall project management?
15. What is the difference between syntax, logic and runtime errors?
"""),
    ("Software", "Object-Oriented Programming (OOP)",
"""Understanding OOP

Apply the key features of an object-oriented programming (OOP) language
• Objects
• Classes
• Encapsulation
• Abstraction
• Inheritance
• Generalisation
• Polymorphism

Compare procedural programming with OOP

Use data flow diagrams, structure charts and class diagrams to represent a system

Describe the process of design used to develop code in an OOP language
• Task definition
• Top-down and bottom-up
• Facade pattern
• Agility

Assess the effectiveness of programming code developed to implement an algorithm

Investigate how OOP languages handle message-passing between objects

Explain code optimisation in software engineering

Outline the features of OOP that support collaborative code development
• Consistency
• Code commenting
• Version control
• Feedback

Programming in OOP

Design and implement computer programs involving branching, iteration and functions in an OOP language for an identified need or opportunity

Implement and modify OOP programming code
• Clear and uncluttered mainline
• One logical task per subroutine
• Use of stubs
• Use of control structures and data structures
• Ease of maintenance
• Version control
• Regular backup

Apply methodologies to test and evaluate code
• Unit, subsystem and system testing
• Black, white and grey box testing
• Quality assurance
""",

"""1. What are objects and classes in OOP?
2. What is encapsulation?
3. What is abstraction?
4. What is inheritance?
5. What is polymorphism?
6. How is procedural programming different from OOP?
7. What is the purpose of a class diagram?
8. What is the difference between top-down and bottom-up design?
9. What is the facade pattern?
10. How do OOP languages handle message-passing between objects?
11. What is code optimisation?
12. How does OOP support collaborative code development?
13. Why should a subroutine complete one logical task?
14. Why are version control and regular backups important?
15. What is the difference between unit, subsystem and system testing?
"""),
    ("Software", "Programming Mechatronics",
"""Understanding mechatronic hardware and software

Outline applications of mechatronic systems in a variety of specialised fields

Identify the hardware requirements to run a program and the effect on code development
• Assessing the relationship of microcontrollers and the central processing unit (CPU)
• The influence of instruction set and opcodes
• The use of address and data registers

Identify and describe a range of sensors, actuators and end effectors/manipulators within existing mechatronic systems
• Motion sensors
• Light level sensors
• Hydraulic actuators
• Robotic grippers

Use different types of data and understand how it is obtained and processed in a mechatronic system, including diagnostic data and data used for optimisation

Experiment with software to control interactions and dependencies within mechatronic systems
• Motion constraints
• Degrees of freedom
• Combination of subsystems
• Combination of sensors, actuators and end effectors to create viable subsystems

Determine power, battery and material requirements for components of a mechatronic system

Develop wiring diagrams for a mechatronic system, considering data and power supply requirements

Determine specialist requirements that influence the design and functions of mechatronic systems designed for people with disability

Designing control algorithms

Develop, modify and apply algorithms to control a mechatronic system

Explore the algorithmic patterns, code and applications for open and closed control systems

Outline the features of an algorithm and program code used for autonomous control

Programming and building

Design, develop and produce a mechatronic system for a real-world problem
• Software control
• Mechanical engineering
• Electronics and mathematics

Implement algorithms and design programming code to drive mechatronic devices

Develop simulations and prototypes of a potential mechatronic system to test programming code

Design, develop and implement programming code for a closed loop control system

Apply programming code to integrate sensors, actuators and end effectors/manipulators

Implement specific control algorithms that enhance the performance of a mechatronic system

Design, develop and implement a user interface (UI) to control a mechatronic system

Create and use unit tests to determine the effectiveness and repeatability of each component's control algorithm
""",

"""1. What are some applications of mechatronic systems in specialised fields?
2. How do microcontrollers and CPUs relate to mechatronic systems?
3. What is the role of instruction sets and opcodes?
4. What are address and data registers used for?
5. What is the difference between a sensor and an actuator?
6. Give examples of sensors used in mechatronic systems.
7. What are end effectors or manipulators?
8. How is data obtained and processed in a mechatronic system?
9. What are motion constraints and degrees of freedom?
10. Why are power, battery and material requirements important?
11. Why are wiring diagrams useful in mechatronic system design?
12. What is the difference between open loop and closed loop control?
13. What features are needed for autonomous control?
14. Why are simulations and prototypes useful when developing mechatronic systems?
15. Why are unit tests important for testing control algorithms?
"""),
    ("Software", "Programming for the Web",
"""Data transmission using the web

Explore the applications of web programming
• Interactive websites/webpages
• E-commerce
• Progressive Web Apps (PWAs)

Investigate and practise how data is transferred on the internet
• Data packets
• Internet Protocol (IP) addresses including IPv4
• Domain Name Systems (DNS)

Investigate and describe the function of web protocols and their ports
• HTTP, HTTPS
• TCP/IP
• DNS
• FTP, SFTP
• SSL, TLS
• SMTP, POP3, IMAP

Explain the processes for securing the web
• Secure Sockets Layer (SSL) certificates
• Encryption algorithms
• Encryption keys
• Plain text and cipher text
• Authentication and authorisation
• Hash values
• Digital signatures

Investigate the effect of big data on web architecture
• Data mining
• Metadata
• Streaming service management

Designing web applications

Investigate and explain the role of the World Wide Web Consortium (W3C)
• Web Accessibility Initiative (WAI)
• Internationalisation
• Web security
• Privacy
• Machine-readable data

Model elements that form a web development system
• Client-side (front-end) web programming
• Server-side (back-end) web programming
• SQL databases
• Non-SQL databases

Explore and explain the influence of a web browser on web development, including the use of developer tools

Investigate CSS and its impact on web design
• Consistency of appearance
• Flexibility with browsers and devices
• CSS maintenance tools

Investigate the reasons for version control

Explore code libraries for front-end development
• Frameworks
• Template engines
• Predesigned CSS classes

Explain open-source software

Investigate methods to improve web application load times

Research Content Management Systems (CMS)

Assess the contribution of back-end web development

Observe the back-end process used to manage a web request
• Webserver software
• Web frameworks
• Objects
• Libraries
• Databases

Develop a web application using scripting and shell scripts

Apply a web-based database and execute SQL
• Selecting fields
• GROUP BY
• WHERE clauses
• Table joins

Compare ORM to SQL

Describe collaboration between front-end and back-end developers

Design, develop and implement a Progressive Web App (PWA)
• UI principles
• UX principles
• Fonts
• Colours
• Audio
• Video
• Navigation
• Accessibility
• Inclusivity
""",

"""1. What are three common applications of web programming?
2. What is a Progressive Web App (PWA)?
3. What are data packets?
4. What is the purpose of an IP address?
5. What is the role of DNS on the internet?
6. What is the difference between HTTP and HTTPS?
7. What is the purpose of SSL and TLS?
8. What is the difference between authentication and authorisation?
9. What is the role of the W3C in web development?
10. What is the difference between front-end and back-end development?
11. Why is CSS important in web development?
12. What are the benefits of version control?
13. What is SQL used for in web applications?
14. What is the difference between ORM and SQL?
15. Why are accessibility and inclusivity important when designing a PWA?
"""), 
    ("Software", "Secure Software Architecture",
"""Designing software

Describe the benefits of developing secure software
• Data protection
• Minimising cyber attacks and vulnerabilities

Interpret and apply fundamental software development steps to develop secure code
• Requirements definition
• Determining specifications
• Design
• Development
• Integration
• Testing and debugging
• Installation
• Maintenance

Describe how the capabilities and experience of end users influence the secure design features of software

Developing secure code

Explore fundamental software design security concepts when developing programming code
• Confidentiality
• Integrity
• Availability
• Authentication
• Authorisation
• Accountability

Apply security features incorporated into software including data protection, security, privacy and regulatory compliance

Use and explain the contribution of cryptography and sandboxing to the 'security by design' approach in the development of software solutions

Use and explain the 'privacy by design' approach in the development of software solutions
• Proactive not reactive approach
• Embed privacy into design
• Respect for user privacy

Test and evaluate the security and resilience of software by determining vulnerabilities, hardening systems, handling breaches, maintaining business continuity and conducting disaster recovery

Apply and evaluate strategies used by software developers to manage the security of programming code
• Code review
• Static Application Security Testing (SAST)
• Dynamic Application Security Testing (DAST)
• Vulnerability assessment
• Penetration testing

Design, develop and implement code using defensive data input handling practices
• Input validation
• Sanitisation
• Error handling

Design, develop and implement a safe Application Programming Interface (API) to minimise software vulnerabilities

Design, develop and implement code considering efficient execution for the user
• Memory management
• Session management
• Exception management

Design, develop and implement secure code to minimise vulnerabilities in user action controls
• Broken authentication and session management
• Cross-site scripting (XSS)
• Cross-site request forgery (CSRF)
• Invalid forwarding and redirecting
• Race conditions

Design, develop and implement secure code to protect user file and hardware vulnerabilities from file attacks and side channel attacks

Impact of safe and secure software development

Apply and describe the benefits of collaboration to develop safe and secure software
• Considering various points of view
• Delegating tasks based on expertise
• Quality of the solution

Investigate and explain the benefits to an enterprise of the implementation of safe and secure development practices
• Improved products or services
• Influence on future software development
• Improved work practices
• Productivity
• Business interactivity

Evaluate the social, ethical and legal issues and ramifications that affect people and enterprises resulting from the development and implementation of safe and secure software
• Employment
• Data security
• Privacy
• Copyright
• Intellectual property
• Digital disruption
""",

"""1. What are the benefits of developing secure software?
2. Why is data protection important in software development?
3. What are the main stages of the software development lifecycle?
4. How do end users influence the design of secure software?
5. What is the difference between authentication and authorisation?
6. Explain the concepts of confidentiality, integrity and availability (CIA).
7. What role does cryptography play in secure software development?
8. What is meant by 'privacy by design'?
9. What is the purpose of sandboxing?
10. What is the difference between SAST and DAST?
11. Why are code reviews important in secure software development?
12. What is input validation and why is it important?
13. What is a secure API and why is it necessary?
14. What are XSS and CSRF attacks?
15. What social, ethical and legal issues must be considered when developing secure software?
"""),
    ("Software", "Software Automation",
"""Investigate how machine learning (ML) supports automation through the use of DevOps, robotic process automation (RPA) and business process automation (BPA)

Distinguish between artificial intelligence (AI) and ML

Explore models of training ML
• Supervised learning
• Unsupervised learning
• Semi-supervised learning
• Reinforcement learning

Investigate common applications of key ML algorithms
• Data analysis and forecasting
• Virtual personal assistants
• Image recognition

Research models used by software engineers to design and analyse ML
• Decision trees
• Neural networks

Describe types of algorithms associated with ML
• Linear regression
• Logistic regression
• K-nearest neighbour (KNN)

Programming for automation

Design, develop and apply ML regression models using OOP to predict numeric values
• Linear regression
• Polynomial regression
• Logistic regression

Apply neural network models using OOP to make predictions

Significance and impact of ML and AI

Assess the impact of automation on the individual, society and the environment
• Safety of workers
• People with disability
• The nature and skills required for employment
• Production efficiency, waste and the environment
• The economy and distribution of wealth

Explore by implementation how patterns in human behaviour influence ML and AI software development
• Psychological responses
• Patterns related to acute stress response
• Cultural protocols
• Belief systems

Investigate the effect of human and dataset source bias in the development of ML and AI solutions
""",

"""1. Distinguish between AI and ML.
2. Explain supervised learning.
3. Explain unsupervised learning.
4. Explain reinforcement learning.
5. Describe one application of ML.
6. What is a decision tree?
7. What is a neural network?
8. Explain linear regression.
9. Explain logistic regression.
10. What is KNN?
11. How can OOP be used in ML?
12. How can automation improve workplace safety?
13. How can AI systems become biased?
14. Explain the impact of automation on employment.
15. Describe the role of DevOps in automation.
""")
]

business_topics = [
    ("Business", "Operations",
"""Role of Operations Management

• Strategic Role of Operations Management – Cost Leadership, Good/Service Differentiation
• Goods and/or Services in Different Industries
• Interdependence with Other Key Business Functions

Influences

• Globalisation, Technology, Quality Expectations, Cost-Based Competition, Government Policies, Legal Regulation, Environmental Sustainability

• Corporate Social Responsibility
  - The Difference Between Legal Compliance and Ethical Responsibility
  - Environmental Sustainability and Social Responsibility

Operations Processes

• Inputs
  - Transformed Resources (Materials, Information, Customers)
  - Transforming Resources (Human Resources, Facilities)

• Transformation Processes
  - The Influence of Volume, Variety, Variation in Demand and Visibility (Customer Contact)
  - Sequencing and Scheduling – Gantt Charts, Critical Path Analysis
  - Technology, Task Design and Process Layout
  - Monitoring, Control and Improvement

• Outputs
  - Customer Service
  - Warranties

Operations Strategies

• Performance Objectives – Quality, Speed, Dependability, Flexibility, Customisation, Cost

• New Product or Service Design and Development

• Supply Chain Management – Logistics, E-Commerce, Global Sourcing

• Outsourcing – Advantages and Disadvantages

• Technology – Leading Edge, Established

• Inventory Management – Advantages and Disadvantages of Holding Stock, LIFO (Last-In-First-Out), FIFO (First-In-First-Out), JIT (Just-In-Time)

• Quality Management
  - Control
  - Assurance
  - Improvement

• Overcoming Resistance to Change – Financial Costs, Purchasing New Equipment, Redundancy Payments, Retraining, Reorganising Plant Layout, Inertia

• Global Factors – Global Sourcing, Economies of Scale, Scanning and Learning, Research and Development
""",

"""1. What is the strategic role of operations management?
2. What is the difference between cost leadership and differentiation?
3. What are transformed and transforming resources?
4. Explain the transformation process.
5. What is the influence of volume, variety, variation and visibility?
6. What are Gantt charts and critical path analysis?
7. What are the six performance objectives?
8. Explain supply chain management.
9. What are the advantages and disadvantages of outsourcing?
10. What is the difference between leading-edge and established technology?
11. Compare FIFO, LIFO and JIT inventory management.
12. Explain quality control, quality assurance and quality improvement.
13. What factors can cause resistance to change?
14. How do global factors influence operations management?
15. Explain the difference between legal compliance and ethical responsibility.
"""),
("Business", "Financial Management",
"""Role of Financial Management

• Strategic role of financial management

• Objectives of financial management
  - Profitability
  - Growth
  - Efficiency
  - Liquidity
  - Solvency
  - Short-term and Long-term

• Interdependence with other key business functions

Influences on Financial Management

• Internal sources of finance – Retained profits

• External sources of finance
  - Debt – Short-term borrowing (Overdraft, Commercial Bills, Factoring), Long-term borrowing (Mortgage, Debentures, Unsecured Notes, Leasing)
  - Equity – Ordinary Shares (New Issues, Rights Issues, Placements, Share Purchase Plans), Private Equity

• Financial institutions – Banks, Investment Banks, Finance Companies, Superannuation Funds, Life Insurance Companies, Unit Trusts and the Australian Securities Exchange

• Influence of Government – Australian Securities and Investments Commission, Company Taxation

• Global Market Influences – Economic Outlook, Availability of Funds, Interest Rates

Processes of Financial Management

• Planning and Implementing – Financial Needs, Budgets, Record Systems, Financial Risks, Financial Controls
  - Debt and Equity Financing – Advantages and Disadvantages of Each
  - Matching the Terms and Source of Finance to Business Purpose

• Monitoring and Controlling – Cash Flow Statement, Income Statement, Balance Sheet

• Financial Ratios
  - Liquidity – Current Ratio (Current Assets ÷ Current Liabilities)
  - Gearing – Debt to Equity Ratio (Total Liabilities ÷ Total Equity)
  - Profitability – Gross Profit Ratio (Gross Profit ÷ Sales); Net Profit Ratio (Net Profit ÷ Sales); Return on Equity Ratio (Net Profit ÷ Total Equity)
  - Efficiency – Expense Ratio (Total Expenses ÷ Sales), Accounts Receivable Turnover Ratio (Sales ÷ Accounts Receivable)
  - Comparative Ratio Analysis – Over Different Time Periods, Against Standards, With Similar Businesses

• Limitations of Financial Reports – Normalised Earnings, Capitalising Expenses, Valuing Assets, Timing Issues, Debt Repayments, Notes to the Financial Statements

• Ethical Issues Related to Financial Reports

Financial Management Strategies

• Cash Flow Management
  - Cash Flow Statements
  - Distribution of Payments, Discounts for Early Payment, Factoring

• Working Capital Management
  - Control of Current Assets – Cash, Receivables, Inventories
  - Control of Current Liabilities – Payables, Loans, Overdrafts
  - Strategies – Leasing, Sale and Lease Back

• Profitability Management
  - Cost Controls – Fixed and Variable, Cost Centres, Expense Minimisation
  - Revenue Controls – Marketing Objectives

• Global Financial Management
  - Exchange Rates
  - Interest Rates
  - Methods of International Payment – Payment in Advance, Letter of Credit, Clean Payment, Bill of Exchange
  - Hedging
  - Derivatives
""",

"""1. What Is The Strategic Role Of Financial Management?
2. What Are The Objectives Of Financial Management?
3. What Is The Difference Between Internal And External Sources Of Finance?
4. What Is The Difference Between Debt Finance And Equity Finance?
5. What Role Do Financial Institutions Play In Financial Management?
6. How Does Government Influence Financial Management?
7. How Do Global Market Influences Affect Financial Management?
8. What Is Involved In Planning And Implementing Financial Management?
9. What Is The Purpose Of The Cash Flow Statement, Income Statement And Balance Sheet?
10. What Are Liquidity, Gearing, Profitability And Efficiency Ratios?
11. What Are The Limitations Of Financial Reports?
12. What Ethical Issues Can Arise In Financial Reporting?
13. What Strategies Are Used In Cash Flow Management?
14. What Strategies Are Used In Working Capital Management?
15. How Do Exchange Rates, Interest Rates, Hedging And Derivatives Affect Global Financial Management?
"""),
    ("Business", "Marketing",
"""Role of Marketing

• Strategic Role of Marketing Goods and Services

• Interdependence with Other Key Business Functions

• Production, Selling, Marketing Approaches

• Types of Markets – Resource, Industrial, Intermediate, Consumer, Mass, Niche

Influences on Marketing

• Factors Influencing Customer Choice – Psychological, Sociocultural, Economic, Government

• Consumer Laws
  - Deceptive and Misleading Advertising
  - Price Discrimination
  - Implied Conditions
  - Warranties

• Ethical Issues
  - Truth, Accuracy and Good Taste in Advertising
  - Products That May Damage Health
  - Engaging in Fair Competition
  - Sugging

Marketing Process

• Situational Analysis – SWOT, Product Life Cycle

• Market Research

• Establishing Market Objectives

• Identifying Target Markets

• Developing Marketing Strategies

• Implementation, Monitoring and Controlling
  - Developing a Financial Forecast
  - Comparing Actual and Planned Results
  - Revising the Marketing Strategy

Marketing Strategies

• Market Segmentation, Product/Service Differentiation and Positioning

• Products – Goods and/or Services
  - Branding
  - Packaging

• Price Including Pricing Methods – Cost, Market, Competition-Based
  - Pricing Strategies – Skimming, Penetration, Loss Leaders, Price Points
  - Price and Quality Interaction

• Promotion
  - Elements of the Promotion Mix – Advertising, Personal Selling and Relationship Marketing, Sales Promotions, Publicity and Public Relations
  - The Communication Process – Opinion Leaders, Word of Mouth

• Place/Distribution
  - Distribution Channels
  - Channel Choice – Intensive, Selective, Exclusive
  - Physical Distribution Issues – Transport, Warehousing, Inventory

• People, Processes and Physical Evidence

• E-Marketing

• Global Marketing
  - Global Branding
  - Standardisation
  - Customisation
  - Global Pricing
  - Competitive Positioning
""",

"""1. What Is The Strategic Role Of Marketing?
2. What Is The Difference Between Production, Selling And Marketing Approaches?
3. What Are The Different Types Of Markets?
4. What Factors Influence Customer Choice?
5. What Consumer Laws Affect Marketing Activities?
6. What Ethical Issues Must Businesses Consider When Marketing Products?
7. What Is A SWOT Analysis?
8. What Is The Purpose Of Market Research?
9. Why Is It Important To Identify Target Markets?
10. What Is Market Segmentation And Positioning?
11. What Are The Different Pricing Methods And Pricing Strategies?
12. What Are The Elements Of The Promotion Mix?
13. What Factors Affect Place And Distribution Decisions?
14. What Is E-Marketing?
15. What Strategies Are Used In Global Marketing?
"""),
    ("Business", "Human Resource Management",
"""Role of Human Resource Management

• Strategic Role of Human Resources

• Interdependence with Other Key Business Functions

• Outsourcing
  - Human Resource Functions
  - Using Contractors – Domestic, Global

Key Influences

• Stakeholders – Employers, Employees, Employer Associations, Unions, Government Organisations, Society

• Legal – The Current Legal Framework
  - The Employment Contract – Common Law (Rights and Obligations of Employers and Employees), Minimum Employment Standards, Minimum Wage Rates, Awards, Enterprise Agreements, Other Employment Contracts
  - Work Health and Safety and Workers Compensation
  - Antidiscrimination and Equal Employment Opportunity

• Economic

• Technological

• Social – Changing Work Patterns, Living Standards

• Ethics and Corporate Social Responsibility

Processes of Human Resource Management

• Acquisition

• Development

• Maintenance

• Separation

Strategies in Human Resource Management

• Leadership Style

• Job Design – General or Specific Tasks

• Recruitment – Internal or External, General or Specific Skills

• Training and Development – Current or Future Skills

• Performance Management – Developmental or Administrative

• Rewards – Monetary and Non-Monetary, Individual or Group, Performance Pay

• Global – Costs, Skills, Supply

• Workplace Disputes
  - Resolution – Negotiation, Mediation, Grievance Procedures, Involvement of Courts and Tribunals

Effectiveness of Human Resource Management

• Indicators
  - Corporate Culture
  - Benchmarking Key Variables
  - Changes in Staff Turnover
  - Absenteeism
  - Accidents
  - Levels of Disputation
  - Worker Satisfaction
""",

"""1. What Is The Strategic Role Of Human Resource Management?
2. How Does Human Resource Management Interact With Other Business Functions?
3. What Is Outsourcing And What Are Its Advantages And Disadvantages?
4. Who Are The Key Stakeholders In Human Resource Management?
5. How Does The Legal Framework Influence Human Resource Management?
6. What Are The Rights And Obligations Contained In An Employment Contract?
7. How Do Economic, Technological And Social Factors Influence Human Resource Management?
8. What Is The Difference Between Acquisition, Development, Maintenance And Separation?
9. How Does Leadership Style Affect Human Resource Management?
10. What Is The Difference Between Internal And External Recruitment?
11. Why Are Training And Development Important For Employees?
12. What Is Performance Management?
13. What Types Of Rewards Can Be Used To Motivate Employees?
14. How Can Workplace Disputes Be Resolved?
15. What Indicators Are Used To Measure The Effectiveness Of Human Resource Management?
""")
]

cur.execute("DELETE FROM topics")

insert_topics(math_topics)
insert_topics(english_topics)
insert_topics(software_topics)
insert_topics(business_topics)


conn.commit()

cur.execute("SELECT id, subject, title FROM topics")
for row in cur.fetchall():
    print(row)

conn.close()
print("Database created and populated")

