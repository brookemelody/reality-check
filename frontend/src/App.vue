<script setup>
</script>

<template>
  <main>
    <nav>
      <RouterLink to="/">Case Overview</RouterLink>
      <RouterLink to="/timeline">Timeline</RouterLink>
      <RouterLink to="/evidence">Evidence</RouterLink>
    </nav>
    <router-view></router-view>
  </main>
</template>

<style scoped>
nav {
  display: flex;
  gap: 1em;
  text-transform: uppercase;
}
</style>
