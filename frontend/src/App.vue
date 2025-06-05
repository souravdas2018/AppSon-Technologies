<!-- <template>
  <v-app>
    <v-container>
      <h1 class="mb-4">Student & Course Management</h1>
      <CourseForm @refresh="fetchAll" />
      <CourseTable :courses="courses" @refresh="fetchAll" />
      <StudentForm :courses="courses" @refresh="fetchAll" />
      <StudentTable :students="students" :courses="courses" @refresh="fetchAll" />
      <ReportTable :report="report" />
    </v-container>
  </v-app>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import CourseForm from './components/CourseForm.vue'
import StudentForm from './components/StudentForm.vue'
import StudentTable from './components/StudentTable.vue'
import ReportTable from './components/ReportTable.vue'
import CourseTable from './components/CourseTable.vue'
const students = ref([])
const courses = ref([])
const report = ref([])

const fetchAll = async () => {
  students.value = await (await fetch('http://localhost:5000/students')).json()
  courses.value = await (await fetch('http://localhost:5000/report')).json()
  const rawCourses = await (await fetch('http://localhost:5000/courses')).json()
  courses.value = rawCourses
  report.value = await (await fetch('http://localhost:5000/report')).json()
}

onMounted(fetchAll)
</script>


 -->

<template>
  <v-app>
    <v-app-bar app color="primary" dark>
      <v-toolbar-title>Student & Course Management</v-toolbar-title>
      <v-spacer />
      <v-btn to="/" text>Students</v-btn>
      <v-btn to="/courses" text>Courses</v-btn>
      <v-btn text to="/report" component="router-link">Report</v-btn>
    </v-app-bar>

    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>