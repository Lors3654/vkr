<template>
  <div class="container" >
    <div class="row">
      <div class="col-lg-4">
        <NavigationMain />
      </div>
      <div class="col-lg-8 mt-5">
        <div class="d-flex justify-content-between">
          <div class="col-lg-4">
            <!-- фильтрация по коллекциям -->
            <select class="form-select form-select-sm" aria-label=".form-select-sm example" id="filter">
              <option selected id='resultId'>COLLECTIONS</option>
              <option value="desert" id="desert">DESERT</option>
              <option value="city" id="city">CITY</option>
            </select>
          </div>      
          <div class="col-lg-4">
            <!-- поле поиска -->
            <div class="d-flex justify-content-between">
              <div class="input-group">
                <input name="searchBar" id="searchBar" type="search" class="form-control rounded" placeholder="Search" aria-label="Search" aria-describedby="search-addon" autocomplete="off" />
              </div>
              <button type="button" class="btn btn-light btn-small">
                <svg class="icon">
                  <use xlink:href="../assets/styles/sprite.svg#search_fill"></use>
                </svg>
              </button>
            </div>
          </div>
        </div>
        <div class="conteiner mt-5">
          <div class="row row-cols-1 row-cols-md-3 row-cols-lg-2 g-5" id="clothesList">
          </div>
        </div>
        <!-- <script src="search.js"></script> -->
      </div>
    </div>
  </div>
</template>
      
<script>
  import NavigationMain from '@/components/NavigationMain.vue';

  export default {
    name: 'Search',
    components: {
      NavigationMain
    }
  } 
</script>