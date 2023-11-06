$(function () {

    "use strict";

    //===== Prealoder

    $('.preloader').delay(500).fadeOut(500);

    //faq
      const faqs = document.querySelectorAll(".single-faq");
      faqs.forEach((el) => {
        el.querySelector(".faq-btn").addEventListener("click", () => {
          el.querySelector(".icon").classList.toggle("rotate-180");
          el.querySelector(".faq-content").classList.toggle("hidden");
        });
      });
    
    //===== Sticky

    $(window).on('scroll', function (event) {
        var scroll = $(window).scrollTop();
        if (scroll < 20) {
            $(".navbar-area").removeClass("sticky");
            $(".navbar .navbar-brand img").attr("src", "assets/images/logo.svg");
        } else {
            $(".navbar-area").addClass("sticky");
            $(".navbar .navbar-brand img").attr("src", "assets/images/logo-2.svg");
        }
    });

    //===== Navbar
      const navbarToggler = document.getElementById("navbarToggler");
      const navbarCollapse = document.getElementById("navbarCollapse");

      navbarToggler.addEventListener("click", () => {
        navbarCollapse.classList.toggle("hidden");
      });    

    //===== Section Menu Active

    var scrollLink = $('.page-scroll');
    // Active link switching
    $(window).scroll(function () {
        var scrollbarLocation = $(this).scrollTop();

        scrollLink.each(function () {

            var sectionOffset = $(this.hash).offset().top - 73;

            if (sectionOffset <= scrollbarLocation) {
                $(this).parent().addClass('active');
                $(this).parent().siblings().removeClass('active');
            }
        });
    });


    //===== close navbar-collapse when a  clicked

    $(".navbar-nav a").on('click', function () {
        $(".navbar-collapse").removeClass("show");
    });

    $(".navbar-toggler").on('click', function () {
        $(this).toggleClass("active");
        $(".navbar-collapse").toggleClass("show");
    });

    $(".navbar-nav a").on('click', function () {
        $(".navbar-toggler").removeClass('active');
    });    
    
    //===== Back to top

    // Show or hide the sticky footer button
    $(window).on('scroll', function (event) {
        if ($(this).scrollTop() > 600) {
            $('.back-to-top').fadeIn(200);
        } else {
            $('.back-to-top').fadeOut(200);
        }
    });


    //Animate the scroll to yop
    $('.back-to-top').on('click', function (event) {
        event.preventDefault();

        $('html, body').animate({
            scrollTop: 0,
        }, 1500);
    });


    //=====  WOW active

    new WOW().init();

});

const images = document.querySelectorAll('.grid1 > div');
const overlay = document.createElement('div');
overlay.className = 'overlay';

images.forEach((image, index) => {
  const caption = document.createElement('div');
  caption.className = 'caption';
  caption.innerText = getImageCaption(index);

  const link = document.createElement('a');
  link.href = getImageLink(index); // Replace with your function to get links
  link.appendChild(image.querySelector('img').cloneNode(true));
  link.appendChild(overlay.cloneNode());
  link.appendChild(caption);

  image.innerHTML = ''; // Clear the original content of the image container
  image.appendChild(link);

  image.addEventListener('mouseenter', () => {
    caption.style.opacity = '1';
    image.querySelector('.overlay').style.opacity = '1';
  });

  image.addEventListener('mouseleave', () => {
    caption.style.opacity = '0';
    image.querySelector('.overlay').style.opacity = '0';
  });
});

//home images
function getImageCaption(index) {
  const captions = ['Landscape', 'Travel', 'Architecture', 'Nature'];
  return captions[index];
}

function getImageLink(index) {
  const links = ['landscape.html', 'travel.html', 'architecture.html', 'nature.html']; // Replace with actual URLs
  return links[index];
}

// Function to open the popup
function openPopup(imageSrc, title, description) {
  document.getElementById("popupImage").src = imageSrc;
  document.getElementById("popupTitle").textContent = title;
  document.getElementById("popupDescription").textContent = description;
  document.getElementById("overlay").style.display = "block";
  document.getElementById("popupModal").style.display = "block";
}

// Function to close the popup
function closePopup() {
  document.getElementById("overlay").style.display = "none";
  document.getElementById("popupModal").style.display = "none";
}

// dark mode
document.addEventListener('DOMContentLoaded', function () {
  const darkModeToggle = document.getElementById('darkModeToggle');
  const body = document.body;
  const textBlackElements = document.querySelectorAll('.text-black');
  const bgWhiteElements = document.querySelectorAll('.bg-white');
  const darkModeClass = 'dark-mode-active';

  const sunIcon = document.querySelector('.icon.sun');
  const moonIcon = document.querySelector('.icon.moon');

  // Check if dark mode is already set
  if (localStorage.getItem('darkMode') === darkModeClass) {
    document.documentElement.classList.add(darkModeClass);
  }

  // Check if dark mode state is saved in localStorage
  const isDarkMode = localStorage.getItem('darkMode') === 'true';

  // Apply dark mode if it was previously enabled
  if (isDarkMode) {
    body.classList.add('dark-mode');
    textBlackElements.forEach(element => {
      element.classList.add('text-white');
    });
    bgWhiteElements.forEach(element => {
      element.classList.add('bg-black');
    });
  }else{
    sunIcon.style.display = 'none';
  }

  darkModeToggle.addEventListener('click', function () {
    document.documentElement.classList.toggle(darkModeClass);
    body.classList.toggle('dark-mode');

    // Toggle text color for elements with class "text-black"
    textBlackElements.forEach(element => {
      element.classList.toggle('text-white');
    });

    // Save the dark mode state in localStorage
    localStorage.setItem('darkMode', body.classList.contains('dark-mode'));

    // Check if dark mode is already set
    if (localStorage.getItem('darkMode') === 'true') {
      document.documentElement.classList.add(darkModeClass);
      moonIcon.style.display = 'none';
      sunIcon.style.display = 'block';
    } else{
      sunIcon.style.display = 'none';
      moonIcon.style.display = 'block';
    }    
  });
});
