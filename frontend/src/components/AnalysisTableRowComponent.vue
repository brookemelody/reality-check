<script setup>
    defineProps({
        timestamp: Number, // in seconds
        reason: String
    })

    function formatTimestamp(seconds) {
        if (seconds < 60) {
            return `0:${String(seconds).padStart(2, '0')}`;
        }
        else if (seconds >= 60) {
            let minutes = seconds / 60;
            let remainingSeconds = seconds % 60;
            return `${minutes}:${String(remainingSeconds).padStart(2, '0')}`;
        }
    }

    function jumpToTimeStamp(seconds) {
        console.log(seconds);
        // const video = document.getElementById("evidence_video");
        // console.log(video);
        // video.currentTime = seconds;
    }
</script>

<template>
    <tr>
        <td>
            <span @click="jumpToTimeStamp(timestamp)"><strong>{{ formatTimestamp(timestamp) }}</strong></span>
        </td>
        <td>
            {{ reason }}
        </td>
    </tr>
</template>

<style scoped>
td {
    border: 0.1em solid black;
    padding: 1em;
}
</style>