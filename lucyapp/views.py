from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    """View for the home page"""
    return render(request, 'home.html')

def about(request):
    """View for the about page"""
    return render(request, 'about.html')

def contact(request):
    """View for the contact page with form handling"""
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        message_text = request.POST.get('message', '')
        
        try:
            # Send email
            subject = f"Portfolio Contact from {name}"
            email_body = f"""
New contact form submission:

Name: {name}
Email: {email}

Message:
{message_text}
"""
            
            send_mail(
                subject,
                email_body,
                settings.EMAIL_HOST_USER,  # From email
                ['ainembabaziliciarachel02@gmail.com'],  # Your email
                fail_silently=False,
            )
            
            messages.success(request, "Thank you for your message! I'll get back to you soon.")
            return redirect('home')
            
        except Exception as e:
            print(f"Email error: {str(e)}")  # This will show in your terminal
            messages.error(request, f"Sorry, there was an error sending your message. Please try again later.")
            return redirect('home')
    
    return redirect('home')