<template>
  <div class="container" >
    <div class="row">
      <div class="col-lg-4">
        <!-- Прячем колонку с навигацией для маленького экрана -->
        <div class="row d-none d-lg-block">
          <!-- Наваигация -->
          <ul class="nav flex-column">
            <li class="nav-item" style="margin-top:50px;">
              <router-link class="nav-link" to="/sign-up" aria-label="SignUp page"><strong>REGISTRATION</strong></router-link>
            </li>
            <li class="nav-item" style="margin-top:30px;">
              <router-link class="nav-link" to="/categories" aria-label="Categories page">BOHEMIN COLLECTION</router-link>
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
        <!-- Typical sign up form with additional buttons -->
        <form onsubmit="signup(event)">
          <div class="form-outline mb-4">
            <label for="name">NAME</label>
            <input type="name" class="form-control" id="name" name="name" placeholder="Your Name" required>
          </div>
          <div class="form-outline mb-4">
            <label for="latname">LAST NAME</label>
            <input type="lastname" class="form-control" id="lastname" name="lastname" placeholder="Your Last Name" required>
          </div>
          <div class="form-outline mb-4">
            <label for="birthday">BIRTHDAY</label>
            <input type="birthday" class="form-control" id="birthday" name="birthday" placeholder="DATE OF BIRTH (MM/DD/YYYY)" required>
          </div>
          <div class="form-outline mb-4">
            <label for="email">EMAIL ADDRESS</label>
            <input type="email" class="form-control" id="email" name="email" placeholder="Enter Email" required>
          </div>  
          <div class="form-outline mb-4">
            <label for="password">PASSWORD</label>
            <input type="password" class="form-control" id="password" name="password" placeholder="Password" required>
          </div> 
          <div class="form-outline mb-2">
            <div class="form-check">
              <input class="form-check-input" type="checkbox" value="" id="example" checked>
              <label class="form-check-label" for="example"><p>I agree to the processing of personal data</p></label>
            </div>
          </div>
          <div class="justify-content">
            <button type="submit" class="w-100 btn btn-dark btn-sm mb-5"><small>REGISTER</small></button>
          </div>
          <!-- Register buttons -->
          <div class="text-center mb-5">
              <p>Are you a member?<router-link class="nav-link" to="/sign-in" aria-label="SignIn page"><u>Sig in</u></router-link></p>
            </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'SignUp'
  } 
</script>