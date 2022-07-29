//animations circle


const buttons = document.querySelectorAll('#services .services__wrapper-icons .icon');
const buttons_hidden = document.querySelectorAll('#services .services__wrapper-icons .icon_hidden');
const circles = document.querySelectorAll('#services .services__wrapper-icons .circle')
const info  = document.querySelectorAll('#services .services__wrapper-icons .icon_hidden .info')
for (let i = 0; i < 4; i++) {
    buttons[i].addEventListener('click', function () {        
        let index = i;
        for (let j = 0; j < 4; j++) {
            if (j == index) {
                buttons[j].style.display = 'none';
                buttons_hidden[j].style.display = 'inline-block';
                info[j].style.display = 'block';
                circles[j].style.display = 'block';

            }
            else {
              circles[j].style.display = 'none';
              buttons_hidden[j].style.display = 'block  ';
                buttons[j].style.display = 'inline-block';
                info[j].style.display = 'none';
            }
        }
    });
}

for (let i = 0; i < 4; i++) {
  circles[i].addEventListener('click', function () {
        let index = i;
        for (let j = 0; j < 4; j++) {
          buttons[j].style.display = 'inline-block';
          buttons_hidden[j].style.display = 'block';
          circles[j].style.display = 'none';
          info[j].style.display = 'none';

      }
    });
}

///бургер меню
let btnBurgerActiv = document.querySelector(".HeaderbtnOpen");
let btnBurgerClose = document.querySelector(".HeaderbtnClose");
let burgerMenu = document.querySelector(".burger-menu");
const burgerItem = document.querySelectorAll(".burger-item");

burgerItem.forEach((item) => {
  item.addEventListener("click", () => {
    activeBurger();
  });
});
document.addEventListener("DOMContentLoaded", function () {
  btnBurgerActiv.addEventListener("click", activeBurger);
});

document.addEventListener("DOMContentLoaded", function () {
  btnBurgerClose.addEventListener("click", activeBurger);
});

const activeBurger = () => {
  burgerMenu.classList.toggle("burger-menu-Active");
  if (btnBurgerClose.classList.contains("btnHeaderActive")) {
    btnBurgerClose.classList.remove("btnHeaderActive");
    btnBurgerActiv.classList.add("btnHeaderActive");
  } else if (btnBurgerActiv.classList.contains("btnHeaderActive")) {
    btnBurgerActiv.classList.remove("btnHeaderActive");
    btnBurgerClose.classList.add("btnHeaderActive");
  } else {
    btnBurgerClose.classList.add("btnHeaderActive");
  }
};

//слайдер отзывы
const prevL = document.querySelector(".feedback_btn-mobL");
const prev = document.querySelector(".feedback__slider-btnPrev");
const nextR = document.querySelector(".feedback_btn-mobR");
const next = document.querySelector(".feedback__slider-btnNext");
const slides = document.querySelectorAll(".feedback__slide");
const dots = document.querySelectorAll(".dot");
let index = 0;

const activeSlideFeedback = (n) => {
  for (let slide of slides) {
    slide.classList.remove("active");
  }
  slides[n].classList.add("active");
};

const activeDotFeedback = (n) => {
  for (let dot of dots) {
    dot.classList.remove("active");
  }
  dots[n].classList.add("active");
};

const prepareCurrentsSlide = (ind) => {
  activeSlideFeedback(ind);
  activeDotFeedback(ind);
};

const nextSlide = () => {
  if (index == slides.length - 1) {
    index = 0;
    prepareCurrentsSlide(index);
  } else {
    index++;
    prepareCurrentsSlide(index);
  }
};

const prevSlide = () => {
  if (index == 0) {
    index = slides.length - 1;
    prepareCurrentsSlide(index);
  } else {
    index--;
    prepareCurrentsSlide(index);
  }
};

dots.forEach((item, indexDot) => {
  item.addEventListener("click", () => {
    index = indexDot;
    prepareCurrentsSlide(index);
  });
});

document.addEventListener("DOMContentLoaded", function () {
  next.addEventListener("click", nextSlide);
  nextR.addEventListener("click", nextSlide);
});
document.addEventListener("DOMContentLoaded", function () {
  prev.addEventListener("click", prevSlide);
  prevL.addEventListener("click", prevSlide);
});

//grid slide
const close = document.querySelector(".slider-lg-btnClose");
const slideClose = document.querySelector(".wrapper-slide-lg");

const activeSlidebtn = () => {
  slideClose.style.display = "none";
};
document.addEventListener("DOMContentLoaded", function () {
  close.addEventListener("click", activeSlidebtn);
});

$(document).ready(function () {
  $(".slider-lg").slick({
    arrows: true,
    fade: true,
    responsive: [
      {
        breakpoint: 1111,
        settings: {
          centerMode: true,
          slidesToShow: 1,
          slidesToScroll: 1,
          initialSlide: 1,
          Infinity: true,
          variableWidth: true,
          fade: false,
        },
      },
      {
        breakpoint: 740,
        settings: {
          centerMode: true,
          slidesToShow: 1,
          slidesToScroll: 1,
          initialSlide: 1,
          Infinity: true,
          variableWidth: true,
          fade: false,
          arrows: false,
          autoplay: true,
        },
      },
      {
        breakpoint: 500,
        settings: {
          centerMode: true,
          slidesToShow: 1,
          slidesToScroll: 1,
          initialSlide: 1,
          Infinity: true,
          variableWidth: true,
          fade: false,
          arrows: false,
          autoplay: true,
        },
      },
      {
        breakpoint: 460,
        settings: {
          centerMode: true,
          slidesToShow: 1,
          slidesToScroll: 1,
          initialSlide: 1,
          Infinity: true,
          variableWidth: true,
          fade: false,
          arrows: false,
          autoplay: true,
        },
      },
      {
        breakpoint: 320,
        settings: {
          centerMode: true,
          slidesToShow: 1,
          slidesToScroll: 1,
          initialSlide: 1,
          Infinity: true,
          variableWidth: true,
          fade: false,
          arrows: false,
          autoplay: true,
        },
      },
    ],
  });
  $("a[data-slide]").click(function (e) {
    e.preventDefault();
    var slideno = $(this).data("slide");
    slideClose.style.display = "flex";
    $(".slider-lg").slick("slickGoTo", slideno - 1);
    $(".slider-lg").slick("setPosition");
  });
});


