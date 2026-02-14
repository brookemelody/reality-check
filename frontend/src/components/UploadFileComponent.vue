<script setup>
import EvidenceAnalysisResult from './EvidenceAnalysisResult.vue';
</script>

<template>
  <form method="post" enctype="multipart/form-data">
    <label for="file">The Agency accepts the following file formats: .jpg, .jpeg, .png, .mp4</label>
    <input type="file" accept=".jpg,.jpeg,.png,.mp4"/>
    <button>Analyze</button>
  </form>
  <EvidenceAnalysisResult/>
</template>

<style scoped>

form {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  margin-bottom: 3em;
}
</style>
