<template>
  <v-card class="mb-4" elevation="2">
    <v-card-title>All Courses</v-card-title>
    <v-data-table :headers="headers" :items="courses" item-value="id">
      <template #item.fee="{ item }">
        ₹ {{ item.fee }}
      </template>

      <template #item.actions="{ item }">
        <v-btn @click="openEdit(item)" color="primary" class="mr-2">Edit</v-btn>
        <v-btn @click="deleteCourse(item.id)" color="error">Delete</v-btn>
      </template>
    </v-data-table>

    <!-- Edit Course Dialog -->
    <v-dialog v-model="dialog" max-width="500px">
      <v-card>
        <v-card-title>Edit Course</v-card-title>
        <v-card-text>
          <v-form @submit.prevent="updateCourse">
            <v-text-field v-model="edited.name" label="Course Name" required />
            <v-text-field v-model="edited.duration" label="Duration" required />
            <v-text-field v-model="edited.fee" label="Fee" type="number" required />
            <v-btn type="submit" color="blue" class="mt-2">Update</v-btn>
            <v-btn text @click="dialog = false" class="mt-2 ml-2">Cancel</v-btn>
          </v-form>
        </v-card-text>
      </v-card>
    </v-dialog>
  </v-card>
</template>

<script setup>
import { ref } from 'vue'

const props = defineProps(['courses'])
const emit = defineEmits(['refresh'])

const dialog = ref(false)
const edited = ref({})

const headers = [
  { title: 'ID', key: 'id' },
  { title: 'Course Name', key: 'name' },
  { title: 'Duration', key: 'duration' },
  { title: 'Fee', key: 'fee' },
  { title: 'Actions', key: 'actions', sortable: false }
]

const openEdit = (course) => {
  edited.value = { ...course }
  dialog.value = true
}

const updateCourse = async () => {
  await fetch(`http://localhost:5000/courses/${edited.value.id}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(edited.value)
  })
  dialog.value = false
  emit('refresh')
}

const deleteCourse = async (id) => {
  const confirmed = confirm("Are you sure you want to delete this course?");
  if (!confirmed) return;

  const res = await fetch(`http://localhost:5000/courses/${id}`, {
    method: 'DELETE'
  })

  if (res.ok) {
    emit('refresh')
  } else {
    const err = await res.json()
    alert(err.error || 'Delete failed')  // ✅ Show backend error
  }
}
</script>
