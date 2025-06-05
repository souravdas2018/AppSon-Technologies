<template>
  <v-card class="mb-4" elevation="2">
    <v-card-title>Report: Students per Course</v-card-title>
    <v-data-table :headers="headers" :items="report" />
  </v-card>
</template>

<script setup>
const props = defineProps(['report'])

const headers = [
  { title: 'Course', key: 'course' },
  { title: 'Student Count', key: 'count' },
  { title: 'Total Fee', key: 'total_fee' }
]
</script>
