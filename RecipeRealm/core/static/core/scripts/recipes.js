searchForm = document.querySelector('.search-form');

document.querySelector('#search-btn').onclick = () =>{
    searchForm.classList.toggle('active');
}

window.onscroll = () =>{ 
    
    searchForm.classList.remove('active');

    if(window.scrollY > 80){
        document.querySelector('.header .header-2').classList.add('active');
    }else{
        document.querySelector('.header .header-2').classList.remove('active');
    }

}
window.onload = () =>{

    if(window.scrollY > 80){
        document.querySelector('.header .header-2').classList.add('active');
    }else{
        document.querySelector('.header .header-2').classList.remove('active');
    }
}

var swiper = new Swiper(".books-slider", {
    loop:true,
    centeredSldes: true,
    autoplay:{
        delay:9500,
        disableOnInteraction: false,
    },
    breakpoints: {
      0: {
        slidesPerView: 1,
      },
      768: {
        slidesPerView: 2,
      },
      1024: {
        slidesPerView: 3,
      },
    },
  });

  var swiper = new Swiper(".popular-slider", {
    spaceBetween:10,
    loop:true,
    centeredSldes: true,
    autoplay:{
        delay:9500,
        disableOnInteraction: false,
    },
    breakpoints: {
      0: {
        slidesPerView: 1,
      },
      768: {
        slidesPerView: 2,
      },
      1024: {
        slidesPerView: 3,
      },
    },
  });
  
//dark theme
  const body = document.querySelector("body");
  const toggle = document.querySelector("#toggle");
  const sunIcon = document.querySelector(".toggle .bxs-sun");
  const moonIcon = document.querySelector(".toggle .bx-moon");
  
  toggle.addEventListener("change", () => {
  
      body.classList.toggle("dark");
      sunIcon.className = sunIcon.className == "bx bxs-sun" ? "bx bx-sun" : "bx bxs-sun";
      moonIcon.className = moonIcon.className == "bx bxs-moon" ? "bx bx-moon" : "bx bxs-moon";
  
  
  });
