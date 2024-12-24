
#  K🖩Calculator  :-          ##  Last Update  :-  2024-11-27  



import K_MATH as KM  



from os import name as os_name , system  

def clear_screen() :  #  if \033c not work  
  system ( 'cls' if os_name == 'nt' else 'clear' )  










operations_list = (  '0 ~> Exit\n'  
, '1 . Mathematical Expression'  
, '2 . SUM Numbers'  
, '3 . NUM1 - NUM2'  
, '4 . Multiplying Numbers'  
, '5 . NUM1 ÷ NUM2'  
, '6 . NUM ^ POWER'  
, '7 . Factorial of NUM!'  
, '8 . Multiplication Table'  
, '9 . Numbers Range'  
, '10. ᴿᴼᴼᵀ√(NUM)'  
, '11. Percentage %'  
, '12. Rounding NUM'  
, '13. 𝕊 ⪻ ===⪼  𝔻'  
, '14. NUM --> Even or Odd ?'  
, '15. NUM --> Prime ?'  
, '16. Year --> Leap ?'  #  مش عارف انا حاطط دى هنا ليه بس اشطاا  
, '17. Geometric Shapes'  
, '18. Units Conversion'  
, '19. Purchase Calculation'  
)  ;  print_operations_list = '\n' . join ( operations_list )  





while True :  

  operation = KM.user_chooses (f''' 
   ***** Welcome To K🖩Calculator ***** 

Enter The Operation Number :- 

{ print_operations_list } 
''' , ' ▶️ ' , tuple( map( str , range( len( operations_list ) ) ) ) )  
##            tuple( map( str , range( len( operations_list ) ) ) )    |--->  ( '0' , '1' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' , '10' , '11' , '12' , '13' , '14' , '15' , '16' , '17' , '18' , '19' )  





  if operation == '0' :  #  EXIT  
    clear_screen() #  if \033c not work  
    print ('\033c\n *** Thanks 😁 for using K🖩Calculator *** \n\nGood Bye 👋 \nHave a nice time 😘 ')  
    ###     \033c -->  Clear Screen  
    ###     \033  -->  ANSI Escape Codes  -->  https://replit.com/@Kareem0Aikka/ANSI  
    break  



  clear_screen()  
  print (f'''\033c\n   ***** Welcome To K🖩Calculator ***** 
\n    ▶️▶️▶️  { operations_list [ int( operation ) ] }  ◀️◀️◀️   \n''')  










  if operation == '1' :  #  1️⃣ . Mathematical Expression  
    result = f"Result = { KM.solve_expression() }"  





  elif operation == '2' :  #  2️⃣ . SUM Numbers  
    print ('\n(Note : Press Enter 2 Times To See SUM)')  

    result = f"SUM = { sum( KM.nums_list() ) }"  





  elif operation == '3' :  #  3️⃣ . NUM1 - NUM2  
    print()  ;  num_1 = KM.user_input_number(("NUM1 = " , '' ))  
    print()  ;  num_2 = KM.user_input_number(("NUM2 = " , '' ))  

    result = f'{ num_1 } - { num_2 } = { num_1 - num_2 }'  





  elif operation == '4' :  #  4️⃣ . Multiplying Numbers  
    print ('\n(Note : Press Enter 2 Times To See The Multiplication Result)')  

    result = f"The Multiplication Result = { KM.product( KM.nums_list() ) }"  





  elif operation == '5' :  #  5️⃣ . NUM1 ÷ NUM2  
    division = KM.user_chooses ('''1. Division : NUM1 / NUM2 
2. Remainder Of Division : NUM1 mod NUM2 
''' , ' > ' , ( '1' , '2' ) )  


    print ('\n    NUM1 ' + ( '/' , 'mod' ) [ int( division ) - 1 ] + ' NUM2')  

    print()  ;  num_1 = KM.user_input_number(('NUM1 = ' , '' ))  
    print()  ;  num_2 = KM.user_input_number(('NUM2 = ' , '' )  
    , include_zero__zero_message = ( False , 'Can\'t Divide by zero' ) )  


    result = ( f'{ num_1 } / { num_2 } = { num_1 / num_2 }'  if division == '1' else  f'{ num_1 } mod { num_2 } = { num_1 % num_2 }' )  





  elif operation == '6' :  #  6️⃣ . NUM ^ POWER  
    print()  ;  num   = KM.user_input_number(("NUM = "   , '' ))  
    print()  ;  power = KM.user_input_number(("POWER = " , '' ))  

    result = f'{ num } ^ { power } = { num ** power }'  





  elif operation == '7' :  #  7️⃣ . Factorial of NUM!  
    print()  ;  num = KM.user_input_number(("NUM = "  
    , 'Please enter a positive integer number to calculate factorial of this number :- ' )  
    , int_only = True , positive_negative = "+" )  


    result = f'''The Factorial Of { num }  :  ( { " × " . join( map( str , tuple( range( 1 , num + 1 ) ) ) ) } ) 
\n  ~> { num }! = { KM.factorial( num ) }'''  





  elif operation == '8' :  #  8️⃣ . Multiplication Table  
    result = f"\033[F\033[2K{ KM.multiplication_table() }\n"  





  elif operation == '9' :  #  9️⃣ . Numbers Range  
    result = KM.nums_range()  





  elif operation == '10' :  #  1️⃣ 0️⃣ . ᴿᴼᴼᵀ√(NUM)  
    print()  ;  num  = KM.user_input_number(('NUM = '  , '' ))  
    print()  ;  root = KM.user_input_number(('ROOT = ' , '' )  
    , include_zero__zero_message = ( False , 'Can\'t take the zero root' ) )  


    result = f"The({ root })Root of { num } = { num ** ( 1 / root ) }"  





  elif operation == '11' :  #  1️⃣ 1️⃣ . Percentage %  
    result = KM.percentage()  





  elif operation == '12' :  #  1️⃣ 2️⃣ . Rounding NUM  
    print()  ;  num            = KM.user_input_number(('NUM = '  
    , 'Please enter the number you want to round :- ' ) )  

    print()  ;  decimal_places = KM.user_input_number(('Decimal Places = '  
    , 'Please enter the integer positive number of decimal places to round to :- ' )  
    , int_only = True , positive_negative = '+' )  


    result = f'({ num }) after rounded to ({ decimal_places }) decimal places well be ({ round( num , decimal_places ) })'  





  elif operation == '13' :  #  1️⃣ 3️⃣ . 𝕊 ⪻===⪼ 𝔻  
    result = KM.S_D()  





  elif operation == '14' :  #  1️⃣ 4️⃣ . NUM --> Even or Odd ?  
    print()  ;  num = KM.user_input_number((' > '  
    , 'Please enter an integer number to determine if it is Even OR Odd :-' )  
    , int_only = True )  


    result = f'({ num }) ~> ' + ( 'EVEN' if num % 2 == 0  else 'ODD' )  





  elif operation == '15' :  #  1️⃣ 5️⃣ . NUM --> Prime ?  
    print()  ;  num = KM.user_input_number((' > '  
    , 'Please enter a positive integer number (Not Zero) to determine if it is Prime OR Not :-' )  
    , int_only = True , positive_negative = '+' , include_zero__zero_message = ( False , '?' )  )  


    result = f'({ num }) ~> ' + ( '\033[92mPrime Number .' if KM.is_prime( num ) else '\033[31mNOT a Prime Number .' )  





  elif operation == '16' :  #  1️⃣ 6️⃣ . Year --> Leap ?  
    print()  ;  year = KM.user_input_number((' > '  
    , 'Please enter the year to determine if it is leap year OR Not :-' )  
    , int_only = True , positive_negative = '+' , include_zero__zero_message = ( False , '?' )  )  


    result = f'({ year }) ~> ' + ( 'Leap Year .' if KM.is_leap( year ) else 'NOT a Leap Year .' )  





  elif operation == '17' :  #  1️⃣ 7️⃣ . Geometric Shapes  
    result = KM.geometric_shapes()  





  elif operation == '18' :  #  1️⃣ 8️⃣ . Units Conversion  
    result = KM.units_conversion()  





  elif operation == '19' :  #  1️⃣ 9️⃣ . Purchase Calculation  
    result = KM.purchase_calculation()  










  print (f'\n\n--->\033[100;1m { result } \033[0m')  



  print ('\n\n     \033[91;1m------------------------------\033[0m \n\n')  
  input ('Press Enter To Continue ... ')                                   
  print ('\n\n     \033[91;1m------------------------------\033[0m \n\n')  





