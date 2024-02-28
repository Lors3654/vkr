<template>
  <div class="container" >
    <div class="row">
      <div class="col-lg-4">
        <!-- Прячем колонку с навигацией для маленького экрана -->
        <div class="row d-none d-lg-block">
          <!-- Наваигация -->
          <ul class="nav nav-pills flex-column" style="margin-top:30px;" id="menu">
            <li class="sidebar-item">
              <router-link class="nav-link sidebar-link collapsed has-dropdown" to="/categories" data-bs-toggle="collapse" data-bs-target="#categories" aria-label="Categories page" aria-expanded="false"><strong>BOHEMIN COLLECTION/</strong></router-link>         
              <ul id="categories" class="sidebar-dropdown list-unstyled collapse"  data-bs-parent="#sidebar">
                <li class="sidebar-item"><router-link class="nav-link" to="/Dresses" aria-label="Dresses page"><strong>/DRESSES/</strong></router-link></li>
                <li><router-link class="nav-link sidebar-link" to="/Shirts" aria-label="Shirts page">/SHIRTS/</router-link></li>
                <li><router-link class="nav-link sidebar-link" to="/Skirts" aria-label="Skirts page">/SKIRTS/</router-link></li>
              </ul>
            </li>
            <li class="nav-item" style="margin-top:50px;">
              <router-link class="nav-link" to="/sign-in" aria-label="SignIn page">SIGN IN/REGISTER</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/search" aria-label="Search page">SEARCH   
                <svg class="icon">
                  <use xlink:href="../assets/styles/sprite.svg#search"></use>
                </svg></router-link> 
            </li>
          </ul>
        </div>
      </div>
      <div class="col-lg-8 mt-5">
        <!-- карточки с каталогом одежды -->
        <div class="row row-cols-sm-2 row-cols-md-2 row-cols-lg-2 g-5">
          <div class="col">
            <div class="card">                
              <div id="carouselExampleFade1" class="carousel slide carousel-fade">
                <div class="carousel-inner">
                  <div class="carousel-item active">
                    <img src="../assets/images/prof/images for page with dresses/photo_2022-10-08_00-46-16.jpg" class="card-img-top d-block w-100" alt="grey silk dress 1">
                  </div>
                  <div class="carousel-item">
                    <img src="../assets/images/prof/images for page with dresses/silk_grey_dress2.jpg" class="card-img-top d-block w-100" alt="grey silk dress 2">
                  </div>
                </div>
                <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleFade1" data-bs-slide="prev">
                  <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                  <span class="visually-hidden">Previous</span>
                </button>
                <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleFade1" data-bs-slide="next">
                  <span class="carousel-control-next-icon" aria-hidden="true"></span>
                  <span class="visually-hidden">Next</span>
                </button>
              </div>
              <div class="card-body">
                <h5 class="title-h6 text-center">Silk Maxi Dress with Long Flared Sleeves</h5>
                <p class="title-carddes card-text text-center">1270 AED</p>
              </div>
            </div>
          </div>
          <div class="col">
            <div class="card">
              <div id="carouselExampleFade2" class="carousel slide carousel-fade">
                <div class="carousel-inner">
                  <div class="carousel-item active">
                    <img src="../assets/images/prof/images for page with dresses/photo_2022-10-08_00-46-13.jpg" class="card-img-top d-block w-100" alt="milk dress 1">
                  </div>
                  <div class="carousel-item">
                    <img src="../assets/IMG_1.gif" class="card-img-top d-block w-100" alt="milk dress 2">
                  </div>
                </div>
                <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleFade2" data-bs-slide="prev">
                  <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                  <span class="visually-hidden">Previous</span>
                </button>
                <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleFade2" data-bs-slide="next">
                  <span class="carousel-control-next-icon" aria-hidden="true"></span>
                  <span class="visually-hidden">Next</span>
                </button>
              </div>
              <div class="card-body">
                <h5 class="title-h6 text-center">Maxi Sleeveless Milk Dress</h5>
                <p class="title-carddes card-text text-center">890 AED</p>
              </div>
            </div>
          </div>
          <div class="col">
            <div class="card">
              <div id="carouselExampleFade3" class="carousel slide carousel-fade">
                <div class="carousel-inner">
                  <div class="carousel-item active">
                    <img src="../assets/images/prof/images for page with dresses/photo_2022-10-08_00-46-28.jpg" class="card-img-top d-block w-100" alt="perple dress 1">
                  </div>
                  <div class="carousel-item">
                    <img src="../assets/images/prof/images for page with dresses/perple_dress_2.jpg" class="card-img-top d-block w-100" alt="perple dress 2">
                  </div>
                  <div class="carousel-item">
                    <img src="../assets/images/prof/images for page with dresses/perple_dress_3.jpg" class="card-img-top d-block w-100" alt="perple dress 3">
                  </div>
                </div>
                <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleFade3" data-bs-slide="prev">
                  <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                  <span class="visually-hidden">Previous</span>
                </button>
                <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleFade3" data-bs-slide="next">
                  <span class="carousel-control-next-icon" aria-hidden="true"></span>
                  <span class="visually-hidden">Next</span>
                </button>
              </div>
              <div class="card-body">
                <h5 class="title-h6 text-center">Purple Dress</h5>
                <p class="title-carddes card-text text-center">1300 AED</p>
              </div>
            </div>
          </div>
          <div class="col">
            <div class="card">
              <div id="carouselExampleFade4" class="carousel slide carousel-fade">
                <div class="carousel-inner">
                  <div class="carousel-item active">
                    <img src="../assets/images/prof/images for page with dresses/photo_2022-10-08_00-46-34 — копия.jpg" class="card-img-top d-block w-100" alt="blue dress 1">
                  </div>
                  <div class="carousel-item">
                    <img src="../assets/images/prof/images for page with dresses/blue_dress2.jpg" class="card-img-top d-block w-100" alt="blue dress 2">
                  </div>
                </div>
              </div>
              <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleFade4" data-bs-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Previous</span>
              </button>
              <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleFade4" data-bs-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Next</span>
              </button>
              <div class="card-body">
                <h5 class="title-h6 text-center">Midnight Blue Knitted Fabric Dress</h5>
                <p class="title-carddes card-text text-center">1500 AED</p>
              </div>
            </div>
          </div>
          <div class="col">
            <div class="card">
              <div id="carouselExampleFade5" class="carousel slide carousel-fade">
                <div class="carousel-inner">
                  <div class="carousel-item active">
                    <img src="../assets/images/prof/images for page with dresses/photo_2022-10-08_00-46-14.jpg" class="card-img-top" alt="maxi grey dress 1">
                  </div>
                  <div class="carousel-item">
                    <img src="../assets/images/prof/images for page with dresses/maxi_grey_dress2.jpg" class="card-img-top" alt="maxi grey dress 2">
                  </div>
                </div>
              </div>
              <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleFade5" data-bs-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Previous</span>
              </button>
              <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleFade5" data-bs-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Next</span>
              </button>
              <div class="card-body">
                <h5 class="title-h6 text-center">Grey Sillk Dress</h5>
                <p class="title-carddes card-text text-center">1450 AED</p>
              </div>
            </div>
          </div>
          <div class="col">
            <div class="card">
              <div id="carouselExampleFade6" class="carousel slide carousel-fade">
                <div class="carousel-inner">
                  <div class="carousel-item active">
                    <img src="../assets/images/prof/images for page with dresses/photo_2022-10-08_00-46-37 — копия.jpg" class="card-img-top" alt="sleeveless dress 1">
                  </div>
                  <div class="carousel-item">
                    <img src="../assets/images/prof/images for page with dresses/sleeveless_dress2.jpg" class="card-img-top" alt="sleeveless dress 2">
                  </div>
                </div>
              </div>
              <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleFade6" data-bs-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Previous</span>
              </button>
              <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleFade6" data-bs-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Next</span>
              </button>
              <div class="card-body">
                <h5 class="title-h6 text-center">Sleeveless Dress</h5>
                <p class="title-carddes card-text text-center">760 AED</p>

              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
      
<script>
  export default {
    name: 'Dresses'
  } 
</script>