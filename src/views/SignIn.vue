<template>
  <div class="container" >
    <div class="row">
      <div class="col-lg-4">
        <!-- Прячем колонку с навигацией для маленького экрана -->
        <div class="row d-none d-lg-block">
          <!-- Наваигация -->
          <ul class="nav flex-column">
            <li class="nav-item" style="margin-top:50px;">
              <router-link class="nav-link" to="/sign-in" aria-label="SignIn page"><strong>SIGN IN</strong></router-link>
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
        <!-- Typical sign in / login form with additional register buttons -->
        <form onsubmit="login(event)">
          <div class="row">
            <!-- Email input -->
            <div class="form-outline mb-4">
              <label class="form-label" for="email">EMAIL ADDRESS</label>
              <input type="email" id="email" class="form-control" name="email" placeholder="name@example.com" autocomplete="off" required>
            </div>
            <!-- Password input -->
            <div class="form-outline mb-4">
              <label class="form-label" for="password">PASSWORD</label>
              <input type="password" id="password" class="form-control" name="password" placeholder="password" autocomplete="off" required>
            </div>
            <!-- Checkbox -->
            <div class="form-outline mb-2">
              <div class="form-check">
                <input class="form-check-input" type="checkbox" value="" id="rememberme" checked>
                <label class="form-check-label" for="rememberme"><p>Remember me</p></label>
              </div>
            </div>
            <!-- Submit button -->
            <div class="justify-content">
              <button type="submit" class="w-100 btn btn-dark btn-sm mb-5">SIGN IN</button>
            </div>
            <!-- Register buttons -->
            <div class="text-center mb-5">
              <p>Not a member?<router-link class="nav-link" to="/sign-up" aria-label="SignUp page"><u>Register</u></router-link></p>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>
  
<script>
  export default {
    name: 'SignIn'
  } 
</script>