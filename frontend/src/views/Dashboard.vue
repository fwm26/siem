<template>
  <div class="dashboard-container">
    <Sidebar />


    <!-- Main Content -->
    <div class="main-content">
      <!-- Top Welcome Message -->
      <div class="welcome-message">
        <h1>Hello, {{ capitalizeFirstLetter(username) }}</h1>
      </div>

      <!-- HTTP Events Section - Full Width -->
      <div class="events-section">
        <h2>HTTP Events</h2>
        <div class="events-cards-container">
          <!-- 5xx Server Events Card -->
          <div class="event-card">
            <h3>5xx Server Errors</h3>
            <p>{{ errorCounts.serverErrors }}</p>
          </div>

          <!-- 4xx Client Events Card -->
          <div class="event-card">
            <h3>4xx Client Errors</h3>
            <p>{{ errorCounts.clientErrors }}</p>
          </div>

          <!-- 3xx Redirects Card -->
          <div class="event-card">
            <h3>3xx Redirects</h3>
            <p>{{ errorCounts.redirectErrors }}</p>
          </div>

          <!-- 1xx Informational Card -->
          <div class="event-card">
            <h3>1xx Informational</h3>
            <p>{{ errorCounts.informational }}</p>
          </div>
        </div>
      </div>

  <div class="events-section">
    <h2>Login Events</h2>
    <div class="events-cards-container">
      <!-- Successful Logins Card -->
      <div class="event-card" @click="filterLogsByEvent('User login')">
        <h3>Successful Logins</h3>
        <p>{{ errorCounts.successfulLogins }}</p>
      </div>

      <!-- Unsuccessful Logins Card -->
      <div class="event-card" @click="filterLogsByEvent('Unsuccessful login')">
        <h3>Unsuccessful Logins</h3>
        <p>{{ errorCounts.unsuccessfulLogins }}</p>
      </div>

      <!-- Password Resets Card -->
      <div class="event-card" @click="filterLogsByEvent('Password reset')">
        <h3>Password Resets</h3>
        <p>{{ errorCounts.passwordResets }}</p>
      </div>

      <!-- Logouts Card -->
      <div class="event-card" @click="filterLogsByEvent('Logout')">
        <h3>Logouts</h3>
        <p>{{ errorCounts.logouts }}</p>
      </div>
    </div>

    <!-- Modal for displaying filtered logs -->
    <div v-if="showModal" class="modal-overlay" @click="closeModal">
      <div class="modal-content" @click.stop>
        <h2>Filtered Logs</h2>
        <input type="text" v-model="searchTerm" placeholder="Search logs..." />
        <table>
          <thead>
            <tr>
              <th>Event</th>
              <th>User</th>
              <th>Timestamp</th>
              <th>IP Address</th>
              <th>Action</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="log in filteredLogsTable" :key="log.id">
              <td>{{ log.event }}</td>
              <td>{{ log.user }}</td>
              <td>{{ log.timestamp }}</td>
              <td>{{ log.ip }}</td>
              <td><button @click="viewLogDetails(log)">View</button></td>
            </tr>
          </tbody>
        </table>
        <button @click="closeModal">Close</button>
      </div>
    </div>
  </div>

      <div class="events-section">
        <h2>Themes, Plugins & File System</h2>
        <div class="events-cards-container">
          <!-- 5xx Server Events Card -->
          <div class="event-card">
            <h3>Plugin Activations</h3>
            <p>{{ errorCounts.serverErrors }}</p>
          </div>

          <!-- 4xx Client Events Card -->
          <div class="event-card">
            <h3>Plugin Deactivations</h3>
            <p>{{ errorCounts.clientErrors }}</p>
          </div>

          <!-- 3xx Redirects Card -->
          <div class="event-card">
            <h3>Theme Changes</h3>
            <p>{{ errorCounts.redirectErrors }}</p>
          </div>

          <!-- 1xx Informational Card -->
          <div class="event-card">
            <h3>File System Changes</h3>
            <p>{{ errorCounts.informational }}</p>
          </div>
        </div>
      </div>      

      <!-- Logs Table -->
      <div class="events-section">
        <h2>Logs</h2>
        <table class="logs-table">
          <thead>
            <tr>
              <th>Site URL</th>           
              <th>Timestamp</th>
              <th>Event</th>
              <th>User</th>
              <th>IP</th>
              <th>URL</th>
              <th>Method</th>
              <th>User Agent</th>
              <th>Extra</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="log in logs" :key="log.id">
              <td>{{ log.site_url }}</td>            
              <td>{{ log.timestamp }}</td>
              <td>{{ log.event }}</td>
              <td>{{ log.user }}</td>
              <td>{{ log.ip }}</td>
              <td>{{ log.url }}</td>
              <td>{{ log.method }}</td>
              <td>{{ log.user_agent }}</td>
              <td>{{ log.extra }}</td>
            </tr>
          </tbody>
        </table>
      </div>      
      <!-- You can add other sections here as needed -->
    </div>
  </div>
</template>

<script lang="ts">
  import { defineComponent } from 'vue';
  import Sidebar from '@/components/Sidebar.vue';
  import axios from 'axios';

  export default defineComponent({
    name: 'Dashboard',
    components: {
      Sidebar // Register Sidebar component
    },  
    data() {
      return {
        username: '', // Placeholder for the username
        errorCounts: {
          successfulLogins: 0,
          unsuccessfulLogins: 0,
          passwordResets: 0,
          logouts: 0
        },
        logs: [], // Array to hold logs
        filteredLogs: [], // Array to hold logs filtered by event type
        showModal: false, // Control whether the modal is shown
        searchTerm: '', // Search term for filtering inside the modal
      };
    },
    mounted() {
      // Fetch the username and logs when the component is first mounted
      this.fetchUsername();
      this.fetchLogs();
    },
    activated() {
      // Fetch the username and logs when the component is re-activated from cache
      this.fetchUsername();
      this.fetchLogs();
    },
    methods: {
      async fetchUsername() {
        try {
          const response = await axios.get('http://localhost:8000/users/me', {
            headers: {
              Authorization: `Bearer ${localStorage.getItem('token')}` // Send the token in the Authorization header
            }
          });
          this.username = response.data.username; // Set the username from the response
        } catch (err) {
          console.error('Error fetching username:', err);
          this.$router.push('/login'); // Redirect to login if unauthorized
        }
      },
      async fetchLogs() {
        try {
          const response = await axios.get('http://localhost:8000/logs', {
            headers: {
              Authorization: `Bearer ${localStorage.getItem('token')}` // Send the token in the Authorization header
            }
          });
          this.logs = response.data; // Store logs in the logs array
          this.countEvents(); // Count specific log events
        } catch (err) {
          console.error('Error fetching logs:', err);
        }
      },
      countEvents() {
        // Count occurrences of specific events like "User login", "Password reset", etc.
        this.errorCounts.successfulLogins = this.logs.filter(log => log.event === 'User login').length;
        this.errorCounts.unsuccessfulLogins = this.logs.filter(log => log.event === 'Unsuccessful login').length;
        this.errorCounts.passwordResets = this.logs.filter(log => log.event === 'Password reset').length;
        this.errorCounts.logouts = this.logs.filter(log => log.event === 'Logout').length;
      },
      filterLogsByEvent(event) {
        // Filter logs by the event type
        this.filteredLogs = this.logs.filter(log => log.event === event);
        this.showModal = true; // Show modal when logs are filtered
      },
      closeModal() {
        this.showModal = false; // Hide the modal
      },
      viewLogDetails(log) {
        // Handle viewing more details about a specific log
        console.log('Log details:', log);
      },
      logout() {
        localStorage.removeItem('token');
        this.$router.push('/login');
      },
      capitalizeFirstLetter(username: string) {
        if (!username) return '';
        return username.charAt(0).toUpperCase() + username.slice(1);
      }
    },
    computed: {
      filteredLogsTable() {
        // Filter logs based on search term in the modal
        return this.filteredLogs.filter(log =>
          log.event.toLowerCase().includes(this.searchTerm.toLowerCase()) ||
          (log.user && log.user.toLowerCase().includes(this.searchTerm.toLowerCase())) ||
          log.ip.includes(this.searchTerm)
        );
      }
    }
  });
</script>



<style>

  body, html {
    margin: 0;
    padding: 0;
    height: 100%; /* Ensure the body and html take full height */
    overflow-x: hidden; /* Prevent horizontal scrolling */
  }

  .dashboard-container {
    display: flex;
    height: 100vh; /* Ensure it takes the full viewport height */
    width: 100vw;  /* Ensure it doesn't overflow horizontally */
  }

  .main-content {
    margin-left: 20%; /* Make space for the fixed sidebar */
    padding: 20px;
    width: 80%;
  }


/* Welcome Message */
.welcome-message h1 {
  font-family: 'Poppins', sans-serif;
  margin-left: 30px;
  margin-bottom: 20px;
}

/* Events Section */
.events-section {
  width: 95%;
  max-width: 1280px;
  background-color: #fff;
  padding: 30px;  /* Generous padding */
}

.events-cards-container {
  display: flex;
  justify-content: space-between;
  gap: 20px;  /* Space between cards */
}

.event-card {
  flex: 1;
  background-color: #f4f4f4;
  padding: 15px;  /* Generous padding */
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  text-align: center;
}

.event-card h3 {
  margin-bottom: 10px;
  font-size: 1.25rem;
  color: #0B132B;
}

.event-card p {
  font-size: 2.5rem;
  font-weight: bold;
  color: #DB162F;
}

/* Styles for the logs table */

div.http-events-section:nth-child(5) > h3:nth-child(1){
  font-size: 1.25rem;
}

.logs-table {
  width: 100%;
  border-collapse: collapse;
  font-family: 'Poppins', sans-serif;  
}

.logs-table th, .logs-table td {
  padding: 12px;
  text-align: left;
}

.logs-table th {
  background-color: #EDC9FF;
}

.logs-table tr:nth-child(even) {
  background-color: #fafafa;
}

/* Modal Styles */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-color: rgba(0, 0, 0, 0.7);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal-content {
  background-color: white;
  padding: 20px;
  border-radius: 10px;
  width: 80%;
  max-width: 800px;
}

table {
  width: 100%;
  border-collapse: collapse;
}

th, td {
  padding: 10px;
  border: 1px solid #ccc;
}

th {
  background-color: #f4f4f4;
}

button {
  padding: 10px;
  margin-top: 10px;
}

</style>
