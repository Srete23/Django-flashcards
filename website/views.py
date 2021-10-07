from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {})

def add(request):
    from random import randint
    
    num_1 = randint(0, 10)
    num_2 = randint(0, 10)
    if request.method == "POST":
        answer = request.POST['answer']
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']
        
         # Error handling if no answer is entered in Form
        if not answer.isnumeric():
            my_answer = "ERROR - No valid answer was entered! - Try again! "
            color = 'warning'
            return render(request, 'add.html', {
            'my_answer':my_answer,
            'answer' :answer,
            'num_1' :num_1,
            'num_2' :num_2,
            'color' :color,
            })
        
        
        
        correct_answer = int(old_num_1) + int(old_num_2)
        if int(answer) == correct_answer:
            my_answer = "Correct!  " + old_num_1 + " + " + old_num_2 + " = " + answer
            color = "success"
        else:
            my_answer = "Incorrect!  " + old_num_1 + " + " + old_num_2 + " is not " + answer + " it is " + str(correct_answer)  
            color = "danger"
        
        
        
        return render(request , 'add.html', {
            'answer' :answer,
            'my_answer' :my_answer,
            'num_1' :num_1,
            'num_2' :num_2,
            'color' :color,
            })
    
        
    return render(request, 'add.html', {
        'num_1' :num_1,
        'num_2' :num_2,
    })

def subtract(request):
    from random import randint
    
    num_1 = randint(0, 10)
    num_2 = randint(0, 10)
    if request.method == "POST":
        answer = request.POST['answer']
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']
        
         # Error handling if no answer is entered in Form
        if not answer:
            my_answer = "ERROR - No valid answer was entered! - Try again! "
            color = 'warning'
            return render(request, 'subtract.html', {
            'my_answer':my_answer,
            'answer' :answer,
            'num_1' :num_1,
            'num_2' :num_2,
            'color' :color,
            })
        
        correct_answer = int(old_num_1) - int(old_num_2)
        if int(answer) == correct_answer:
            my_answer = "Correct!  " + old_num_1 + " - " + old_num_2 + " = " + answer
            color = "success"
        else:
            my_answer = "Incorrect!  " + old_num_1 + " - " + old_num_2 + " is not " + answer + " it is " + str(correct_answer)  
            color = "danger"
        
        
        
        return render(request , 'subtract.html', {
            'answer' :answer,
            'my_answer' :my_answer,
            'num_1' :num_1,
            'num_2' :num_2,
            'color' :color,
            })
    
        
    return render(request, 'subtract.html', {
        'num_1' :num_1,
        'num_2' :num_2,
    })
    
    return render(request, 'subtract.html', {})

def multiply(request):
    from random import randint
    
    num_1 = randint(0, 10)
    num_2 = randint(0, 10)
    if request.method == "POST":
        answer = request.POST['answer']
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']
        
         # Error handling if no answer is entered in Form
        if not answer.isnumeric():
            my_answer = "ERROR - No valid answer was entered! - Try again! "
            color = 'warning'
            return render(request, 'multiply.html', {
            'my_answer':my_answer,
            'answer' :answer,
            'num_1' :num_1,
            'num_2' :num_2,
            'color' :color,
            })
        
        correct_answer = int(old_num_1) * int(old_num_2)
        if int(answer) == correct_answer:
            my_answer = "Correct!  " + old_num_1 + " X " + old_num_2 + " = " + answer
            color = "success"
        else:
            my_answer = "Incorrect!  " + old_num_1 + " X " + old_num_2 + " is not " + answer + " it is " + str(correct_answer)  
            color = "danger"
        
        
        
        return render(request , 'multiply.html', {
            'answer' :answer,
            'my_answer' :my_answer,
            'num_1' :num_1,
            'num_2' :num_2,
            'color' :color,
            })
    
        
    return render(request, 'multiply.html', {
        'num_1' :num_1,
        'num_2' :num_2,
    })
    
    return render(request, 'multiply.html', {})

def divide(request):
    from random import randint
    
    num_1 = randint(1, 10)
    num_2 = randint(1, 10)
    if request.method == "POST":
        answer = request.POST['answer']
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']
        
        # Error handling if no answer is entered in Form
        if not answer.isnumeric():
            my_answer = "ERROR - No valid answer was entered! - Try again! "
            color = 'warning'
            return render(request, 'divide.html', {
            'my_answer':my_answer,
            'answer' :answer,
            'num_1' :num_1,
            'num_2' :num_2,
            'color' :color,
            })
        
        correct_answer = int(old_num_1) / int(old_num_2)
        if float(answer) == correct_answer:
            my_answer = "Correct!  " + old_num_1 + " / " + old_num_2 + " = " + answer
            color = "success"
        else:
            my_answer = "Incorrect!  " + old_num_1 + " / " + old_num_2 + " is not " + answer + " it is " + str(correct_answer)  
            color = "danger"
        
        
        
        return render(request , 'divide.html', {
            'answer' :answer,
            'my_answer' :my_answer,
            'num_1' :num_1,
            'num_2' :num_2,
            'color' :color,
            })
    
        
    return render(request, 'divide.html', {
        'num_1' :num_1,
        'num_2' :num_2,
    })

# Elements page
def elements(request):
    from random import randint
    
    num_1 = randint(1001, 1118)
    num_2 = randint(1001, 1118)
    if request.method == "POST":
        answer = request.POST['answer']
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']
        
         # Error handling if no answer is entered in Form
        if not answer:
            my_answer = "ERROR - No sums was entered! "
            color = 'warning'
            return render(request, 'elements.html', {
            'my_answer':my_answer,
            'answer' :answer,
            'num_1' :num_1,
            'num_2' :num_2,
            'color' :color,
            })
        
        
        old_num_int_1 = int(old_num_1) - 1000
        old_num_int_2 = int(old_num_2) - 1000
        correct_answer = old_num_int_1 + old_num_int_2
        if int(answer) == (correct_answer):
            my_answer = "Correct!  " + str(old_num_int_1) + " + " + str(old_num_int_2) + " = " + answer
            color = "success"
        else:
            my_answer = "Incorrect!  " + str(old_num_int_1) + " + " + str(old_num_int_2) + " is not " + answer + " it is " + str(correct_answer)  
            color = "danger"
        
        
        
        return render(request , 'elements.html', {
            'answer' :answer,
            'my_answer' :my_answer,
            'num_1' :num_1,
            'num_2' :num_2,
            'color' :color,
            })
    
        
    return render(request, 'elements.html', {
        'num_1' :num_1,
        'num_2' :num_2,
    })
