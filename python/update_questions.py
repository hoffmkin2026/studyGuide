import sqlite3

conn = sqlite3.connect("study.db")
cur = conn.cursor()

math_questions = {
    "Probability": "1. What is the probability of rolling an even number?\n2. A bag has 3 red and 2 blue balls. What is P(blue)?",
    "Differentiation": "1. Differentiate 5x³.\n2. If f(x)=x²+4x, what is f′(x)?",
    "Product Rule": "1. Differentiate y = x²·sin(x).\n2. State the formula for the product rule.",
    "Chain Rule": "1. Differentiate y = (2x + 5)³.\n2. What does the chain rule help you find?",
    "Quotient Rule": "1. Differentiate y = (x²)/(x+1).\n2. Write the quotient rule formula.",
    "Trigonometry": "1. Define sin(θ).\n2. A right triangle has opposite=4 and hypotenuse=8. Find sin(θ).",
    "SOH CAH TOA": "1. What does CAH stand for?\n2. Find tan(θ) if opposite=5 and adjacent=2.",
    "Trig Identities": "1. State the Pythagorean identity.\n2. What is sin(0)?"
}

english_questions = {
    "Simile": "1. Write a simile describing a storm.\n2. What words often signal a simile?",
    "Metaphor": "1. Write a metaphor for happiness.\n2. How does a metaphor differ from a simile?",
    "Personification": "1. Personify the sea.\n2. Why do writers use personification?",
    "Alliteration": "1. Create an alliteration about winter.\n2. What effect does alliteration have?",
    "Hyperbole": "1. Write a hyperbole about homework.\n2. Why is hyperbole not meant to be taken literally?",
    "Onomatopoeia": "1. List 3 onomatopoeic words.\n2. How does it enhance writing?",
    "Imagery": "1. Write one sentence using strong imagery.\n2. What sense does this sentence appeal to?",
    "Repetition": "1. Why might a writer use repetition?\n2. Give an example of repetition.",
    "Emotive Language": "1. Give an example of emotive language.\n2. What emotion does it create?",
    "Rhetorical Question": "1. Write a rhetorical question.\n2. Why are rhetorical questions persuasive?"
}

software_questions = {
    "Agile": "1. Name one Agile framework.\n2. Why are sprints useful?",
    "Version Control (Git)": "1. What does 'git commit' do?\n2. Why is Git useful?",
    "Object-Oriented Programming (OOP)": "1. What is an object?\n2. Name one benefit of OOP.",
    "Encapsulation": "1. What is encapsulation?\n2. Why is data hiding useful?",
    "Inheritance": "1. Define inheritance.\n2. Give an example of inheritance in programming.",
    "Polymorphism": "1. What is polymorphism?\n2. Why is it helpful?",
    "Testing": "1. What is unit testing?\n2. Why is software testing important?"
}

def update_questions(subject,data):
    for title, questions in data.items():
        cur.execute("UPDATE topics SET questions=? WHERE subject=? AND title=?", (questions, subject, title))

update_questions("Math", math_questions)
update_questions("English", english_questions)
update_questions("Software", software_questions) 

conn.commit()
conn.close()

print("Updated all topic questions")
