import { createRouter, createWebHistory } from 'vue-router';
import Login from '../views/Login.vue';
import Dashboard from '../views/Dashboard.vue';
import SiteScanner from '../views/SiteScanner.vue';
import VulnerabilityScanner from '../views/VulnerabilityScanner.vue';

const routes = [
  {
    path: '/login',
    name: 'Login',
    component: Login,
    meta: { hideSidebar: true } // Sidebar should be hidden on login
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: () => import('@/views/Dashboard.vue'),
    meta: { requiresAuth: true, keepAlive: true } // Show Sidebar on dashboard
  },
  {
    path: '/site-scanner',
    name: 'SiteScanner',
    component: () => import('@/views/SiteScanner.vue'),
    meta: { requiresAuth: true, keepAlive: true } // Show Sidebar on site scanner
  },
{
  path: '/vulnerability-scanner',
  name: 'VulnerabilityScanner',
  component: () => import('@/views/VulnerabilityScanner.vue'),
  meta: { requiresAuth: true, keepAlive: true } // Ensure keepAlive is false or omitted
},
  {
    path: '/',
    redirect: '/login'
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

// Navigation Guard
router.beforeEach((to, from, next) => {
  const isAuthenticated = !!localStorage.getItem('token'); // Check if token exists

  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (!isAuthenticated) {
      next('/login'); // Redirect to login if not authenticated
    } else {
      next(); // Continue to the protected route
    }
  } else {
    next(); // Continue to the non-protected route
  }
});

export default router;
