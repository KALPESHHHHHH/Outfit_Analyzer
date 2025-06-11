after selectig language getting follwin error 
Page not found (404)
Request Method:	GET
Request URL:	http://127.0.0.1:8000/hi/hi/
Using the URLconf defined in outfit_recommender.urls, Django tried these URL patterns, in this order:

admin/
hi/ [name='home']
hi/ api/
hi/ api/fashion_feedback/ [name='fashion_feedback']
hi/ upload/ [name='upload']
hi/ recommendations/ [name='recommendations']
hi/ recommendations/<int:pk>/ [name='recommendation_detail']
hi/ about/ [name='about']
hi/ api/voice-input/ [name='voice_input']
api/
^media/(?P<path>.*)$
favicon.ico
The current path, hi/hi/, didn’t match any of these.

You’re seeing this error because you have DEBUG = True in your Django settings file. Change that to False, and Django







i want after selecting the languae whole website text should be change based on the selectin of langauge update the following code without affecting any

#base.html
<!DOCTYPE html>
{% load static i18n %}

<html lang="en" data-bs-theme="light">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}{% trans "Outfit Recommender" %}{% endblock %}</title>

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">

    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&family=Playfair+Display:wght@400;500;600;700&display=swap" rel="stylesheet">

    <!-- Load static template tag -->
    {% load static %}

    {% block extra_css %}{% endblock %}
    <style>
        :root {
            --primary: #7c4dff;
            --primary-light: #b47cff;
            --primary-dark: #4a1dcc;
            --secondary: #ff6d00;
            --secondary-light: #ff9e40;
            --accent: #00c853;
            --dark: #1a1a2e;
            --light: #f8f9fa;
            --gray: #e0e0e0;
            --dark-gray: #757575;
            --gradient: linear-gradient(135deg, var(--primary) 0%, var(--primary-light) 100%);
            --card-shadow: 0 10px 20px rgba(0,0,0,0.1);
            --transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
        }

        body {
            font-family: 'Poppins', sans-serif;
            background-color: var(--light);
            color: var(--dark);
            padding-top: 70px;
            transition: background-color 0.3s ease, color 0.3s ease;
        }

        body[data-bs-theme="dark"] {
            background-color: #121212;
            color: #f5f5f5;
        }

        body[data-bs-theme="dark"] .navbar {
            background-color: rgba(26, 26, 46, 0.95);
        }

        body[data-bs-theme="dark"] .sidebar-container {
            background: linear-gradient(135deg, var(--dark) 0%, #2a2a4a 100%);
        }

        /* Navbar Styles */
        .navbar {
            background-color: rgba(5, 5, 5, 0.95);
            box-shadow: 0 2px 15px rgba(0, 0, 0, 0.1);
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            z-index: 1030;
            height: 70px;
            padding: 0.5rem 2rem;
            transition: var(--transition);
            backdrop-filter: blur(10px);
        }

        .navbar-brand {
            font-family: 'Playfair Display', serif;
            font-weight: 700;
            font-size: 1.5rem;
            color: var(--primary) !important;
            display: flex;
            align-items: center;
            transition: var(--transition);
        }

        .navbar-brand:hover {
            color: var(--primary-dark) !important;
        }

        .navbar-brand i {
            margin-right: 10px;
            font-size: 1.4rem;
        }

        /* Sidebar Styles */
        .sidebar-container {
            position: fixed;
            top: 0;
            left: 0;
            height: 100vh;
            width: 280px;
            background: var(--gradient);
            box-shadow: 5px 0 25px rgba(0, 0, 0, 0.1);
            overflow-y: auto;
            transition: transform 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            z-index: 1040;
            transform: translateX(-100%);
        }

        .sidebar-container.show {
            transform: translateX(0);
        }

        .sidebar-header {
            background-color: rgba(0,0,0,0.1);
            color: #fff;
            padding: 1.5rem 1.5rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
            border-bottom: 1px solid rgba(255,255,255,0.1);
            height: 70px;
        }

        .sidebar-header h3 {
            font-family: 'Playfair Display', serif;
            font-weight: 700;
            margin: 0;
            color: black;
            font-size: 1.5rem;
        }

        .sidebar-menu {
            list-style: none;
            padding: 1.5rem 0;
            margin: 0;
        }

        .sidebar-menu li a {
            display: flex;
            align-items: center;
            padding: 1rem 1.5rem;
            color: rgba(5, 5, 5, 0.9);
            text-decoration: none;
            transition: var(--transition);
            border-left: 4px solid transparent;
            font-weight: 500;
            margin: 0.25rem 1rem;
            border-radius: 8px;
        }

        .sidebar-menu li a:hover {
            background-color: rgba(255,255,255,0.15);
            color: #fff;
            border-left: 4px solid #fff;
            transform: translateX(5px);
        }

        .sidebar-menu li.active a {
            background-color: rgba(255,255,255,0.2);
            color: #fff;
            border-left: 4px solid #fff;
        }

        .sidebar-menu li a i {
            margin-right: 15px;
            width: 20px;
            text-align: center;
            font-size: 1.2rem;
        }

        /* Toggle Button Styles */
        .sidebar-toggle {
            background: var(--gradient);
            border: none;
            color: white;
            width: 45px;
            height: 45px;
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: var(--transition);
            box-shadow: var(--card-shadow);
            margin-right: 1rem;
        }

        .sidebar-toggle:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 15px rgba(0, 0, 0, 0.2);
        }

        /* Close Button Styles */
        .btn-close-sidebar {
            background: none;
            border: none;
            color: white;
            font-size: 1.5rem;
            opacity: 0.7;
            transition: var(--transition);
            width: 40px;
            height: 40px;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 50%;
        }

        .btn-close-sidebar:hover {
            opacity: 1;
            background-color: rgba(255,255,255,0.1);
            transform: rotate(90deg);
        }

        /* Overlay Styles */
        .sidebar-overlay {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background-color: rgba(0,0,0,0.5);
            z-index: 1035;
            opacity: 0;
            visibility: hidden;
            transition: opacity 0.3s ease, visibility 0.3s ease;
            backdrop-filter: blur(5px);
        }

        .sidebar-overlay.show {
            opacity: 1;
            visibility: visible;
        }

        /* Main Content Area */
        .main-content {
            transition: margin-left 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            min-height: calc(100vh - 70px);
        }

        .content-container {
            padding: 2.5rem 2rem;
            animation: fadeIn 0.5s ease-in-out;
        }

        /* Card Styles */
        .card {
            border: none;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: var(--card-shadow);
            transition: var(--transition);
            margin-bottom: 1.5rem;
        }

        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 30px rgba(0,0,0,0.15);
        }

        .card-img-top {
            height: 200px;
            object-fit: cover;
        }

        .card-body {
            padding: 1.5rem;
        }

        .card-title {
            font-family: 'Playfair Display', serif;
            font-weight: 600;
            margin-bottom: 0.75rem;
        }

        /* Buttons */
        .btn-primary {
            background-color: var(--primary);
            border-color: var(--primary);
            padding: 0.5rem 1.5rem;
            border-radius: 8px;
            font-weight: 500;
            transition: var(--transition);
        }

        .btn-primary:hover {
            background-color: var(--primary-dark);
            border-color: var(--primary-dark);
            transform: translateY(-2px);
        }

        .btn-outline-primary {
            color: var(--primary);
            border-color: var(--primary);
            padding: 0.5rem 1.5rem;
            border-radius: 8px;
            font-weight: 500;
            transition: var(--transition);
        }

        .btn-outline-primary:hover {
            background-color: var(--primary);
            border-color: var(--primary);
            transform: translateY(-2px);
        }

        /* Footer Styles */
        .footer {
            background-color: var(--dark);
            color: white;
            padding: 3rem 0;
            margin-top: 3rem;
        }

        .footer h5 {
            font-family: 'Playfair Display', serif;
            font-weight: 600;
            margin-bottom: 1.5rem;
            color: white;
        }

        .footer a {
            color: rgba(255,255,255,0.7);
            text-decoration: none;
            transition: var(--transition);
        }

        .footer a:hover {
            color: white;
            transform: translateX(3px);
        }

        .footer .social-icons a {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 40px;
            height: 40px;
            border-radius: 50%;
            background-color: rgba(255,255,255,0.1);
            margin-right: 10px;
            transition: var(--transition);
        }

        .footer .social-icons a:hover {
            background-color: var(--primary);
            transform: translateY(-3px);
        }

        /* Theme Switch */
        .theme-switch {
            padding: 1.5rem;
            display: flex;
            align-items: center;
        }

        .theme-switch label {
            display: flex;
            align-items: center;
            cursor: pointer;
            color: rgba(255,255,255,0.9);
            font-weight: 500;
        }

        .theme-switch i {
            margin-right: 10px;
            font-size: 1.1rem;
        }

        /* Animations */
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        @keyframes slideIn {
            from { transform: translateX(-100%); }
            to { transform: translateX(0); }
        }

        @keyframes slideOut {
            from { transform: translateX(0); }
            to { transform: translateX(-100%); }
        }

        /* Utility Classes */
        .rounded-xl {
            border-radius: 12px;
        }

        .shadow-soft {
            box-shadow: 0 5px 15px rgba(0,0,0,0.08);
        }

        /* Hero Section */
        .hero-section {
            background: var(--gradient);
            color: white;
            padding: 5rem 0;
            border-radius: 0 0 20px 20px;
            margin-bottom: 3rem;
            position: relative;
            overflow: hidden;
        }

        .hero-section::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background-image: url('{% static 'images/autumn-leaves-composition.jpg' %}');
            opacity: 0.1;
        }

        .hero-title {
            font-family: 'Playfair Display', serif;
            font-weight: 700;
            font-size: 3rem;
            margin-bottom: 1.5rem;
        }

        .hero-subtitle {
            font-size: 1.25rem;
            opacity: 0.9;
            margin-bottom: 2rem;
            max-width: 600px;
        }

        /* Feature Icons */
        .feature-icon {
            width: 60px;
            height: 60px;
            background-color: rgba(255,255,255,0.2);
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.5rem;
            color: white;
            margin-bottom: 1.5rem;
            transition: var(--transition);
        }

        .feature-card:hover .feature-icon {
            background-color: white;
            color: var(--primary);
            transform: rotate(10deg) scale(1.1);
        }

        /* Responsive Adjustments */
        @media (max-width: 768px) {
            .hero-title {
                font-size: 2.2rem;
            }

            .content-container {
                padding: 1.5rem 1rem;
            }

            .navbar {
                padding: 0.5rem 1rem;
            }
        }

        /* Background Image for Pages */
        {% block background_image %}
        body {
            background-image: url('{% static 'images/fashion-bg.jpg' %}');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            background-repeat: no-repeat;
        }

        body::before {
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background-color: rgba(255,255,255,0.9);
            z-index: -1;
        }

        body[data-bs-theme="dark"]::before {
            background-color: rgba(0,0,0,0.85);
        }
        {% endblock %}
    </style>
</head>
<body>
    <!-- Sidebar -->
    <div class="sidebar-container" id="sidebarContainer">
        <div class="sidebar">
            <div class="sidebar-header">
                <h3>{% trans "StyleAI" %}</h3>
                <button class="btn-close-sidebar" id="closeSidebar">
                    <i class="fas fa-times"></i>
                </button>
            </div>
            <ul class="sidebar-menu">
                <li class="{% if request.path == '/' %}active{% endif %}">
                    <a href="{% url 'core:home' %}">
                        <i class="fas fa-home"></i>
                        <span>{% trans "Home" %}</span>
                    </a>
                </li>
                <li class="{% if '/upload/' in request.path %}active{% endif %}">
                    <a href="{% url 'core:upload' %}">
                        <i class="fas fa-cloud-upload-alt"></i>
                        <span>{% trans "Upload" %}</span>
                    </a>
                </li>
                <li class="{% if '/recommendations/' in request.path %}active{% endif %}">
                    <a href="{% url 'core:recommendations' %}">
                        <i class="fas fa-tshirt"></i>
                        <span>{% trans "Recommendations" %}</span>
                    </a>
                </li>
                <li class="{% if '/about/' in request.path %}active{% endif %}">
                    <a href="{% url 'core:about' %}">
                        <i class="fas fa-info-circle"></i>
                        <span>{% trans "About Us" %}</span>
                    </a>
                </li>
            </ul>
            <div class="sidebar-footer" style="margin-left: 20px; margin-bottom: 30px;">
                <div class="form-check form-switch theme-switch d-flex align-items-center">
                    <input class="form-check-input" type="checkbox" id="themeSwitch">
                    <label class="form-check-label d-flex align-items-center ms-2" for="themeSwitch">
                        <i class="fas fa-moon me-2"></i>
                        <span>{% trans "Dark Mode" %}</span>
                    </label>
                </div>
            </div>
        </div>
    </div>

    <!-- Overlay for mobile -->
    <div class="sidebar-overlay" id="sidebarOverlay"></div>

    <!-- Main Content -->
    <div class="main-content" id="mainContent">
        <!-- Top Navigation -->
        <nav class="navbar navbar-expand-lg navbar-light">
            <div class="container-fluid">
                <button class="sidebar-toggle" id="sidebarToggle">
                    <i class="fas fa-bars"></i>
                </button>
                <a class="navbar-brand" href="{% url 'core:home' %}">
                    <i class="fas fa-tshirt"></i>
                    {% trans "StyleAI" %}
                </a>
                <!-- Language Selection Dropdown -->
                <div class="dropdown">
                    <button class="btn btn-secondary dropdown-toggle" type="button" id="languageDropdown" data-bs-toggle="dropdown" aria-expanded="false">
                        <i class="fas fa-language"></i> {% trans "Language" %}
                    </button>
                    <ul class="dropdown-menu" aria-labelledby="languageDropdown">
                        <li><a class="dropdown-item" href="{% url 'core:home' %}" data-language="en">English</a></li>
                        <li><a class="dropdown-item" href="{% url 'core:home' %}" data-language="hi">Hindi</a></li>
                        <li><a class="dropdown-item" href="{% url 'core:home' %}" data-language="gu">Gujarati</a></li>
                        <li><a class="dropdown-item" href="{% url 'core:home' %}" data-language="bn">Bengali</a></li>
                        <li><a class="dropdown-item" href="{% url 'core:home' %}" data-language="mr">Marathi</a></li>
                        <li><a class="dropdown-item" href="{% url 'core:home' %}" data-language="kn">Kannada</a></li>
                        <li><a class="dropdown-item" href="{% url 'core:home' %}" data-language="te">Telugu</a></li>
                        <li><a class="dropdown-item" href="{% url 'core:home' %}" data-language="ta">Tamil</a></li>
                        <li><a class="dropdown-item" href="{% url 'core:home' %}" data-language="ur">Urdu</a></li>
                        <li><a class="dropdown-item" href="{% url 'core:home' %}" data-language="or">Odia</a></li>
                        <li><a class="dropdown-item" href="{% url 'core:home' %}" data-language="ml">Malayalam</a></li>
                        <li><a class="dropdown-item" href="{% url 'core:home' %}" data-language="pa">Punjabi</a></li>
                    </ul>
                </div>
                <!-- Voice Assistant Button -->
                <button class="btn btn-primary" id="voiceAssistantBtn">
                  <i class="fas fa-microphone"></i> {% trans "Voice Assistant" %}
                </button>
            </div>
        </nav>

        <!-- Messages -->
        {% if messages %}
        <div class="container mt-3 content-container">
            {% for message in messages %}
            <div class="alert alert-{{ message.tags }} alert-dismissible fade show" role="alert">
                <i class="fas {% if message.tags == 'success' %}fa-check-circle{% elif message.tags == 'error' %}fa-exclamation-circle{% else %}fa-info-circle{% endif %} me-2"></i>
                {{ message }}
                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
            </div>
            {% endfor %}
        </div>
        {% endif %}

        <!-- Content -->
        <div class="container-fluid content-container">
            {% block content %}{% endblock %}
        </div>

        <!-- Footer -->
        <footer class="footer">
            <div class="container">
                <div class="row">
                    <div class="col-lg-4 mb-4 mb-lg-0">
                        <h5>{% trans "StyleAI" %}</h5>
                        <p class="text-muted">{% trans "AI-powered outfit recommendations to help you look your best every day." %}</p>
                        <div class="social-icons mt-3">
                            <a href="#" class="btn btn-sm btn-outline-light me-2"><i class="fab fa-instagram"></i></a>
                            <a href="#" class="btn btn-sm btn-outline-light me-2"><i class="fab fa-twitter"></i></a>
                            <a href="#" class="btn btn-sm btn-outline-light me-2"><i class="fab fa-facebook-f"></i></a>
                            <a href="#" class="btn btn-sm btn-outline-light"><i class="fab fa-linkedin-in"></i></a>
                        </div>
                    </div>
                    <div class="col-lg-2 col-md-6 mb-4 mb-md-0">
                        <h5>{% trans "Quick Links" %}</h5>
                        <ul class="list-unstyled">
                            <li class="mb-2"><a href="{% url 'core:home' %}">{% trans "Home" %}</a></li>
                            <li class="mb-2"><a href="{% url 'core:upload' %}">{% trans "Upload" %}</a></li>
                            <li class="mb-2"><a href="{% url 'core:recommendations' %}">{% trans "Recommendations" %}</a></li>
                            <li class="mb-2"><a href="{% url 'core:about' %}">{% trans "About Us" %}</a></li>
                        </ul>
                    </div>
                    <div class="col-lg-2 col-md-6 mb-4 mb-md-0">
                        <h5>{% trans "Support" %}</h5>
                        <ul class="list-unstyled">
                            <li class="mb-2"><a href="#">{% trans "FAQ" %}</a></li>
                            <li class="mb-2"><a href="#">{% trans "Contact" %}</a></li>
                            <li class="mb-2"><a href="#">{% trans "Feedback" %}</a></li>
                        </ul>
                    </div>
                    <div class="col-lg-4">
                        <h5>{% trans "Newsletter" %}</h5>
                        <p class="text-muted">{% trans "Subscribe to get updates on new features and fashion tips." %}</p>
                        <div class="input-group mb-3">
                            <input type="email" class="form-control" placeholder="{% trans 'Your email' %}" aria-label="{% trans 'Your email' %}">
                            <button class="btn btn-primary" type="button">{% trans "Subscribe" %}</button>
                        </div>
                    </div>
                </div>
                <hr class="my-4 bg-secondary">
                <div class="row">
                    <div class="col-md-6 text-center text-md-start">
                        <p class="mb-0 text-muted">&copy; {% now "Y" %} {% trans "StyleAI. All rights reserved." %}</p>
                    </div>
                    <div class="col-md-6 text-center text-md-end">
                        <p class="mb-0 text-muted">
                            <a href="#" class="text-decoration-none me-3">{% trans "Privacy Policy" %}</a>
                            <a href="#" class="text-decoration-none">{% trans "Terms of Service" %}</a>
                        </p>
                    </div>
                </div>
            </div>
        </footer>
    </div>

    <!-- Bootstrap JS Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>

    <!-- Custom JS -->
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const sidebarContainer = document.getElementById('sidebarContainer');
            const sidebarToggle = document.getElementById('sidebarToggle');
            const closeSidebar = document.getElementById('closeSidebar');
            const sidebarOverlay = document.getElementById('sidebarOverlay');

            // Toggle sidebar function
            function toggleSidebar() {
                sidebarContainer.classList.toggle('show');
                sidebarOverlay.classList.toggle('show');

                // Prevent scrolling when sidebar is open on mobile
                if (sidebarContainer.classList.contains('show')) {
                    document.body.style.overflow = 'hidden';
                } else {
                    document.body.style.overflow = '';
                }
            }

            // Toggle sidebar when button is clicked
            sidebarToggle.addEventListener('click', function(e) {
                e.preventDefault();
                e.stopPropagation();
                toggleSidebar();
            });

            // Close sidebar when close button is clicked
            closeSidebar.addEventListener('click', function(e) {
                e.preventDefault();
                sidebarContainer.classList.remove('show');
                sidebarOverlay.classList.remove('show');
                document.body.style.overflow = '';
            });

            // Close sidebar when overlay is clicked
            sidebarOverlay.addEventListener('click', function() {
                sidebarContainer.classList.remove('show');
                sidebarOverlay.classList.remove('show');
                document.body.style.overflow = '';
            });

            // Close sidebar when clicking outside on mobile
            document.addEventListener('click', function(e) {
                if (window.innerWidth < 992 &&
                    !sidebarContainer.contains(e.target) &&
                    e.target !== sidebarToggle) {
                    sidebarContainer.classList.remove('show');
                    sidebarOverlay.classList.remove('show');
                    document.body.style.overflow = '';
                }
            });

            // Theme switcher functionality
            const themeSwitch = document.getElementById('themeSwitch');

            // Check for saved theme preference
            if (localStorage.getItem('theme') === 'dark') {
                document.documentElement.setAttribute('data-bs-theme', 'dark');
                themeSwitch.checked = true;
            }

            // Handle theme switch change
            themeSwitch.addEventListener('change', function() {
                if (this.checked) {
                    document.documentElement.setAttribute('data-bs-theme', 'dark');
                    localStorage.setItem('theme', 'dark');
                } else {
                    document.documentElement.setAttribute('data-bs-theme', 'light');
                    localStorage.setItem('theme', 'light');
                }
            });

            // Handle window resize
            function handleResize() {
                if (window.innerWidth >= 992) {
                    // Desktop view - ensure sidebar is hidden
                    sidebarContainer.classList.remove('show');
                    sidebarOverlay.classList.remove('show');
                    document.body.style.overflow = '';
                }
            }

            window.addEventListener('resize', handleResize);

            // Language selection dropdown
            document.querySelectorAll('[data-language]').forEach(item => {
              item.addEventListener('click', function(e) {
                e.preventDefault();
                const language = this.getAttribute('data-language');
                localStorage.setItem('language', language);
                // Change the language of the UI
                window.location.href = `/${language}${window.location.pathname}`;
              });
            });

            // Voice assistant button
            const voiceAssistantBtn = document.getElementById('voiceAssistantBtn');

            voiceAssistantBtn.addEventListener('click', function() {
              const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
              recognition.lang = localStorage.getItem('language') || 'en-US';

              recognition.onresult = function(event) {
                const transcript = event.results[0][0].transcript;
                // Handle the voice input, e.g., navigate to a page or perform an action
                console.log('Voice input:', transcript);
              };

              recognition.start();
            });
        });
    </script>

    {% block extra_js %}{% endblock %}
</body>
</html>








#views.py


from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from django.conf import settings
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import OutfitUpload, OutfitRecommendation
from .serializers import OutfitUploadSerializer, OutfitRecommendationSerializer
from .forms import OutfitUploadForm
from .gemini_ai import analyze_outfit
import os
import json

class OutfitUploadViewSet(viewsets.ModelViewSet):
    queryset = OutfitUpload.objects.all()
    serializer_class = OutfitUploadSerializer

class OutfitRecommendationViewSet(viewsets.ModelViewSet):
    queryset = OutfitRecommendation.objects.all()
    serializer_class = OutfitRecommendationSerializer

@api_view(['POST'])
def fashion_feedback(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            question = data.get('question', "Is outfit looking good on me?")
            image_url = data.get('image_path')
            image_path = os.path.join(settings.MEDIA_ROOT, image_url.split('/media/')[-1])
            result = analyze_outfit(image_path, user_prompt=question)
            return Response({
                "direct_response": result.get("direct_response", ""),
                "looks_good": result.get('score', 0) >= 70,
                "percentage_score": result.get('score', 0),
                "explanation": result.get('score_explanation', ""),
                "strengths": result.get('strengths', []),
                "improvements": result.get('improvements', []),
                "alternative_outfits": result.get('alternative_outfits', []),
                "personalized_suggestions": result.get('personalized_suggestions', []),
                "response": result.get('response', ""),
                "suggestions": result.get('suggestions', ""),
                "instagram_analysis": result.get('instagram_analysis', {})
            })
        except Exception as e:
            return Response({"error": f"Failed to analyze: {str(e)}"}, status=500)
    return Response({"error": "Invalid request"}, status=400)

def home(request):
    return render(request, 'core/home.html')

def upload(request):
    if request.method == 'POST':
        form = OutfitUploadForm(request.POST, request.FILES)
        if form.is_valid():
            outfit = form.save()
            try:
                image_path = os.path.join(settings.MEDIA_ROOT, outfit.image.name)
                analysis = analyze_outfit(image_path, user_prompt="Is outfit looking good on me?")
                recommendation = OutfitRecommendation(
                    outfit=outfit,
                    looks_good=analysis.get('score', 0) >= 70,
                    percentage_score=analysis.get('score', 0),
                    explanation=analysis.get('score_explanation', "")
                )
                recommendation.set_feedback_json({
                    'strengths': analysis.get('strengths', []),
                    'improvements': analysis.get('improvements', [])
                })
                recommendation.set_suggestions_json({
                    'alternative_outfits': analysis.get('alternative_outfits', []),
                    'personalized_suggestions': analysis.get('personalized_suggestions', [])
                })
                recommendation.save()
                return redirect('core:recommendation_detail', pk=outfit.id)
            except Exception as e:
                messages.error(request, f"Error analyzing outfit: {str(e)}")
                return redirect('core:upload')
    else:
        form = OutfitUploadForm()
    return render(request, 'core/upload.html', {'form': form})

def recommendations(request):
    outfits = OutfitUpload.objects.filter(recommendation__isnull=False).order_by('-uploaded_at')
    return render(request, 'core/recommendations.html', {'outfits': outfits})

def recommendation_detail(request, pk):
    outfit = get_object_or_404(OutfitUpload, pk=pk)
    if not hasattr(outfit, 'recommendation'):
        messages.error(request, "No recommendation found for this outfit.")
        return redirect('upload')
    recommendation = outfit.recommendation
    feedback = recommendation.get_feedback_json()
    suggestions = recommendation.get_suggestions_json()
    context = {
        'outfit': outfit,
        'recommendation': recommendation,
        'strengths': feedback.get('strengths', []),
        'improvements': feedback.get('improvements', []),
        'alternative_outfits': suggestions.get('alternative_outfits', []),
        'personalized_suggestions': suggestions.get('personalized_suggestions', []),
        'percentage_score': recommendation.percentage_score,
        'explanation': recommendation.explanation
    }
    return render(request, 'core/recommendation_detail.html', context)

def about(request):
    return render(request, 'core/about.html')



# views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def voice_input(request):
    if request.method == 'POST':
        transcript = request.data.get('transcript', '')
        # Process the voice input and return a response
        response = {'message': f'You said: {transcript}'}
        return Response(response)
    return Response({'error': 'Invalid request'}, status=400)

#middleware.py

# core/middleware.py
from django.utils import translation
from django.conf import settings

class LanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get language from session, or use default from settings
        language = request.session.get('language', settings.LANGUAGE_CODE)
        translation.activate(language)
        request.LANGUAGE_CODE = translation.get_language()
        
        response = self.get_response(request)
        
        # Set language in response header
        if hasattr(response, 'set_cookie'):
            response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
        
        translation.deactivate()
        return response