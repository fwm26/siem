<!-- Sidebar.vue -->
<template>
  <nav class="sidebar">
      <div class="logo">
        <img src="@/assets/logo.png" alt="Logo" />
      </div>
    <ul class="nav-menu">
      <li><router-link to="/dashboard" exact-active-class="active-tab"><i class="fas fa-chart-bar"></i> Dashboard</router-link></li>
      <li><router-link to="/site-scanner" exact-active-class="active-tab"><i class="fas fa-globe"></i> Site Scanner</router-link></li>
      <li><router-link to="/vulnerability-scanner" exact-active-class="active-tab"><i class="fas fa-shield-alt"></i> Vulnerability Scanner</router-link></li>
    </ul>
    <div class="logout">
      <a @click.prevent="logout">
        <i class="fas fa-sign-out-alt"></i> Logout
      </a>
    </div>
  </nav>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'Sidebar',
  methods: {
    logout() {
      localStorage.removeItem('token'); // Clear token on logout
      this.$router.push('/login'); // Redirect to login page
    }
  }
});
</script>

<style scoped>

.sidebar {
  background-color: #0B132B;
  width: 20%;
  padding: 20px;
  border-radius: 15px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  position: fixed; /* Make the sidebar fixed */
  height: 92vh; /* Full height of the viewport */
  top: 0;
  left: 0;
}

.logo img {
  width: 50%;
  height: auto;
  margin-bottom: 40px;
}


/* For general layout and styling */
.nav-menu a.router-link-exact-active:hover {
  color: #DB162F;
}

.nav-menu {
  list-style: none;
  padding: 0;
  margin: 0;
  flex-grow: 1;  /* Allow the nav menu to grow and fill available space */
  overflow-y: auto;  /* Allow scrolling if menu is too long */
  max-height: calc(100vh - 120px); /* Ensure the nav-menu doesn’t push the logout button out of view */
}

.nav-menu li {
  margin-bottom: 20px;
}

.nav-menu a {
  color: white;
  text-decoration: none;
  font-size: 18px;
  display: flex;
  align-items: center;
}

.nav-menu a.router-link-exact-active {
  color: #DB162F;
}

.nav-menu a:hover {
  color: #DB162F;
}

.nav-menu i {
  margin-right: 15px;
}

.logout {
  margin-top: auto;
}

.logout a:hover {
  color: #DB162F;
}

.logout a {
  color: white;
  text-decoration: none;
  cursor: pointer;
  display: flex;
  align-items: center;
}

.logout i {
  margin-right: 10px;
}
</style>
