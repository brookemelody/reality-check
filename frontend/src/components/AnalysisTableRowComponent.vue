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
        const video = document.getElementById("evidence_video");
        video.currentTime = seconds;
    }
</script>

<template>
    <tr>
        <td>
            <span id="timestamp_button" @click="jumpToTimeStamp(timestamp)"><strong>{{ formatTimestamp(timestamp) }}</strong></span>
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

#timestamp_button:hover {
    text-decoration: underline;
    cursor: pointer;
}
</style>