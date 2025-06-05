<template>
  <v-container>
    <h2>Course Management</h2>
    <CourseForm class="mt-5" @refresh="fetchCourses" />
    <CourseTable :courses="courses" @refresh="fetchCourses" />
  </v-container>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import CourseForm from '@/components/CourseForm.vue'
import CourseTable from '@/components/CourseTable.vue'

const courses = ref([])

const fetchCourses = async () => {
  try {
    const res = await fetch('http://localhost:5000/courses')
    const data = await res.json()

    if (res.ok) {
      courses.value = data
    } else {
      alert(data.error || 'Failed to fetch courses.')
    }
  } catch (error) {
    alert('Network error while fetching courses.')
    console.error(error)
  }
}

onMounted(fetchCourses)
</script>
