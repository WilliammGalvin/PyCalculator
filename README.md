# PyCalculator
Simple calculator with order precedence and nested sub expressions in Python. Read the Medium article associated [here](https://medium.com/@williammgalvin/exploring-the-foundation-of-language-processing-be2d4bc577c1).

## Features
- Addition and subtraction
- Mulitiplication and division
- Nested sub expressions (parantheses)
- Order precedence

## How it's built
I understand that calculators are generally a first program type of project
HOWEVER when you factor in order precedence and nested sub expressions you need
to consider a whole different approach. This is a great project to get a feel
for a programming language because you need to tokenize the input, build an
abstract syntax tree (AST), and then evaluate the expression.
