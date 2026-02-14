<script setup>
import CharacterProfile from './CharacterProfile.vue';
</script>

<template>
<h1>Reality Check</h1>
<h2 class="typewriter">Greetings, Detective.</h2>
<div class="character_profiles">
    <h2>Characters</h2>
    <CharacterProfile
        firstName="Chad"
        lastName="Siren"
        status = "Victim"
        age = 32
        gender = "Male"
        occupation = "Hacker"
        imageURL = "https://www.nicepng.com/png/full/300-3002785_silhouette-male-silhouette-man-head.png"
        description="Has accused his wife of adultery. He's provided the Agency with video footage as evidence, but is this video real or AI-generated?"
    />
    <CharacterProfile
        firstName="Miss"
        lastName="Information" 
        status = "Suspect"
        age = 28
        gender = "Female"
        occupation = "Software Engineer"
        imageURL = "https://www.imb.org/students/wp-content/uploads/sites/4/2023/08/woman-head-silhouette-png-black-and-white-download-female-silhouette-head-11563010560sqe7wt34hg.png"
        description = "Has been accused of cheating on her husband... on Valentine's Day of all days (How scandalous!)"
    />
    <CharacterProfile
        firstName="Arthur"
        lastName="Dimmesdale" 
        status = "Suspect"
        age = 22
        gender = "Male"
        occupation = "Junior Software Engineer"
        imageURL = "https://www.nicepng.com/png/full/300-3002785_silhouette-male-silhouette-man-head.png"
        description = "Mr. Siren's provided video evidence shows Miss Information and Mr. Dimmesdale having a romantic date at Carowinds, sharing a romantic cone of Howling Cow ice cream."
    />
</div>

</template>

<style scoped>
.character_profiles {
    display: flex;
    flex-direction: column;
    gap: 1em;
    color: hsla(160, 100%, 37%, 1);
}

.character_profiles h2 {
    text-transform: uppercase;
}
</style>