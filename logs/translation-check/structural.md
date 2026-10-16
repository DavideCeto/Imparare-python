# Controllo strutturale della traduzione

- File con problemi: 44
- Errori: 6 · Avvisi: 45 · Info: 0

## `teachers-guide/adding-custom-python-labs.md`

- **error** `code-logic` — blocco di codice #5: la logica del codice è diversa

  ```
  --- EN
  +++ IT
  @@ -1,18 +1,18 @@
  -Does the lab need turtle graphics or run in the shared textbook?
  -  └─ YES → Use Skulpt (Option 1)
  +Il laboratorio ha bisogno della grafica turtle o viene eseguito nel manuale condiviso?
  +  └─ SÌ → Usa Skulpt (Opzione 1)
   
  -Does the lab need third-party packages (numpy, matplotlib, requests)?
  -  ├─ Data science / ML / visualisation → Use Jupyter + Conda (Options 8 + 4)
  -  └─ General packages only             → Use venv (Option 3)
  +Il laboratorio ha bisogno di pacchetti di terze parti (numpy, matplotlib, requests)?
  +  ├─ Data science / ML / visualizzazione → Usa Jupyter + Conda (Opzioni 8 + 4)
  +  └─ Solo pacchetti generali                → Usa venv (Opzione 3)
   
  -Is this a student's first time running Python locally?
  -  └─ YES → Use Thonny (Option 6)
  +È la prima volta che lo studente esegue Python localmente?
  +  └─ SÌ → Usa Thonny (Opzione 6)
   
  -Do you need a fully reproducible sandbox with no student setup?
  -  └─ YES → Use Docker (Option 5)
  +Hai bisogno di una sandbox pienamente riproducibile senza configurazione per lo studente?
  +  └─ SÌ → Usa Docker (Opzione 5)
   
  -Is the student writing narrative code (code + explanation + charts)?
  -  └─ YES → Use Jupyter (Option 8)
  +Lo studente sta scrivendo codice narrativo (codice + spiegazione + grafici)?
  +  └─ SÌ → Usa Jupyter (Opzione 8)
   
  -Is the student ready for professional tools / multi-file projects?
  -  └─ YES → Use VS Code (Option 7)
  +Lo studente è pronto per strumenti professionali / progetti multi-file?
  +  └─ SÌ → Usa VS Code (Opzione 7)
  ```


## `teachers-guide/order-of-concepts.md`

- **error** `code-logic` — blocco di codice #1: la logica del codice è diversa

  ```
  --- EN
  +++ IT
  @@ -1,3 +1,4 @@
  -What are the key concepts in learning Python for a 9th
  -grade student in the US?  List the concepts in the order
  -they should be taught and add justification for ordering.
  +Quali sono i concetti chiave per imparare Python per uno
  +studente di terza media negli USA? Elenca i concetti
  +nell'ordine in cui dovrebbero essere insegnati e aggiungi
  +una giustificazione per l'ordinamento.
  ```

- **error** `code-logic` — blocco di codice #2: la logica del codice è diversa

  ```
  --- EN
  +++ IT
  @@ -1,5 +1,5 @@
  -Now assume that all students have access to the
  -trinket.io website that allows students to learn
  -using turtle graphics to get fast visual feedback.
  -Generate a list of the key Python concepts and the
  -order they should be taught.
  +Ora supponi che tutti gli studenti abbiano accesso al
  +sito trinket.io che permette agli studenti di imparare
  +usando la grafica turtle per ottenere un riscontro visivo
  +rapido. Genera un elenco dei concetti Python chiave e
  +l'ordine in cui dovrebbero essere insegnati.
  ```


## `turtle-graphics-gallery/honeycomb-grid/index.md`

- **error** `code-count` — blocchi di codice: EN 4, IT 3
- **error** `code-logic` — blocco di codice #2: la logica del codice è diversa

  ```
  --- EN
  +++ IT
  @@ -1,49 +1,29 @@
  +import turtle
   import math
  -import turtle
  +monty = turtle.Turtle()
  +monty.speed(0)
  +monty.hideturtle()
   
  +def hexagon(x, y, size, color):
  +    monty.penup()
  +    monty.goto(x, y)
  +    monty.setheading(30)
  +    monty.pendown()
  +    monty.color(color)
  +    monty.begin_fill()
  +    for _ in range(6):
  +        monty.forward(size)
  +        monty.left(60)
  +    monty.end_fill()
   
  -def draw_hexagon(size):
  -    """Draws a single regular hexagon."""
  -    for _ in range(6):
  -        turtle.forward(size)
  -        turtle.left(60)
  +size = 30
  +colors = ['gold', 'orange']
  +h = size * 2                     # height of a pointy-top hexagon
  +col_w = size * math.sqrt(3)      # width of a pointy-top hexagon
   
  -
  -def draw_honeycomb(rows, cols, size):
  -    """Draws a grid of hexagons offset to form a honeycomb pattern."""
  -    # Calculate geometric spacing based on hexagon properties
  -    w = size * math.sqrt(3)  # Width of the hexagon
  -    h = size * 1.5  # Vertical distance to the next row
  -
  -    for r in range(rows):
  -        for c in range(cols):
  -            # Calculate the starting X position
  -            x = c * w
  -            # Offset every odd row to the right by half a hexagon width
  -            if r % 2 == 1:
  -                x += w / 2
  -
  -            # Calculate the starting Y position
  -            y = r * h
  -
  -            # Move turtle to the cell position without drawing
  -            turtle.penup()
  -            turtle.goto(x, y)
  -            turtle.pendown()
  -
  -            # Render the hexagon
  -            draw_hexagon(size)
  -
  -
  -# Main setup
  -if __name__ == "__main__":
  -    # Optimize drawing speed
  -    turtle.speed(0)
  -    turtle.delay(0)
  -
  -    # Configuration: Rows, Columns, Edge Size
  -    draw_honeycomb(rows=6, cols=8, size=30)
  -
  -    # Keep window open
  -    turtle.hideturtle()
  -    turtle.done()
  +for row in range(7):
  +    for col in range(8):
  +        offset = col_w / 2 if row % 2 == 1 else 0
  +        x = -200 + col * col_w + offset
  +        y = 150 - row * h * 0.75
  +        hexagon(x, y, size, colors[(row + col) % 2])
  ```

- **error** `code-logic` — blocco di codice #3: la logica del codice è diversa

  ```
  --- EN
  +++ IT
  @@ -20,4 +20,4 @@
   colors = ['gold', 'orange']
  -h = size * 2                     # height of a pointy-top hexagon
  -col_w = size * math.sqrt(3)      # width of a pointy-top hexagon
  +h = size * 2
  +col_w = size * math.sqrt(3)
   
  @@ -25,3 +25,3 @@
       for col in range(8):
  -        offset = col_w / 2 if row % 2 == 1 else 0
  +        offset = col_w if row % 2 == 1 else 0
           x = -200 + col * col_w + offset
  ```

- **warning** `count-headings` — headings: EN 12, IT 8
- **warning** `count-code_blocks` — code_blocks: EN 4, IT 2

## `about.md`

- **warning** `links-changed` — links presenti in EN ma non in IT: ['https://trinket.io/announcement']
- **warning** `untranslated` — 1 paragrafo/i sembrano ancora in inglese

  ```
  ## Riferimenti  
  [^1]: Computer Science Teachers Association. (2023). *State of K-12 Computer Science Education*. https://advocacy.code.org/stateofcs  
  [^2]: U.S. Bureau of Labor Statistics. (2024). *
  ```


## `chapters/07-for-loops-and-shapes/index.md`

- **warning** `untranslated` — 1 paragrafo/i sembrano ancora in inglese

  ```
  1. for Loop over Sequence
  2. for Loop with range()
  3. Range with Start Stop Step
  4. Loop Counter Variable
  5. Loop Accumulator Pattern
  6. Absolute Positioning goto()
  7. Drawing circle() and Polygons
  8.
  ```


## `chapters/09-decisions-if-else/index.md`

- **warning** `untranslated` — 1 paragrafo/i sembrano ancora in inglese

  ```
  1. Boolean Type
  2. Comparison Operators
  3. Logical Operators
  4. Boolean in Conditions
  5. Chained Comparisons
  6. if Statement
  7. if...else Block
  8. elif Chains
  9. Nested if Statements
  ```


## `chapters/index.md`

- **warning** `untranslated` — 3 paragrafo/i sembrano ancora in inglese

  ```
  This textbook is organized into 38 chapters covering 450 concepts, guiding you from your very first Python program all the way to machine learning.
  
  1. [Welcome to Python and Skulpt] — Meet Monty, run your first , write , and see what's coming.
  2. [Python Code Structure] — Indentation, code blocks, keywords, whitespace, and named colors.
  3. [Varia
  
  Start at Chapter 1 and work through in order — each chapter builds on the previous ones.
  Chapters 1–12 focus on turtle graphics so you get visual, immediate feedback on every concept.
  From Chapter 13 
  ```


## `course-description.md`

- **warning** `count-headings` — headings: EN 12, IT 9
- **warning** `links-changed` — links presenti in EN ma non in IT: ['./faq.md', './teachers-guide/index.md']

## `faq.md`

- **warning** `untranslated` — 100 paragrafo/i sembrano ancora in inglese

  ```
  BFS and DFS are the two standard algorithms for searching a graph.
  
  The ** module** provides functions for generating random numbers and making random
  choices. The most common ones in this course are:
  
  -  — random integer between  and  (inclusive)
  -  — pick one random item from a list
  -  — random float between 0.0 and 1.0
  -  — shuffle a list in place
  
  **Machine learning** is a branch of artificial intelligence where a program learns patterns
  from data instead of following hand-written rules. You provide labeled examples and the program
  adjusts inte
  
  A **list comprehension** is a compact way to build a new list by transforming or filtering
  another sequence. It combines a  loop and an optional  condition into a single line:
  ```


## `img/cover-image-prompt.md`

- **warning** `untranslated` — 9 paragrafo/i sembrano ancora in inglese

  ```
  Please generate a cover image for a "Learning Python" textbook that can be used by social media previews.
  The image should follow the open graph image standards with a Wide landscape format  (1.91:1)
  
  
  A vibrant, friendly textbook cover illustration for a children's coding book titled "Learning Python", designed for "Ages 10 and Up", suitable for a web book cover and social media preview card.
  
  Left side: A cheerful cartoon green python snake named Monty sits center-left, wearing round reading glasses, looking curious and excited. Monty has a friendly, approachable expression — not scary at 
  
  Title: The title "Learning Python" must be placed in the center of the cover page using a white font.
  The title should not cover the mascot on the left side.
  
  - A turtle graphics canvas of a square outline with a turtle icon finishing the last edge.
  - A turtle graphics canvas showing a colorful geometric flower made of petals in yellow, and green leaves
  - A
  ```


## `intermediate/01-docker-python.md`

- **warning** `untranslated` — 26 paragrafo/i sembrano ancora in inglese

  ```
  So far in this course you have run Python programs in two ways:
  
  Now we add a third option: **Docker**.  Docker lets you run Python inside a
  tiny, isolated box called a *container* — directly on your computer, but safely
  separated from everything else.  The contain
  
  This is actually how many real companies run student code in coding platforms!
  
  You must have the Docker execution service running in a separate terminal before
  the labs on this page will work.
  
  If Docker is not installed the script will print detailed instructions for
  every operating system.  Once the service is running you will see:
  ```


## `jupyter/.ipynb_checkpoints/01-setup-checkpoint.md`

- **warning** `untranslated` — 3 paragrafo/i sembrano ancora in inglese

  ```
  We will be using the turtle library in Python 3.3
  
  ## Jupyter Notebook Setup
  We will be running this library from within a Jypyter notebook.
  
  After you run the last command it will open a web browser.
  ```


## `learning-graph/book-metrics.md`

- **warning** `untranslated` — 6 paragrafo/i sembrano ancora in inglese

  ```
  **Note**: Student-facing content metrics exclude  and  directories. Chapter-only metrics show what students see in the main chapters.
  
  The twelve tracked elements of an intelligent textbook. The **Status** column shows whether each element is *Required*, *Recommended*, or *Optional*; a ⚠️ marks a required element that is still missin
  
  | # | Element | Value | Status | Notes |
  |---|---------|-------|--------|-------|
  | 1 | Concepts | 450 | Required | Concepts from learning graph |
  | 2 | Chapters | 38 | Required | Chapter directories 
  
  | Metric Name | All Content | Chapters Only | Notes |
  |-------------|-------------|---------------|-------|
  | Diagrams | 0 | 0 | H4 headers starting with '#### Diagram:' |
  | Equations | 6 | 5 | LaTeX 
  
  - **Concepts** *(required)*: Number of rows in learning-graph.csv
  - **Chapters** *(required)*: Count of chapter directories containing index.md files
  - **MicroSims** *(recommended)*: Directories in do
  ```


## `learning-graph/chapter-metrics.md`

- **warning** `untranslated` — 2 paragrafo/i sembrano ancora in inglese

  ```
  | Chapter | Name | Sections | Diagrams | Equations | Words | Links | Quiz | Refs |
  |---------|------|----------|----------|-----------|-------|-------|------|------|
  | 1 | [Welcome to Python and Skulp
  
  - **Chapter**: Chapter number (leading zeros removed)
  - **Name**: Chapter title from index.md
  - **Sections**: Count of H2 and H3 headers in chapter markdown files
  - **Diagrams**: Count of H4 headers s
  ```


## `learning-graph/concept-list-v1.md`

- **warning** `untranslated` — 22 paragrafo/i sembrano ancora in inglese

  ```
  1. Python interpreter overview
  2. Python 2 vs Python 3 differences
  3. Trinket.io — web-based Python environment
  4. repl.it — online Python IDE
  5. Thonny — beginner-friendly Python IDE
  6. Spyder IDE — 
  
  ### Strings
  42. String type () — text enclosed in quotes
  43. Single vs double quotes
  44. String concatenation with 
  45. String repetition with 
  46. String indexing (0-based)
  47. String slicing ()
  48. 
  
  60.  — convert to integer
  61.  — convert to float
  62.  — convert to string
  63.  — convert to boolean
  64.  — inspect a variable's type
  65.  — check if object is an instance of a type
  
  66.  function — read text from user
  67. Prompting the user (passing a string to )
  68. Converting input strings to numbers with  / 
  69. Input validation basics
  
  76.  loop — iterating over a sequence
  77.  loop with 
  78. 
  79.  loop — condition-based repetition
  80.  — exit a loop early
  81.  — skip to next iteration
  82.  clause on loops
  83. Nested loops
  84. Loop 
  ```


## `learning-graph/concept-list.md`

- **warning** `untranslated` — 11 paragrafo/i sembrano ancora in inglese

  ```
  76. None Value and NoneType
  77. Functions Returning None
  78. Checking for None with is
  
  92. if Statement
  93. if...else Block
  94. elif Chains
  95. Nested if Statements
  96. Conditional Ternary Expression
  97. match/case Statement
  98. Truthiness in Conditions
  99. Compound Conditions
  
  100. for Loop over Sequence
  101. for Loop with range()
  102. range(start, stop, step)
  103. while Loop
  104. break Statement
  105. continue Statement
  106. else Clause on Loops
  107. Nested Loops
  108. Loop 
  
  137. List Type
  138. Creating a List
  139. List Indexing
  140. Negative Indexing
  141. List Slicing
  142. len() for Lists
  143. List append() insert() extend()
  144. List remove() pop() clear()
  145. List sor
  
  163. Dictionary Type
  164. Creating a Dictionary
  165. Accessing Values by Key
  166. dict get() Method
  167. Adding and Updating Key-Value Pairs
  168. Removing Entries pop() del
  169. Dictionary keys() valu
  ```


## `learning-graph/faq-quality-report.md`

- **warning** `untranslated` — 1 paragrafo/i sembrano ancora in inglese

  ```
  1. **Boolean Type** (concetto 51) — centrale per tutti i condizionali
  2. **Augmented Assignment Operators** (+=, -=) — concetto 36
  3. **Logical Operators** (and/or/not) — concetto 53
  4. **Membership w
  ```


## `learning-graph/quality-metrics.md`

- **warning** `untranslated` — 2 paragrafo/i sembrano ancora in inglese

  ```
  - **2**: Python 2 vs Python 3
  - **4**: Repl.it Online IDE
  - **5**: Thonny Beginner IDE
  - **6**: Spyder Scientific IDE
  - **7**: VS Code Editor
  - **9**: JupyterLab Environment
  - **12**: Virtual Environm
  
  | Posizione | ID Concetto | Etichetta del Concetto | Grado Entrante |
  |------|-----------|---------------|----------|
  | 1 | 137 | List Type | 34 |
  | 2 | 58 | String Type | 33 |
  | 3 | 115 | Defining a 
  ```


## `learning-graph/taxonomy-distribution.md`

- **warning** `untranslated` — 6 paragrafo/i sembrano ancora in inglese

  ```
  - 137. List Type
  - 138. Creating a List
  - 139. List Indexing
  - 140. Negative Indexing
  - 141. List Slicing
  - 142. len() for Lists
  - 143. List append() insert() extend()
  - 144. List remove() pop() clear
  
  - 305. import turtle
  - 306. turtle.Turtle() Object
  - 307. turtle.Screen() Object
  - 308. Screen Setup and bgcolor()
  - 309. Movement forward() backward()
  - 310. Turning left() right()
  - 311. Absolute Po
  
  - 86. input() Function
  - 87. Prompting the User
  - 88. Converting Input to Numbers
  - 89. Input Validation Basics
  - 90. Reading Multiple Inputs
  - 91. Strip Whitespace from Input
  - 92. if Statement
  - 93.
  
  - 364. Abstract Data Types Overview
  - 365. Stack LIFO Structure
  - 366. Queue FIFO Structure
  - 367. Queue enqueue() dequeue()
  - 368. Graph Nodes and Edges
  - 369. Adjacency List Representation
  - 370. Br
  
  - 285. Objects and Classes Overview
  - 286. Attributes of an Object
  - 287. Methods of an Object
  - 288. class Keyword
  - 289. __init__() Constructor
  - 290. self Parameter
  - 291. Creating Class Instances
  ```


## `sims/microsim-ideas.md`

- **warning** `untranslated` — 44 paragrafo/i sembrano ancora in inglese

  ```
  This document was produced by scanning all 38 chapters in , the
  17 Python labs, the learning graph, and the turtle graphics gallery. Every
  chapter already has strong Skulpt/CodeMirror "see it, run it,
  
  - **Directory:**  with , ,
    , and  (scaffolded by )
  - **Library routing** follows the generator's routing table (p5.js for custom
    simulations, Chart.js for charts, Plotly for f(x) plots, vis-networ
  
  | Tier | Focus | Sims | Rationale |
  |------|-------|------|-----------|
  | 1 | Core mental models (Ch 1–10) | 11 | The book's foundation; misconceptions formed here persist for years |
  | 2 | Data and f
  
  - **Chapter:** 1–2 (Welcome to Python; Python Code Structure)
  - **Concept and gap:** Students run whole programs and see only final output.
    They never see the interpreter walking the code top to bot
  
  - **Chapter:** 3 (Variables and Numbers)
  - **Concept and gap:**  is invisible magic. The sticky-note
    metaphor is described in prose but never shown operating. Reassignment
    ("the old value is repla
  ```


## `trinket/00-introduction.md`

- **warning** `untranslated` — 8 paragrafo/i sembrano ancora in inglese

  ```
  !!! warning "Deprecated Lab — Trinket is shutting down"
      This lab was written for **Trinket.io**, which is [shutting down in August 2026]. The embedded  links on this page will stop working after t
  
  These pages are kept for reference only. The current version of this course now runs every lab as an inline **[Skulpt]** editor right in the page — no account or install needed. **Start at [Chapter 1:
  
  These labs assume that you have internet access and a modern web browser such as Chrome.
  
  We use the [Trinket web site] because it a kid-safe place that has many of the basic turtle drawing libraries implemented in and easy-to-use web environment.  It is appropriate for students just getti
  
  If you want to try another web-based system that support turtle graphics and Python 3.X we suggest the web site [repl.it].  Note that repl.it is not specifically designed for kids.
  ```


## `trinket/01a-trinket-account.md`

- **warning** `untranslated` — 5 paragrafo/i sembrano ancora in inglese

  ```
  !!! warning "Deprecated Lab — Trinket is shutting down"
      This lab was written for **Trinket.io**, which is [shutting down in August 2026]. The embedded  links on this page will stop working after t
  
  These pages are kept for reference only. The current version of this course now runs every lab as an inline **[Skulpt]** editor right in the page — no account or install needed. **Start at [Chapter 1:
  
  These labs assume that you have internet access and a modern web browser such as Chrome.
  
  We use the [Trinket web site] because it a kid-save place that has many of the basic turtle drawing libraries implemented in and easy-to-use web environment.  It is appropriate for students just getti
  
  1. You can save programs
  1. You can rename programs
  1. You can create folders of programs
  1. You can run your program
  1. You can make the program fill the screen (fullscreen)
  1. Download your Python c
  ```


## `trinket/01b-turtle-graphics.md`

- **warning** `untranslated` — 16 paragrafo/i sembrano ancora in inglese

  ```
  !!! warning "Deprecated Lab — Trinket is shutting down"
      This lab was written for **Trinket.io**, which is [shutting down in August 2026]. The embedded  links on this page will stop working after t
  
  These pages are kept for reference only. The current version of this course now runs every lab as an inline **[Skulpt]** editor right in the page — no account or install needed. **Start at [Chapter 1:
  
  ## What is the turtle graphics library?
  Turtle graphs have been around for almost [50 years].  A turtle is a drawing object that has position, direction, and a pen to draw as it moves around a grid.  
  
  For many of our introductory python labs, we will use the turtle python library.  Although there are many different versions of the turtle library, most of the commands are similar.  What you learn wi
  
  ## Initialization commands
  There are three lines that will appear at the top of these labs:
  ```


## `trinket/02-simple-square.md`

- **warning** `untranslated` — 8 paragrafo/i sembrano ancora in inglese

  ```
  !!! warning "Deprecated Lab — Trinket is shutting down"
      This lab was written for **Trinket.io**, which is [shutting down in August 2026]. The embedded  links on this page will stop working after t
  
  These pages are kept for reference only. The current version of this course now runs every lab as an inline **[Skulpt]** editor right in the page — no account or install needed. **Start at [Chapter 1:
  
  ## Drawing a Square
  The following code is an example of drawing a square using turtle graphics.  In this example the turtle moves forward 100 units and then turns right.  The angle for the right turn 
  
  ## Try it out
  Here is a link to the Trinket web site with this program running:
  [https://trinket.io/python/564899ffe9]
  You can click on this link and then press the Run button.  You should see the pyt
  
  ## Explanation
  The first three lines will be the same for all our programs.  They import the turtle library into our program, create a new turtle object and then assign the turtle a shape icon.  Altho
  ```


## `trinket/03-variables.md`

- **warning** `untranslated` — 5 paragrafo/i sembrano ancora in inglese

  ```
  !!! warning "Deprecated Lab — Trinket is shutting down"
      This lab was written for **Trinket.io**, which is [shutting down in August 2026]. The embedded  links on this page will stop working after t
  
  These pages are kept for reference only. The current version of this course now runs every lab as an inline **[Skulpt]** editor right in the page — no account or install needed. **Start at [Chapter 1:
  
  In the simple square program we repeated the numbers for the distance and turning angle four times in four different places.  If we wanted to change the size of our box we would have to change the cod
  
  In this example program we will make the turtle go forward 40 steps and then make a right turn of 90 degrees.  We will repeat this four times to complete a square.
  
  ## Experiments
  Can you make the turtle draw a larger square?  Hint: change the forward(40) to be forward(100)
  ```


## `trinket/04-loops.md`

- **warning** `untranslated` — 4 paragrafo/i sembrano ancora in inglese

  ```
  !!! warning "Deprecated Lab — Trinket is shutting down"
      This lab was written for **Trinket.io**, which is [shutting down in August 2026]. The embedded  links on this page will stop working after t
  
  These pages are kept for reference only. The current version of this course now runs every lab as an inline **[Skulpt]** editor right in the page — no account or install needed. **Start at [Chapter 1:
  
  In this example program we will make the turtle go forward 40 steps and then make a right turn of 90 degrees.  
  We will repeat this four times to complete a square.
  
  ## Experiments
  1. Can you make the turtle draw a larger square?  Hint: change the distance to be 80.  How big can you make the square before the turtle goes off the screen?
  2. Can you make a hexagon? 
  ```


## `trinket/04a-stop-sign.md`

- **warning** `untranslated` — 3 paragrafo/i sembrano ancora in inglese

  ```
  !!! warning "Deprecated Lab — Trinket is shutting down"
      This lab was written for **Trinket.io**, which is [shutting down in August 2026]. The embedded  links on this page will stop working after t
  
  These pages are kept for reference only. The current version of this course now runs every lab as an inline **[Skulpt]** editor right in the page — no account or install needed. **Start at [Chapter 1:
  
  In this lesson, we will use variables and for loop to draw a stop sign.
  We will also show how to use the penup, pendown, color, begin_fill, end_fill and write functions.
  Our write function will also c
  ```


## `trinket/05-conditionals.md`

- **warning** `untranslated` — 9 paragrafo/i sembrano ancora in inglese

  ```
  !!! warning "Deprecated Lab — Trinket is shutting down"
      This lab was written for **Trinket.io**, which is [shutting down in August 2026]. The embedded  links on this page will stop working after t
  
  These pages are kept for reference only. The current version of this course now runs every lab as an inline **[Skulpt]** editor right in the page — no account or install needed. **Start at [Chapter 1:
  
  In this example program we will make the turtle draw
  different sides of the square using different colors.
  
  There are two things we do with equations in Python.  The first is to use the equal sign to **assign values** on the left side of the equal sign to the values on the right side.  The second thing we d
  
  Here is the basic syntax of the Python conditional operator.
  ```


## `trinket/06-functions.md`

- **warning** `untranslated` — 4 paragrafo/i sembrano ancora in inglese

  ```
  !!! warning "Deprecated Lab — Trinket is shutting down"
      This lab was written for **Trinket.io**, which is [shutting down in August 2026]. The embedded  links on this page will stop working after t
  
  These pages are kept for reference only. The current version of this course now runs every lab as an inline **[Skulpt]** editor right in the page — no account or install needed. **Start at [Chapter 1:
  
  Now we will create a new function that will draw each side.
  
  ## Experiments
  Can you change the name of the function to be "petal"?
  ```


## `trinket/07-flower.md`

- **warning** `untranslated` — 4 paragrafo/i sembrano ancora in inglese

  ```
  !!! warning "Deprecated Lab — Trinket is shutting down"
      This lab was written for **Trinket.io**, which is [shutting down in August 2026]. The embedded  links on this page will stop working after t
  
  These pages are kept for reference only. The current version of this course now runs every lab as an inline **[Skulpt]** editor right in the page — no account or install needed. **Start at [Chapter 1:
  
  Now we will create a new function that will draw a triangle for
  each side.  It will do this by going forward and right three times
  at an angle of 120 degrees.  We will put that triangle into a
  functio
  
  ## Experiments
  1. Can you change the colors of the petals?
  2. Can you change the width of the stem of the flower using the pensize() function?
  3. Can you change the size of the petals?
  4. Can you chan
  ```


## `trinket/07-function-parameters.md`

- **warning** `untranslated` — 4 paragrafo/i sembrano ancora in inglese

  ```
  !!! warning "Deprecated Lab — Trinket is shutting down"
      This lab was written for **Trinket.io**, which is [shutting down in August 2026]. The embedded  links on this page will stop working after t
  
  These pages are kept for reference only. The current version of this course now runs every lab as an inline **[Skulpt]** editor right in the page — no account or install needed. **Start at [Chapter 1:
  
  ## Lesson Objective
  Now we will create a new function that draw a square with a specific color at a specific x and y point.  The function will take three inputs:
  - the color
  - the horizontal x positio
  
  1. Can you change the name of the function to be "petal"?
  2. Can you change the function to include the ability to pass in one color for the border, and one color for the center fill?
  [Sample of Borde
  ```


## `trinket/08-list.md`

- **warning** `untranslated` — 5 paragrafo/i sembrano ancora in inglese

  ```
  !!! warning "Deprecated Lab — Trinket is shutting down"
      This lab was written for **Trinket.io**, which is [shutting down in August 2026]. The embedded  links on this page will stop working after t
  
  These pages are kept for reference only. The current version of this course now runs every lab as an inline **[Skulpt]** editor right in the page — no account or install needed. **Start at [Chapter 1:
  
  How would we create and access a list of colors in Python?
  Here is a list of colors:
  
  To access any color you can reference the index of the color by using a number.  For example to get the third
  color you would use:
  
  1. Can you change the name of the function to be "petal"?
  1. What does ```` return?
  1. Go to the [Trinket colors page] and see the name of other colors you can use.
  1. What happens if a list does not 
  ```


## `trinket/08-random.md`

- **warning** `untranslated` — 5 paragrafo/i sembrano ancora in inglese

  ```
  !!! warning "Deprecated Lab — Trinket is shutting down"
      This lab was written for **Trinket.io**, which is [shutting down in August 2026]. The embedded  links on this page will stop working after t
  
  These pages are kept for reference only. The current version of this course now runs every lab as an inline **[Skulpt]** editor right in the page — no account or install needed. **Start at [Chapter 1:
  
  In this exercise we will draw 10 random circles on the screen.  We will use the random function **randint(min, max)** that will generate a random number between the minimum and maximum values.  Since 
  
  After this line runs, the variable myNumber will be assigned some random number between -200 and 200.   We will then use this number to go to that location before we draw a circle.
  
  ## Experiments
  1. Can you create a variable that is used to control the distance from the origin to wander?  Right now the distance is set to be 200 on each extent.
  2. Can you create a variable for th
  ```


## `trinket/08b-random-stars.md`

- **warning** `untranslated` — 5 paragrafo/i sembrano ancora in inglese

  ```
  !!! warning "Deprecated Lab — Trinket is shutting down"
      This lab was written for **Trinket.io**, which is [shutting down in August 2026]. The embedded  links on this page will stop working after t
  
  These pages are kept for reference only. The current version of this course now runs every lab as an inline **[Skulpt]** editor right in the page — no account or install needed. **Start at [Chapter 1:
  
  In this exercise we will draw 5 stars of different colors:
  The colors are randomly picked from the list of colors
  
  After these line runs, the variable mycolor will be assigned some random color from the list of colors myColorList.   We will then use this color to fill a star.
  The stars are drawn at random location
  
  ## Experiments
  1. Can you create a variable for the number of circles to draw?
  2. Go to the [Trinket colors page] and see the name of other colors you can use.  Note that you can use any of these colo
  ```


## `trinket/08c-turtle-shapes.md`

- **warning** `untranslated` — 5 paragrafo/i sembrano ancora in inglese

  ```
  !!! warning "Deprecated Lab — Trinket is shutting down"
      This lab was written for **Trinket.io**, which is [shutting down in August 2026]. The embedded  links on this page will stop working after t
  
  These pages are kept for reference only. The current version of this course now runs every lab as an inline **[Skulpt]** editor right in the page — no account or install needed. **Start at [Chapter 1:
  
  With the turtle shape() method we can change your turtle shape to be any of the following shapes
  
  ## Using a List of Shapes
  What if we want to use a list of shapes?
  
  ## Experiments
  Can you use the new shapes to draw a star or any other shape of your chosing
  ```


## `trinket/11-input.md`

- **warning** `untranslated` — 4 paragrafo/i sembrano ancora in inglese

  ```
  !!! warning "Deprecated Lab — Trinket is shutting down"
      This lab was written for **Trinket.io**, which is [shutting down in August 2026]. The embedded  links on this page will stop working after t
  
  These pages are kept for reference only. The current version of this course now runs every lab as an inline **[Skulpt]** editor right in the page — no account or install needed. **Start at [Chapter 1:
  
  We can prompt the user to supply a number using the input() function.
  
  1. Write a program that will prompt the user to enter the number of shapes to draw, the size of the shapes, the color of the shapes and the range of the screen to draw them (50 to 200).
  2. Add some ad
  ```


## `trinket/12-recursion.md`

- **warning** `untranslated` — 7 paragrafo/i sembrano ancora in inglese

  ```
  !!! warning "Deprecated Lab — Trinket is shutting down"
      This lab was written for **Trinket.io**, which is [shutting down in August 2026]. The embedded  links on this page will stop working after t
  
  These pages are kept for reference only. The current version of this course now runs every lab as an inline **[Skulpt]** editor right in the page — no account or install needed. **Start at [Chapter 1:
  
  ## Recursion
  Recursion is when we write a function that calls itself.  It usually passes a parameter that changes and when it hits a limit it stops going.  This lab does a lot of drawing so to speed i
  
  Our recursive function is the draw_branch function.  It will draw a single branch and then call itself two times at its tip to draw two more smaller branches.
  
  ## Explanation
  The first three lines will be the same for all our programs.  They import the turtle library into our program, create a new turtle object and then assign the turtle a shape icon.
  ```


## `trinket/13-shape-module.md`

- **warning** `untranslated` — 3 paragrafo/i sembrano ancora in inglese

  ```
  !!! warning "Deprecated Lab — Trinket is shutting down"
      This lab was written for **Trinket.io**, which is [shutting down in August 2026]. The embedded  links on this page will stop working after t
  
  These pages are kept for reference only. The current version of this course now runs every lab as an inline **[Skulpt]** editor right in the page — no account or install needed. **Start at [Chapter 1:
  
  In this lab we will create a set of drawing function and put them together into a new file.  We will then import this file into our main.py file.
  ```


## `trinket/14-color-picker.md`

- **warning** `untranslated` — 5 paragrafo/i sembrano ancora in inglese

  ```
  !!! warning "Deprecated Lab — Trinket is shutting down"
      This lab was written for **Trinket.io**, which is [shutting down in August 2026]. The embedded  links on this page will stop working after t
  
  These pages are kept for reference only. The current version of this course now runs every lab as an inline **[Skulpt]** editor right in the page — no account or install needed. **Start at [Chapter 1:
  
  You are not limited to the colors by name [Trinket Colors].
  You can use Hex and RGB values and let your imagination run wild.
  
  ## Experiments
  Can you try different colors? 
  Can you change font properties in style object?
  
  The font name can as 'Arial', 'Courier', or 'Times New Roman'
  The font size in pixels.
  The font type, which can be 'normal', 'bold', or 'italic'
  ```


## `trinket/15-sine-wave.md`

- **warning** `untranslated` — 4 paragrafo/i sembrano ancora in inglese

  ```
  !!! warning "Deprecated Lab — Trinket is shutting down"
      This lab was written for **Trinket.io**, which is [shutting down in August 2026]. The embedded  links on this page will stop working after t
  
  These pages are kept for reference only. The current version of this course now runs every lab as an inline **[Skulpt]** editor right in the page — no account or install needed. **Start at [Chapter 1:
  
  Here is an example of plotting a sine function with turtle goto() functions.  We calculate the new vertical value with the following function:
  
  And we loop through about 400 values from -200 to 200.  We use the radians() function to convert the numbers into a a number that will give us a single sine in the X range.
  ```


## `trinket/16-changing-background.md`

- **warning** `untranslated` — 6 paragrafo/i sembrano ancora in inglese

  ```
  !!! warning "Deprecated Lab — Trinket is shutting down"
      This lab was written for **Trinket.io**, which is [shutting down in August 2026]. The embedded  links on this page will stop working after t
  
  These pages are kept for reference only. The current version of this course now runs every lab as an inline **[Skulpt]** editor right in the page — no account or install needed. **Start at [Chapter 1:
  
  We can use trinkets to change the background and change the shape of the turtle with a custom image.
  Also we can control the screen with the mouse. It gives a starting point for how to create a game.
  
  The following blog lays out the steps for creating a rocket ship
  https://blog.trinket.io/using-images-in-turtle-programs/
  
  The images have to be the same size as the the screen size. Here are some other images that have been resized.
  ```


## `trinket/17-controlling-mouseclicks.md`

- **warning** `untranslated` — 6 paragrafo/i sembrano ancora in inglese

  ```
  !!! warning "Deprecated Lab — Trinket is shutting down"
      This lab was written for **Trinket.io**, which is [shutting down in August 2026]. The embedded  links on this page will stop working after t
  
  These pages are kept for reference only. The current version of this course now runs every lab as an inline **[Skulpt]** editor right in the page — no account or install needed. **Start at [Chapter 1:
  
  We can use trinkets to change the background and control mouse clicks.
  Also we have access to the exact position where the mouse was clicked. That creates a lot of possibilities 
  for creating differen
  
  Here is an example of setting the screen color. We then draw a square in the center of the screen. 
  When the user clicks a circle is drawn within the circle. On next click the circle increases in diam
  
  If the user clicks the screen outside the square the screen is refreshed
  ```


## `trinket/examples.md`

- **warning** `untranslated` — 3 paragrafo/i sembrano ancora in inglese

  ```
  !!! warning "Deprecated Lab — Trinket is shutting down"
      This lab was written for **Trinket.io**, which is [shutting down in August 2026]. The embedded  links on this page will stop working after t
  
  These pages are kept for reference only. The current version of this course now runs every lab as an inline **[Skulpt]** editor right in the page — no account or install needed. **Start at [Chapter 1:
  
  Use the [Turtle API] documentation to check out what else is available.
  ```


## `turtle-graphics-gallery/t-square-fractal/index.md`

- **warning** `untranslated` — 1 paragrafo/i sembrano ancora in inglese

  ```
  Posizioni degli angoli:
  - In alto a sinistra: 
  - In alto a destra: 
  - In basso a sinistra: 
  - In basso a destra:
  ```

