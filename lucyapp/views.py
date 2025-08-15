from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    """
    View for the home page
    """
    return render(request, 'lucyapp/home.html')

def about(request):
    """
    View for the about page
    """
    return render(request, 'lucyapp/about.html')

def contact(request):
    """
    View for the contact page with form handling
    """
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')
        
        try:
            # Send email
            subject = f"Portfolio Contact from {name}"
            email_body = f"""
            New contact form submission:
            
            Name: {name}
            Email: {email}
            Message:
            {message}
            """
            
            send_mail(
                subject,
                email_body,
                email,  # From email
                [settings.DEFAULT_FROM_EMAIL],  # To email
                fail_silently=False,
            )
            
            messages.success(request, "Thank you for your message! I'll get back to you soon.")
            return redirect('contact')
            
        except Exception as e:
            messages.error(request, "Sorry, there was an error sending your message. Please try again later.")
            return render(request, 'lucyapp/contact.html', {
                'name': name,
                'email': email,
                'message': message,
            })
    
    return render(request, 'lucyapp/contact.html')
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')