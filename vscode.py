from turtle import *

t = Turtle()
sc = Screen()

t.speed(0)
t.hideturtle()
t.width(5)

#### SCREEN COLORS ####
VSCODE_BG = "#002B36"
VSCODE_ACTIVE_TAB = "#002B37"
VSCODE_INACTIVE_TAB = "#004052"
VSCODE_LIGHT_GREEN = "#89D185"
VSCODE_LIGHT_GRAY = "#C5C5C5"
VSCODE_FILE_EXPLORER_BG = "#00212B"
VSCODE_ICON_TAB = "#003847"
VSCODE_ACTIVE_WHITE = "#FFFFFF"
VSCODE_INACTIVE_WHITE = "#B4B4B4"
VSCODE_GRAY = "#858D82"
VSCODE_MENU_BLUE = "#1A343C"
VSCODE_ACTIVE_FILE_NAME = "#003440"
VSCODE_CONSOLE_BG = VSCODE_ICON_TAB
VSCODE_INACTIVE_TAB_NAME = "#93A1A1"
### TEXT COLORS ###
KEYWORD_GREEN = "#859900"
CLASS_RED = "#CB4B16"
VAR_BLUE = "#268BD2"
STR_TEAL = "#2AA198"
INT_PURPLE = "#C7357E"
COMMENT_COLOR = "#657B83"

### SCREEN SETUP ###
sc.setup(width=800, height=600)
sc.bgcolor(VSCODE_BG)

### TURTLE SETUP ###
t.up()
t.goto(-405, 295)
t.down()

### FUNCTIONS ###
def rect(w, h, color):
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(w)
        t.rt(90)
        t.forward(h)
        t.rt(90)
    t.end_fill()


def blank_move(dist):
    t.up()
    t.fd(dist)
    t.down()


def blank_move_rt(dist):
    t.rt(90)
    blank_move(dist)
    t.lt(90)


### DRAWING ###
rect(50, 600, VSCODE_ICON_TAB)
blank_move(50)
rect(95, 600, VSCODE_FILE_EXPLORER_BG)
blank_move(100)
rect(650, 25, VSCODE_INACTIVE_TAB)
blank_move(100)
rect(100, 25, VSCODE_ACTIVE_TAB)
t.color(VSCODE_LIGHT_GREEN)
blank_move_rt(25)
blank_move(470)
t.write(u"\u1405", False, align="center", font=("Arial", 15))
blank_move_rt(2.5)
blank_move(30)
t.color(VSCODE_LIGHT_GRAY)
t.write(u"\uea79", False, align="center", font=("Arial", 15))
blank_move_rt(-8)
blank_move(30)
t.write(u"\u2026", False, align="center", font=("Arial", 15))
t.up()
t.goto(-380, 270)
t.down()
t.color(VSCODE_ACTIVE_WHITE)
t.write("📄", False, align="center", font=("Arial", 15))
t.color(VSCODE_INACTIVE_WHITE)
blank_move_rt(35)
t.write("🔎", False, align="center", font=("Arial", 15))
blank_move_rt(38)
t.write("▶", False, align="center", font=("Arial", 20))
blank_move_rt(25)
blank_move(15)
t.write("🖥️", False, align="center", font=("Arial", 15))
blank_move_rt(35)
blank_move(-13.8)
t.write("⏹️", False, align="center", font=("Arial", 15))
blank_move_rt(390)
t.write("👤", False, align="center", font=("Arial", 15))
blank_move_rt(35)
t.write("⚙️", False, align="center", font=("Arial", 15))
t.up()
t.goto(-325, 270)
t.down()
t.color(VSCODE_GRAY)
t.write("EXPLORER", False, align="center", font=("Arial", 8))
blank_move_rt(8)
blank_move(-30)
rect(95, 15, VSCODE_MENU_BLUE)
blank_move_rt(15)
blank_move(43)
t.color(VSCODE_ACTIVE_WHITE)
t.write("> OPEN EDITORS", False, align="center", font=("Arial", 8))
blank_move_rt(5)
blank_move(-43)
rect(95, 15, VSCODE_MENU_BLUE)
blank_move_rt(15)
blank_move(43)
t.color(VSCODE_ACTIVE_WHITE)
t.write("⬇ OPEN FOLDERS", False, align="center", font=("Arial", 8))
blank_move_rt(18)
t.write("🐍 __init__.py", False, align="center", font=("Arial", 8))
blank_move_rt(10)
blank_move(-43)
rect(95, 15, VSCODE_ACTIVE_FILE_NAME)
t.color(VSCODE_ACTIVE_WHITE)
blank_move(43)
blank_move_rt(13)
t.write("🐍 vscode.py", False, align="center", font=("Arial", 8))
blank_move_rt(420)
blank_move(-43)
rect(95, 15, VSCODE_MENU_BLUE)
blank_move_rt(15)
blank_move(43)
t.color(VSCODE_ACTIVE_WHITE)
t.write("> MAVEN", False, align="center", font=("Arial", 8))
blank_move_rt(5)
blank_move(-43)
rect(95, 15, VSCODE_MENU_BLUE)
blank_move_rt(15)
blank_move(43)
t.color(VSCODE_ACTIVE_WHITE)
t.write("> OUTLINE", False, align="center", font=("Arial", 8))
blank_move_rt(5)
blank_move(-43)
rect(95, 15, VSCODE_MENU_BLUE)
blank_move_rt(15)
blank_move(43)
t.color(VSCODE_ACTIVE_WHITE)
t.write("> DEPENDENCIES", False, align="center", font=("Arial", 8))
blank_move_rt(5)
blank_move(-43)
t.up()
t.goto(-405, 280)
t.fd(200)
t.down()
blank_move_rt(5)
t.color(VSCODE_INACTIVE_TAB_NAME)
t.write("🐍 __init__.py", False, align="center", font=("Arial", 8))
blank_move(100)
t.color(VSCODE_ACTIVE_WHITE)
t.write("🐍 vscode.py  X", False, align="center", font=("Arial", 8))
blank_move_rt(30)
blank_move(-140)
t.color(VSCODE_INACTIVE_TAB_NAME)
for i in range(1, 31):
    t.write(i, False, align="center", font=("Arial", 8))
    blank_move_rt(13)
# blank_move(-10)
t.setx(-255)
rect(650, 145, VSCODE_CONSOLE_BG)
blank_move_rt(20)
blank_move(30)
t.color(VSCODE_INACTIVE_WHITE)
t.write("PROBLEMS", False, align="center", font=("Arial", 8))
blank_move(55)
t.write("OUTPUT", False, align="center", font=("Arial", 8))
blank_move(55)
t.color(VSCODE_ACTIVE_WHITE)
t.write("TERMINAL", False, align="center", font=("Arial", 8))
blank_move_rt(20)
t.color(VSCODE_INACTIVE_TAB_NAME)
t.up();t.setx(-165);t.down()
t.write("mordy@mordys-pc:~/vscode-py$  ls", False, align="center", font=("Arial", 8))
t.color(VSCODE_ACTIVE_WHITE)
blank_move(-33)
blank_move_rt(20)
t.write("__init.py__  vscode.py", False, align="center", font=("Arial", 8))
blank_move_rt(20)
blank_move(26)
t.color(VSCODE_INACTIVE_TAB_NAME)
t.write("mordy@mordys-pc:~/vscode-py$", False, align="center", font=("Arial", 8))
# Lines of code to display on the screen
lines = [
    "#!/usr/bin/python3",
    "from turtle import *",
    "",
    "t = Turtle()",
    "sc = Screen()",
    "",
    "sc.setup(width=800, height=600)",
    "sc.bgcolor(VSCODE_BG)",
    "",
    "### TURTLE SETUP ###",
    "t.up()",
    "t.goto(-405, 295)",
    "t.down()",
    "",
    "### FUNCTIONS ###",
    "def rect(w, h, color):",
    "\tt.color(color)",
    "\tt.begin_fill()",
    "\tfor _ in range(2):",
    "\t\tt.forward(w)",
    "\t\tt.rt(90)",
    "\t\tt.forward(h)",
    "\t\tt.rt(90)",
    "\t\tt.end_fill()",
    "",
    "def blank_move(dist):",
    "\tt.up()",
    "\tt.fd(dist)",
    "\tt.down()",
]
t.up()
t.goto(-230, 245)
for index, line in enumerate(lines):
    if line.startswith("#"):
        t.color(COMMENT_COLOR)
    elif "=" in line:
        t.color(VAR_BLUE)
    elif "." in line:
        t.color(STR_TEAL)
    elif line.startswith("def"):
        t.color(CLASS_RED)
    else:
        t.color(STR_TEAL)
    t.write(line, False, align="left", font=("Arial", 8))
    blank_move_rt(13)
mainloop()
