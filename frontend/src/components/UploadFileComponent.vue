<script setup>
import EvidenceAnalysisResult from './EvidenceAnalysisResult.vue';
import axios from 'axios';

function onUploadFile() {
  let url = ""; // TODO: API Endpoint
  const formData = new FormData();
  formData.append('video', document.getElementById('fileInput').files[0]);
  axios.post(url, formData, {
    'Content-Type': 'multipart/form-data'
  })
  .then(response => console.log(response.data))
  .catch(error => console.error(error));
}

</script>

<template>
  <form method="post" enctype="multipart/form-data">
    <label for="file">The Agency accepts the following file formats: <strong>.jpg, .jpeg, .png, .mp4</strong></label>
    <input type="file" id="fileInput" accept=".jpg,.jpeg,.png,.mp4"/>
    <button @click="onUploadFile">Analyze</button>
  </form>
  <EvidenceAnalysisResult/>
</template>

<style scoped>

form {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 1em;
  margin-bottom: 3em;
  border: 0.1em solid hsla(160, 100%, 37%, 1);
  padding: 1em;
}

input::file-selector-button {
  background-color: hsla(160, 100%, 37%, 1);
  border: none;
  padding: 1em;
  font-weight: bold;
  font-family: "Syne Mono", monospace;
}

input::file-selector-button:hover {
  filter: brightness(0.65);
  transition: 0.5s ease-in-out;
}
</style>
