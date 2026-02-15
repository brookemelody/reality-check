<script setup>
  defineProps({
    timestamp: Date,
    summary: String,
    type: String,
    user: String
  })
</script>

<template>
    <div class="card">
        <div class="event_info">
            <h3>{{ timestamp }}</h3>
            <h3><strong>{{ type }}</strong></h3>
        </div>
        <h2>{{ summary }}</h2>
        <p>Data entry logged by <strong>{{ user }}</strong></p>
    </div>
</template>

<style scoped>
.card {
    color: hsla(160, 100%, 37%, 1);
    border: 0.1em solid hsla(160, 100%, 37%, 1);
    padding: 1em;
    display: flex;
    flex-direction: column;
    gap: 1em;
}

.card::before {
    content: "";
    background-color: hsla(160, 100%, 37%, 1);
    width: 1em;
    height: 1em;
}

.event_info {
    display: flex;
    justify-content: space-between;
}

.card:hover {
    color: black;
    background-color: hsla(160, 100%, 37%, 1);
    transition: 0.5s ease-in-out;
}

.card:hover::before {
    content: "";
    background-color: black;
    width: 1em;
    height: 1em;
}
</style>

