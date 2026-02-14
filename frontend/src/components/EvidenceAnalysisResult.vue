<script setup>
</script>

<template>
  <div class="case_file">
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
  z-index: -1;
  min-height: 40em;
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
</style>
