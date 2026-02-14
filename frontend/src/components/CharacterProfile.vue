<script setup>
  defineProps({
    firstName: String,
    lastName: String,
    status: String,
    age: Number,
    gender: String,
    occupation: String,
    imageURL: String,
    description: String
  })
</script>

<template>
  <div class="card">
    <div class="image_container">
      <img :src="imageURL">
    </div>
    <div class="info_container">
      <h2>{{ firstName }} {{ lastName }}</h2>
      <h3><u>{{ status }}</u></h3>
      <p><strong>Age: </strong>{{ age }} y.o.</p>
      <p><strong>Gender: </strong>{{ gender }}</p>
      <p><strong>Occupation: </strong>{{ occupation }}</p>
      <p><strong>Description: </strong>{{ description }}</p>
    </div>
  </div>
</template>

<style scoped>
.card {
  color: hsla(160, 100%, 37%, 1);
  border: 0.1em solid hsla(160, 100%, 37%, 1);
  padding: 1em;
  display: flex;
  gap: 1em;
}

.image_container {
  background-color: hsla(160, 100%, 37%, 1);
  height: 10em;
}

.image_container img {
  width: 10em;
  height: 10em;
}

strong {
  font-weight: bold;
}
</style>

