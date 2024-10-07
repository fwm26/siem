<script setup lang="ts">
import { RouterView, useRoute } from 'vue-router';
import Sidebar from '@/components/Sidebar.vue'; // Ensure the Sidebar path is correct

// Access the current route
const route = useRoute();
</script>

<template>
  <div id="app">
    <!-- Conditionally render the Sidebar only if hideSidebar is not set to true -->
    <Sidebar v-if="!route.meta.hideSidebar" /> <!-- Sidebar hidden on login -->

      <router-view v-slot="{ Component, route }">
        <keep-alive v-if="route.meta.keepAlive">
          <component :is="Component" />
        </keep-alive>
        <component v-else :is="Component" />
      </router-view>

  </div>
</template>


<style>

/* Global styles in App.vue */
h1, h2, h3, h4, h5, h6 {
  font-family: 'Poppins', sans-serif;
}

p {
 font-family: 'Poppins', sans-serif;
}

a {
    font-family: 'Poppins', sans-serif;
    font-weight:800;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
}

/* Apply Poppins font to all headers site-wide */
h1, h2, h3, h4, h5, h6 {
  font-family: 'Poppins', sans-serif;
}

</style>
