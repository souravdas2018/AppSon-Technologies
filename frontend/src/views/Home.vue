<template>
  <v-container>
    <h2>Student Registration</h2>
    <StudentForm :courses="courses" @refresh="fetchAll" />
    <StudentTable class="mt-5" :students="students" :courses="courses" @refresh="fetchAll" />
  </v-container>
</template>

<script setup>
import StudentForm from '@/components/StudentForm.vue'
import StudentTable from '@/components/StudentTable.vue'
import ReportTable from '@/components/ReportTable.vue'
import { ref, onMounted } from 'vue'

const students = ref([])
const courses = ref([])
const report = ref([])

const fetchAll = async () => {
  students.value = await (await fetch('http://localhost:5000/students')).json()
  courses.value = await (await fetch('http://localhost:5000/courses')).json()
  report.value = await (await fetch('http://localhost:5000/report')).json()
}

onMounted(fetchAll)
</script>
