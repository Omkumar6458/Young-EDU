from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name ='about'),
    path('teachers/', views.teachers, name='teachers'),
    path('Study/', views.vehicles, name='Study'),
    path('contact/', views.contact, name='contact'),
    path('about1/', views.about1, name ='about1'),
    path('p/',views.p, name='p'),
    path('learnmore/',views.learn,name='learn'),

     
    path('check/', views.check, name='check'),
    path('calculate_armstrong/', views.calculate_armstrong, name='calculate_armstrong'),
    path('calculate_prime/', views.calculate_prime, name='calculate_prime'),
    path('calculate_factorial/', views.calculate_factorial, name='calculate_factorial'),
    path('calculate_fibonacci/', views.calculate_fibonacci, name='Fibonacci'),
    path('leap/', views.check_leap_year, name='check_leap_year'),
    path('reverse_string/', views.reverse_string, name='reverse_string'),
    path('Sorting/',views.Sorting,name ='sorting'),
    path('variable/',views.Variable,name ='variable'),




    path('fact/', views.factPage, name='factPage'),
    path('arm/', views.armPage, name='armpage'),
    path('fibo/', views.FiboPage, name='Fibopage'),
    path('prime/',views.PrimePage,name = 'primepage'),
    path('leap/',views.leapPage,name = 'leapPage'),
    path('reverse/',views.Reverse, name= 'reversepage'),
    path('sort/',views.SortPage, name = 'sortpage'),
     



    path('factA/',views.factpageA, name ='factpageA'),
    path('test/',views.Test, name ='test'),
    path('quiz/',views.quiz, name ='quiz'),


   path('intro/',views.intro,name ='intro'),
   path('basic_command/',views.basic, name='basic'),
   path('var/',views.var,name='var'),
   path('loop/',views.loop,name ='loop'),
   path('condition/',views.cond,name='cond'),
   path('functional/',views.function,name='func'),
   path('syntax/',views.syntax,name = 'syntax'),




  

  path('array/',views.array, name='array'),
  path('linked/',views.linked,name='linkedList'),
  path('stack/',views.stack,name ='stack'),
  path('Queue/',views.Queue, name ='Queue'),
  path('Tree/',views.Tree, name ='Tree'),
  path('Graph/',views.Graph, name='Graph'),















 path('introduction/',views.introduction, name='introduction'),
 path('start/',views.start,name='start'),
 path('basic_command/', views.command, name='command'),
 path('variable/', views.Variable,name= 'variable'),
 path('LOOP/',views.Loop, name='loop1'),
 path('Condition/',views.Condition, name='Condition'),
 path('Function/',views.Function, name='Function'),
 path('Syntax/',views.Syantxi, name= 'Syntax'),






 path('sumofdigit/',views.sumofdigit, name='sumofdigit'),
 path('even-odd/', views.evenodd, name='evenodd'),
 path('palindrone/', views.palindrone , name ='palin'),
 path('gcd/',views.gcd, name='gcd'),
 path('LCM',views.lcm, name ='lcm'),





 path('array/',views.array,name='array1'),
 path('linkedlist/',views.linked, name='linked'),
 path('stack1/',views.Stack,name='stack1'),

 path('hash/',views.hashmap, name='hash'),

path('q/',views.q,name='q'),
path('t/',views.t,name='t'),





path('c/', views.c, name='c'),
path('c++/', views.cadd, name ='cdd'),
path('java/', views.java, name ='java'),
path('javascript', views.javascript, name ='javascript'),

]





    
   

