{% load static %}
<!-- Navbar -->
<nav class="navbar navbar-expand-lg navbar-dark bg-primary sticky-top">
    <div class="container">
      <a class="navbar-brand" href="{% url 'index' %}">
        <img src="{% static 'img/logo.png' %}" class="logo" alt="">
      </a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
        <ul class="navbar-nav">
          <li
            {% if '/' == request.path %}
              class="nav-item active mr-3"
            {% else %}
              class="nav-item mr-3"
            {% endif %}
          >
            <a class="nav-link" href="{% url 'index' %}">Home</a>
          </li>
          <li
            {% if 'about' in request.path %}
              class="nav-item active mr-3"
            {% else %}
              class="nav-item mr-3"
            {% endif %}
          >
            <a class="nav-link" href="{% url 'about' %}">About</a>
          </li>
          <li
            {% if 'listings' in request.path %}
              class="nav-item active mr-3"
            {% else %}
              class="nav-item mr-3"
            {% endif %}
          >
            <a class="nav-link" href="{% url 'listings' %}">Featured Listings</a>
          </li>
        </ul>

        <ul class="navbar-nav ml-auto">
          {% if user.is_authenticated %}
            <li
            {% if 'dashboard' in request.path %} class="nav-item active mr-3"
            {% else %} class="nav-item mr-3"
            {% endif %}>
            
              <a class="nav-link" href="{% url 'dashboard' %}">
               Welcome {{ user.username }} (Dashboard)</a>
            </li>
            <li class="nav-item mr-3">
              <a href="javascript:{document.getElementById('logout').submit()}" class="nav-link">
                <i class="fas fa-sign-out-alt"></i> Logout
              </a>
              <form action="{% url 'logout' %}" method="POST" id="logout">
                {% csrf_token %}
                <input type="hidden">
              </form>
            </li>
          {% else %}
            <li
            {% if 'register' in request.path %}
              class="nav-item active mr-3"
            {% else %}
              class="nav-item mr-3"
            {% endif %}
            >
              <a class="nav-link" href="{% url 'register' %}">
                <i class="fas fa-user-plus"></i> Register</a>
            </li>
            <li
            {% if 'login' in request.path %}
              class="nav-item active mr-3"
            {% else %}
              class="nav-item mr-3"
            {% endif %}
            >
              <a class="nav-link" href="{% url 'login' %}">
                <i class="fas fa-sign-in-alt"></i>

                Login</a>
            </li>
          {% endif %}
        </ul>
      </div>
    </div>
  </nav>
