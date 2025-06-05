<template>
  <v-container>
    <h2>Students Per Course Report</h2>
    <ReportTable :report="report" />
  </v-container>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import ReportTable from '@/components/ReportTable.vue'

const report = ref([])

const fetchReport = async () => {
  report.value = await (await fetch('http://localhost:5000/report')).json()
}

onMounted(fetchReport)
</script>
