<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'SiteScanner',
  data() {
    return {
      content: 'SiteScanner content here...' // Example content
    };
  },
  mounted() {
    this.loadData();
  },
  activated() {
    this.loadData(); // Re-fetch or process content when the view is active
  },
  methods: {
    loadData() {
      console.log('SiteScanner content loaded');
    }
  }
});
</script>

<template>
  <div>
    <h1>SiteScanner</h1>
    <p>{{ content }}</p>
  </div>
</template>
