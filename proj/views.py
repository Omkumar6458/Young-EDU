from django.shortcuts import render,redirect
import subprocess

def calculate_functionality(request, class_name, template_name):
    if request.method == 'POST':
        try:
            input_value = request.POST['input_value']
            # Specify the directory containing the Java class files
            classpath = "C:\\Users\\DELL\\Desktop\\EDU\\PROJECT\\java"

            # Call the specified Java program
            result = subprocess.check_output(
                ['java', '-cp', classpath, class_name, input_value],
                universal_newlines=True
            )
            result = result.strip()
        except subprocess.CalledProcessError as e:
            result = f"Error: {e.output.strip()}"
        except Exception as e:
            result = f"Error: {e}"
    else:
        result = None

    return render(request, template_name, {'result': result})

def calculate_armstrong(request):
    return calculate_functionality(request, 'Armstrong', 'armstrong.html')

def Sorting(request):
    return calculate_functionality(request,'Sorting','Algorithm/Sorting.html')




def home(request):
    return render(request, 'base.html')  # Render the actual home page

def about(request):
    return render(request, 'about.html')  # Render the about page

def teachers(request):
    return render(request, 'teachers.html')  # Render the teachers page

def vehicles(request):
    return render(request, 'Study.html')  # Render the vehicles (study) page

def contact(request):
    return render(request, 'contact.html')  # Render the contact page

def about1(request):
    return render(request, 'about1.html')

def learn(request):
    return render(request,'Grid/learnmore.html')


def p(request):
    return render(request,'practice.html')

# Additional views (if needed)
def header(request):
    return render(request, 'header.html')  # If you want a separate header view

def hero(request):
    return render(request, 'hero.html')  # If you want a separate hero section

def footer(request):
    return render(request, 'footer.html')  # If you want a separate footer view

def check(request):
    return render(request, 'about.html')

def calculate_prime(request):
    return calculate_functionality(request, 'Prime', 'prime.html')

def calculate_factorial(request):
    return calculate_functionality(request, 'Factorial', 'factorial.html')

def check_leap_year(request):
    return calculate_functionality(request, 'LeapYear', 'leap.html')

def reverse_string(request):
    return calculate_functionality(request, 'ReverseString', 'reverse_string.html')

def calculate_fibonacci(request):
    return calculate_functionality(request,'Fibonacci','Fibonacci.html')

def sorting(request):
    return calculate_functionality(request,'Sorting', 'Algorithm/Sorting.html')


def factPage(request):
    return render(request,'Grid/Factorial.html')

def armPage(request):
    return render(request,'Grid/ArmStrong.html')

def FiboPage(request):
    return render(request,'Grid/Fibonacci.html')

def PrimePage(request):
    return render(request,'Grid/PrimePage.html')

def leapPage(request):
    return render(request,'Grid/Leap.html')

def Reverse(request):
    return render(request,'Grid/Reverse.html')

def SortPage(request):
    return render(request,'Grid/Sorting.html')
def Variable(request):
    return render(request,'Grid/Variable.html')





def factpageA(request):
    return render(request,'Analysis/factorial.html')

def Test(request):
    return render(request,'Test/Test.html')

def quiz(request):
    return render(request,'quiz/quiz.html')


def intro(request):
    return render(request,'quiz/intro.html')
def basic(request):
    return render(request,'quiz/syntax.html')
def var(request):
    return render(request,'quiz/variable.html')
def loop(request):
    return render(request,'quiz/loop.html')
def cond(request):
    return render(request,'quiz/conditional.html')
def function(request):
    return render(request,'quiz/function.html')
def syntax(request):
    return render(request,'quiz/syntax.html')




def array(request):
    return render(request,'quiz/DATA STRUCTURE/Array.html')
def linked(request):
    return render(request,'quiz/DATA STRUCTURE/LinkedList.html')
def stack(request):
    return render(request,'quiz/DATA STRUCTURE/Stack.html')
def Queue(request):
    return render(request,'quiz/DATA STRUCTURE/Queue.html')
def Tree(request):
    return render(request,'quiz/DATA STRUCTURE/Tree.html')
def Graph(request):
    return render(request,'quiz/DATA STRUCTURE/Graph.html')












def introduction(request):
    return render(request,'content/content.html')
def start(request):
    return render(request,'content/intro.html')
def command(request):
    return render(request,'content/command.html')
def variable(request):
    return render(request,'content/variable.html')
def Loop(request):
    return render(request,'content/loop.html')
def Condition(request):
    return render(request,'content/condition.html')
def Function(request):
    return render(request,'content/Function.html')
def Syantxi(request):
    return render(request,'content/Syntax.html')
def sumofdigit(request):
    return render(request,'content/digit-sum.html')
def evenodd(request):
    return render(request,'content/even-odd.html')
def palindrone(request):
    return render(request,'content/palindrome.html')
def gcd(request):
    return render(request,'content/gcd.html')
def lcm(request):
    return render(request, 'content/lcm.html')


def array(request):
    return render(request,'content/array.html')
def linked(request):
    return render(request, 'content/linkedlist.html')
def Stack(request):
    return render(request, 'content/stack.html')
def hashmap(request):
    return render(request,'content/hash.html')
def t(request):
    return render(request, 'content/trees.html')

def q(request):
    return render(request, 'content/queue.html')

def c(request):
    return render(request,'quiz/Programing/c.html')

def cadd(request):
    return render(request,'quiz/Programing/c++.html')

def java(request):
    return render(request,'quiz/Programing/java.html')

def javascript(request):
    return render(request,'quiz/Programing/javacript.html')

