<script setup>
import axios from 'axios';
import { ref } from 'vue';
import AnalysisTableRowComponent from './AnalysisTableRowComponent.vue';

let testResponse = ref("Loading data...");

axios.get('https://api.sampleapis.com/switch/games').then((response) => {
  console.log(testResponse.value);
  let index = Math.floor(Math.random() * response.data.length);
  testResponse.value = response.data[index].name;
  console.log(testResponse.value);
})
</script>

<template>
  <div class="case_file">
    <video id="evidence_video" controls>
      <source src="../assets/demo_video.mp4" type="video/mp4">
    </video>
    <table>
      <thead>
        <tr>
          <th scope="col">Timestamp</th>
          <th scope="col">Reasoning</th>
        </tr>
      </thead>
      <tbody>
        <AnalysisTableRowComponent
          :timestamp="1"
          reason="Cats aren't snakes."
        />
        <AnalysisTableRowComponent
          :timestamp="2"
          reason="And Miss Information never cheated on her husband."
        />
        <AnalysisTableRowComponent
          :timestamp="3"
          reason="Crime may change its shape, but it never changes its purpose."
        />
        <AnalysisTableRowComponent
          :timestamp="5"
          reason="Operatives, this case deserves a good crackin' with better ways of detecting criminals' lies and AI sources."
        />
        <AnalysisTableRowComponent
          :timestamp="7"
          reason="The siren's callin', but it ain't aware of what it's bringin' in."
        />
      </tbody>
    </table>
  </div>
</template>

<style scoped>
.case_file {
  color: black;
  padding: 1em;
  background-color: #F2DDB4; /* Folder color */
  border-radius: 0 10px 10px 10px; /* Rounded corners on top-right, bottom-right, and bottom-left */
  position: relative; /* Required for absolute positioning of pseudo-element */
  padding: 15px;
  box-shadow: 2px 2px 5px rgba(0,0,0,0.2);
  min-height: 40em;

  display: flex;
  justify-content: center;
  align-items: flex-start;
  gap: 1em;
}

.case_file::before {
  /* The "tab" part of the folder */
  content: "CASE NO.20260214 (\"Siren's Call\")";
  display: flex;
  justify-content: center;
  font-weight: bold;
  color: maroon;
  font-family: 'Courier New', Courier, monospace;

  position: absolute;
  top: -20px; /* Position above the main body, accounting for border/padding */
  left: -0.01px; /* Align with the left edge */
  width: 40%; /* Width of the tab */
  height: 20px; /* Height of the tab */
  background-color: #F2DDB4; /* Same color as the folder body */
  border-bottom: none; /* Hide the bottom border to blend with the main body */
  border-top-right-radius: 8px; /* Smooth top-right corner of the tab */
  border-top-left-radius: 4px; /* Slight curve on the top-left */
}

#evidence_video {
  max-width: 50em;
  max-height: 50em;
}

table, th {
  border: 0.1em solid black;
}

th {
  font-weight: bold;
}

</style>
