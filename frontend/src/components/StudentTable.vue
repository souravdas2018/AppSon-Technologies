<template>
  <v-card class="mb-4" elevation="2">
    <v-card-title>All Students</v-card-title>
    <v-data-table :headers="headers" :items="students" item-value="id">
      <template #item.actions="{ item }">
  <v-btn @click="openEdit(item)" color="primary" class="mr-2">
    Edit
  </v-btn>
  <v-btn @click="deleteStudent(item.id)" color="error">
    Delete
  </v-btn>
</template>
    </v-data-table>

    <!-- Edit Dialog -->
    <v-dialog v-model="dialog" max-width="500px">
      <v-card>
        <v-card-title>Edit Student</v-card-title>
        <v-card-text>
          <v-form @submit.prevent="updateStudent">
            <v-text-field v-model="edited.first_name" label="First Name" required />
            <v-text-field v-model="edited.last_name" label="Last Name" required />
            <v-text-field v-model="edited.dob" label="Date of Birth" required />
            <v-text-field v-model="edited.address" label="Address" required />
            <v-select
              v-model="edited.course_id"
              :items="courses.map(c => ({ title: c.name, value: c.id }))"
              label="Course"
              required
            />
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

const props = defineProps(['students', 'courses'])
const emit = defineEmits(['refresh'])

const dialog = ref(false)
const edited = ref({})

const headers = [
  { title: 'ID', key: 'id' },
  { title: 'First Name', key: 'first_name' },
  { title: 'Last Name', key: 'last_name' },
  { title: 'DOB', key: 'dob' },
  { title: 'Address', key: 'address' },
  { title: 'Course', key: 'course' },
  { title: 'Actions', key: 'actions', sortable: false }
]

const deleteStudent = async (id) => {
  const confirmed = confirm("Are you sure you want to delete this student?");
  if (!confirmed) return;

  const res = await fetch(`http://localhost:5000/students/${id}`, {
    method: 'DELETE'
  })

  if (res.ok) {
    alert('Student deleted successfully.')
    emit('refresh')
  } else {
    const err = await res.json()
    alert(err.error || 'Failed to delete student.')
  }
}

const updateStudent = async () => {
  await fetch(`http://localhost:5000/students/${edited.value.id}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(edited.value)
  })
  dialog.value = false
  emit('refresh')
}
</script>
